# DM583 — Evaluation of Failed First Attempt (June 2026)

Source: `failed_first_exam.pdf` (9 questions, 38 sub-questions, 100 points total).
Scoring: each head question's points split evenly over its sub-questions; correct = `+points/n`, wrong = `−points/n`, blank = `0`. Passing bar ≈ 50.

Every question below was re-solved computationally (see `tmp` verification script; algorithms cross-checked against `old_scripts/`). Correct answers marked with the reasoning that produces them.

## Final score reconstruction

| Q | Topic | Points | Sub-results (mine vs. correct) | Score |
|---|-------|--------|-------------------------------|-------|
| 1 | Non-parametric density estimation | 12 | ✓ ✗ ✗ ✗ | **−6.0** |
| 2 | kNN / LOF outlier ordering | 14 | ✗ ✗ ✓ ✗ | **−7.0** |
| 3 | Similarity / distance measures | 10 | ✗ ✓ ✓ ✓ | **+5.0** |
| 4 | Hierarchical clustering (AHC) | 16 | ✓ ✓ ✗ ✗ ✓ | **+3.2** |
| 5 | Apriori candidate pruning | 4 | ✓ ✗ ✓ ✓ | **+2.0** |
| 6 | DBSCAN | 10 | ✓ ✓ ✓ ✓ | **+10.0** |
| 7 | EM-GMM | 10 | ✓ ✓ ✗ ✗ | **0.0** |
| 8 | Apriori + association rules | 10 | ✓ ✓ – ✗ ✗ | **0.0** |
| 9 | k-Means | 14 | ✓ ✓ ✓ ✓ | **+14.0** |
| | **Total** | **100** | 21 ✓ / 16 ✗ / 1 blank | **≈ 21.2** |

### The single most important finding

Correct answers earned **+59.6** points. Wrong answers cost **−38.4** points.

> **If every wrong answer had been left blank, the score would have been ≈ 59.6 — a pass.**
> The knowledge demonstrated on this exam was already sufficient. Guessing is what failed the exam. The 16 wrong answers were not coin-flip unlucky (a coin flip nets 0 in expectation); they were confident misconceptions, which are *worse* than random because they are systematically wrong.

---

## Question-by-question analysis

### Q1 — Non-parametric density estimation (12 pts) → **−6.0** ❌ worst topic

Data (n=20): `{1,1,2,2,3,4,4,4,5,5,5,5,6,9,9,10,10,10,10,11}`. Formula family: `f(x) = k / (n·V)`.

| Sub | Claim | Correct | Mine | Result |
|-----|-------|---------|------|--------|
| 1 | Discrete kernel, x=4, h=1 → 1/10 | **False** — window [3.5,4.5] holds 3 points → 3/(20·1) = 3/20 | False | ✓ +3 |
| 2 | kNN density, x=7, k=2 (tie-adjusted) → 3/80 | **False** — 2nd-NN radius r=2, ties give 7 points in ball, V=2r=4 → 7/80 | True | ✗ −3 |
| 3 | kNN density, x=7, k=1 → 1/40 | **True** — r=1 (the point 6), V=2 → 1/(20·2) = 1/40 | False | ✗ −3 |
| 4 | Discrete kernel, x=4, h=2 → 1/5 | **True** — window [3,5] holds 8 points (3, three 4s, four 5s) → 8/(20·2) = 1/5 | False | ✗ −3 |

Diagnosis: no script existed for this topic (only Gaussian KDE in the cheatsheet), and the by-hand attempt got the window/ball bookkeeping and tie adjustment wrong on 3 of 4 subs. This is the clearest "study hard + build tool" topic.

### Q2 — Outlier score orderings, Manhattan, k=2 (14 pts) → **−7.0** ❌

Points (read from grid): A(5,2) B(1,7) C(3,4) D(6,6) E(4,7) F(5,5) G(4,6) H(3,7).
Computed scores (query point excluded from own neighborhood, ties included in N(p)):

- kNN score (dist to 2nd NN): A=4, B=3, C=3, D=2, E=1, F=2, G=2, H=2
- LOF: A≈1.458, B=1.250, C≈1.571, D≈1.071, E≈1.071, F≈1.071, G=0.875, H≈0.981

| Sub | Claim | Correct | Mine | Result |
|-----|-------|---------|------|--------|
| 1 | C,D,E ordered w.r.t. kNN (k=2) | **Yes** (3 ≥ 2 ≥ 1) | No | ✗ −3.5 |
| 2 | A,B,C ordered w.r.t. LOF (k=2) | **No** (C=1.571 is the largest but listed last) | Yes | ✗ −3.5 |
| 3 | A,C,D ordered w.r.t. LOF (k=2) | **No** (A=1.458 < C=1.571) | No | ✓ +3.5 |
| 4 | A,B,D ordered w.r.t. kNN (k=2) | **Yes** (4 ≥ 3 ≥ 2) | No | ✗ −3.5 |

Diagnosis: **`old_scripts/outliers.py` already contained everything needed** — `knn_outlier`, `lof`, tie-correct neighborhoods, and a pluggable distance (`dist.mand` for Manhattan). It was evidently not used (or used with the default Euclidean metric). Both kNN subs were answered inverted, suggesting the scores were never actually computed. Pure workflow failure: the blocker was getting 2-D grid points typed in and the right metric selected under time pressure.

### Q3 — Similarity / dissimilarity measures (10 pts) → **+5.0** ⚠️

| Sub | Claim | Correct | Mine | Result |
|-----|-------|---------|------|--------|
| 1 | Σ=[[1,2],[2,1]] ⇒ Mahalanobis = Euclidean to mean | **False** — only Σ = I gives that; this Σ isn't even positive-definite (det = −3) | True | ✗ −2.5 |
| 2 | All symmetric non-binary nominal ⇒ SMC = Jaccard | **True** — with no asymmetric variables there are no 0-0 absences for Jaccard to discard | True | ✓ +2.5 |
| 3 | Cosine on one-hot "never suitable, dominated by 0-0 matches" | **False** — cosine ignores 0-0 matches entirely (dot product only counts co-occurrences) | False | ✓ +2.5 |
| 4 | Σ = I, mean at origin, point on an axis ⇒ Mahalanobis = Euclidean = Manhattan = Suprema | **True** — all reduce to \|x₁\| | True | ✓ +2.5 |

Diagnosis: theory question, mostly fine. The miss is a core Mahalanobis fact: it equals Euclidean **only when Σ = I** (and here Σ wasn't a valid covariance matrix at all — a giveaway).

### Q4 — AHC dendrogram (16 pts) → **+3.2** ⚠️

Merge sequences from the distance matrix (verified with `cluster.ahc` logic):

- **Single**: (1,2)@2, (4,5)@6, (3∪45)@8, root@10 → **matches the dendrogram exactly (topology AND scale)**
- **Complete**: (1,2)@2, (4,5)@6, (3∪45)@10, root@22 → same topology, different scale
- **Average**: (1,2)@2, (4,5)@6, (3∪45)@9, root@16.33 → does NOT match

| Sub | Claim | Correct | Mine | Result |
|-----|-------|---------|------|--------|
| 1 | Complete-linkage: same topology, not same scale | **True** | True | ✓ +3.2 |
| 2 | Single/Complete need only the 3 inter-cluster distances; Average needs more (cluster sizes) | **True** — Lance-Williams; average is size-weighted | True | ✓ +3.2 |
| 3 | Dendrogram fully corresponds to Single-Linkage | **True** (2, 6, 8, 10 exactly) | False | ✗ −3.2 |
| 4 | Dendrogram corresponds to Average-Linkage | **False** (merge heights 9 and 16.33) | True | ✗ −3.2 |
| 5 | Cut at level 4 ⇒ {1,2},{3},{4,5} | **False** — at level 4 only (1,2) has merged ⇒ {1,2},{3},{4},{5} | False | ✓ +3.2 |

Diagnosis: `cluster.py::ahc(D, method)` takes a distance matrix directly and would have answered subs 3 and 4 in seconds — it apparently wasn't run for all three linkages. Subs 3/4 look like a guessed complementary pair ("it's probably not single, maybe average"). Running all linkages and comparing merge heights to the dendrogram scale is mechanical.

### Q5 — Apriori 4-candidate pruning (4 pts) → **+2.0** ⚠️

Frequent 3-itemsets: ABC, ABD, ABE, ABF, AEF, BCD, BCE, BDF, BEF, CEF. A 4-candidate is prunable iff some 3-subset is not frequent.

| Sub | Prunable? | Missing 3-subsets | Mine | Result |
|-----|-----------|-------------------|------|--------|
| ABCE | **Yes** | ACE | Yes | ✓ +1 |
| BCDE | **Yes** | BDE, CDE | No | ✗ −1 |
| ABEF | **No** | (all of ABE, ABF, AEF, BEF frequent) | No | ✓ +1 |
| ABDE | **Yes** | ADE, BDE | Yes | ✓ +1 |

Diagnosis: by-hand subset enumeration slipped on BCDE (4 subsets to check, missed BDE/CDE). Trivially scriptable.

### Q6 — DBSCAN, 2-D Manhattan (10 pts) → **+10.0** ✅

All four subs correct (S border @ ε=2/MinPts=6; P not in M's cluster @ MinPts=4 — P is noise since its only neighbor M is not core; P core hence not noise @ MinPts=2; G core @ MinPts=6 with |N(G)|=6). Verified computationally — all four match.

Diagnosis: success. `cluster.py::dbscan` supports 2-D data with `d=mand` and counts the query point, exactly matching the exam's convention. This (or careful by-hand work) clearly worked.

### Q7 — EM-GMM (10 pts) → **0.0** ⚠️

Posterior sums: Σγ₁ = 3.8, Σγ₂ = 2.2.

| Sub | Claim | Correct | Mine | Result |
|-----|-------|---------|------|--------|
| 1 | M-step priors = 3.8/6 and 2.2/6 | **True** | True | ✓ +2.5 |
| 2 | M-step means = 14.2/3.8 and 9.8/2.2 | **False** — numerators swapped; μ₁ = 9.8/3.8 ≈ 2.58, μ₂ = 14.2/2.2 ≈ 6.45 | False | ✓ +2.5 |
| 3 | Hard partition needs only the final posteriors P(Cᵢ\|x) | **True** — assign each x to argmaxᵢ P(Cᵢ\|x); nothing else needed | False | ✗ −2.5 |
| 4 | Model uniquely described by 3 numerical coefficients | **False** — 2 means + 2 variances + 1 free prior = **5** parameters | True | ✗ −2.5 |

Diagnosis: the computational subs (script-assisted arithmetic) were right; both **conceptual** subs were wrong. Two facts to internalize: (a) hard clustering from GMM = argmax posterior, posteriors suffice; (b) parameter count for a k-component univariate GMM = k means + k variances + (k−1) priors.

### Q8 — Apriori & association rules (10 pts) → **0.0** ⚠️

`old_scripts/apriori copy.py` has this exam's exact transaction DB hard-coded — direct evidence the script was used mid-exam. Computed ground truth: frequent 1-itemsets {A,B,C,D,F,G}; frequent 2-itemsets AB,AC,AD,CD,CG,DF,DG; the **only** frequent 3-itemset at σ=3 is ACD; supp(AD)=4, supp(ACD)=3.

| Sub | Claim | Correct | Mine | Result |
|-----|-------|---------|------|--------|
| 1 | conf(AD⇒C) < θ ⇒ conf(A⇒CD) < θ certain | **Yes** — conf(A⇒CD) = s(ACD)/s(A) ≤ s(ACD)/s(AD) = conf(AD⇒C) since s(A) ≥ s(AD) | Yes | ✓ +2 |
| 2 | σ=3: more than one frequent 3-itemset, incl. ACD | **No** — ACD is the only one | No | ✓ +2 |
| 3 | Candidate 2-itemsets from frequent 1-itemsets = the 7 listed, all frequent | **No** — the *candidates* are all C(6,2)=15 pairs of {A,B,C,D,F,G}; the 7 listed are the *frequent* ones | blank | 0 |
| 4 | (C,D),(C,G),(D,G) all frequent ⇒ (C,D,G) guaranteed frequent | **No** — anti-monotonicity is necessary, not sufficient; supp(CDG)=2 < 3 | Yes | ✗ −2 |
| 5 | Rule AD⇒C: support 3, confidence 3/4 | **Yes** — s(ACD)=3 (count convention consistent with σ=3 as a count), conf = 3/4 | No | ✗ −2 |

Diagnosis: the script answered the itemset-counting subs (1, 2 ✓). The three misses are conceptual/tooling: (3) candidate-generation step not understood and the script's pre-prune candidate printout was **commented out**; (4) the classic Apriori misconception — frequent subsets do NOT guarantee a frequent superset; (5) rule support/confidence were one `freq.support` / `freq.confidence` call away — those functions existed and weren't used.

### Q9 — k-Means, 1-D (14 pts) → **+14.0** ✅

All four subs correct and verified: convergence in exactly 3 assign+update cycles to {A,B,E},{C,D,H},{F,G,I}; the partition {A,B,E},{C,D,H,F},{G,I} is a fixed point (local minimum, SSE 63.25) while a better solution exists (SSE 39.33); simplified silhouette of A differs between the partitions (0.897 vs 0.915) because b(A) changes; the SSE comparison claim is false.

Diagnosis: success — `cluster.py` (`kmeans`, `sse`, centroid logic) covers all of it.

---

## Grading caveats

- Q1: assumes the course conventions — window of width h means volume h with inclusive boundaries, and kNN density with tie-adjusted k, V = 2r (matching the exam's own hint). Under these conventions the claimed values 1/5 and 1/40 come out *exactly*, which strongly indicates they are the intended True answers.
- Q2/Q6: point coordinates were read off the printed grids; DBSCAN results were robust to that reading, and the Q2 conclusions hold for both dist-to-kth-NN and average-of-k-NN kNN-score definitions.
- Q8 sub 5: uses the support-as-count convention, consistent with the exam's "σ = 3" usage.

## Summary of failure modes, ranked by points lost

| Failure mode | Points lost | Questions |
|---|---|---|
| Guessing instead of blanking (all 16 wrong answers) | −38.4 gross | everywhere |
| Non-parametric density estimation: no tool, weak formula fluency | −9 | Q1 |
| Outlier scores never actually computed despite existing tool | −10.5 | Q2 |
| AHC: didn't run/compare all linkages against the dendrogram scale | −6.4 | Q4 |
| EM-GMM conceptual facts (argmax posterior, parameter counting) | −5 | Q7 |
| Apriori concepts (candidate generation, anti-monotonicity direction, rule support) | −4 + blank | Q5, Q8 |
| Mahalanobis ≠ Euclidean unless Σ = I | −2.5 | Q3 |

See `PLAN.md` for the tool-development and study plan derived from this analysis.
