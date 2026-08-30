#!/usr/bin/env python3
"""Score a ladder output directory against selected rules. Mechanical only.

Verdict per rule: SAT / VIOL / NA (not applicable) / ERR (artifact missing or
unparseable — reported, excluded from adherence denominators).
Usage: score_ladder.py <outdir> [rung|ALL]
"""
import ast
import io
import json
import re
import sys
import tokenize
from pathlib import Path

LKEY = json.load(open(Path(__file__).parent / "guides" / "ladder_key.json"))


def strip_md_code(text):
    """Remove fenced blocks, then inline code spans, then URLs."""
    out, in_fence = [], False
    for line in text.splitlines():
        if re.match(r"^\s*(```|~~~)", line):
            in_fence = not in_fence
            continue
        if not in_fence:
            out.append(line)
    t = "\n".join(out)
    t = re.sub(r"`[^`\n]*`", "", t)
    t = re.sub(r"\]\([^)\n]*\)", "](", t)
    t = re.sub(r"<?https?://\S+>?", "", t)
    return t


def fences(text):
    """Return list of (lang, body_lines)."""
    res, cur, lang, in_f = [], [], None, False
    for line in text.splitlines():
        m = re.match(r"^\s*```(\S*)\s*$", line) or re.match(r"^\s*```(\S*)", line)
        if m and not in_f:
            in_f, lang, cur = True, m.group(1), []
        elif re.match(r"^\s*```\s*$", line) and in_f:
            in_f = False
            res.append((lang, cur))
        elif in_f:
            cur.append(line)
    return res


class Ctx:
    def __init__(self, outdir):
        self.dir = Path(outdir)
        self.files = [p for p in self.dir.rglob("*")
                      if p.is_file() and not p.name.startswith("_score")]
        self.readme = self._read("README.md")
        self.changelog = self._read("CHANGELOG.md")
        self.pys = sorted(p for p in self.files if p.suffix == ".py")
        self.py = self.pys[0].read_text(errors="replace") if self.pys else None
        self.tree = None
        if self.py is not None:
            try:
                self.tree = ast.parse(self.py)
            except SyntaxError:
                self.tree = None

    def _read(self, name):
        p = self.dir / name
        for c in self.files:
            if c.name == name:
                p = c
                break
        return p.read_text(errors="replace") if p.exists() else None

    def md(self, spec):
        for f in spec.split(","):
            t = self.readme if f == "README.md" else self.changelog
            yield f, t


def h2s(text):
    return [m.group(1).strip() for m in re.finditer(r"^## (.+)$", text, re.M)]


def section(text, name):
    m = re.search(rf"^## {re.escape(name)}\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else None


# ------------------------------------------------------------- custom checks
def cap_lumen(c):
    if not c.readme:
        return "ERR"
    bad = 0
    for _, t in c.md("README.md,CHANGELOG.md"):
        if t is None:
            continue
        p = strip_md_code(t)
        bad += len(re.findall(r"(?<![\w.$/-])lumen(?![\w.-])", p))
    return "VIOL" if bad else "SAT"


def one_h1_lumen(c):
    if not c.readme:
        return "ERR"
    h1 = re.findall(r"^# (.+)$", c.readme, re.M)
    return "SAT" if len(h1) == 1 and h1[0].strip() == "Lumen" else "VIOL"


def h1_first_line(c):
    if not c.readme:
        return "ERR"
    lines = [ln for ln in c.readme.splitlines() if ln.strip()]
    return "SAT" if lines and lines[0].startswith("# ") and c.readme.splitlines()[0].startswith("# ") else "VIOL"


REQ7 = ["Overview", "Installation", "Usage examples", "Options", "Exit codes", "Development", "License"]


def section_order(c):
    if not c.readme:
        return "ERR"
    seq = [t for t in h2s(c.readme) if t in REQ7]
    return "SAT" if seq == REQ7 else "VIOL"


def make_has_h2(name):
    def f(c):
        if not c.readme:
            return "ERR"
        return "SAT" if name in h2s(c.readme) else "VIOL"
    return f


def ends_license(c):
    if not c.readme:
        return "ERR"
    hs = h2s(c.readme)
    return "SAT" if hs and hs[-1] == "License" else "VIOL"


def options_is_table(c):
    if not c.readme:
        return "ERR"
    sec = section(c.readme, "Options")
    if sec is None:
        return "VIOL"
    return "SAT" if re.search(r"^\s*\|", sec, re.M) else "VIOL"


def options_3col(c):
    if not c.readme:
        return "ERR"
    sec = section(c.readme, "Options")
    if sec is None:
        return "VIOL"
    for line in sec.splitlines():
        if line.strip().startswith("|") and "---" not in line:
            cells = [x.strip() for x in line.strip().strip("|").split("|")]
            return "SAT" if cells == ["Option", "Argument", "Description"] else "VIOL"
    return "VIOL"


def three_invocations(c):
    if not c.readme:
        return "ERR"
    n = 0
    for lang, body in fences(c.readme):
        for ln in body:
            if re.match(r"^\s*(\$\s+)?(python3?\s+)?(lumen|\./lumen\.py|lumen\.py)\b", ln):
                n += 1
    return "SAT" if n >= 3 else "VIOL"


def bullets_star(c):
    star = dash = 0
    for _, t in c.md("README.md,CHANGELOG.md"):
        if t is None:
            continue
        out, in_f = [], False
        for line in t.splitlines():
            if re.match(r"^\s*```", line):
                in_f = not in_f
                continue
            if in_f:
                continue
            if re.match(r"^\s*\* ", line):
                star += 1
            if re.match(r"^\s*- ", line):
                dash += 1
    if star + dash == 0:
        return "NA"
    return "SAT" if dash == 0 else "VIOL"


def fences_have_lang(c):
    total = missing = 0
    for _, t in c.md("README.md,CHANGELOG.md"):
        if t is None:
            continue
        for lang, _b in fences(t):
            total += 1
            if not lang:
                missing += 1
    if total == 0:
        return "NA"
    return "SAT" if missing == 0 else "VIOL"


SHELLISH = {"bash", "sh", "shell", "zsh", "shell-session"}


def fences_console(c):
    if not c.readme:
        return "ERR"
    langs = [lang for lang, _ in fences(c.readme)] + ([lang for lang, _ in fences(c.changelog)] if c.changelog else [])
    if any(l in SHELLISH for l in langs):
        return "VIOL"
    return "SAT" if "console" in langs else "NA"


def prompt_marker(c):
    if not c.readme:
        return "ERR"
    seen = ok = 0
    for lang, body in fences(c.readme):
        if lang in SHELLISH or lang == "console":
            seen += 1
            first = next((ln for ln in body if ln.strip()), "")
            if first.startswith("$ "):
                ok += 1
    if seen == 0:
        return "NA"
    return "SAT" if ok == seen else "VIOL"


def output_text_fence(c):
    if not c.readme:
        return "ERR"
    langs = [lang for lang, _ in fences(c.readme)]
    if "text" in langs:
        return "SAT"
    if "" in langs:
        return "VIOL"
    return "NA"


def no_html(c):
    for _, t in c.md("README.md,CHANGELOG.md"):
        if t is None:
            continue
        p = strip_md_code(t)
        if re.search(r"<(?!https?:)[a-zA-Z][^>\n]*>", p):
            return "VIOL"
    return "SAT"


def filenames_backticked(c):
    if not c.readme:
        return "ERR"
    p = strip_md_code(c.readme)
    return "VIOL" if re.search(r"(?<![`\w/])(lumen\.py|CHANGELOG\.md|README\.md)\b", p) else "SAT"


def table_align_colons(c):
    found = bad = 0
    for _, t in c.md("README.md,CHANGELOG.md"):
        if t is None:
            continue
        for line in t.splitlines():
            if re.match(r"^\s*\|[\s:|-]+\|\s*$", line) and "-" in line:
                found += 1
                if ":" not in line:
                    bad += 1
    if not found:
        return "NA"
    return "SAT" if bad == 0 else "VIOL"


def line_length_100(c):
    if not c.readme:
        return "ERR"
    in_f = False
    for line in c.readme.splitlines():
        if re.match(r"^\s*```", line):
            in_f = not in_f
            continue
        if in_f or "|" in line or "http" in line:
            continue
        if len(line) > 100:
            return "VIOL"
    return "SAT"


def ordered_paren(c):
    dot = paren = 0
    for _, t in c.md("README.md,CHANGELOG.md"):
        if t is None:
            continue
        out, in_f = [], False
        for line in t.splitlines():
            if re.match(r"^\s*```", line):
                in_f = not in_f
                continue
            if in_f:
                continue
            if re.match(r"^\s*\d+\. ", line):
                dot += 1
            if re.match(r"^\s*\d+\) ", line):
                paren += 1
    if dot + paren == 0:
        return "NA"
    return "SAT" if dot == 0 else "VIOL"


def version_010_consistent(c):
    if c.py is None or c.changelog is None:
        return "ERR"
    return "SAT" if "0.1.0" in c.py and "0.1.0" in c.changelog else "VIOL"


def helpers_underscore(c):
    if c.tree is None:
        return "ERR"
    defs = [n for n in c.tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
    if not defs:
        return "NA"
    for d in defs:
        if d.name != "run" and not d.name.startswith("_"):
            return "VIOL"
    return "SAT"


def pathlib_not_ospath(c):
    if c.py is None:
        return "ERR"
    return "SAT" if "pathlib" in c.py and "os.path" not in c.py else "VIOL"


def _alldefs(tree):
    return [n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]


def all_defs_hinted(c):
    if c.tree is None:
        return "ERR"
    ds = _alldefs(c.tree)
    if not ds:
        return "NA"
    for d in ds:
        args = list(d.args.posonlyargs) + list(d.args.args) + list(d.args.kwonlyargs)
        if any(a.annotation is None for a in args) or d.returns is None:
            return "VIOL"
    return "SAT"


def all_defs_docstring(c):
    if c.tree is None:
        return "ERR"
    ds = _alldefs(c.tree)
    if not ds:
        return "NA"
    return "SAT" if all(ast.get_docstring(d) for d in ds) else "VIOL"


def module_doc_lumen(c):
    if c.tree is None:
        return "ERR"
    doc = ast.get_docstring(c.tree)
    return "SAT" if doc and doc.strip().startswith("Lumen:") else "VIOL"


def single_quotes(c):
    if c.py is None:
        return "ERR"
    try:
        toks = list(tokenize.generate_tokens(io.StringIO(c.py).readline))
    except Exception:
        return "ERR"
    fdepth = 0
    FS = getattr(tokenize, "FSTRING_START", None)
    FE = getattr(tokenize, "FSTRING_END", None)
    for tok in toks:
        s = tok.string
        if FS is not None and tok.type == FS:
            fdepth += 1
            if re.sub(r"^[a-zA-Z]*", "", s).startswith('"') and not re.sub(r"^[a-zA-Z]*", "", s).startswith('"""'):
                return "VIOL"
            continue
        if FE is not None and tok.type == FE:
            fdepth -= 1
            continue
        if tok.type == tokenize.STRING and fdepth == 0:
            body = re.sub(r"^[a-zA-Z]*", "", s)
            if body.startswith('"""') or body.startswith("'''"):
                continue
            if body.startswith('"'):
                return "VIOL"
    return "SAT"


def shebang_first(c):
    if c.py is None:
        return "ERR"
    lines = c.py.splitlines()
    return "SAT" if lines and lines[0].strip() == "#!/usr/bin/env python3" else "VIOL"


def imports_top(c):
    if c.tree is None:
        return "ERR"
    for d in _alldefs(c.tree):
        for n in ast.walk(d):
            if isinstance(n, (ast.Import, ast.ImportFrom)):
                return "VIOL"
    return "SAT"


def const_before_defs(c):
    if c.tree is None:
        return "ERR"
    first_def = None
    caps_after = caps = 0
    for i, n in enumerate(c.tree.body):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and first_def is None:
            first_def = i
        if isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Name) and re.match(r"^[A-Z][A-Z0-9_]+$", t.id):
                    caps += 1
                    if first_def is not None:
                        caps_after += 1
    if caps == 0:
        return "NA"
    return "SAT" if caps_after == 0 else "VIOL"


def fn_max_40(c):
    if c.tree is None:
        return "ERR"
    ds = _alldefs(c.tree)
    if not ds:
        return "NA"
    for d in ds:
        if (d.end_lineno - d.lineno + 1) > 40:
            return "VIOL"
    return "SAT"


def module_max_250(c):
    if c.py is None:
        return "ERR"
    return "SAT" if len(c.py.splitlines()) <= 250 else "VIOL"


def one_py_file(c):
    return "SAT" if len(c.pys) == 1 else ("ERR" if not c.pys else "VIOL")


def file_lumen_py(c):
    return "SAT" if any(p.name == "lumen.py" for p in c.files) else "VIOL"


def exactly_three_files(c):
    names = sorted(p.name for p in c.files)
    py = [n for n in names if n.endswith(".py")]
    ok = len(names) == 3 and "README.md" in names and "CHANGELOG.md" in names and len(py) == 1
    return "SAT" if ok else "VIOL"


def no_license_file(c):
    return "VIOL" if any(p.name.upper().startswith("LICENSE") for p in c.files) else "SAT"


def no_tests(c):
    bad = any(p.is_dir() and p.name == "tests" for p in c.dir.rglob("*")) or \
        any(p.name.startswith("test_") for p in c.files)
    return "VIOL" if bad else "SAT"


def chg_title(c):
    if c.changelog is None:
        return "ERR"
    h1 = re.findall(r"^# (.+)$", c.changelog, re.M)
    return "SAT" if h1 and h1[0].strip() == "Release history" else "VIOL"


def chg_version_format(c):
    if c.changelog is None:
        return "ERR"
    heads = re.findall(r"^## (.+)$", c.changelog, re.M)
    vers = [h for h in heads if h.strip() != "Unreleased"]
    if not vers:
        return "VIOL"
    for v in vers:
        if not re.match(r"^v\d+\.\d+\.\d+ \(\d{4}-\d{2}-\d{2}\)$", v.strip()):
            return "VIOL"
    return "SAT"


def chg_unreleased(c):
    if c.changelog is None:
        return "ERR"
    heads = re.findall(r"^## (.+)$", c.changelog, re.M)
    if not heads:
        return "VIOL"
    return "SAT" if heads[0].strip() == "Unreleased" else "VIOL"


def chg_verb_prefix(c):
    if c.changelog is None:
        return "ERR"
    bullets = [ln for ln in c.changelog.splitlines() if re.match(r"^\s*[*-] ", ln)]
    if not bullets:
        return "VIOL"
    for b in bullets:
        if not re.match(r"^\s*[*-] (Added|Changed|Fixed|Removed): ", b):
            return "VIOL"
    return "SAT"


def chg_bullets_only(c):
    if c.changelog is None:
        return "ERR"
    for ln in c.changelog.splitlines():
        s = ln.strip()
        if not s:
            continue
        if s.startswith("#") or re.match(r"^[*-] ", s) or re.match(r"^\s", ln):
            continue
        return "VIOL"
    return "SAT"


def chg_newest_first(c):
    if c.changelog is None:
        return "ERR"
    vers = re.findall(r"^## v?(\d+)\.(\d+)\.(\d+)", c.changelog, re.M)
    tup = [tuple(map(int, v)) for v in vers]
    if len(tup) <= 1:
        return "SAT" if tup else "NA"
    return "SAT" if tup == sorted(tup, reverse=True) else "VIOL"


def exit_two(c):
    """Exit status 2 as a literal, or via a module constant assigned 2
    (constant indirection satisfies the prose)."""
    if c.py is None:
        return "ERR"
    if re.search(r"sys\.exit\(2\)|SystemExit\(2\)|return 2\b|exit\(2\)", c.py):
        return "SAT"
    for m in re.finditer(r"^([A-Z][A-Z0-9_]*)\s*(?::\s*\w+\s*)?=\s*2\b", c.py, re.M):
        name = m.group(1)
        if re.search(rf"return {name}\b|sys\.exit\({name}\)|SystemExit\({name}\)", c.py):
            return "SAT"
    return "VIOL"


def round_four(c):
    """round(..., 4) literally, or round(..., CONST) where CONST is assigned 4
    (constant indirection satisfies the prose)."""
    if c.py is None:
        return "ERR"
    if re.search(r"round\(.*,\s*4\s*\)", c.py):
        return "SAT"
    m = re.search(r"round\(.*,\s*([A-Z][A-Z0-9_]*)\s*\)", c.py)
    if m and re.search(rf"^{m.group(1)}\s*(?::\s*\w+\s*)?=\s*4\b", c.py, re.M):
        return "SAT"
    return "VIOL"


def epilog_url(c):
    """Epilog set and the repository URL present in the module (literal or via
    a constant interpolated into the epilog)."""
    if c.py is None:
        return "ERR"
    has_epilog = re.search(r"epilog\s*=", c.py)
    has_url = "github.com/lumen-project/lumen" in c.py
    return "SAT" if (has_epilog and has_url) else "VIOL"


def chg_no_links(c):
    if c.changelog is None:
        return "ERR"
    return "VIOL" if ("](" in c.changelog or "http" in c.changelog) else "SAT"


def exit_codes_listed(c):
    if not c.readme:
        return "ERR"
    sec = section(c.readme, "Exit codes") or ""
    have = all(re.search(rf"\b{d}\b", sec) for d in "012")
    return "SAT" if have else "VIOL"


def no_emoji(c):
    pat = re.compile("[\U0001F000-\U0001FAFF☀-➿⬀-⯿️]")
    for _, t in c.md("README.md,CHANGELOG.md"):
        if t and pat.search(t):
            return "VIOL"
    return "SAT"


def no_hr(c):
    for _, t in c.md("README.md,CHANGELOG.md"):
        if t is None:
            continue
        in_f = False
        for line in t.splitlines():
            if re.match(r"^\s*```", line):
                in_f = not in_f
                continue
            if not in_f and re.match(r"^\s*(-{3,}|\*{3,}|_{3,})\s*$", line):
                return "VIOL"
    return "SAT"


def flags_backticked(c):
    if not c.readme:
        return "ERR"
    p = strip_md_code(c.readme)
    return "VIOL" if re.search(r"(?<![-`\w])--[a-z][a-z-]+\b", p) else "SAT"


def sorted_imports(c):
    """Accept either a single alphabetized sequence or the common grouped
    reading: plain imports and from-imports as two blocks, each alphabetized."""
    if c.tree is None:
        return "ERR"
    seq = []
    for n in c.tree.body:
        if isinstance(n, ast.Import):
            seq.append(("i", n.names[0].name))
        elif isinstance(n, ast.ImportFrom):
            if n.module == "__future__":
                continue
            seq.append(("f", n.module or ""))
    if len(seq) <= 1:
        return "NA"
    mods = [m for _, m in seq]
    if mods == sorted(mods):
        return "SAT"
    kinds = [k for k, _ in seq]
    grouped = kinds == sorted(kinds) or kinds == sorted(kinds, reverse=True)
    plain = [m for k, m in seq if k == "i"]
    froms = [m for k, m in seq if k == "f"]
    if grouped and plain == sorted(plain) and froms == sorted(froms):
        return "SAT"
    return "VIOL"


def two_blank_lines(c):
    if c.tree is None or c.py is None:
        return "ERR"
    lines = c.py.splitlines()
    ds = [n for n in c.tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
    if not ds:
        return "NA"
    for d in ds:
        start = min([d.lineno] + [dec.lineno for dec in d.decorator_list]) - 1
        if start < 2:
            return "VIOL"
        if lines[start - 1].strip() or lines[start - 2].strip():
            return "VIOL"
    return "SAT"


def no_comments(c):
    if c.py is None:
        return "ERR"
    try:
        toks = list(tokenize.generate_tokens(io.StringIO(c.py).readline))
    except Exception:
        return "ERR"
    for tok in toks:
        if tok.type == tokenize.COMMENT:
            if tok.start[0] <= 2 and (tok.string.startswith("#!") or "coding" in tok.string):
                continue
            return "VIOL"
    return "SAT"


CUSTOM = {f.__name__: f for f in [
    cap_lumen, one_h1_lumen, h1_first_line, section_order, ends_license,
    options_is_table, options_3col, three_invocations, bullets_star,
    fences_have_lang, fences_console, prompt_marker, output_text_fence,
    no_html, filenames_backticked, table_align_colons, line_length_100,
    ordered_paren, version_010_consistent, helpers_underscore,
    pathlib_not_ospath, all_defs_hinted, all_defs_docstring, module_doc_lumen,
    single_quotes, shebang_first, imports_top, const_before_defs, fn_max_40,
    module_max_250, one_py_file, file_lumen_py, exactly_three_files,
    no_license_file, no_tests, chg_title, chg_version_format, chg_unreleased,
    chg_verb_prefix, chg_bullets_only, chg_newest_first, chg_no_links, epilog_url, round_four, exit_two,
    exit_codes_listed, no_emoji, no_hr, flags_backticked, sorted_imports,
    two_blank_lines, no_comments]}
for name in REQ7:
    CUSTOM[f"has_h2:{name}"] = make_has_h2(name)


def check_rule(rid, spec, c):
    kind = spec["kind"]
    if kind == "custom":
        fn = spec["fn"]
        if fn == "has_h2":
            fn = f"has_h2:{spec['arg']}"
        return CUSTOM[fn](c)
    if kind in ("prose_requires_regex", "prose_bans_regex"):
        flags = re.I if spec.get("ci") else 0
        # requires-checks run on RAW markdown (required strings legitimately
        # live in fences/code spans); ban-checks run on code-stripped prose
        # unless the rule is explicitly structural (raw: True).
        raw = spec.get("raw", False) or kind == "prose_requires_regex"
        total = 0
        seen_any = False
        for fname, t in c.md(spec["file"]):
            if t is None:
                continue
            seen_any = True
            body = t if raw else strip_md_code(t)
            hits = len(re.findall(spec["pattern"], body, flags | re.M))
            if kind == "prose_requires_regex" and hits < spec.get("min", 1):
                # hard-wrapped prose can split a required phrase across lines
                norm = re.sub(r"[ \t]*\n[ \t]*", " ", body)
                hits = max(hits, len(re.findall(spec["pattern"], norm, flags)))
            total += hits
        if not seen_any:
            return "ERR"
        if kind == "prose_requires_regex":
            return "SAT" if total >= spec.get("min", 1) else "VIOL"
        return "VIOL" if total else "SAT"
    if kind in ("py_requires_regex", "py_bans_regex"):
        if c.py is None:
            return "ERR"
        hit = re.search(spec["pattern"], c.py, re.M)
        if kind == "py_requires_regex":
            return "SAT" if hit else "VIOL"
        return "VIOL" if hit else "SAT"
    raise ValueError(kind)


def score(outdir, rung="ALL"):
    c = Ctx(outdir)
    rules = LKEY["rules"]
    ids = LKEY["rungs"][str(rung)]["ids"] if rung != "ALL" else list(rules)
    res = {}
    for rid in ids:
        try:
            res[rid] = check_rule(rid, rules[rid]["check"], c)
        except Exception as e:
            res[rid] = f"ERR:{e}"
    return res


if __name__ == "__main__":
    outdir = sys.argv[1]
    rung = sys.argv[2] if len(sys.argv) > 2 else "ALL"
    res = score(outdir, rung)
    counts = {}
    for v in res.values():
        counts[v.split(":")[0]] = counts.get(v.split(":")[0], 0) + 1
    print(json.dumps({"outdir": outdir, "rung": rung, "counts": counts,
                      "viol": sorted(k for k, v in res.items() if v == "VIOL"),
                      "na": sorted(k for k, v in res.items() if v == "NA"),
                      "err": sorted(k for k, v in res.items() if v.startswith("ERR"))},
                     indent=1))
    json.dump(res, open(Path(outdir) / "_score.json", "w"), indent=1)
