#!/usr/bin/env python3
"""A6 PR21: bounded original ANEIC em() loop diagnostics, synthetic data only.

Uses a PRIVATE compat-v2 module made by PR20. Creates compat-v3 in an ignored
folder. Does not modify historical Git clones or read the genuine ivory CSV.
Not a reproduction of the 2014 published results. Requires NumPy/pandas/SciPy.
"""
from __future__ import annotations
import csv
import difflib
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import traceback

BASE = Path("downloads/private-workflow/a6-reproduction")
OUT = Path("downloads/private-review/a6-ivories")
SOURCE = BASE / "compat-v2/src/aneic/mfm.py"
DEST = BASE / "compat-v3/src/aneic/mfm.py"
CORE_SHA = "43a394f3a2409f2918d38f9d3cfc6dd5472970c1"
checks = []

def check(name, condition, detail):
    state = "PASS" if bool(condition) else "FAIL"
    checks.append((name, state, str(detail)))
    print(state, "|", name, "|", detail)

def head(path):
    p = subprocess.run(["git", "-C", str(path), "rev-parse", "HEAD"],
                       capture_output=True, text=True, check=False)
    return p.stdout.strip() if p.returncode == 0 else None

def report(stage, extra=None):
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT/"A6_AUTHOR_FULL_EM_TOY_CHECKS_PRIVATE.csv").open(
        "w", encoding="utf-8", newline=""
    ) as f:
        w = csv.writer(f)
        w.writerow(["check", "status", "detail"])
        w.writerows(checks)
    passed = sum(x[1] == "PASS" for x in checks)
    failed = sum(x[1] == "FAIL" for x in checks)
    meta = {
        "stage": stage, "passed": passed, "failed": failed,
        "status": "PASS" if failed == 0 else "FAIL",
        "limitations": [
            "All inputs are invented; no real ivory dataset is opened.",
            "Compat-v3 modifies the original EM control flow/parameter names.",
            "No authors' historical run, K sweep, cross-validation or paper results.",
            "Iteration stop and returned q/g alignment are assessed separately.",
            "The original MAP formula's mathematical validity is not established."
        ],
    }
    if extra: meta.update(extra)
    (OUT/"A6_AUTHOR_FULL_EM_TOY_REPORT_PRIVATE.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2)+"\n", encoding="utf-8"
    )
    print("\nOVERALL:", meta["status"], f"— {passed} PASS / {failed} FAIL")
    print("Private reports:", OUT)
    return failed == 0

def main():
    check("Original core Git commit unchanged",
          head(BASE/"aneic-core") == CORE_SHA, head(BASE/"aneic-core"))
    check("PR20 compat-v2 available", SOURCE.is_file(), SOURCE)
    if any(s == "FAIL" for _,s,_ in checks):
        report("preflight"); return 1
    old = SOURCE.read_text(encoding="utf-8")
    # Strictly scope semantic edits to the original em() function.
    anchor = "\ndef em(real, cat, K=None, u=None, eps=1e-5, max_iter=100, g0=None, theta0=None):"
    check("Single original EM function anchor", old.count(anchor) == 1, old.count(anchor))
    if checks[-1][1] == "FAIL":
        report("preflight");return 1
    before, em = old.split(anchor, 1)
    substitutions = [
        ("{'a': None, 'b': None, 'rho': None, 'z': None}",
         "{'a': None, 'b': None, 'alpha': None, 'beta': None}", 1,
         "Align default prior option keys"),
        ("u['a'], u['b'], u['rho'], u['z']",
         "u['a'], u['b'], u['alpha'], u['beta']", 3,
         "Align all three E/M prior argument sites"),
        ("if g0 is None and (not K is None):",
         "if g0 is None and (K is not None):", 1,
         "Simplify K initialization condition without changing truth value"),
        ("    else: \n        raise ValueError('One of K, g0, or theta0 must be specified.')",
         "    elif g0 is None:\n        raise ValueError('One of K, g0, or theta0 must be specified.')", 1,
         "Accept explicit g0 and theta0 initialization"),
    ]
    modified = em
    for target, replacement, required, label in substitutions:
        n = modified.count(target)
        check("Scoped patch: "+label, n == required, f"found {n}; expected {required}")
        if n == required:
            modified = modified.replace(target, replacement)
    if any(s == "FAIL" for _,s,_ in checks):
        report("patch anchors");return 1
    patched = before + anchor + modified
    DEST.parent.mkdir(parents=True, exist_ok=True)
    if DEST.exists():
        check("Private compat-v3 matches expected patch",
              DEST.read_text(encoding="utf-8") == patched,
              "no overwrite of conflicting copy")
    else:
        DEST.write_text(patched, encoding="utf-8")
        check("Private compat-v3 created", True, DEST)
    if checks[-1][1] == "FAIL":
        report("patch conflict");return 1
    patch = "".join(difflib.unified_diff(old.splitlines(True),patched.splitlines(True),
        fromfile="PRIVATE/compat-v2/mfm.py",tofile="PRIVATE/compat-v3/mfm.py"))
    (BASE/"compat-v3/A6_V2_TO_V3_PATCH_PRIVATE.patch").write_text(patch,encoding="utf-8")
    check("Patch is limited to EM function",
          patched.startswith(before+anchor) and bool(patch), "diff stored privately")

    import numpy as np
    import pandas as pd
    import scipy
    spec = importlib.util.spec_from_file_location("a6_author_em_v3_toy",DEST)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Completely invented numbers, with more observations to avoid a toy singularity.
    idx = [f"toy-{i:02d}" for i in range(1,9)]
    x = [-2.0, -1.1, -0.3, 0.4, 1.0, 1.6, 2.5, float("nan")]
    labels = ["A","A","B","A","B","B","B",None]
    real = pd.DataFrame({"x":x}, index=idx)
    cat = module.convert_indicator(pd.DataFrame({"cat":labels}, index=idx))

    # Only two components; a=2, b=2 regularizes Gaussian precision.
    u = {
        "a": 2.0,
        "b": pd.DataFrame({0:[2.0],1:[2.0]}, index=["x"]),
        "alpha": None,
        "beta": None,
    }
    runs = []
    for run in range(2):
        np.random.seed(17)
        q, gamma, L, g0 = module.em(real,cat,K=2,u=u,eps=1e-8,max_iter=3)
        runs.append((q,gamma,L,g0))
    q,g,L,g0 = runs[0]
    check("Historical em() completes with bounded synthetic setup",
          len(L)>0 and len(L)<=8, "recorded objective values="+str(len(L)))
    vals = np.asarray(L, dtype=float)
    check("Recorded objectives are finite", bool(np.isfinite(vals).all()),
          [round(float(t),8) for t in vals])
    check("Responsibility matrix shape and simplex",
          g.shape==(8,2) and bool(np.allclose(g.sum(axis=1).to_numpy(),1.0)),
          f"shape={g.shape}")
    check("Initial weights are normalized", bool(np.allclose(g0.sum(axis=1),1.0)),
          "K=2 Dirichlet seed 17")
    check("Mixture proportions normalize", bool(np.isclose(float(q["pi"].sum()),1)),
          q["pi"].to_dict())
    check("Gaussian precision finite and positive",
          bool(np.isfinite(q["l"].to_numpy()).all() and
               (q["l"].to_numpy()>0).all()),
          q["l"].to_numpy().tolist())
    check("Categorical probabilities normalize",
          bool(np.allclose(q["rho"].groupby(level=0).sum().to_numpy(),1.0)),
          "per feature by cluster")
    run2 = runs[1]
    check("Same seed yields same objective trace",
          bool(np.allclose(vals,np.asarray(run2[2], dtype=float),atol=1e-12)),
          "seed=17 repeated run")
    check("Same seed yields same final mixture proportions",
          bool(np.allclose(q["pi"].to_numpy(),run2[0]["pi"].to_numpy())),
          "K=2 repeated run")
    # Diagnostic only: original stopping rule/returned q/g phase alignment
    # cannot be established from completing a bounded run.
    check("Original source retains unmodified stopping condition",
          "if it > 1 and ((dL < eps) or it > max_iter):" in patched,
          "no convergence claim; inspect return semantics in next phase")
    check("Original commit still fixed", head(BASE/"aneic-core")==CORE_SHA,
          head(BASE/"aneic-core"))
    meta = {
        "python": sys.version.split()[0], "numpy": np.__version__,
        "pandas": pd.__version__, "scipy": scipy.__version__,
        "source_sha256": hashlib.sha256(old.encode()).hexdigest(),
        "compat_v3_sha256": hashlib.sha256(patched.encode()).hexdigest(),
        "iterations_reported": len(L),
        "max_iter_config": 3, "seed":17,"K":2,
        "objective_trace":[float(v) for v in vals],
    }
    return 0 if report("bounded synthetic original EM",meta) else 1

if __name__=="__main__":
    try:
        sys.exit(main())
    except Exception as err:
        check("Unexpected source function / environment exception", False,
              type(err).__name__+": "+str(err))
        report("exception",{"exception":traceback.format_exc(limit=8)})
        raise
