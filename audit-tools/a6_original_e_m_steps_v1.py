#!/usr/bin/env python3
"""A6 historical ANEIC E/M-step smoke test on invented observations ONLY.

Uses the A6 private compat-v1 module, copies it to compat-v2 with a transparent
three-replacement delta, and calls original e_step and m_step on toy data.
Never edits original aneic-core / scripts, never reads the genuine corpus,
never runs historical training loops or cross-validation.
Requires numpy, pandas, scipy in the dedicated private venv.
"""
from __future__ import annotations
import csv
import difflib
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import subprocess
import sys

ROOT = Path("downloads/private-workflow/a6-reproduction")
REPORT = Path("downloads/private-review/a6-ivories")
CORE_SHA = "43a394f3a2409f2918d38f9d3cfc6dd5472970c1"
SRC = ROOT / "compat-v1/src/aneic/mfm.py"
DST = ROOT / "compat-v2/src/aneic/mfm.py"
FIXES = [
    (".as_matrix()", ".to_numpy()"),
    ("counts.sum(level=0)", "counts.groupby(level=0).sum()"),
    ("pi /= pi.sum(1)", "pi /= pi.sum()"),
]
checks = []

def check(name, condition, detail):
    ok = bool(condition)
    checks.append((name, "PASS" if ok else "FAIL", str(detail)))
    print(("PASS" if ok else "FAIL")+" | "+name+" | "+str(detail))

def close(a, b, tol=1e-10):
    return math.isclose(float(a), float(b), abs_tol=tol, rel_tol=tol)

def head(path):
    result = subprocess.run(["git", "-C", str(path), "rev-parse", "HEAD"],
                            text=True, capture_output=True, check=False)
    return result.stdout.strip() if result.returncode == 0 else None

def save(metadata):
    REPORT.mkdir(parents=True, exist_ok=True)
    with (REPORT/"A6_AUTHOR_E_M_TOY_CHECKS_PRIVATE.csv").open(
        "w", encoding="utf-8", newline=""
    ) as fh:
        writer = csv.writer(fh)
        writer.writerow(("check","status","detail"))
        writer.writerows(checks)
    passed = sum(s == "PASS" for _,s,_ in checks)
    failed = len(checks) - passed
    metadata.update({
        "passed": passed, "failed": failed,
        "status": "PASS" if failed == 0 else "FAIL",
        "limitations": [
            "Only four wholly invented observations.",
            "Only limited author e_step/m_step function calls.",
            "M-step pi.sum(1) corrected to pi.sum() as semantic normalization fix.",
            "Original historical EM loop, random restarts and CV NOT executed.",
            "The original source's MAP update formula is checked against literal "
            "arithmetic translation, not independently validated as the intended posterior.",
            "Missingness and one toy input do not establish full backward compatibility."
        ]
    })
    (REPORT/"A6_AUTHOR_E_M_TOY_REPORT_PRIVATE.json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False)+"\n",encoding="utf-8")
    print(f"\nOVERALL: {metadata['status']} — {passed} PASS / {failed} FAIL")
    print("PRIVATE reports:", REPORT)
    return failed == 0

def main():
    check("Fixed original core commit",head(ROOT/"aneic-core")==CORE_SHA,
          head(ROOT/"aneic-core"))
    check("V1 private compatibility copy exists",SRC.is_file(),SRC)
    if any(s=="FAIL" for _,s,_ in checks):
        save({"phase":"input validation"});return 1
    v1=SRC.read_text(encoding="utf-8")
    patched=v1
    expected={" .as_matrix()":2}
    for old,new in FIXES:
        n=patched.count(old)
        required=2 if old==".as_matrix()" else 1
        check(f"Exact V2 patch anchor: {old}",n==required,
              f"{n} occurrence(s), expected {required}")
        if n==required:
            patched=patched.replace(old,new)
    if any(s=="FAIL" for _,s,_ in checks):
        save({"phase":"patch preflight"});return 1
    DST.parent.mkdir(parents=True,exist_ok=True)
    if DST.exists():
        check("Existing V2 private work copy is identical",
              DST.read_text(encoding="utf-8")==patched,"refuse to overwrite differences")
    else:
        DST.write_text(patched,encoding="utf-8")
        check("Created isolated V2 private work copy",True,DST)
    if any(s=="FAIL" for _,s,_ in checks):
        save({"phase":"copy conflict"});return 1
    diff="".join(difflib.unified_diff(v1.splitlines(True),patched.splitlines(True),
                                    fromfile="PRIVATE/compat-v1/mfm.py",
                                    tofile="PRIVATE/compat-v2/mfm.py"))
    (DST.parents[2]/"A6_V1_TO_V2_PATCH_PRIVATE.patch").write_text(diff,encoding="utf-8")
    check("V1-to-V2 diff is nonempty",bool(diff),"patch saved privately")
    import numpy as np
    import pandas as pd
    import scipy
    spec=importlib.util.spec_from_file_location("a6_aneic_compat_v2_toy",DST)
    m=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)

    # Entirely synthetic; no genuine site, artifactual record or location.
    idx=["toy-1","toy-2","toy-3","toy-4"]
    real=pd.DataFrame({"x":[0.,2.,float("nan"),1.]},index=idx)
    raw=pd.Series(["A","B","A",None],index=idx)
    cat=m.convert_indicator(pd.DataFrame({"cat":raw},index=idx))
    states=[0,1]
    pi=pd.Series([.6,.4],index=states)
    mu=pd.DataFrame({0:[0.],1:[2.]},index=["x"])
    precision=pd.DataFrame({0:[1.],1:[1.]},index=["x"])
    rho=pd.DataFrame({0:[.8,.2],1:[.3,.7]},index=cat.columns)

    # Expected posteriors are computed independently using only math.
    def gaussian(x,mean):
        return math.exp(-.5*(x-mean)**2)/math.sqrt(2*math.pi)
    expectations=[]
    for i in range(4):
        x=real.iloc[i,0]
        value=raw.iloc[i]
        weights=[]
        for k in states:
            likelihood_n=1. if pd.isna(x) else gaussian(x,float(mu.loc["x",k]))
            likelihood_c=1. if pd.isna(value) else float(rho.loc[("cat",value),k])
            weights.append(float(pi[k])*likelihood_n*likelihood_c)
        expectations.append([w/sum(weights) for w in weights])
    expected=np.asarray(expectations)

    gamma,L=m.e_step(real,cat,pi,mu,precision,rho)
    g=gamma.to_numpy(dtype=float)
    check("Author e_step shape",g.shape==(4,2),str(g.shape))
    check("Author e_step posterior vs independent arithmetic",
          bool(np.allclose(g,expected,atol=1e-10,rtol=1e-10)),
          f"first={g[0,0]:.12f}; missing-x={g[2,0]:.12f}; missing-cat={g[3,0]:.12f}")
    check("Author e_step row normalization",bool(np.allclose(g.sum(axis=1),1.)),
          "four synthetic probability rows")
    objective=sum(math.log(sum([
        float(pi[k])*
        (1. if pd.isna(real.iloc[i,0]) else gaussian(float(real.iloc[i,0]),float(mu.loc["x",k])))*
        (1. if pd.isna(raw.iloc[i]) else float(rho.loc[("cat",raw.iloc[i]),k]))
        for k in states])) for i in range(4))
    check("Author unregularized E objective matches independent log-likelihood",
          close(L,objective),f"author={float(L):.10f}; independent={objective:.10f}")

    next_pi, next_mu, next_prec, next_rho=m.m_step(real,cat,gamma)
    ref_pi=expected.mean(axis=0)
    check("Author M mixture weights vs independent row averages",
          bool(np.allclose(next_pi.to_numpy(dtype=float),ref_pi)),
          [round(float(x),10) for x in next_pi])
    ref_mu=[]
    ref_var=[]
    for k in states:
        nonmissing=[i for i in range(4) if not pd.isna(real.iloc[i,0])]
        mass=sum(expected[i,k] for i in nonmissing)
        avg=sum(expected[i,k]*float(real.iloc[i,0]) for i in nonmissing)/mass
        ex2=sum(expected[i,k]*float(real.iloc[i,0])**2 for i in nonmissing)/mass
        ref_mu.append(avg)
        ref_var.append(1./(ex2-avg*avg))
    check("Author M means exclude missing numerical value",
          bool(np.allclose(next_mu.loc["x"].to_numpy(dtype=float),ref_mu)),
          [round(x,10) for x in ref_mu])
    check("Author M Gaussian precisions match weighted reciprocal variances",
          bool(np.allclose(next_prec.loc["x"].to_numpy(dtype=float),ref_var)),
          [round(x,10) for x in ref_var])
    categories=["A","B"]
    ref_rho=np.asarray([[
        sum(expected[i,k] for i in range(4) if raw.iloc[i]==category)/
        sum(expected[i,k] for i in range(4) if not pd.isna(raw.iloc[i]))
        for k in states] for category in categories])
    check("Author M category probabilities vs weighted counts",
          bool(np.allclose(next_rho.to_numpy(dtype=float),ref_rho)),
          "A/B per-state probabilities from observed toy categories")
    check("Author M category probabilities normalize per feature",
          bool(np.allclose(next_rho.sum(axis=0).to_numpy(dtype=float),1.)),
          "each cluster has A+B=1")

    # Only one MAP-prior branch is exercised: a=2, b>0, alpha/beta None.
    # This directly checks implementation arithmetic, not historical inference.
    a=2.
    b=pd.DataFrame({0:[2.],1:[2.]},index=["x"])
    prior_pi,prior_mu,prior_prec,prior_rho=m.m_step(
        real,cat,gamma,a=a,b=b,alpha=None,beta=None)
    check("MAP Gaussian precision branch yields finite positive output",
          bool(np.isfinite(prior_prec.to_numpy()).all() and
               (prior_prec.to_numpy()>0).all()),
          prior_prec.to_numpy().tolist())
    nu=2*(a-1)
    ref_prior=[]
    for k in states:
        observations=[i for i in range(4) if not pd.isna(real.iloc[i,0])]
        mass=sum(expected[i,k] for i in observations)
        X=sum(expected[i,k]*float(real.iloc[i,0]) for i in observations)
        X2=sum(expected[i,k]*float(real.iloc[i,0])**2 for i in observations)
        mean=X/mass
        chi=4.-nu*mean**2
        ref_prior.append(1./((X2-2*mean*X+chi)/(mass+nu)+mean**2))
    check("MAP precision agrees with literal historical update expression",
          bool(np.allclose(prior_prec.loc["x"].to_numpy(dtype=float),ref_prior)),
          "a=2, b=2, one Gaussian feature")
    _, regularized_L=m.e_step(
        real,cat,prior_pi,prior_mu,prior_prec,prior_rho,a=a,b=b)
    check("Author E objective with Gaussian prior produces finite scalar",
          bool(np.isfinite(float(regularized_L))),
          f"MAP objective={float(regularized_L):.10f}")
    check("Original fixed commit remains unchanged",head(ROOT/"aneic-core")==CORE_SHA,
          head(ROOT/"aneic-core"))
    metadata={
       "phase":"toy E/M functions with isolated V2 patch",
       "python":sys.version.split()[0],"numpy":np.__version__,
       "pandas":pd.__version__,"scipy":scipy.__version__,
       "compat_v1_sha256":hashlib.sha256(v1.encode()).hexdigest(),
       "compat_v2_sha256":hashlib.sha256(patched.encode()).hexdigest()
    }
    return 0 if save(metadata) else 1

if __name__=="__main__":
    try: sys.exit(main())
    except Exception as err:
        check("Unexpected compatibility/runtime exception",False,
              type(err).__name__+": "+str(err))
        save({"phase":"exception","exception_type":type(err).__name__})
        raise
