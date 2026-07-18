#!/usr/bin/env python3
"""Wire-measure MCP tool-definition sizes via JSON-RPC tools/list over stdio.

The tools/list result is the schema payload a static-loading client embeds in
context at session start. Token estimate: chars/4 (stated estimator).
"""
import json
import subprocess
import sys
import time

SERVERS = {
    "gworkspace": ["uvx", "workspace-mcp", "--single-user", "--tools", "gmail", "drive", "docs"],
    "playwright": ["npx", "@playwright/mcp@latest", "--isolated"],
    "best-practices": ["/home/jerem/claude-code-project-best-practices/mcp-server/.venv/bin/python", "-m", "best_practices_mcp.server"],
}


def rpc(proc, obj):
    proc.stdin.write((json.dumps(obj) + "\n").encode())
    proc.stdin.flush()


def read_msg(proc, want_id, deadline):
    buf = b""
    while time.time() < deadline:
        line = proc.stdout.readline()
        if not line:
            time.sleep(0.05)
            continue
        line = line.strip()
        if not line:
            continue
        try:
            m = json.loads(line)
        except Exception:
            continue
        if m.get("id") == want_id:
            return m
    return None


def measure(name, cmd):
    try:
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=subprocess.DEVNULL,
                                cwd="/home/jerem/claude-code-project-best-practices")
    except FileNotFoundError as e:
        return {"server": name, "error": str(e)}
    deadline = time.time() + 120
    rpc(proc, {"jsonrpc": "2.0", "id": 1, "method": "initialize",
               "params": {"protocolVersion": "2025-06-18",
                          "capabilities": {},
                          "clientInfo": {"name": "measure", "version": "0.0.1"}}})
    init = read_msg(proc, 1, deadline)
    if not init:
        proc.kill()
        return {"server": name, "error": "no initialize response"}
    rpc(proc, {"jsonrpc": "2.0", "method": "notifications/initialized"})
    rpc(proc, {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
    resp = read_msg(proc, 2, deadline)
    proc.kill()
    if not resp or "result" not in resp:
        return {"server": name, "error": f"no tools/list result: {str(resp)[:200]}"}
    tools = resp["result"].get("tools", [])
    total = len(json.dumps(tools))
    per = []
    for t in tools:
        j = len(json.dumps(t))
        d = len(t.get("description", "") or "")
        s = len(json.dumps(t.get("inputSchema", {})))
        per.append({"name": t.get("name"), "json_chars": j, "desc_chars": d, "schema_chars": s})
    per.sort(key=lambda x: -x["json_chars"])
    schema_share = sum(p["schema_chars"] for p in per) / max(total, 1)
    return {"server": name, "n_tools": len(tools), "total_json_chars": total,
            "est_tokens_chars4": total // 4,
            "mean_chars_per_tool": total // max(len(tools), 1),
            "input_schema_share": round(schema_share, 3),
            "top3": per[:3],
            "names_only_chars": sum(len(p["name"] or "") + 1 for p in per)}


out = []
for name, cmd in SERVERS.items():
    r = measure(name, cmd)
    out.append(r)
    print(json.dumps(r, indent=1))
json.dump(out, open(sys.path[0] + "/mcp_wire_results.json", "w"), indent=1)
