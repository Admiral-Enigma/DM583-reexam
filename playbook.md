# DM583 June 2026 — Complete Solving Playbook

How to work every question with the toolkit (`uv run python` → `from exam import *` → `cheat()`).
Companion to `walkthrough.md` (the graded post-mortem). Dry-run 2026-08-03: **86.8/100**, one ✗ (June: 21.2).

## The rules (worth more than any answer below)

1. **Answer only what a tool printed or you derived on paper.** Recall < ~75% sure → BLANK. Blank = 0, wrong = −p/n.
2. **Count the input.** `analyze` prints `n=…`, `apriori` prints `N=…` — compare against the figure/table before reading any result. One missing point silently flips answers (a missing F(4,3) turned G from core into border in rehearsal).
3. **Find the hinge word.** Exam bait = true fragment + one poisoned word: *candidates*, *guaranteed*, *fully corresponds*, *necessarily*, *exactly*. Check THAT word against output, not the familiar numbers around it.
4. **Never answer a sub-pair as an inverted guess** (June Q4.3/4.4: −6.4 that way).
5. Labels like P₁/P₂ can mean different partitions in different subs — re-read per sub.

## The six memorized facts (not computable mid-exam)

1. Hard partition = argmax posterior; the posteriors ALONE suffice.
2. 1-D GMM parameters: k means + k variances + (k−1) priors → 2 components = **5**.
3. Apriori candidates = ALL pairs of frequent 1-itemsets, C(m,2); the "frequent" list is what survives counting.
4. Anti-monotonicity is one-directional: frequent ⇒ subsets frequent. Converse gives a candidate, never a guarantee.
5. "Corresponds to a dendrogram" = topology **AND** merge heights.
6. Mahalanobis = Euclidean **iff** Σ = I; average linkage needs cluster **sizes** (Lance–Williams), single/complete don't.

Extra facts from the official sample MCQ (theory subs the June exam didn't use):

7. EM-GMM **uses Bayes' rule** (the E-step is Bayes); it IS sensitive to initialization (local optima, like k-means).
8. Full-covariance GMM does NOT assume independence within clusters. Diagonal Σ ⇒ axis-aligned **ellipses**; spherical only if all variances are equal.
9. In 1-D, all Minkowski distances (p=1, 2, ∞, …) coincide.
10. DBSCAN with MinPts = 1: every point is core ⇒ **noise is impossible**, isolated points become singleton clusters. Raising to MinPts = 2 can turn them into noise.
11. Maximal = frequent with NO frequent superset. Closed = NO superset with the SAME support. `apriori_full(db, σ)` prints both lists.
12. MLE for a single Gaussian: sample mean, variance with **/n** (not n−1) — `mle(data)`.
13. E-step numeric subs (densities + priors → posteriors): `responsibilities([d1, d2], [pi1, pi2])`.

From Exercise 3 (partitioning):

14. Squared vs standard Euclidean in k-Means: **same partition** (monotone transform — closest centroid unchanged). k-Means' objective is defined on the squared version.
15. Parallel/distributed k-Means is EXACT: each site sends per-cluster (count, coordinate-sum); central node computes centroids as Σsums/Σcounts. No even-data-split requirement, no approximation.
16. Incremental centroid update: v_new = (|C|·v + Σjoining − Σleaving) / (|C| + #join − #leave).
17. Per-point silhouettes, both versions: `silhouette_point(data, partition, "12")` — full SWC (avg distances to members) AND simplified (centroid distances). `kmeans_trace`/`analyze_partitions` also take 2-D points: `{'1': (1,2), ...}`, init `[(6,6),(4,6),(5,10)]`.
18. Elbow method: SSE knee. SWC method: **maximum peak**, and SWC is undefined for k=1 (start at k=2).

From chhan24's drill bank (recall-only items, no tool needed):

19. Single/complete linkage have **no inversions** — merge heights are non-decreasing. Single-link suffers **chaining** (elongated clusters via close intermediate points); complete-link resists it (max distance). **Ward** merges the pair with the smallest increase in total within-cluster SSE.
20. Kernel bandwidth: h → 0 undersmooths — spiky, HIGH variance; large h oversmooths — high bias (bias-variance tradeoff). kNN density is **locally adaptive**: r shrinks in dense regions, grows in sparse ones.
21. kNN outlier score with larger k = smoother/more global, LESS sensitive to tiny local fluctuations. LOF ≈ 1 → normal point; LOF ≫ 1 → outlier; a point with a SMALL kNN-distance can still have HIGH LOF (its neighbours sit in much denser surroundings — LOF is relative density).
22. k-Means: one Lloyd iteration is O(n·k·d); guaranteed to terminate finitely (SSE never increases, finitely many partitions); a centroid need NOT be a data point; favors compact/convex, similar-size clusters — fails on elongated/varied-density shapes.
23. EM-GMM: no fixed iteration bound exists (only monotone likelihood ascent); initializing components IDENTICALLY is a degenerate fixed point — they stay identical, symmetry never breaks; GMMs approximate any continuous density as K → ∞.
24. Cosine similarity: [0,1] for non-negative data (TF-IDF, one-hot); [−1,1] in general. Minkowski p=1 Manhattan, p=2 Euclidean, p→∞ Chebyshev/supremum.

---

## Q1 · Density estimation (12 pts, ±3)

Data (n=20): `{1,1,2,2,3,4,4,4,5,5,5,5,6,9,9,10,10,10,10,11}`

```python
data = [1,1,2,2,3,4,4,4,5,5,5,5,6,9,9,10,10,10,10,11]
density_report(data, [("kernel",4,1), ("knn",7,2), ("knn",7,1), ("kernel",4,2)])
```

Conventions: `f = k/(n·V)`. Kernel: window `[x−h/2, x+h/2]` **inclusive**, V = h. kNN: r = k-NN distance, **tie-adjust k to all points at d ≤ r**, V = 2r.

| # | Claim | Work | Verdict |
|---|-------|------|---------|
| 1 | kernel x=4, h=1 → 1/10 | window [3.5,4.5] holds the three 4s → 3/20 | **F** |
| 2 | kNN x=7, k=2 (tie-adj.) → 3/80 | r=2, but SEVEN points at d≤2 {5,5,5,5,6,9,9} → 7/80 | **F** |
| 3 | kNN x=7, k=1 → 1/40 | r=1, only point 6 → 1/(20·2) | **T** |
| 4 | kernel x=4, h=2 → 1/5 | [3,5] holds {3,4,4,4,5,5,5,5}=8 → 8/40 | **T** |

Trap: sub 2 announces "adjustable in case of ties" and then claims the un-adjusted value. The tool prints `tie-adjusted!` when k_eff ≠ k — that flag IS the answer.

## Q2 · Outlier orderings, Manhattan, k=2 (14 pts, ±3.5)

"Correctly ordered" = non-strictly decreasing scores; query excluded from own neighborhood.

```python
res = analyze("A 5 2 / B 1 7 / C 3 4 / D 6 6 / E 4 7 / F 5 5 / G 4 6 / H 3 7",
              "man", k=2)
check_order("C,D,E", res["knn"])   # each sub = one call
check_order("A,B,C", res["lof"])
check_order("A,C,D", res["lof"])
check_order("A,B,D", res["knn"])
```

Computed: kNN A4 B3 C3 D2 E1 F2 G2 H2 · LOF A≈1.458 B=1.25 C≈1.571 D=E=F≈1.071 G=0.875 H≈0.981.

| # | Claim | Check | Verdict |
|---|-------|-------|---------|
| 1 | C,D,E per kNN | 3 ≥ 2 ≥ 1 | **Yes** |
| 2 | A,B,C per LOF | C (1.571) is the max but listed last | **No** |
| 3 | A,C,D per LOF | 1.458 < 1.571 at the first step | **No** |
| 4 | A,B,D per kNN | 4 ≥ 3 ≥ 2 | **Yes** |

Ties are allowed ("not strictly") — a flat sequence is correctly ordered. `check_order` prints the full ranking; read each claimed sequence off it.

## Q3 · Similarity measures (10 pts, ±2.5)

```python
dist_compare([[1,2],[2,1]])                 # sub 1: PSD check + Mah vs Euc per point
dist_compare([[1,0],[0,1]], points=[[3,0],[0,-2]])   # sub 4: axis points
binary_compare([1,1,0],[1,0,1], pad=20)     # subs 2–3: SMC / Jaccard / cosine vs 0-0
```

| # | Claim | Reason | Verdict |
|---|-------|--------|---------|
| 1 | Σ=[[1,2],[2,1]]: Mahalanobis = Euclidean necessarily | equality iff Σ=I; this Σ has det −3 (not even PSD) — tool flags it | **F** |
| 2 | symmetric non-binary nominal ⇒ SMC = Jaccard | no absence state → nothing for Jaccard to discard → both = matches/n | **T** |
| 3 | one-hot cosine dominated by 0-0 matches | backwards — cosine IGNORES 0-0 (nothing enters dot product or norms); `pad=20` demo: cosine unchanged, SMC inflates | **F** |
| 4 | Σ=I, mean 0, point on an axis: Mah=Euc=Man=Sup | one nonzero coordinate → all four = \|x₁\|; tool marks "all four EQUAL" | **T** |

Caveat: numeric tests **prove False** by counterexample; for "necessarily True" claims pair the tool with the one-line reason (facts #6). Can't state the reason → blank candidate.

## Q4 · AHC & dendrogram (16 pts, ±3.2)

Figure: {1,2}@2 · {4,5}@6 · 3+{4,5}@8 · root@10.

```python
D, labels = sqmat("0 2 14 22 18 / 2 0 10 18 16 / 14 10 0 8 10 / 22 18 8 0 6 / 18 16 10 6 0")
# paste rows as printed — validates square/diagonal/SYMMETRY (catches typos);
# pairwise form instead: D, labels = pairmat("d(1,2)=2 d(1,3)=14 ...")
match_dendrogram(D, [2,6,8,10], labels=labels)
cut_height(D, "single", 4, labels=labels)
```

Computed heights: single **2,6,8,10** · complete 2,6,10,22 · average 2,6,9,16.33. All three share the figure's topology (same merge partners in the printed sequences).

| # | Claim | Check | Verdict |
|---|-------|-------|---------|
| 1 | Complete: same topology, not scale | shape ✓ (read merge list), heights 10,22 ≠ 8,10 ✓ — both halves of the AND hold | **T** |
| 2 | Single/Complete proceed from the 3 inter-cluster distances alone; Average needs more | single/complete update = min/max of stored numbers; average needs cluster **sizes** (fact #6) | **T** |
| 3 | Figure **fully** corresponds to Single | heights AND topology match exactly | **T** |
| 4 | Figure corresponds to Average | heights 9, 16.33 ≠ 8, 10 → dead regardless of shape | **F** |
| 5 | Cut @4 ⇒ {1,2},{3},{4,5} | only the @2 merge is below the line; {4,5} merges at 6>4 → four clusters | **F** |

"Corresponds" decomposition: (a) topology — compare printed merge sequence to the picture; (b) scale — `match_dendrogram` verdict. Statement true only per its exact quantifier ("only…but not" = AND). Cut rule: horizontal line at h, merges with height < h have happened; cut exactly ON a merge height → convention-dependent → blank candidate.

## Q5 · Apriori candidate pruning (4 pts, ±1)

Frequent 3-sets: ABC ABD ABE ABF AEF BCD BCE BDF BEF CEF.

```python
F3 = ["ABC","ABD","ABE","ABF","AEF","BCD","BCE","BDF","BEF","CEF"]
for c in ["ABCE","BCDE","ABEF","ABDE"]: prunable(c, F3)
```

Rule: prunable ⇔ ANY (k−1)-subset missing from the frequent list (fact #4, downward direction). Drop each item in turn, look up:

| Candidate | Missing 3-subsets | Verdict |
|-----------|-------------------|---------|
| ABCE | ACE | **Yes, prune** |
| BCDE | BDE, CDE | **Yes** |
| ABEF | none (ABE, ABF, AEF, BEF all frequent) | **No** — must count support |
| ABDE | ADE, BDE | **Yes** |

Traps: "survives pruning" ≠ "frequent" (ABEF still needs counting). Search systematically — June missed BDE/CDE by eyeballing.

## Q6 · DBSCAN, Manhattan, self counts (10 pts, ±2.5)

```python
data = ("A 3 1 / B 2 2 / C 3 2 / D 4 2 / E 2 3 / F 4 3 / G 3 4 / H 5 4 / "
        "I 5 5 / J 6 5 / K 7 5 / L 8 5 / M 3 6 / N 6 6 / O 7 6 / P 2 7 / "
        "Q 6 7 / R 7 7 / S 5 8")            # 19 points — COUNT THEM vs the figure!
res = analyze(data, "man", db=[(2,6), (2,4), (2,2)])
```

| # | Claim | Read-off | Verdict |
|---|-------|----------|---------|
| 1 | S border, ε=2, MinPts=6 | eps=2/6 block: `S:border` (\|N(S)\|=2, but S ∈ N(Q) and Q is core) | **T** |
| 2 | P clusters with M, ε=2, MinPts=4 | eps=2/4 block: `P:noise` (P not core, its only neighbor M isn't core either) | **F** |
| 3 | P noise, ε=2, MinPts=2 | eps=2/2 block: `P:core` (\|N(P)\|=2 ≥ 2, self + M) | **F** |
| 4 | G core, ε=2, MinPts=6 | eps=2/6 block: `G:core` (N(G)={G,M,C,E,F,H}=6) | **T** |

All three (ε, MinPts) settings in ONE `analyze` call, then each sub is a lookup. The whole question lives or dies on transcription — n=19, spot-check one distance in the matrix (e.g. F→G = 2) before answering anything. Definitions: core \|N\| ≥ MinPts (self counts here); border = non-core within ε of a core; noise = rest.

## Q7 · EM-GMM (10 pts, ±2.5)

```python
xs = [2, 3, 7, 9, 2, 1]
g  = [[.9,.1],[.8,.2],[.3,.7],[.1,.9],[.9,.1],[.8,.2]]   # rows = points!
mstep1d(xs, g)
hard_partition(g)      # sub 3
param_count(2, 1)      # sub 4
```

`mstep1d` = ONE M-step: fixes the given posteriors, re-estimates π, μ, σ² with every numerator/denominator printed. (Reverse direction, if params given instead: `gauss` + `responsibilities`.)

| # | Claim | Check | Verdict |
|---|-------|-------|---------|
| 1 | priors → 3.8/6, 2.2/6 | Σγ₁=3.8, Σγ₂=2.2, π=Σγ/n; sanity 3.8+2.2=6 | **T** |
| 2 | means → 14.2/3.8, 9.8/2.2 | printout: μ₁ = **9.8**/3.8, μ₂ = **14.2**/2.2 — numerators swapped | **F** |
| 3 | hard partition needs only posteriors | fact #1: argmax posterior | **T** |
| 4 | model = 3 numerical coefficients | fact #2: 2+2+1 = **5** ("3" counts parameter *types*) | **F** |

Sub-2 trap: every claimed number is a real intermediate value, just mispaired. Match numerator AND denominator per component.

## Q8 · Apriori & association rules (10 pts, ±2)

```python
db = parse_db("A,B,C,D / A,C,D,F / A,C,D,E,G / A,B,D,F / B,C,G / D,F,G / A,B,G / C,D,F,G")
apriori(db, 3)                       # levels: 15 candidates -> 7 frequent -> ACD only 3-set
rule(db, "AD", "C")                  # sub 5
conf_compare(db, "AD", "C", moved="D")   # sub 1
support(db, "CDG")                   # sub 4 counterexample: 2
```

| # | Claim | Check | Verdict |
|---|-------|-------|---------|
| 1 | conf(AD⇒C) < θ ⇒ conf(A⇒CD) < θ, certain | same numerator supp(ACD); supp(A) ≥ supp(AD) ⇒ conf(A⇒CD) ≤ conf(AD⇒C); here both 3/4 (equality allowed) | **Yes** |
| 2 | σ=3: >1 frequent 3-itemset, incl. ACD | L3 printout: ACD(3) is the ONLY one | **No** |
| 3 | candidate 2-itemsets = the 7 listed, all frequent | candidates = C(6,2) = **15** (L2 table rows); the 7 are the *frequent survivors* — poisoned word: "candidates" (fact #3) | **No** |
| 4 | CD, CG, DG frequent ⇒ CDG **guaranteed** frequent | converse of anti-monotonicity (fact #4); no calculation needed — and supp(CDG)=2<3 is the counterexample sitting in the L3 printout | **No** |
| 5 | rule AD⇒C: support 3, confidence 3/4 | `rule` prints supp count = supp(ACD) = 3, conf = 3/4 | **Yes** |

Conventions: rule support = supp(antecedent ∪ consequent); σ is a **count** here (`rule` prints count and fraction both). `parse_db` swallows `"1: A B C D / …"` — id prefixes stripped; check `N=8`.

## Q9 · k-Means, k=3 (14 pts, ±3.5)

```python
data = dict(A=2, B=4, C=10, D=12, E=3, F=20, G=28, H=13, I=25)
kmeans_trace(data, [2, 4.5, 6])
analyze_partitions(data,
    {"natural": [["A","B","E"],["C","D","H"],["F","G","I"]],
     "trap":    [["A","B","E"],["C","D","H","F"],["G","I"]]},
    compare_point="A")
```

| # | Claim | Check | Verdict |
|---|-------|-------|---------|
| 1 | init (2, 4.5, 6): exactly 3 iterations → {ABE},{CDH},{FGI} | trace: iters 1–3 change, iter 4 confirms; convention = count *changing* cycles | **T** |
| 2 | {ABE},{CDHF},{GI} = trapped local minimum, better exists | `fixed point True` + trap flag; SSE 63.25 vs natural 39.33 | **T** |
| 3 | s(A) certain to be equal in both partitions since A's cluster unchanged | a(A)=1 both, but b(A) = dist to nearest OTHER centroid: 9.67 vs 11.75 → s 0.897 vs 0.915 | **F** |
| 4 | {ABE},{CDHF},{GI} better SSE than {ABE},{CDH},{FGI} | better = LOWER; 63.25 > 39.33 | **F** |

Traps: sub-3 bait — "own cluster unchanged" fixes a, but b depends on the other clusters. P₁/P₂ labels swap between subs 3 and 4 — name partitions yourself. "Better SSE" = lower, always.

---

## Warm-up ritual (rehearse to < 2 min)

```
uv run python
>>> from exam import *
>>> cheat()                                   # tool map on screen
>>> res = analyze("A 5 2 / B 1 7", "man", k=2)   # finger-check the pipeline
```

Per question: type data → **check n against the figure** → spot-check one matrix cell → run the calls above → answer only what's printed → grade discipline, not luck.
