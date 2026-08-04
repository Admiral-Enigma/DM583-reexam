# Sample MCQ (official example paper) — Tool Walkthrough

Source: `old_cheatsheets/Sample MCQ Questions - DM583 Data Mining.pdf` (3 questions, 15 subs).
Every sub is either a tool read-off or one playbook fact (numbers reference `playbook.md`).
All computed values below verified live against `src/exam` (2026-08-04).

## Q1 · EM-GMM theory

```python
responsibilities([0.0086, 0.0136], [0.3, 0.7])   # sub 3 -> [0.2132, 0.7868]
```

| # | Claim | How settled | Verdict |
|---|-------|-------------|---------|
| 1 | EM-GMM uses Bayes' rule | fact 7 — the E-step IS Bayes: γᵢ ∝ πᵢ·fᵢ(x) | **T** |
| 2 | Assumes independence within clusters (zero covariance) | fact 8 — full-covariance GMM allows arbitrary within-cluster covariance | **F** |
| 3 | densities 0.0086/0.0136, priors 0.3/0.7 → posteriors ≈ 0.213/0.787 | tool: 0.2132 / 0.7868 — exact match | **T** |
| 4 | Diagonal Σ ⇒ necessarily spherical clusters | fact 8 — diagonal = axis-aligned **ellipses**; spherical needs equal variances | **F** |
| 5 | EM-GMM not sensitive to initialization (unlike k-Means) | fact 7 — local optima, same as k-Means | **F** |

## Q2 · Dataset {−20, −10, 10, 40, 55, 95, 100}

```python
d2 = [-20, -10, 10, 40, 55, 95, 100]
mle(d2)                                          # sub 1
D = proxmat([[x] for x in d2], mand)
ahc(D, "single"); ahc(D, "complete")             # sub 2
pts = " / ".join(f"P{i} {x}" for i, x in enumerate(d2, 1))
analyze(pts, "man", k=1)                         # sub 4
analyze(pts, "man", db=[(15, 1), (15, 2)])       # sub 5
```

| # | Claim | How settled | Verdict |
|---|-------|-------------|---------|
| 1 | MLE Gaussian: μ = sample mean, σ² = Σ(x−μ)²/7 | `mle` prints exactly these formulas (**/n**, not n−1) — fact 12 | **T** |
| 2 | 1-D ⇒ single-linkage = complete-linkage necessarily | tool counterexample: single merges {−20,−10,10}∪{40,55}@30 then {95,100}@40; complete pairs {40,55}∪{95,100}@60 first, root@120 — different **topology**, not just heights | **F** |
| 3 | Parallel k-Means impossible with odd n (can't split evenly) | fact 15 — distributed k-Means is exact via per-site (count, sum); no even-split requirement | **F** |
| 4 | kNN outlier k=1 scores = {10, 10, 20, 15, 15, 5, 5} | tool reproduces the list point-for-point; "any Minkowski" safe: in 1-D all Lp coincide (fact 9) | **T** |
| 5 | ε=15, MinPts=1 or 2: both give 4 clusters incl. C2={10} | MinPts=1 → 4 clusters, {10} a singleton **cluster** ✓; MinPts=2 → {10} is **noise**, 3 clusters — "in both cases" fails (fact 10) | **F** |

## Q3 · Apriori (word items!), σ = 5 (count)

Items are words → pass **lists**, never `"BM"`-style strings.

```python
db = parse_db("""BEER,CRACKERS / BREAD,BUTTER,DIAPERS,MILK / BEER,DIAPERS /
BREAD,BUTTER,DIAPERS,MILK / BREAD,BUTTER,DIAPERS,MILK / BEER,CRACKERS,DIAPERS /
BREAD,BUTTER,CRACKERS / BREAD,CRACKERS,DIAPERS,MILK / BREAD,BUTTER,MILK /
BEER,BREAD,DIAPERS,MILK / BUTTER,DIAPERS / BREAD,BUTTER,DIAPERS""")   # N=12 — check!
apriori(db, 5)
is_maximal(db, ["DIAPERS", "MILK"], thresh=5)      # sub 3 -> False
is_closed(db, ["BREAD", "DIAPERS"])                # sub 4 -> True
rule(db, ["DIAPERS"], ["BREAD", "MILK"])           # sub 5 -> supp 5, conf 5/9
```

`apriori` printout: L1 → BREAD(8), BUTTER(7), DIAPERS(9), MILK(6) frequent (BEER, CRACKERS out).
L2 → 6 candidates, {BUTTER,MILK}(4) fails → 5 frequent. L3 → join produces {B,Bu,D}, {B,Bu,M},
{B,D,M}; **prune removes {B,Bu,M}** ({BUTTER,MILK} infrequent); counts: {B,Bu,D}=4 fails,
**{B,D,M}=5 frequent**.

| # | Claim | How settled | Verdict |
|---|-------|-------------|---------|
| 1 | {BUTTER,DIAPERS,MILK} produced from the **candidate** 2-itemsets, support computed as 3 | candidates come from **frequent** 2-itemsets (hinge word); the join never generates it (L3 shows only BREAD-prefixed triples) — its support is never computed | **F** |
| 2 | {BREAD,BUTTER,MILK} produced from frequent 2-itemsets, then support **must** be computed | produced by the join, yes — then **pruned** ({BUTTER,MILK} infrequent), so support is never computed; the prune line in the printout is the answer | **F** |
| 3 | {DIAPERS,MILK} maximal, ascertainable **from the table alone** | the table can't settle it ({B,D,M} is a surviving candidate whose support isn't shown) — and supp(B,D,M)=5 is a frequent superset, so DM isn't even maximal | **F** |
| 4 | {BREAD,DIAPERS} is closed | `is_closed` → True: supp 6; supersets {B,Bu,D}=4, {B,D,M}=5 — none equals 6 (fact 11) | **T** |
| 5 | Rule DIAPERS ⇒ {BREAD,MILK}: supp 5, conf 5/9 | `rule` prints supp count 5, conf 5/9; and it follows from frequent 3-set {B,D,M} | **T** |

## Answer key + takeaways

```
Q1: T F T F F     Q2: T F F T F     Q3: F F F T T
```

- 12/15 subs are direct tool read-offs; 3 are playbook facts (7, 8, 15). Zero blanks needed.
- 9/15 are **False via a single hinge word**: *candidates*, *necessarily*, *guaranteed*,
  *both cases*, *ascertain from the table alone*. The examiner's bait style is stable
  across papers — find the hinge word, check it against output.
- New sub-types vs June this paper introduced, all covered: E-step posteriors,
  MLE, closed/maximal, MinPts=1 semantics, distributed k-Means, word-item DBs.
