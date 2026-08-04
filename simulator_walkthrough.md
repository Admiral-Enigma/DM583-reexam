# Practice Simulator (fresh items) — Tool Walkthrough

Source: `practice/simulator.html` — 40 items, 8 topics, 98 pts, ± scoring.
Attempt 2026-08-04: **84 / 98 (85.7 %), zero wrong**, 6 blanks (2 GMM + 4 similarity).
All values below verified live against `src/exam`. Facts referenced from `playbook.md`.

---

## 1 · Non-parametric density (12 pts, ±2) — 6 ✓

```python
X = [2,3,3,4,5,5,6,8,8,9,9,9,10,12,13,15]      # n = 16
density_report(X, [("kernel",5,2), ("kernel",9,3), ("knn",7,1),
                   ("knn",7,2), ("knn",7,4), ("kernel",13,2)])
```

| # | Claim | Work | Verdict |
|---|-------|------|---------|
| 1 | kernel x=5, h=2 → 1/8 | [4,6] holds {4,5,5,6} = 4 → 4/(16·2) = 1/8 | **T** |
| 2 | kernel x=9, h=3 → 1/8 | [7.5,10.5] holds {8,8,9,9,9,10} = 6 → 6/(16·3) = 1/8 | **T** |
| 3 | kNN x=7, k=1 → 1/32 | r=1 but THREE points at d ≤ 1 (6,8,8) → k_eff=3 → **3/32** | **F** |
| 4 | kNN x=7: k=2 same as k=1 | 2nd NN also at distance 1 → same r, same tie set → both 3/32 | **T** |
| 5 | kNN x=7, k=4 → 1/8 | r=2, points within 2 = 8 → 8/(16·4) = 1/8 | **T** |
| 6 | kernel x=13, h=2 → 1/8 | [12,14] holds {12,13} = 2 → 2/32 = **1/16** | **F** |

Trap: sub 3 is the tie-adjustment (1/32 = the un-adjusted answer). Tool prints `tie-adjusted!`
whenever k_eff ≠ k — that flag is the answer.

## 2 · Outliers, Manhattan, k=2 (14 pts, ±2.8) — 5 ✓

```python
res = analyze("A 1 2 / B 2 1 / C 2 3 / D 3 2 / E 6 6 / F 7 5 / G 2 7", "man", k=2)
check_order("G,E,A", res["knn"]);  check_order("G,F,C", res["lof"])
```

Computed — kNN: A=B=C=D=2, E=5, F=7, G=5 · LOF: A=B=C=D=1.0, E=1.128, **F=2.257**, G=1.5

| # | Claim | Check | Verdict |
|---|-------|-------|---------|
| 1 | kNN scores of A, B, C, D all = 2 | each has two neighbours at distance 2 | **T** |
| 2 | G, E, A ordered by kNN | 5 ≥ 5 ≥ 2 — ties allowed ("not strictly") | **T** |
| 3 | G, F, C ordered by LOF | 1.5 < 2.257 — rises at step 1 | **F** |
| 4 | E, F, A ordered by kNN | 5 < 7 — rises at step 1 | **F** |
| 5 | F has the highest LOF | 2.257 vs next-highest G 1.5 | **T** |

Sub 5 is the LOF concept (fact 21): F's kNN distance is largest too, but what makes its LOF
extreme is that its neighbours sit in much denser surroundings — relative density, not absolute.

## 3 · AHC (16 pts, ±3.2) — 5 ✓

```python
D, labels = pairmat("d(1,2)=4 d(1,3)=10 d(1,4)=20 d(1,5)=18 d(2,3)=8 "
                    "d(2,4)=18 d(2,5)=16 d(3,4)=12 d(3,5)=14 d(4,5)=6")
match_dendrogram(D, [4,6,8,12], labels=labels)
cut_height(D, "single", 7, labels=labels)
```

Heights — single **4, 6, 8, 12** · complete 4, 6, 10, 20 · average 4, 6, 9, 16.33.
All three share the figure's topology; merge 3 is `{1,2}+{3}` (note: 3 joins the LEFT pair here,
unlike June where it joined {4,5}).

| # | Claim | Check | Verdict |
|---|-------|-------|---------|
| 1 | Figure corresponds exactly to Single-Linkage | heights AND topology match | **T** |
| 2 | Complete produces the same merge order (topology) | same partners, heights 10/20 differ | **T** |
| 3 | Figure corresponds exactly to Complete-Linkage | scale fails (10, 20 ≠ 8, 12) | **F** |
| 4 | Average: third merge at height 8.5 | avg(d(3,1)=10, d(3,2)=8) = **9** | **F** |
| 5 | Cut @7 ⇒ {1,2}, {3}, {4,5} | merges @4 and @6 are below 7; 3 joins at 8 | **T** |

## 4 · Apriori (12 pts, ±2) — 6 ✓

```python
db = parse_db("A,B,D / A,C,D / B,C,E / A,B,C,D / B,D / A,C,D,E")   # N = 6, σ = 3
apriori(db, 3);  prunable("ABD", ["AC","AD","BD","CD"]);  rule(db, "AD", "C")
```

Printout: counts A4 B4 C4 D5 E2 → frequent 1-sets **A, B, C, D** · **6 candidates** (C(4,2)),
supports AB2 AC3 AD4 BC2 BD3 CD3 → 4 frequent · L3 → only **ACD (3)**.

| # | Claim | Check | Verdict |
|---|-------|-------|---------|
| 1 | Frequent 1-itemsets are exactly A, B, C, D | E has support 2 < 3 | **T** |
| 2 | Exactly 6 candidate 2-itemsets generated | C(4,2) = 6 — ALL pairs, before counting (fact 3) | **T** |
| 3 | sup({A,B}) = 3 | AB ⊆ t1, t4 only → 2 | **F** |
| 4 | {A,B,D} prunable without counting | 2-subset {A,B} has support 2 < σ | **T** |
| 5 | AC, AD, CD frequent ⇒ ACD **guaranteed** frequent | converse of anti-monotonicity (fact 4) — it's only a candidate; counting happens to give 3, but nothing was guaranteed | **F** |
| 6 | conf(AD⇒C) = 3/4 and conf(A⇒CD) = 3/4 | s(ACD)=3, s(AD)=s(A)=4 → both 3/4 (equality allowed by conf(A⇒CD) ≤ conf(AD⇒C)) | **T** |

## 5 · DBSCAN, Manhattan, self counts (10 pts, ±2.5) — 4 ✓

```python
res = analyze("P1 1 1 / P2 2 1 / P3 2 2 / P4 3 2 / P5 3 3 / P6 6 6 / P7 7 6 / P8 7 7",
              "man", db=[(1,3), (2,4)])
```

ε=1, MinPts=3 → core P2, P3, P4, P7 · border P1, P5, P6, P8 · no noise
ε=2, MinPts=4 → core P2, P3, P4 · border P1, P5 · **noise P6, P7, P8**

| # | Claim | Check | Verdict |
|---|-------|-------|---------|
| 1 | ε=1, mp=3: P7 core, P6 and P8 border | N(P7)={P6,P7,P8}=3 ≥ 3; P6/P8 have \|N\|=2 but lie within ε of core P7 | **T** |
| 2 | ε=1, mp=3: P5 is noise | \|N(P5)\|=2 → not core, but P4 IS core and P5 ∈ N(P4) → **border** | **F** |
| 3 | ε=2, mp=4: P6, P7, P8 all noise | each has \|N\|=3 < 4, no core nearby | **T** |
| 4 | ε=2, mp=4: exactly two clusters | only ONE cluster ({P1…P5}); **noise is not a cluster** | **F** |

Sub 2 trap: few neighbours ≠ noise — noise also requires no core point within ε.
Sub 4 trap: counting the noise blob as a second cluster.

## 6 · EM-GMM (10 pts, ±2) — 3 ✓, **2 blanks**

```python
xs = [1, 2, 6, 8, 3]
g  = [[.9,.1], [.8,.2], [.2,.8], [.1,.9], [.7,.3]]      # rows = points; γ2 = 1 − γ1
mstep1d(xs, g)          # Σγ 2.7 / 2.3 · μ1 = 6.6/2.7 = 2.444 · μ2 = 13.4/2.3 = 5.826
param_count(3, 1)       # 3 + 3 + 2 = 8
```

| # | Claim | Check | Verdict |
|---|-------|-------|---------|
| 1 | π₁ = 2.7/5, π₂ = 2.3/5 | Σγ₁=2.7, Σγ₂=2.3, n=5; sanity 2.7+2.3=5 | **T** |
| 2 | μ₁ = 13.4/2.7, μ₂ = 6.6/2.3 | printout: μ₁ = **6.6**/2.7, μ₂ = **13.4**/2.3 — numerators swapped | **F** |
| 3 | Hard partition from posteriors alone (argmax) | fact 1 — MAP uses only the γ table | **T** |
| 4 | 1-D GMM with 3 components has 9 free parameters | 3 means + 3 variances + **2** free priors = **8** (fact 2) | **F** |
| 5 | M-step holds responsibilities fixed, updates π, μ, σ² | definition; E-step is the mirror | **T** |

The two blanks were almost certainly 3 and 4 — both are pure recall, and both have a tool that
prints the answer: `hard_partition(g)` and `param_count(3, 1)`. Worth 4 pts, zero risk.

## 7 · k-Means & SSE (14 pts, ±2.8) — 5 ✓

```python
data = dict(A=1, B=2, C=3, D=8, E=9, F=10, G=15, H=16)
kmeans_trace(data, [1, 2, 3])
analyze_partitions(data, {"converged": [["A"],["B","C"],["D","E","F","G","H"]],
                          "gap-cut":   [["A","B","C"],["D","E","F"],["G","H"]]})
silhouette_point(data, [["A"],["B","C"],["D","E","F","G","H"]], "A")
```

Trace: iter1 {A}{B}{C…H} → iter2 {A}{B,C}{D…H} → iter3 unchanged (2 changing iterations).
SSE: converged **53.7**, gap-cut **4.5**. Both are fixed points. s(A): 1.0 vs 0.875.

| # | Claim | Check | Verdict |
|---|-------|-------|---------|
| 1 | init (1,2,3) converges to {A}, {B,C}, {D,E,F,G,H} | trace | **T** |
| 2 | That partition attains the **global minimum** SSE | counterexample: gap-cut partition 4.5 < 53.7 | **F** |
| 3 | It is a fixed point (reassignment changes nothing) | tool `fixed point True`; also implied by "converged" in sub 1 | **T** |
| 4 | SSE of {A,B,C}, {D,E,F}, {G,H} = 5.0 | 2 + 2 + 0.5 = **4.5** | **F** |
| 5 | s(A) higher in {A},{B,C},{D…H} than in the gap-cut partition | singleton → a=0 → s=1 vs 0.875 | **T** |

Candidate generation for sub 2 (fact: 1-D optima are contiguous intervals): sort, take the k−1
widest gaps — 3→8 and 10→15 — giving {1,2,3}, {8,9,10}, {15,16}. Sub 5's lesson: a singleton gets
the *perfect* individual silhouette inside a *terrible* partition — per-point silhouette judges fit,
not clustering quality.

## 8 · Similarity & distance (10 pts, ±2.5) — **4 blanks** (0 pts, none lost)

Not "full theory" — 2 of the 4 are direct tool checks:

```python
dist_compare([[2,0],[0,2]], points=[[3,0],[1,1]])
#   x=[3,0]: Mah=2.1213  Euc=3.0000   -> 3/√2 = 2.1213  ✓
#   x=[1,1]: Mah=1.0000  Euc=1.4142   -> 1.4142/√2 = 1.0 ✓
binary_compare([1,1,0], [1,0,1], pad=20)
#   +0 zeros: SMC 0.3333  Jaccard 0.3333  cosine 0.5
#   +20 zeros: SMC 0.9130 Jaccard 0.3333  cosine 0.5
cosine([1,1,0,0,0], [0,0,1,1,0])   # -> 0.0
```

| # | Claim | Check | Verdict |
|---|-------|-------|---------|
| 1 | Σ = 2I ⇒ Mahalanobis = Euclidean/√2 for every point | Σ⁻¹ = I/2 ⇒ d_M = √(dᵀd/2) = d_E/√2; tool confirms on both test points | **T** |
| 2 | Jaccard ≥ SMC always, for binary vectors | reversed — SMC adds f₀₀ to numerator AND denominator, pulling toward 1, so **SMC ≥ Jaccard** (equal iff f₀₀ = 0). Demo: 0.913 vs 0.333 | **F** |
| 3 | Minkowski with p = 1 is the Euclidean distance | p=1 Manhattan, p=2 Euclidean, p→∞ Chebyshev (fact 24) | **F** |
| 4 | Cosine of two one-hot objects sharing no 1-positions = 0, regardless of appended shared 0-columns | dot product = 0; 0-0 positions add nothing to dot product or norms | **T** |

Blanking these was correct discipline under uncertainty — but the cost was 10 pts, the single
biggest block on the sheet. Fix before the exam: subs 1 and 4 are `dist_compare` / `cosine` calls,
subs 2 and 3 are facts 24 + "SMC ≥ Jaccard". Direction-of-inequality is the whole game in sub 2.

---

## Result

| Topic | ✓ | ✗ | — | Score |
|---|---|---|---|---|
| 1 Density | 6 | 0 | 0 | 12 / 12 |
| 2 Outliers | 5 | 0 | 0 | 14 / 14 |
| 3 AHC | 5 | 0 | 0 | 16 / 16 |
| 4 Apriori | 6 | 0 | 0 | 12 / 12 |
| 5 DBSCAN | 4 | 0 | 0 | 10 / 10 |
| 6 GMM | 3 | 0 | 2 | 6 / 10 |
| 7 k-Means | 5 | 0 | 0 | 14 / 14 |
| 8 Similarity | 0 | 0 | 4 | 0 / 10 |
| **Total** | **34** | **0** | **6** | **84 / 98 (85.7 %)** |

**Zero wrong answers on 34 attempted — calibration is exactly right.** All 14 lost points are
blanks, i.e. recoverable upside, not damage. Both blank blocks (GMM 3–4, similarity 1–4) are
covered by an existing tool call or a numbered fact; the remaining work is recall confidence,
not capability.
