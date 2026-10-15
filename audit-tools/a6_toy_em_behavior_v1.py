#!/usr/bin/env python3
"""A6 V1 independent TOY numerical behavior tests (not ANEIC implementation).

Runs only original synthetic numbers created below. No source CSV is opened.
No author module is imported or patched. Python standard library only.
Outputs aggregate PASS/FAIL to ignored downloads/private-review/a6-ivories.
"""
import csv
import math
from pathlib import Path
import sys

OUT = Path("downloads/private-review/a6-ivories")
OUT.mkdir(parents=True, exist_ok=True)
checks = []

def check(label, condition, detail):
    ok = bool(condition)
    checks.append((label, "PASS" if ok else "FAIL", str(detail)))
    print(("PASS" if ok else "FAIL"), "|", label, "|", detail)

def close(a, b, tol=1e-11):
    return math.isclose(a, b, abs_tol=tol, rel_tol=tol)

def normal_pdf(x, mu, sigma=1.0):
    return math.exp(-0.5 * ((x-mu)/sigma)**2)/(math.sqrt(2 * math.pi)*sigma)

def one_hot(value):
    if value is None:
        return {"A": None, "B": None}
    return {k: float(k == value) for k in ("A", "B")}

# SYNTHETIC rows; every input (including apparent provenance) is invented.
toy = [{"x": 0.0, "cat": "A"},
       {"x": 2.0, "cat": "B"},
       {"x": None, "cat": "A"},
       {"x": 1.0, "cat": None}]
pi = [0.6, 0.4]
mu = [0.0, 2.0]
cat_prob = [{"A": 0.8, "B": 0.2}, {"A": 0.3, "B": 0.7}]

encoded = [one_hot(r["cat"]) for r in toy]
check("Toy one-hot category order",
      list(encoded[0]) == ["A", "B"] and encoded[0] == {"A": 1.0, "B": 0.0},
      "A => [1,0]")
check("Toy categorical missingness not converted to zero",
      encoded[3]["A"] is None and encoded[3]["B"] is None,
      "missing category retains missing indicators")

def component_probability(record, k):
    # Missing observations contribute multiplicative factor ONE
    # (zero contribution in log-likelihood). This is the reference
    # contract to later test against historical source, not a claim
    # about historical execution.
    numeric = 1.0 if record["x"] is None else normal_pdf(record["x"], mu[k])
    category = 1.0 if record["cat"] is None else cat_prob[k][record["cat"]]
    return pi[k] * numeric * category

resp = []
for record in toy:
    weights = [component_probability(record, k) for k in range(2)]
    resp.append([v/sum(weights) for v in weights])
check("Toy E-step posterior normalization",
      all(close(sum(r), 1.0) and all(math.isfinite(v) and v >= 0 for v in r) for r in resp),
      "four synthetic responsibilities each sum to one")

manual = (pi[0] * normal_pdf(0.0, 0.0) * 0.8)
manual2 = (pi[1] * normal_pdf(0.0, 2.0) * 0.3)
check("Toy E-step independently calculated first-row posterior",
      close(resp[0][0], manual/(manual+manual2)),
      f"observed {resp[0][0]:.12f}")

# If numerical value is missing, only category discriminates; if category
# is missing, only normal density discriminates.
expected_missing_x = (pi[0]*0.8)/(pi[0]*0.8+pi[1]*0.3)
check("Missing numeric variable is neutral in toy likelihood",
      close(resp[2][0], expected_missing_x),
      f"observed {resp[2][0]:.12f}")
expected_missing_cat = (pi[0]*normal_pdf(1, 0))/(pi[0]*normal_pdf(1, 0)+pi[1]*normal_pdf(1, 2))
check("Missing category is neutral in toy likelihood",
      close(resp[3][0], expected_missing_cat),
      f"observed {resp[3][0]:.12f}")

new_pi = [sum(g[k] for g in resp)/len(resp) for k in range(2)]
check("Toy M-step mixture-weight normalization",
      close(sum(new_pi), 1.0) and all(p > 0 for p in new_pi),
      f"pi = [{new_pi[0]:.6f}, {new_pi[1]:.6f}]")
# Weighted numeric means use ONLY observed values, not missing-as-zero.
means = []
for k in range(2):
    denom = sum(resp[i][k] for i, r in enumerate(toy) if r["x"] is not None)
    numer = sum(resp[i][k] * r["x"] for i, r in enumerate(toy) if r["x"] is not None)
    means.append(numer/denom)
check("Toy M-step numeric missing rows excluded from denominator",
      all(math.isfinite(v) and 0 <= v <= 2 for v in means),
      f"means = [{means[0]:.6f}, {means[1]:.6f}]")

# Per-feature categorical counts exclude missing category; use conditional
# normalisation within that feature (not across all distinct columns).
cat_updated = []
for k in range(2):
    counts = {c: sum(resp[i][k] for i,r in enumerate(toy) if r["cat"] == c)
              for c in ("A", "B")}
    denom = sum(counts.values())
    cat_updated.append({c: counts[c]/denom for c in counts})
check("Toy M-step categorical grouping normalizes independently",
      all(close(sum(p.values()), 1.0) for p in cat_updated),
      "probabilities within A/B feature each sum to one")

# A limited fixed-variance EM monotonicity check using invented data only:
# updates mixture weights and Gaussian means. Categorical probabilities and
# Gaussian variance stay FIXED. This is NOT ANEIC's full MAP M-step.
def toy_loglik(pi_, mu_):
    total = 0.0
    for row in toy:
        components = []
        for k in range(2):
            n = 1.0 if row["x"] is None else normal_pdf(row["x"], mu_[k])
            c = 1.0 if row["cat"] is None else cat_prob[k][row["cat"]]
            components.append(pi_[k] * n * c)
        total += math.log(sum(components))
    return total
before = toy_loglik(pi, mu)
after = toy_loglik(new_pi, means)
check("One synthetic restricted EM update is nondecreasing",
      after + 1e-12 >= before, f"before={before:.9f}; after={after:.9f}")

with (OUT / "A6_TOY_BEHAVIOR_CHECKS_PRIVATE.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(("check", "status", "detail"))
    w.writerows(checks)
total_pass = sum(x[1] == "PASS" for x in checks)
total_fail = len(checks)-total_pass
with (OUT / "A6_TOY_BEHAVIOR_REPORT_PRIVATE.md").open("w", encoding="utf-8") as f:
    f.write("# A6 synthetic numerical behavior specification — PRIVATE\n\n")
    f.write("NOT an ANEIC run, and NOT a reproduction of the original research.\n\n")
    f.write(f"Checks: {total_pass} PASS / {total_fail} FAIL.\n")
    f.write("Covers posterior normalization, neutral missing-value factors, toy weighted updates and one restricted EM comparison.\n")
    f.write("Original 2014 MAP priors, unknown data processing, numerical implementation and full E/M remain untested.\n")
print(f"\nOVERALL: {'PASS' if total_fail == 0 else 'FAIL'} — {total_pass} PASS / {total_fail} FAIL")
print("PRIVATE reports:", OUT)
sys.exit(1 if total_fail else 0)
