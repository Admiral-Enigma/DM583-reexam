# DM583 — Evaluation of the Re-Exam Attempt (August 2026)

Source: `second_attempt.pdf` (12 questions, 72 sub-questions, 100 points total).
Scoring model (same as `eval.md`): each head question's points split evenly over its
sub-questions; correct = `+points/n`, wrong = `−points/n`, blank = `0`. Passing bar ≈ 50.

Every computational question was re-solved with the `src/exam` toolkit (see
`tmp/verify.py`, `tmp/verify_apriori.py`); theory questions are argued from the
course definitions.

## Final score reconstruction

| Q | Page | Topic | Points | n | ±/sub | Sub-results | Score |
|---|------|-------|--------|---|-------|-------------|-------|
| 1 | 1 | Similarity / dissimilarity | 5 | 5 | 1.0 | ✓ ✓ – – – | **+2.0** |
| 2 | 2–3 | Apriori candidate generation | 5 | 10 | 0.5 | ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ | **+5.0** |
| 3 | 4 | Dendrogram reading (yeast) | 5 | 5 | 1.0 | – – – – – | **0.0** |
| 4 | 5 | EM-GMM | 10 | 5 | 2.0 | ✓ ✓ ✓ ✓ ✓ | **+10.0** |
| 5 | 6 | k-Means: SSE vs. silhouette | 10 | 5 | 2.0 | ✓ ✓ ✓ ✓ ✓ | **+10.0** |
| 6 | 7 | Outlier score orderings | 15 | 5 | 3.0 | ✓ ✓ ✓ ✓ ✓ | **+15.0** |
| 7 | 8 | DBSCAN | 9 | 6 | 1.5 | ✓ ✗ ✓ ✓ ✓ ✓ | **+6.0** |
| 8 | 9 | 1-D k-Means | 10 | 5 | 2.0 | ✓ ✓ ✓ ✓ – | **+8.0** |
| 9 | 10 | Non-parametric density | 12 | 5 | 2.4 | ✓ – ✓ – – | **+4.8** |
| 10 | 11 | AHC linkage theory | 9 | 6 | 1.5 | – – – – – – | **0.0** |
| 11 | 12 | Mixed theory | 5 | 5 | 1.0 | ✓ ✓ – ✓ – | **+3.0** |
| 12 | 13 | Rule confidence propagation | 5 | 10 | 0.5 | – – – – – – – – – – | **0.0** |
| | | **Total** | **100** | **72** | | **41 ✓ / 1 ✗ / 30 blank** | **≈ 63.8** |

### Headline

**63.8 / 100 — a comfortable pass (bar ≈ 50), and a ~43-point improvement over the
21.2 of the first attempt.**

Of the 42 sub-questions that were answered, **41 were correct**. That is a 97.6% hit
rate on everything attempted. The single wrong answer cost 3.0 points (1.5 forgone +
1.5 penalty).

The strategy from `eval.md` — *answer only what you can verify, blank the rest* — was
executed almost perfectly. The 30 blanks cost **33.2 points** in forgone credit but
cost **nothing** in penalties.

---

## Question-by-question analysis

### Q1 — Similarity / dissimilarity measures (5 pts) → **+2.0**

| Sub | Claim | Correct | Answered | Result |
|-----|-------|---------|----------|--------|
| 1 | Pearson captures linear trend, scale-invariant | **True** | True | ✓ +1 |
| 2 | Cosine suitable when sensitivity to 0-0 matches is wanted | **False** — cosine ignores 0-0 matches entirely | False | ✓ +1 |
| 3 | One-hot preserves dimensionality; standard for nominal **and ordinal** | **False** — one-hot *increases* dimensionality, and ordinal variables should get ordinal (rank) encoding | blank | 0 |
| 4 | Spearman = +1 iff the two objects are identical | **False** — +1 for *any* monotone-increasing relation, e.g. (1,2,3) vs (10,20,30) | blank | 0 |
| 5 | SMC = 3/5 and Jc = 2/4 for the two weather rows | **True** — 3 of 5 attributes match; discarding the one asymmetric No-No leaves 2 matches of 4 | blank | 0 |

Three points left on the table here, all on facts that are one line of reasoning each.
Sub 5 in particular is pure arithmetic once you accept the convention that Jaccard drops
the asymmetric 0-0 column: 5 attributes, 3 matches → SMC = 3/5; drop attribute 5 → 4
attributes, 2 matches → Jc = 2/4. Both numbers come out *exactly* as printed, which is
the usual tell that a claim is the intended True.

### Q2 — Apriori candidate generation (5 pts) → **+5.0** ✅ perfect

This one was validated end-to-end. Feeding the exam's own 10-transaction database into
`exam.apriori.apriori(db, 3)` reproduces the exam's stated `L₃` **exactly**, which
confirms both the transaction reading and the convention. The toolkit's
`generate_join` (`p[:-1] == q[:-1]`, i.e. share the first k−2 items) then gives

```
C4 = {ABCG, ABCH, ABGH, CDEG, DEGH}
```

| Itemset | Prefix join (correct) | Loose join (distractor) | Answered | Result |
|---------|----------------------|------------------------|----------|--------|
| ABCD | No | No | No | ✓ |
| ABDG | **No** | Yes | No | ✓ |
| ABCG | Yes | Yes | Yes | ✓ |
| DEGH | Yes | Yes | Yes | ✓ |
| CDGH | **No** | Yes | No | ✓ |
| BEGH | **No** | Yes | No | ✓ |
| ABGH | Yes | Yes | Yes | ✓ |
| ABCH | Yes | Yes | Yes | ✓ |
| BCGH | **No** | Yes | No | ✓ |
| CDEG | Yes | Yes | Yes | ✓ |

The question is built as a trap: **every** "No" option (except ABCD) *is* generable if
you merge any two 3-itemsets sharing two items, and is *not* generable under the real
prefix rule. All four traps were avoided. This is the exact topic that scored a blank
and a wrong answer in June — it is now solid.

### Q3 — Dendrogram reading (5 pts) → **0.0** (all blank)

Left entirely blank, so no points either way.

### Q4 — EM-GMM (10 pts) → **+10.0** ✅ perfect

| Sub | Claim | Correct | Answered |
|-----|-------|---------|----------|
| 1 | GMM assumes within-cluster independence ⇒ zero covariance | **False** — general GMMs allow full covariance matrices | False ✓ |
| 2 | EM-GMM uses Bayes' rule | **True** — the E-step posterior is exactly Bayes | True ✓ |
| 3 | Diagonal covariances ⇒ necessarily spherical | **False** — diagonal gives *axis-aligned* ellipses; spherical only if the diagonal entries are equal | False ✓ |
| 4 | densities 0.0086 / 0.0136, priors 0.3 / 0.7 ⇒ posteriors 0.213 / 0.787 | **True** — 0.3·0.0086 = 0.00258, 0.7·0.0136 = 0.00952, sum 0.0121 → 0.21322 / 0.78678 | True ✓ |
| 5 | EM-GMM insensitive to initialisation, unlike k-Means | **False** — EM is equally initialisation-sensitive (and Q11.2 says so explicitly) | False ✓ |

Both conceptual traps from June (argmax-posterior, parameter counting) have clearly been
internalised — the conceptual subs here were all correct.

### Q5 — k-Means solution comparison (10 pts) → **+10.0** ✅ perfect

Data A=1, B=2, C=4, D=6, E=8, F=9, G=10. Computed values:

| Solution | Clusters | SSE | mean simplified silhouette |
|----------|----------|-----|---------------------------|
| S₁ | {A,B,C},{D,E,F,G} | 13.4167 | **0.767441** |
| S₂ | {A,B},{C,D},{E,F,G} | 4.5000 | **0.777381** |
| S₃ | {A,B,C,D},{E,F,G} | 16.7500 | **0.730691** |

| Sub | Claim | Correct | Answered |
|-----|-------|---------|----------|
| 1 | S₁ better than S₃ (simplified silhouette) | **True** (0.7674 > 0.7307) | True ✓ |
| 2 | S₃ better than S₁ (SSE) | **False** (16.75 > 13.42; lower SSE is better) | False ✓ |
| 3 | S₁ and S₂ not fairly comparable on SSE (different k) | **True** — SSE decreases monotonically with k | True ✓ |
| 4 | S₂ better than S₃ (simplified silhouette) | **True** (0.7774 > 0.7307) | True ✓ |
| 5 | S₁ better than S₂ (simplified silhouette) | **False** (0.7674 < 0.7774) | False ✓ |

Subs 1 and 5 hinge on a gap of **0.0099** between S₁ and S₂. That is not a margin you can
eyeball — it had to be computed, and it was. Best-executed question on the paper.

### Q6 — Outlier score orderings (15 pts) → **+15.0** ✅ perfect, biggest win

Points read off the grid: A(5,2) B(1,7) C(3,4) D(6,6) E(4,7) F(5,5) G(4,6) H(3,7) —
identical to the June grid. Manhattan, k=2, query excluded from its own neighbourhood
(matching `exam.outliers`).

- **kNN** (distance to 2nd NN): A=4, B=3, C=3, D=2, E=1, F=2, G=2, H=2
- **Weighted kNN** (mean of 1st and 2nd NN): A=3.5, B=2.5, C=3, D=2, E=1, F=2, G=1.5, H=1.5
- **LOF**: A=1.4583, B=1.2500, C=1.5714, D=1.0714, E=1.0714, F=1.0714, G=0.8750, H=0.9810

| Sub | Subset & method | Values | Correct | Answered |
|-----|-----------------|--------|---------|----------|
| 1 | A,B,D — weighted kNN | 3.5, 2.5, 2.0 | **Yes** (decreasing) | Yes ✓ |
| 2 | B,C,D — LOF | 1.250, 1.571, 1.071 | **No** (B < C) | No ✓ |
| 3 | C,D,E — kNN | 3, 2, 1 | **Yes** | Yes ✓ |
| 4 | C,E,G — kNN | 3, 1, 2 | **No** (E < G) | No ✓ |
| 5 | A,C,D — LOF | 1.458, 1.571, 1.071 | **No** (A < C) | No ✓ |

This was the single worst question in June (−7.0, the scores were evidently never
computed). It is now the single biggest scorer at +15.0. The toolkit was clearly used
with the right metric this time.

### Q7 — DBSCAN (9 pts) → **+6.0** ⚠️ the only lost points

Grid: A(3,1) B(2,2) C(3,2) D(4,2) E(2,3) F(4,3) G(3,4) H(5,4) I(5,5) J(6,5) K(7,5)
L(8,5) M(3,6) N(6,6) O(7,6) P(2,7) Q(6,7) R(7,7) S(5,8). Manhattan, ε=2, query counted
in its own neighbourhood.

Neighbourhood sizes that matter: |N(A)| = 4 {A,B,C,D}; |N(M)| = 3 {G,M,P};
|N(P)| = 2 {M,P}; |N(Q)| = 6; |N(S)| = 2 {Q,S}.

| Sub | Claim | Correct | Answered | Result |
|-----|-------|---------|----------|--------|
| 1 | S in the same cluster as Q (MinPts=3) | **True** — Q is core (6 ≥ 3), S ∈ N(Q) at distance 2, so S joins as a border point | True | ✓ +1.5 |
| 2 | P *directly* density-reachable from M (MinPts=4) | **False** — P ∈ N(M) ✓, but \|N(M)\| = 3 < 4, so **M is not a core point** | True | ✗ **−1.5** |
| 3 | S is noise (MinPts=3) | **False** — S is a border point of Q's cluster | False | ✓ +1.5 |
| 4 | A is core (MinPts=4) | **True** — \|N(A)\| = 4 ≥ 4 exactly | True | ✓ +1.5 |
| 5 | P in the same cluster as M (MinPts=2) | **True** — both are core at MinPts=2 and mutually within ε | True | ✓ +1.5 |
| 6 | P is a border point (MinPts=2) | **False** — \|N(P)\| = 2 ≥ 2, so P is **core**, not border | False | ✓ +1.5 |

**Diagnosis of the one miss.** Sub 2 is the "directly density-reachable" definition trap.
The relation is **asymmetric and requires the *source* to be core**:

> q is directly density-reachable from p ⟺ q ∈ N_ε(p) **AND** |N_ε(p)| ≥ MinPts.

The distance check passes (d(M,P) = |3−2| + |6−7| = 2 ≤ 2), which is presumably what got
checked. But M has only 3 points in its ε-neighbourhood (G, M, P) and MinPts = 4, so M is
a border point — nothing is directly density-reachable *from* M. Note the exam deliberately
paired this with sub 5, where the same M–P pair *is* connected because MinPts drops to 2.

This is the same family of error as June's Q6 sub on P and M, which was answered
correctly then. The rule to burn in: **check the source point's core status first, the
distance second.**

### Q8 — 1-D k-Means (10 pts) → **+8.0**

Data A=−2, B=0, C=4, D=8, E=12, F=14, G=16.

| Sub | Claim | Correct | Answered | Result |
|-----|-------|---------|----------|--------|
| 1 | {A,B,C,D},{E,F,G} is a local optimum | **True** — centroids 2.5 / 14, no point wants to move (D: 5.5 < 6), so it is a fixed point of Lloyd's | True | ✓ +2 |
| 2 | Euclidean = Manhattan = Suprema between any two points | **True** — in 1-D every Minkowski distance collapses to \|x−y\| | True | ✓ +2 |
| 3 | Iterating from {A,B,C},{D,E,F,G} can improve it further | **False** — centroids 0.667 / 12.5, also a fixed point; iterating changes nothing (and its SSE 53.67 is already *lower* than the 67 of sub 1) | False | ✓ +2 |
| 4 | Prototypes init at F=14, G=16 → after first update become 2.5 and 14 | **False** — the first assignment is {A,B,C,D,E,F} vs {G}, so the new prototypes are **6 and 16** | False | ✓ +2 |
| 5 | Impossible to compute Mahalanobis in 1-D | **False** — in 1-D it is just \|x−μ\|/σ, perfectly well-defined | blank | 0 |

Sub 5 is worth flagging: it is the *same* misconception family as the June Q3 Mahalanobis
miss, and it was blanked rather than guessed. Safe, but 2 points that were available.

### Q9 — Non-parametric density estimates (12 pts) → **+4.8**

Same 8-point grid as Q6, n = 8. Discrete kernel in 2-D: window is a square of side h
centred at the query (so the "volume" is an area, V = h² = 4), points counted with
|xᵢ − qᵢ| ≤ h/2 in **both** coordinates.

| Sub | Claim | Correct | Answered | Result |
|-----|-------|---------|----------|--------|
| 1 | Discrete kernel at G=(4,6), h=2, is 3/32 | **False** — window [3,5]×[5,7] holds E, F, G, H → k=4, f = 4/(8·4) = **1/8** | False | ✓ +2.4 |
| 2 | Discrete kernel = flat weight inside the window; Gaussian = all points, distance-weighted | **True** — textbook description of both kernels | blank | 0 |
| 3 | Discrete kernel at (5,6), h=2, is 1/8 | **True** — window [4,6]×[5,7] holds D, E, F, G → k=4, f = 4/32 = 1/8 | True | ✓ +2.4 |
| 4 | kNN density at (5,6), Manhattan, k=2 (tie-adjustable), is 1/8 | **False** — the three points D, F, G all sit at Manhattan distance 1, so r = 1 and the tie-adjusted k = **3**, giving 3/16 (or 3/32 under a square-volume convention). 1/8 is exactly what you get if you *ignore* the tie adjustment the question flags | blank | 0 |
| 5 | kNN with Suprema distance = ratio of a fraction of points in a square region to that region's area | **True** — the Chebyshev ball *is* a square, and f = (k/n)/V | blank | 0 |

**This is the largest single pool of forfeited points on the paper: 7.2.** Both computed
subs that *were* attempted came out right, so the mechanics are there — the two generic
descriptions (subs 2 and 5) were plain-language restatements of the definitions and were
free points. Sub 4 needed the tie adjustment, which the question itself hints at in
parentheses.

Note this was the worst topic in June (−6.0, no tool existed). It produced no wrong
answers this time.

### Q10 — AHC linkage theory (9 pts) → **0.0** (all blank)

Setup: clusters A (10 objects), B (20), C (30), with linkage distances d(A,B), d(A,C),
d(B,C). Correct answers, for reference:

| Sub | Claim | Correct | Why |
|-----|-------|---------|-----|
| 1 | CL and AL merge the same pair if the relative order of distances agrees | **True** | Every AHC variant merges the *minimum*-distance pair; same order ⇒ same minimum |
| 2 | Average-linkage update = (d(A,C)+d(B,C))/2 = 4.5 | **False** | Average linkage is **size-weighted**: (10·4 + 20·5)/30 = **4.667** |
| 3 | Cannot know the merger height without d(A,B) | **True** | The dendrogram height of a merge *is* the linkage distance between the merged clusters |
| 4 | CL update uses only d(A,C), d(B,C), no sizes, no raw pairwise distances | **True** | d(AB,C) = max(d(A,C), d(B,C)) — Lance-Williams with no size terms |
| 5 | CL merges the *maximum*-distance pair | **False** | "Complete" describes how the inter-cluster distance is *defined* (max over point pairs), not which pair gets merged |
| 6 | Height = 3 but cannot recover d(A,B) without knowing the linkage | **False** | Height = d(A,B) regardless of linkage, so d(A,B) = 3 |

Answer pattern: **T, F, T, T, F, F**. Nine points, all mechanical Lance-Williams /
definition facts, no arithmetic beyond one weighted average. The single biggest
recoverable block on the paper.

### Q11 — Mixed theory (5 pts) → **+3.0**

| Sub | Claim | Correct | Answered | Result |
|-----|-------|---------|----------|--------|
| 1 | Unsupervised outlier scoring; high score = anomaly *or* unusual non-anomaly | **True** | True | ✓ +1 |
| 2 | EM-GMM gets stuck in local optima; restart and pick best log-likelihood | **True** | True | ✓ +1 |
| 3 | Larger kernel width / larger k ⇒ *spikier*; smaller ⇒ smoother | **False** — exactly backwards; larger h or k **smooths**, smaller values give spiky/noisy estimates | blank | 0 |
| 4 | Spearman more outlier-robust than Pearson because it ranks | **True** | True | ✓ +1 |
| 5 | A ⇒ B means "A causes B" | **False** — association is co-occurrence, never causation; this is the most repeated warning in the course | blank | 0 |

Both blanks were "reversed statement" / "correlation ≠ causation" items — the two most
formulaic false-statement patterns in the whole subject. 2 free points.

### Q12 — Rule confidence propagation (5 pts) → **0.0** (all blank)

Given conf({A,B,C} ⇒ {D,E,F}) < θ. The governing identity is

> conf(X ⇒ Z∖X) = supp(Z) / supp(X),  where Z = A∪B∪C∪D∪E∪F.

So within **the same itemset Z**, shrinking the antecedent raises supp(X) and therefore
**lowers** confidence. A rule is *certain* to fall below θ iff its antecedent is a subset
of {A,B,C} **and** its item union is exactly Z = {A,B,C,D,E,F}. Everything else is
indeterminate.

| Rule | Union = Z? | Antecedent ⊆ {A,B,C}? | Certain below θ? |
|------|-----------|----------------------|------------------|
| {A,B} ⇒ {D,E} | No (ABDE) | — | **No** |
| {A,C} ⇒ {D,E,F} | No (ACDEF) | — | **No** |
| {A,B,C,D} ⇒ {E,F} | Yes | No — *larger* antecedent ⇒ *higher* confidence | **No** |
| {D,E,F} ⇒ {A,B,C} | Yes | No | **No** |
| {B,C} ⇒ {A,D,E,F} | Yes | Yes | **Yes** |
| {A,B} ⇒ {D,E,F} | No (ABDEF) | — | **No** |
| {A,B} ⇒ {C,D,E,F} | Yes | Yes | **Yes** |
| {A,C} ⇒ {B,D,E,F} | Yes | Yes | **Yes** |
| {A} ⇒ {B,C,D,E,F} | Yes | Yes | **Yes** |
| {C} ⇒ {A,B,D,E,F} | Yes | Yes | **Yes** |

Answer pattern: **No, No, No, No, Yes, No, Yes, Yes, Yes, Yes**.

Five points on a two-line rule, decidable by inspection with no data and no arithmetic.
Note June's Q8 sub 1 was the same theorem in the opposite direction and was answered
**correctly** then — the knowledge was already there.

---

## Where the points went

| Bucket | Points |
|--------|--------|
| Earned from correct answers | **+65.3** |
| Lost to the one wrong answer (penalty) | −1.5 |
| **Net score** | **63.8** |
| Forgone on blanks (had they all been right) | 33.2 |
| Theoretical maximum given the one error | 97.0 |

### Forfeited points, ranked

| Question | Blanks | Points forfeited | Nature of what was skipped |
|----------|--------|------------------|---------------------------|
| Q10 AHC linkage theory | 6 | **9.0** | Lance-Williams update rules + "which pair does linkage merge" |
| Q9 density estimates | 3 | **7.2** | Two plain definition restatements + one tie-adjusted kNN density |
| Q3 dendrogram | 5 | **5.0** | Visual cut-and-count reading |
| Q12 rule confidence | 10 | **5.0** | One monotonicity identity, applied ten times |
| Q1 similarity | 3 | **3.0** | One-hot / Spearman / SMC-Jaccard facts |
| Q8 1-D k-Means | 1 | **2.0** | Mahalanobis is computable in 1-D |
| Q11 mixed theory | 2 | **2.0** | Reversed-statement + causation traps |
| **Total** | **30** | **33.2** | |

**Every single one of these is theory, not computation.** There is not one forfeited
point that required a script. The computational questions — Apriori, EM-GMM, k-Means,
outliers, DBSCAN, density arithmetic — went 41-for-42.

## What changed since June

| | June (first attempt) | August (re-exam) |
|---|---|---|
| Score | 21.2 | **63.8** |
| Sub-questions answered | 37 of 38 | 42 of 72 |
| Correct / wrong | 21 ✓ / 16 ✗ | **41 ✓ / 1 ✗** |
| Accuracy on answered subs | 57% | **97.6%** |
| Points lost to penalties | −38.4 | **−1.5** |

June's diagnosis was: *the knowledge was sufficient; guessing destroyed the score.* That
diagnosis was correct, and the fix worked. Discipline about blanking converted a −38.4
penalty bill into −1.5.

Both June's worst topics were repaired outright: non-parametric density (−6.0 → +4.8,
zero errors) and outlier orderings (−7.0 → +15.0, perfect). Apriori candidate generation,
which produced a blank and a wrong answer in June, was answered perfectly on all ten subs
including four deliberate traps.

## Grading caveats

- The scoring model (+p/n, −p/n, 0) is assumed from `eval.md`; if the real scheme does not
  penalise wrong answers, the score is 65.3 instead of 63.8. Either way it passes.
- Q6/Q7/Q9 point coordinates were read off the printed grids; the Q6 grid is identical to
  June's and the DBSCAN conclusions were checked against the full ε=2 neighbourhood table,
  so they are robust to small misreadings.
- Q9 sub 4 is marked False under both the L1-ball (V = 2r² → 3/16) and square
  (V = (2r)² → 3/32) volume conventions; only ignoring the tie adjustment produces the
  claimed 1/8. It was blank, so it does not affect the score.
- Q2 uses the prefix-join convention, independently confirmed by `exam.apriori`
  reproducing the exam's own `L₃` from the transaction database.
