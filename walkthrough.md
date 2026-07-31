# DM583 June 2026 — Answer Walkthrough

✅ = you were right · ❌ = wrong · ⬜ = blank. Per-sub value = question pts / #subs.

## Q1 — Density estimation (12 pts, ±3) — data n=20: {1,1,2,2,3,4,4,4,5,5,5,5,6,9,9,10,10,10,10,11}

Formula `f(x) = k/(n·V)`. Kernel: window [x±h/2], V=h. kNN: r = k-NN dist, V=2r, k tie-adjusted.

| # | Statement | Work | Truth | You |
|---|-----------|------|-------|-----|
| 1 | kernel x=4, h=1 → 1/10 | [3.5,4.5] holds 3 pts → 3/20 | **F** | F ✅ +3 |
| 2 | kNN x=7, k=2 → 3/80 | r=2, ties → 7 pts in [5,9] → 7/(20·4) = 7/80 | **F** | T ❌ −3 |
| 3 | kNN x=7, k=1 → 1/40 | r=1 (pt 6), no ties → 1/(20·2) = 1/40 | **T** | F ❌ −3 |
| 4 | kernel x=4, h=2 → 1/5 | [3,5] holds 8 pts (3,4×3,5×4) → 8/40 = 1/5 | **T** | F ❌ −3 |

**Score −6**

## Q2 — Outlier orderings, Manhattan, k=2 (14 pts, ±3.5)

A(5,2) B(1,7) C(3,4) D(6,6) E(4,7) F(5,5) G(4,6) H(3,7). "Ordered" = non-strictly decreasing scores.

Computed scores (self excluded, ties included in neighborhoods):

| | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| kNN (2-dist) | 4 | 3 | 3 | 2 | 1 | 2 | 2 | 2 |
| LOF | 1.458 | 1.250 | 1.571 | 1.071 | 1.071 | 1.071 | 0.875 | 0.981 |

| # | Claim | Check | Truth | You |
|---|-------|-------|-------|-----|
| 1 | C,D,E per kNN | 3 ≥ 2 ≥ 1 ✓ | **Yes** | No ❌ −3.5 |
| 2 | A,B,C per LOF | C (1.571) is max but last | **No** | Yes ❌ −3.5 |
| 3 | A,C,D per LOF | A (1.458) < C (1.571) | **No** | No ✅ +3.5 |
| 4 | A,B,D per kNN | 4 ≥ 3 ≥ 2 ✓ | **Yes** | No ❌ −3.5 |

**Score −7**

## Q3 — Similarity measures (10 pts, ±2.5)

| # | Claim | Why | Truth | You |
|---|-------|-----|-------|-----|
| 1 | Σ=[[1,2],[2,1]]: Mahalanobis = Euclidean | Only Σ=I gives equality; this Σ isn't even PSD (det=−3) | **F** | T ❌ −2.5 |
| 2 | All symmetric non-binary nominal ⇒ SMC = Jaccard | No absence state → nothing for Jaccard to discard → both = matches/n | **T** | T ✅ +2.5 |
| 3 | Cosine on one-hot dominated by 0-0 matches | Cosine *ignores* 0-0 (dot product counts only 1-1) | **F** | F ✅ +2.5 |
| 4 | Σ=I, mean 0, point on axis: Mah = Euc = Man = Sup | All reduce to \|x₁\| | **T** | T ✅ +2.5 |

**Score +5**

## Q4 — AHC dendrogram (16 pts, ±3.2) — figure: (1,2)@2, (4,5)@6, 3∪{4,5}@8, root@10

Linkage runs on D:

- **Single**: 2, 6, 8, 10 — **exact match** (topology + scale)
- **Complete**: 2, 6, 10, 22 — same topology, other scale
- **Average**: 2, 6, 9, 16.33 — no match

| # | Claim | Truth | You |
|---|-------|-------|-----|
| 1 | Complete: same topology, not scale | **T** | T ✅ +3.2 |
| 2 | Single/Complete proceed from 3 distances alone; Average needs cluster sizes (Lance-Williams weights) | **T** | T ✅ +3.2 |
| 3 | Figure = Single-Linkage exactly | **T** | F ❌ −3.2 |
| 4 | Figure = Average-Linkage | **F** (9, 16.33 ≠ 8, 10) | T ❌ −3.2 |
| 5 | Cut @4 ⇒ {1,2},{3},{4,5} | **F** — 4,5 merge at 6 > 4 ⇒ {1,2},{3},{4},{5} | F ✅ +3.2 |

**Score +3.2**

## Q5 — Apriori pruning (4 pts, ±1) — frequent 3-sets: ABC ABD ABE ABF AEF BCD BCE BDF BEF CEF

Prunable ⇔ some 3-subset missing.

| Candidate | Missing subsets | Prunable | You |
|-----------|----------------|----------|-----|
| ABCE | ACE | **Yes** | Yes ✅ +1 |
| BCDE | BDE, CDE | **Yes** | No ❌ −1 |
| ABEF | none (all 4 frequent) | **No** | No ✅ +1 |
| ABDE | ADE, BDE | **Yes** | Yes ✅ +1 |

**Score +2**

## Q6 — DBSCAN, Manhattan, self counts (10 pts, ±2.5)

| # | Claim | Work | Truth | You |
|---|-------|------|-------|-----|
| 1 | S border, ε=2, MinPts=6 | \|N(S)\|=2 (S,Q) not core; Q core (\|N(Q)\|=6: Q,R,N,O,J,S); S ∈ N(Q) | **T** | T ✅ |
| 2 | P clusters with M, ε=2, MinPts=4 | P,M not core (\|N\|=2,3); G core, M border via G; P's only nbr M not core ⇒ P noise | **F** | F ✅ |
| 3 | P noise, ε=2, MinPts=2 | \|N(P)\|=2 ≥ 2 ⇒ P core | **F** | F ✅ |
| 4 | G core, ε=2, MinPts=6 | N(G)={G,M,C,E,F,H}=6 | **T** | T ✅ |

**Score +10** 🎯

## Q7 — EM-GMM (10 pts, ±2.5) — Σγ₁=3.8, Σγ₂=2.2

| # | Claim | Work | Truth | You |
|---|-------|------|-------|-----|
| 1 | priors 3.8/6, 2.2/6 | πᵢ = Σγᵢ/n | **T** | T ✅ +2.5 |
| 2 | means 14.2/3.8, 9.8/2.2 | Σγ₁x = 9.8, Σγ₂x = 14.2 → μ₁=9.8/3.8≈2.58, μ₂=14.2/2.2≈6.45 — numerators swapped | **F** | F ✅ +2.5 |
| 3 | hard partition needs only posteriors | assign argmaxᵢ P(Cᵢ\|x) — posteriors suffice | **T** | F ❌ −2.5 |
| 4 | model = 3 numerical coefficients | 2 means + 2 vars + 1 free prior = **5** | **F** | T ❌ −2.5 |

**Score 0**

## Q8 — Apriori + rules (10 pts, ±2)

Supports: A5 B4 C5 D6 E1 F4 G5 · frequent 2-sets: AB3 AC3 AD4 CD4 CG3 DF4 DG3 · only frequent 3-set: **ACD (3)**.

| # | Claim | Work | Truth | You |
|---|-------|------|-------|-----|
| 1 | conf(AD⇒C)<θ ⇒ conf(A⇒CD)<θ | same numerator s(ACD); s(A) ≥ s(AD) ⇒ conf(A⇒CD) ≤ conf(AD⇒C) | **Yes** | Yes ✅ +2 |
| 2 | σ=3: >1 frequent 3-set incl. ACD | ACD is the only one | **No** | No ✅ +2 |
| 3 | 2-set candidates = 7 listed | candidates = all C(6,2)=15 pairs; the 7 are those *frequent after counting* | **No** | ⬜ 0 |
| 4 | CD,CG,DG frequent ⇒ CDG frequent | converse of anti-monotonicity invalid; s(CDG)=2<3 | **No** | Yes ❌ −2 |
| 5 | rule AD⇒C: supp 3, conf 3/4 | s(ACD)=3, s(AD)=4 → conf 3/4 ✓ | **Yes** | No ❌ −2 |

**Score 0**

## Q9 — k-Means 1-D, k=3 (14 pts, ±3.5) — A2 B4 C10 D12 E3 F20 G28 H13 I25

| # | Claim | Work | Truth | You |
|---|-------|------|-------|-----|
| 1 | init (2, 4.5, 6): exactly 3 iterations → {ABE},{CDH},{FGI} | trace: {2,3}\|{4}\|rest → {2,3}\|{4,10}\|rest → {2,3,4}\|{10,12,13}\|{20,25,28}; iter 4 unchanged | **T** | T ✅ +3.5 |
| 2 | {ABE},{CDHF},{GI} = trap | centroids 3, 13.75, 26.5 reproduce same assignment (fixed point); better SSE exists (39.33 < 63.25) | **T** | T ✅ +3.5 |
| 3 | simplified silhouette of A equal in both partitions | a(A)=1 both, but b(A) = dist to nearest other centroid: 9.67 vs 11.75 → 0.897 vs 0.915 | **F** | F ✅ +3.5 |
| 4 | {ABE},{CDHF},{GI} better SSE than {ABE},{CDH},{FGI} | 63.25 vs 39.33 — worse | **F** | F ✅ +3.5 |

**Score +14** 🎯

## Scorecard

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | **Total** |
|---|---|---|---|---|---|---|---|---|---|-----------|
| Score | −6 | −7 | +5 | +3.2 | +2 | +10 | 0 | 0 | +14 | **≈21.2/100** |

21 ✅ · 16 ❌ · 1 ⬜. Earned +59.6, guesses cost −38.4 → **blanking all wrong answers ≈ 59.6 = pass** (bar ≈ 50).

*Conventions: inclusive kernel window V=h; tie-adjusted kNN density V=2r; support as count (matches σ=3); coordinates read from printed grids.*
