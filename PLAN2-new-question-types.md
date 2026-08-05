# DM583 Re-exam Plan 2 — Anticipating New Question Types

Companion to `PLAN.md`. That plan closes the gaps June exposed; this one covers what a
*fresh* re-exam could add. Evidence base: the 250-MCQ bank sorts the whole course into
**nine categories** (Introduction, Data Representation, Probability & Density,
Partitioning, Hierarchical, Density-Based, Outlier Detection, Frequent Itemsets,
EM/GMM), and the exercise sheets match. June's exam drew on seven. The topic pool is
closed — "new" means the two under-used categories, or new variants inside familiar
ones.

## Ranked candidates

### 1. Probability & density fundamentals ⟵ most likely

A full exercise sheet (Ex5) that June only touched via GMM. All already tooled:

| Candidate sub | Tool | Trap |
|---|---|---|
| Sample vs. MLE variance | `var(v)` / `var(v, sample=False)` / `mle(v)` | ÷(n−1) vs ÷n — literally MCQ Q3; distractors include mean and std |
| Bayes / posterior from densities+priors | `bayes(...)`, `posteriors(densities, priors)` | evidence = sum of joints, don't forget a component |
| Marginalise a joint table | `marginal(joint, axis)` | sum rule, not product rule (MCQ Q22 distractor set) |
| Expectation | `expect(vals, probs)` | — |
| **Gaussian**-kernel KDE (not the box kernel) | `kde(x, data, h)` in `prob.py` | different beast from `discrete_kernel` — read which kernel is asked |
| Log-likelihood theory | recall | log is monotone (same argmax), product → sum |

### 2. Data representation as computation, not just theory

June's Q3 was concept-only True/False; the MCQ bank is full of *numeric* versions.
The distractors are always **the other measures** — recognition is the whole game:

| Candidate sub | Tool |
|---|---|
| Manhattan / Euclidean / Chebyshev / Minkowski-p on given vectors | `mand, eucd, supd, mink` — compute all four, match the options |
| Cosine vs. Pearson vs. raw inner product | `cosine, pearson, innerprod` (MCQ Q12: all three appear as options) |
| Spearman rank correlation | `spearman` |
| SMC vs. Jaccard on binary vectors | `smc, jaccard, contingency` (prints n11,n10,n01,n00) |
| z-score / min-max normalisation | `zscore, rescale` |
| Ordinal / one-hot encoding | `ordinal, onehot` |
| Which operations per variable type | recall: nominal =,≠ · ordinal +order · numeric +arithmetic |

### 3. Untouched corners of familiar topics (tools ready, June didn't ask)

- **Closed vs. maximal itemsets** — standard material, absent in June. `apriori_full`
  prints both; point checks: `is_closed(db, X)`, `is_maximal(db, X, thresh)`.
- **Rule measures beyond confidence**: `lift`, `conviction`, `rule_jaccard`.
- **DB(ε,π)-outliers** (Knorr–Ng): `db_outlier(data, eps, pi)` — note it uses the
  fraction of *OTHER* points.
- **Mahalanobis as computation** with a given Σ: `covmat`, `mahalanobis` (June only
  asked theory; square the result to compare with R's `mahalanobis()`).
- **Ward linkage** in the AHC question: `ahc_all` runs it, scipy-verified.
- **Dendrogram cutting / #clusters at level h**: `cut(merges, n, k)`.

### 4. Introduction / KDD theory ⟵ no tool possible

KDD criteria (valid = generalises, novel, useful, understandable), supervised vs.
unsupervised, task taxonomy. Pure recall — this is exactly where `PLAN.md` §0 applies:
**≥ ~75% sure or blank.**

## Known tool gap (the one real to-do)

`knn_density` is **1-D only** (V = 2r). If kNN density is asked on 2-D points, the
volume is a disk: V = πr² (d-dim: ball volume). Ten-minute addition to `density.py`
if wanted before the exam:

- `knn_density(data, x, k, dim=2)` → V = π·r² (with the same tie adjustment), print r,
  count, and V explicitly.
- Note: answers stop being clean fractions once π enters — exam more likely stays 1-D,
  which is why this is a *contingency*, not a priority.

## Drill actions (extends PLAN.md §3)

1. One pass through the 250/500 MCQ banks, tagging each question **[tool]** vs
   **[recall]**. Tool-taggable ones: rehearse the call until it's reflexive. Recall
   ones: apply the 75%-or-blank rule honestly.
2. Rehearse category 2 recognition: given four numeric options, compute
   `mand/eucd/supd/mink` (or `cosine/pearson/innerprod`) in one line and match — the
   wrong options *are* the other measures, so computing all of them identifies the
   question's intent too.
3. Redo Ex5 (density + EM) end-to-end with `prob.py` + `density.py` + `gmm.py` — it is
   the most likely source of a new question type and every piece is one call.
