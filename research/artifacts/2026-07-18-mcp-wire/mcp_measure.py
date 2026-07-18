#!/usr/bin/env python3
"""Measure MCP tool-definition context cost: deferred names-only vs full schemas.

Full-schema sizes come from the ToolSearch results in the loader agent's
transcript (the exact <functions> text a static-loading session would carry).
Token estimate: chars/4 (stated estimator).
"""
import json
import re
import sys
from collections import defaultdict

TRANSCRIPT = "/tmp/claude-1000/-home-jerem-claude-code-project-best-practices/ca4ee1d1-304e-4c91-9528-02a7c82e0abf/tasks/a4da337ae1da1164c.output"

events = []
for ln in open(TRANSCRIPT, errors="replace"):
    try:
        events.append(json.loads(ln))
    except Exception:
        pass

# Collect ToolSearch tool_result payload text
payloads = []
models = defaultdict(int)
for e in events:
    msg = e.get("message") or {}
    if msg.get("model"):
        models[msg["model"]] += 1
    content = msg.get("content")
    if not isinstance(content, list):
        continue
    for blk in content:
        if blk.get("type") == "tool_result":
            c = blk.get("content")
            if isinstance(c, list):
                text = "".join(b.get("text", "") for b in c if isinstance(b, dict))
            else:
                text = str(c or "")
            if "<function>" in text:
                payloads.append(text)

full = "\n".join(payloads)
# Per-definition sizes
defs = re.findall(r"<function>(.*?)</function>", full, re.S)
per_server = defaultdict(lambda: [0, 0])  # server -> [count, chars]
for d in defs:
    m = re.search(r'"name":\s*"(mcp__[^_"]+(?:_[^_"]+)*?)__', d)
    server = m.group(1) if m else "unknown"
    per_server[server][0] += 1
    per_server[server][1] += len(d)

total_def_chars = sum(len(d) for d in defs)
wrapper_chars = len(full) - total_def_chars  # <functions> wrappers, result framing

print(f"definitions parsed: {len(defs)}")
for s, (n, c) in sorted(per_server.items()):
    print(f"  {s}: {n} tools, {c} chars (~{c//4} tokens), mean ~{c//max(n,1)} chars/tool")
print(f"total definition chars: {total_def_chars} (~{total_def_chars//4} tokens)")
print(f"result framing/wrapper chars: {wrapper_chars}")
print(f"total ToolSearch payload chars: {len(full)} (~{len(full)//4} tokens)")
print(f"models serving loader agent: {dict(models)}")

# Deferred names-only cost: the session carries only tool names in a reminder.
NAMES = [
  "mcp__claude_ai_Gmail__apply_sensitive_message_label","mcp__claude_ai_Gmail__apply_sensitive_thread_label","mcp__claude_ai_Gmail__create_draft","mcp__claude_ai_Gmail__create_label","mcp__claude_ai_Gmail__get_message","mcp__claude_ai_Gmail__get_thread","mcp__claude_ai_Gmail__label_message","mcp__claude_ai_Gmail__label_thread","mcp__claude_ai_Gmail__list_drafts","mcp__claude_ai_Gmail__list_labels","mcp__claude_ai_Gmail__search_threads","mcp__claude_ai_Gmail__unlabel_message","mcp__claude_ai_Gmail__unlabel_thread",
  "mcp__claude_ai_Google_Calendar__create_event","mcp__claude_ai_Google_Calendar__delete_event","mcp__claude_ai_Google_Calendar__get_event","mcp__claude_ai_Google_Calendar__list_calendars","mcp__claude_ai_Google_Calendar__list_events","mcp__claude_ai_Google_Calendar__respond_to_event","mcp__claude_ai_Google_Calendar__suggest_time","mcp__claude_ai_Google_Calendar__update_event",
  "mcp__claude_ai_Google_Drive__copy_file","mcp__claude_ai_Google_Drive__create_file","mcp__claude_ai_Google_Drive__download_file_content","mcp__claude_ai_Google_Drive__get_file_metadata","mcp__claude_ai_Google_Drive__get_file_permissions","mcp__claude_ai_Google_Drive__list_recent_files","mcp__claude_ai_Google_Drive__read_file_content","mcp__claude_ai_Google_Drive__search_files",
  "mcp__claude_ai_Mermaid_Chart__authenticate","mcp__claude_ai_Mermaid_Chart__complete_authentication",
  "mcp__gworkspace__batch_modify_gmail_message_labels","mcp__gworkspace__batch_update_doc","mcp__gworkspace__check_drive_file_public_access","mcp__gworkspace__copy_drive_file","mcp__gworkspace__create_doc","mcp__gworkspace__create_drive_file","mcp__gworkspace__create_drive_folder","mcp__gworkspace__create_table_with_data","mcp__gworkspace__debug_docs_runtime_info","mcp__gworkspace__debug_table_structure","mcp__gworkspace__draft_gmail_message","mcp__gworkspace__export_doc_to_pdf","mcp__gworkspace__find_and_replace_doc","mcp__gworkspace__get_doc_as_markdown","mcp__gworkspace__get_doc_content","mcp__gworkspace__get_drive_file_content","mcp__gworkspace__get_drive_file_download_url","mcp__gworkspace__get_drive_file_permissions","mcp__gworkspace__get_drive_shareable_link","mcp__gworkspace__get_gmail_attachment_content","mcp__gworkspace__get_gmail_message_content","mcp__gworkspace__get_gmail_messages_content_batch","mcp__gworkspace__get_gmail_thread_content","mcp__gworkspace__get_gmail_threads_content_batch","mcp__gworkspace__import_to_google_doc","mcp__gworkspace__import_to_google_sheets","mcp__gworkspace__import_to_google_slides","mcp__gworkspace__insert_doc_elements","mcp__gworkspace__insert_doc_image","mcp__gworkspace__inspect_doc_structure","mcp__gworkspace__list_docs_in_folder","mcp__gworkspace__list_document_comments","mcp__gworkspace__list_drive_items","mcp__gworkspace__list_gmail_filters","mcp__gworkspace__list_gmail_labels","mcp__gworkspace__manage_doc_tab","mcp__gworkspace__manage_document_comment","mcp__gworkspace__manage_drive_access","mcp__gworkspace__manage_gmail_filter","mcp__gworkspace__manage_gmail_label","mcp__gworkspace__modify_doc_text","mcp__gworkspace__modify_gmail_message_labels","mcp__gworkspace__search_docs","mcp__gworkspace__search_drive_files","mcp__gworkspace__search_gmail_messages","mcp__gworkspace__send_gmail_message","mcp__gworkspace__set_drive_file_permissions","mcp__gworkspace__start_google_auth","mcp__gworkspace__update_doc_headers_footers","mcp__gworkspace__update_drive_file","mcp__gworkspace__update_paragraph_style",
]
assert len(NAMES) == 82, len(NAMES)
names_chars = sum(len(n) + 1 for n in NAMES)  # one per line
boilerplate = 320  # deferred-listing preamble sentences, measured from session text
print(f"deferred names-only cost: {names_chars} name chars + ~{boilerplate} preamble (~{(names_chars+boilerplate)//4} tokens)")
ratio = (total_def_chars) / max(names_chars + boilerplate, 1)
print(f"full-schema vs names-only ratio: {ratio:.1f}x; reduction {(1 - (names_chars+boilerplate)/max(total_def_chars,1))*100:.1f}%")
