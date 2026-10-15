#!/usr/bin/env python3
"""ANEIC A6: read-only static compatibility and provenance audit (stdlib only).

Usage:
 python3 audit-tools/a6_original_python_compatibility_v1.py \
   downloads/private-workflow/a6-reproduction/aneic-core \
   downloads/private-workflow/a6-reproduction/aneic-scripts

Does not import the original modules, install dependencies, run the model,
modify cloned sources, or publish source records. Writes aggregate reports
only under downloads/private-review/a6-ivories.
"""
import ast
import csv
import hashlib
import json
import pathlib
import re
import subprocess
import sys

CORE_SHA = "43a394f3a2409f2918d38f9d3cfc6dd5472970c1"
SCRIPTS_SHA = "c45445a0e090853c6eb544bffe8042557e4db440"
REL_PATHS = {
    "core_algorithm": ("core", "src/aneic/mfm.py"),
    "core_helper": ("core", "src/aneic/mutual.py"),
    "runner": ("scripts", "130317_01_mfm_sigma_1.0_a_2.0/run_mfm.py"),
    "analysis": ("scripts", "130317_01_mfm_sigma_1.0_a_2.0/analysis_mfm.py"),
    "cv_runner": ("scripts", "130219_01_mfm_sigma_1.0_a_1.001_1_cv_5/run_mfm_cv.py"),
}
OUTPUT = pathlib.Path("downloads/private-review/a6-ivories")

def git_sha(root):
    try:
        p = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"],
                           check=True, capture_output=True, text=True)
        return p.stdout.strip()
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None

def label(name, matched, detail):
    result = "PASS" if matched else "FAIL"
    tests.append((name, result, detail))
    print(result, "|", name, "|", detail)

if len(sys.argv) != 3:
    raise SystemExit("Usage: python3 audit-tools/a6_original_python_compatibility_v1.py <core-clone> <scripts-clone>")
roots = {"core": pathlib.Path(sys.argv[1]).expanduser().resolve(),
         "scripts": pathlib.Path(sys.argv[2]).expanduser().resolve()}
OUTPUT.mkdir(parents=True, exist_ok=True)
tests = []
markers = []
sources = {}

for name, root, expected in (
    ("aneic-core", roots["core"], CORE_SHA),
    ("aneic-scripts", roots["scripts"], SCRIPTS_SHA),
):
    current = git_sha(root)
    label(name + " checked-out SHA", current == expected, current or "not a valid Git checkout")

for label_name, (origin, relative) in REL_PATHS.items():
    file = roots[origin] / relative
    valid = file.is_file()
    label(label_name + " source exists", valid, relative)
    if valid:
        data = file.read_bytes()
        try:
            sources[label_name] = data.decode("utf-8")
        except UnicodeDecodeError:
            sources[label_name] = data.decode("latin-1")
        markers.append((label_name, "source SHA256", "digest", hashlib.sha256(data).hexdigest(), relative))

patterns = {
    "python2 print statements": r"(?m)^\s*print\s+['\"]",
    "deprecated NumPy np.object": r"\bnp\.object\b",
    "deprecated NumPy np.int": r"\bnp\.int\b",
    "deprecated NumPy np.float": r"\bnp\.float\b",
    "removed pandas .ix indexing": r"\.ix\s*\[",
    "old pandas Categorical.from_array": r"Categorical\.from_array",
    "old pandas categorical levels/labels": r"\bcat\.(?:levels|labels)\b",
    "Python2 gzip pickle text mode": r"pickle\.dump[\s\S]{0,180}gzip\.open[\s\S]{0,160}['\"]w['\"]",
    "hard-coded relative project topology": r"work_dir\s*=\s*os\.getcwd\(\)",
    "CV placeholders NU/FOLD": r"\b(?:NU|FOLD)\b",
}
for name, content in sources.items():
    for label_text, regex in patterns.items():
        count = len(re.findall(regex, content))
        if count:
            markers.append((name, label_text, "observed", str(count), REL_PATHS[name][1]))

runner = sources.get("runner", "")
cv = sources.get("cv_runner", "")
core = sources.get("core_algorithm", "")
label("runner uses Site exclusion", bool(re.search(r"['\"]drop_feats['\"]\s*:\s*\[\s*['\"]Site['\"]",runner)), "drop_feats=['Site']")
label("runner uses no object exclusion", bool(re.search(r"['\"]drop_objs['\"]\s*:\s*\[\s*\]",runner)), "drop_objs=[]")
label("runner scans K=2 through K=10", "'K' : [2,3,4,5,6,7,8,9,10]" in runner, "candidate K values")
label("runner has a=2.0 and seed=1", bool(re.search(r"['\"]a['\"]\s*:\s*2\.0",runner)) and bool(re.search(r"['\"]seed['\"]\s*:\s*1",runner)), "one historical run configuration")
label("core declares EM implementation", bool(re.search(r"(?m)^def em\s*\(",core)), "aneic.mfm.em")
label("CV runner references NU and FOLD", bool(re.search(r"['\"]a['\"]\s*:\s*1\s*\+\s*NU",cv)) and bool(re.search(r"['\"]cv_fold['\"]\s*:\s*FOLD",cv)), "external invocation context required")

for key, content in sources.items():
    try:
        ast.parse(content)
        markers.append((key, "Python 3 AST parse", "PASS", "accepted", REL_PATHS[key][1]))
    except SyntaxError as exc:
        markers.append((key, "Python 3 AST parse", "BLOCKED", "line " + str(exc.lineno) + ": " + (exc.msg or "syntax error"), REL_PATHS[key][1]))

# Identify use without importing or running source. These tests are deliberately static.
with (OUTPUT / "A6_COMPAT_CHECKS_PRIVATE.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.writer(f); w.writerow(("check", "status", "detail")); w.writerows(tests)
with (OUTPUT / "A6_COMPAT_MARKERS_PRIVATE.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.writer(f); w.writerow(("source", "marker", "status", "evidence", "relative_path")); w.writerows(markers)
report = [
    "# A6 static compatibility review — PRIVATE", "",
    "No author model code was imported, executed, converted, or edited.",
    "Input provenance:",
    "- aneic-core expected commit: " + CORE_SHA,
    "- aneic-scripts expected commit: " + SCRIPTS_SHA,
    "File existence & method checks: " + str(sum(s == "PASS" for _, s, _ in tests)) +
        " PASS / " + str(sum(s == "FAIL" for _, s, _ in tests)) + " FAIL.",
    "",
    "Compatibility markers (present is NOT a PASS for modern execution):",
]
report += ["- " + src + ": " + m + " [" + status + "] " + evidence
           for src, m, status, evidence, _ in markers if m != "source SHA256"]
report += ["", "This does not establish runtime compatibility, identical numerical behavior,",
           "matching paper tables/figures, or permission to redistribute the corpus.",
           "The historical Python 2 environment and pandas/numpy versions are NOT inferred here."]
(OUTPUT / "A6_COMPAT_REPORT_PRIVATE.md").write_text("\n".join(report) + "\n", encoding="utf-8")
ok = all(s == "PASS" for _, s, _ in tests)
print("\nSTATIC INPUT/ENTRY CHECK:", "PASS" if ok else "FAIL", "—", sum(s == "PASS" for _, s, _ in tests), "PASS /", sum(s == "FAIL" for _, s, _ in tests), "FAIL")
print("Compatibility blockers are listed separately and are NOT cleared by a PASS.")
print("PRIVATE reports:", OUTPUT)
sys.exit(0 if ok else 1)
