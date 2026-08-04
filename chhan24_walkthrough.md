# chhan24's Drill Bank — Tool Walkthrough

Source: `chhan24_code/datamining/practice/main.html` — 104 True/False items, 8 topics, no ± scoring.
Every numeric value below re-derived with `src/exam` (2026-08-04); his answer key checks out
throughout. Facts referenced from `playbook.md`.

> **Two known defects in his repo** (his *key* is fine, these are elsewhere):
> his `DBSCAN.py` hardcodes Euclidean while the drill says L₁; his `kNN.py` drops all zero
> distances, so duplicate points break it. Use our package, not his scripts.

---

## Apriori (21 items)

DB: `t1 ABC · t2 ACD · t3 ABDE · t4 BCD · t5 ABCDE · t6 CDE`

```python
db = parse_db("A,B,C / A,C,D / A,B,D,E / B,C,D / A,B,C,D,E / C,D,E")   # N = 6
apriori(db, 3);  rule(db, "AD", "C");  rule(db, "A", "D")
```

Supports: A4 B4 C5 D5 E3 · AB3 AC3 AD3 BE2 CD4 · ACD2

| # | Claim | Check | ✔ |
|---|-------|-------|---|
| 1 | sup(AD)=3, conf(AD⇒C)=2/3 | AD in t2,t3,t5; ACD in t2,t5 → 2/3 | **T** |
| 2 | CD, CE, DE frequent ⇒ CDE guaranteed frequent | converse of anti-monotonicity (fact 4) | **F** |
| 3 | conf(AD⇒C) < θ ⇒ conf(A⇒CD) < θ, no computation | supp(A) ≥ supp(AD), same numerator ⇒ conf(A⇒CD) ≤ conf(AD⇒C) | **T** |
| 4 | σ=3: all five items frequent | A4 B4 C5 D5 E3 | **T** |
| 5 | σ=4: {A,C} frequent | sup 3 < 4 | **F** |
| 6 | sup(CD) = 4 | t2,t4,t5,t6 | **T** |
| 7 | conf(E⇒D) = 1 | E in t3,t5,t6 — all contain D | **T** |
| 8 | Infrequent ⇒ all supersets infrequent | anti-monotonicity, downward | **T** |
| 9 | Every subset of a frequent itemset is frequent | same law | **T** |
| 10 | Lift > 1 ⇒ positive association | definition | **T** |
| 11 | conf(A⇒D) = 3/4 | sup(A)=4, sup(AD)=3 | **T** |
| 12 | sup(BE)=2, conf(B⇒E)=1/2 | BE in t3,t5; sup(B)=4 | **T** |
| 13 | sup(ABC)=2 at σ=2 ⇒ AB, AC, BC each ≥ 2 | downward closure | **T** |
| 14 | Join = merge (k−1)-sets agreeing on first k−2, then prune infrequent subsets | standard F_{k−1}×F_{k−1} | **T** |
| 15 | sup(AB)=3, conf(B⇒A)=3/4 | AB in t1,t3,t5; sup(B)=4 | **T** |
| 16 | lift(A⇒D) > 1 | (3·6)/(4·5) = 0.9 < 1 → negative | **F** |

**4-itemset pruning drill** — frequent 3-sets: ABC, ABD, ACD, ACE, BCD, BCF, CDE, CDF

```python
F3 = ["ABC","ABD","ACD","ACE","BCD","BCF","CDE","CDF"]
for c in ["ABCD","ACDE","BCDF","CDEF","ABCE"]: prunable(c, F3)
```

| # | Candidate | Missing 3-subsets | ✔ (prunable?) |
|---|-----------|-------------------|---|
| 17 | ABCD | none — ABC, ABD, ACD, BCD all frequent | **F** (must count) |
| 18 | ACDE | ADE | **T** |
| 19 | BCDF | BDF | **T** |
| 20 | CDEF | CEF, DEF | **T** |
| 21 | ABCE | ABE | **T** |

⚠ His explanation for item 3 is garbled ("AD is always <= than A. Therefore it must be >=").
The answer is right; use the reasoning in the table.

## EM-GMM (16 items)

```python
mstep1d([2,4,6,8,10], [[.9,.1],[.7,.3],[.4,.6],[.2,.8],[.8,.2]])   # items 14–16
# Σγ₁ = 3.0 → π₁ = 0.6 · Σγ₁x = 16.6 → μ₁ = 16.6/3.0 = 5.533
param_count(2, 1)    # = 5
```

| # | Claim | Check | ✔ |
|---|-------|-------|---|
| 1 | μ_k = Σγx/Σγ is the mean update | responsibility-weighted average | **T** |
| 2 | 1-D 2-component GMM has 5 free parameters | 2+2+1 (fact 2) | **T** |
| 3 | argmax posterior gives a valid hard partition, nothing else needed | fact 1 | **T** |
| 4 | E-step: parameters fixed, responsibilities recomputed | definition | **T** |
| 5 | M-step: responsibilities fixed, parameters updated | definition | **T** |
| 6 | Mixing coefficients sum to 1 | probability distribution | **T** |
| 7 | Monotone likelihood increase ⇒ global optimum | local optima (fact 7) | **F** |
| 8 | Posteriors of one observation sum to 1 | Bayes normalisation | **T** |
| 9 | Observed log-likelihood never decreases across iterations | EM's central guarantee | **T** |
| 10 | EM converges within a fixed predetermined number of iterations | depends on init/data (fact 23) | **F** |
| 11 | σ²_k = Σγ(x−μ)²/Σγ | weighted variance | **T** |
| 12 | Identical initialisation breaks symmetry naturally | degenerate fixed point — stays identical (fact 23) | **F** |
| 13 | GMM approximates any continuous density as K → ∞ | universal approximator | **T** |
| 14 | γ₁ = .9,.7,.4,.2,.8 ⇒ π₁ = 3.0/5 = 0.6 | tool | **T** |
| 15 | π₂ must also be 0.6 (EM assigns equal priors) | π₂ = 0.4 | **F** |
| 16 | μ₁ ≈ 5.53 with x = 2,4,6,8,10 | 16.6/3.0 = 5.533 | **T** |

## AHC (13 items)

```python
D, l = sqmat("0 3 12 20 15 / 3 0 9 16 13 / 12 9 0 7 11 / 20 16 7 0 5 / 15 13 11 5 0")
ahc_all(D, labels=l)
```

Heights — single **3, 5, 7, 9** · complete 3, 5, 11, 20 · average 3, 5, 9, 14.17

| # | Claim | Check | ✔ |
|---|-------|-------|---|
| 1 | Single: first merge {1,2} @3 | smallest entry | **T** |
| 2 | Single: second merge {4,5} @5 | next smallest | **T** |
| 3 | Single: final merge at height 13 | d({1,2},{3,4,5}) = min(...) = **9** | **F** |
| 4 | Complete: first merge still {1,2} @3 | all linkages agree on singletons | **T** |
| 5 | Single-link merge heights are non-decreasing (no inversions) | fact 19 | **T** |
| 6 | Complete-link more robust to chaining than single | fact 19 | **T** |
| 7 | Ward merges the pair with smallest SSE increase | fact 19 | **T** |
| 8 | Single full order: {1,2}@3, {4,5}@5, {3,4,5}@7, root@9 | tool | **T** |
| 9 | UPGMA = mean of all pairwise distances | definition | **T** |
| 10 | Complete link = minimum pairwise distance | that's single link | **F** |
| 11 | After 2 merges (d = 9, 13, 7): Single can finish the next iteration from those 3 numbers | min only | **T** |
| 12 | Same for Complete | max only | **T** |
| 13 | Same for Average | needs cluster **sizes**: (1·9+2·13)/3 = 11.67 (fact 6) | **F** |

## Density estimation (10 items)

A = {8,11,14,17,19,22,24,27,30,33}, n=10, query x=20 · B = {1,2,2,3,4,4,4,5,6,6,8,9,9,9,10}, n=15

```python
A = [8,11,14,17,19,22,24,27,30,33]
density_report(A, [("knn",20,1), ("knn",20,3), ("knn",20,5), ("knn",20,10)])
B = [1,2,2,3,4,4,4,5,6,6,8,9,9,9,10]
density_report(B, [("kernel",4,2), ("kernel",9,1), ("kernel",6,4)])
```

Verified: kNN k=1 → **1/20**, k=3 → **1/20**, k=5 → **1/24**, k=10 → **1/26** ·
kernel (4, h=2) → **1/6**, (9, h=1) → **1/5**, (6, h=4) → **7/60**

| # | Claim | Check | ✔ |
|---|-------|-------|---|
| 1 | kNN k=1 → 1/20 | r=1 → 1/(10·2) | **T** |
| 2 | kNN k=5 gives the same 1/20 as k=1 | r=6 → 5/120 = 1/24 | **F** |
| 3 | kNN k=10 → 1/26 | r=13 → 10/260 | **T** |
| 4 | kernel f(4), h=2 → 1/6 | [3,5] holds 5 points → 5/30 | **T** |
| 5 | kernel f(9), h=1 → 1/6 | [8.5,9.5] holds three 9s → 3/15 = **1/5** | **F** |
| 6 | kNN k=3 → 1/20 | r=3 → 3/60 | **T** |
| 7 | kernel f(6), h=4 → 7/60 | [4,8] holds 7 points | **T** |
| 8 | h → 0 gives a smoother, lower-variance estimate | opposite — spiky, high variance (fact 20) | **F** |
| 9 | kNN density is locally adaptive (r shrinks where dense) | fact 20 | **T** |
| 10 | Doubling h can only increase or keep the window count | larger window contains the smaller | **T** |

## Outlier detection (11 items)

A(1,1) B(2,2) C(2,3) D(8,8) E(3,2), Manhattan, query excluded from its own neighbourhood

```python
res = analyze("A 1 1 / B 2 2 / C 2 3 / D 8 8 / E 3 2", "man", k=1)
check_order("D,A,B", res["knn"])
```

k=1 scores: **A=2, B=1, C=1, D=11, E=1** (LOF: D=11.0, A=2.0, rest 1.0) · k=2: B=1, E=2

| # | Claim (ordering by kNN, k=1, unless noted) | Check | ✔ |
|---|---|---|---|
| 1 | D, A, B correctly ordered | 11 ≥ 2 ≥ 1 | **T** |
| 2 | A, B, C | 2 ≥ 1 ≥ 1 (ties OK) | **T** |
| 3 | D, E, A | 11, 1, 2 — rises | **F** |
| 4 | B, C, E | 1, 1, 1 — constant is non-increasing | **T** |
| 5 | A point with small kNN-distance can still have high LOF | relative density (fact 21) | **T** |
| 6 | LOF ≈ 1 always means a strong outlier | ≈1 = normal (fact 21) | **F** |
| 7 | D, C, E | 11, 1, 1 | **T** |
| 8 | A, E, C | 2, 1, 1 | **T** |
| 9 | k=2: score of E equals 2 | E's distances 1,2,3,11 → 2nd = 2 | **T** |
| 10 | k=2: score of B equals 1 | B's distances 1,1,2,12 → 2nd = 1 | **T** |
| 11 | Larger k makes the score MORE sensitive to local fluctuations | larger k smooths (fact 21) | **F** |

## DBSCAN (12 items)

P1(1,1) P2(1,2) P3(2,1) P4(2,2) P5(5,5) P6(10,10), L₁, query counts itself

```python
pts = "P1 1 1 / P2 1 2 / P3 2 1 / P4 2 2 / P5 5 5 / P6 10 10"
analyze(pts, "man", db=[(1,3), (1,4), (2,3)])
```

| # | Claim | Check | ✔ |
|---|-------|-------|---|
| 1 | ε=1, mp=3: P1 is core | N(P1) = {P1,P2,P3} = 3 | **T** |
| 2 | ε=1, mp=3: P5 is a border point | nothing within 1, no core near → **noise** | **F** |
| 3 | ε=1, mp=4: none of P1–P4 is core | each \|N\| = 3 < 4 | **T** |
| 4 | ε=1, mp=3: P5 and P6 land in the same cluster since both are noise | noise is unclustered, never grouped (fact 10) | **F** |
| 5 | Increasing ε with MinPts fixed generally gives fewer clusters | larger neighbourhoods merge | **T** |
| 6 | DBSCAN needs the number of clusters up front | it doesn't — unlike k-Means | **F** |
| 7 | A border point is in a core point's neighbourhood without being core | definition | **T** |
| 8 | Noise points are never density-reachable from a core point | else they'd join that cluster | **T** |
| 9 | ε=2, mp=3: P1–P4 all core and in one cluster | all pairwise L₁ ≤ 2 → \|N\| = 4 | **T** |
| 10 | ε=2, mp=3: P5 directly density-reachable from P4 | d(P4,P5) = 6 > 2 | **F** |
| 11 | ε=2, mp=3: P5 and P6 both noise | \|N\| = 1 each | **T** |
| 12 | A thin bridge of points can merge two dense regions (chaining) | transitive density-connectivity | **T** |

## k-Means & SSE (13 items)

D = {1, 2, 3, 10, 11, 12, 20, 21, 22}, k = 3

```python
data = dict(A=1,B=2,C=3,D=10,E=11,F=12,G=20,H=21,I=22)
kmeans_trace(data, [2, 11, 21])      # item 1 — immediate fixed point
kmeans_trace(data, [1, 2, 3])        # item 10 — converges to {A},{B,C},{D…I}
analyze_partitions(data, {"natural": [["A","B","C"],["D","E","F"],["G","H","I"]],
                          "shifted": [["A","B","C","D"],["E","F"],["G","H","I"]]})
```

SSE: natural **6**, shifted **52.5**

| # | Claim | Check | ✔ |
|---|-------|-------|---|
| 1 | Init (2, 11, 21) converges immediately (centroids don't move) | each group's mean is already 2, 11, 21 | **T** |
| 2 | {1,2,3},{10,11,12},{20,21,22} minimises SSE for k=3 | SSE 6; gap-cut = natural grouping | **T** |
| 3 | {1,2,3,10},{11,12},{20,21,22} has lower SSE | 52.5 > 6 | **F** |
| 4 | Depending on init, k-Means can reach a non-global local minimum | fact 22 | **T** |
| 5 | A centroid is always one of the observations | it's the mean (fact 22) | **F** |
| 6 | k-Means minimises SSE | definition | **T** |
| 7 | One cluster per observation ⇒ SSE = 0 | each centroid = its point | **T** |
| 8 | k-Means naturally finds arbitrarily shaped clusters | compact/convex only (fact 22) | **F** |
| 9 | Elbow method = diminishing SSE returns | fact 18 | **T** |
| 10 | Init (1,2,3) can converge to a cluster mixing the {1,2,3} and {10,11,12} groups | trace: {A},{B,C},{D…I} — the third cluster swallows 10–22 | **T** |
| 11 | One Lloyd iteration is ≈ O(n·k·d) | fact 22 | **T** |
| 12 | Guaranteed to terminate in finitely many iterations | SSE non-increasing, finitely many partitions | **T** |
| 13 | Assumes roughly convex, similar-size clusters | fact 22 | **T** |

## Similarity measures (8 items)

```python
dist_compare([[1,0.8],[0.8,1]])           # item 1 — non-diagonal Σ
binary_compare([1,1,0], [1,0,1], pad=20)  # items 2–4
```

| # | Claim | Check | ✔ |
|---|-------|-------|---|
| 1 | Mahalanobis can rank points differently from Euclidean when Σ is non-diagonal | Σ rescales/rotates space | **T** |
| 2 | SMC counts f₀₀ as agreement, Jaccard ignores it entirely | definitions | **T** |
| 3 | If all binary variables are symmetric, SMC and J always agree | J still drops f₀₀ — they differ whenever f₀₀ > 0 | **F** |
| 4 | Cosine is unaffected by 0-0 matches (zero components add nothing) | normalised dot product | **T** |
| 5 | Minkowski p=1 → Manhattan, p=2 → Euclidean | fact 24 | **T** |
| 6 | Cosine ∈ [0,1] for non-negative vectors, ∈ [−1,1] in general | fact 24 | **T** |
| 7 | Mahalanobis reduces to Euclidean when Σ = I | fact 6 | **T** |
| 8 | Jaccard suits asymmetric binary attributes (shared absence uninformative) | why f₀₀ is excluded | **T** |

---

## Notes for drilling

- **His key is reliable** on all 104 items (every numeric one re-derived here). Only the prose in
  a few `explain` strings is sloppy — trust the answer, not the wording.
- Item 3 of the similarity block is the mirror image of the June exam's Q3.2 (non-binary nominal,
  where SMC = Jaccard **is** true because there is no absence state). Read the attribute type
  before answering: **binary with f₀₀ > 0 → they differ; non-binary nominal → they coincide.**
- His bank is heavier on pure theory than the real exam (roughly 60/40 vs June's 25/75), which
  makes it the better drill for facts 19–24 and the weaker drill for data-entry speed.
