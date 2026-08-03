# DM583 Re-exam Plan — Tools & Study Priorities

Derived from `eval.md`. Two levers, in order of impact:

1. **Answer discipline** — the failed attempt already contained a passing score (+59.6 from correct answers); wrong guesses (−38.4) sank it.
2. **Close the specific topic/tool gaps** that produced the wrong answers.

---

## 0. Exam strategy (worth more than any tool)

The scoring is symmetric (+p / −p / 0). A random guess has expected value 0, but *misconception-driven* answers are systematically wrong — worse than random. Rule for the re-exam:

- **Answer only what you have computed with a script or derived on paper.**
- If a sub-question is pure recall and you feel less than ~75% sure, **leave it blank**. Blank is a strategy, not a failure.
- Budget: with 9 questions in the exam window, reserve the first minutes of each question for typing the dataset into the tools (see §1.1). If the dataset can't be entered in time, do the conceptual subs and blank the numeric ones.
- Beware complementary-pair guessing (Q4 subs 3/4 were answered as an inverted pair — both wrong, −6.4).

## 1. Tools to develop

> **STATUS 2026-08-03: BUILT — single package `src/exam/`** (uv-managed; `uv run python`
> → `from exam import *` gives everything in one REPL; see README.md for the tool map).
> The standalone `tools/` dir was merged into the package and deleted. Functions added in
> the merge: `kmeans_trace` (named-point Lloyd trace + iteration count), `analyze_partitions`
> (SSE + fixed-point/trap check + silhouette comparison), `cut_height` (dendrogram cut at a
> level, June Q4.5 style), `hard_partition`, `check_claim`, `conf_compare`, `density_report`.
> `uv run pytest` (24 tests) includes June-exam replays: Q1 3/20·7/80·1/40·1/5; Q4 cut@4 →
> four clusters; Q8 conf monotonicity; Q9 3 iters·trap·SSE 39.33/63.25.

The existing library (`dist.py`, `cluster.py`, `outliers.py`, `freq.py`, `gmm.py`, `prob.py`) is nearly complete algorithmically. The gaps are (a) one missing topic, (b) drivers that make the tools usable in exam time, (c) output that "shows work" so answers can be checked against claimed values.

### 1.1 `density.py` — non-parametric density estimation ⟵ **only genuinely missing algorithm (−9 pts)**

- `discrete_kernel(data, x, h)` → count points with |xᵢ−x| ≤ h/2, return count/(n·h); print the window, the points inside, and the fraction in lowest terms (exam claims are fractions like 1/5).
- `knn_density(data, x, k)` → r = distance to k-th NN, tie-adjust k to all points with d ≤ r, return k_adj/(n·2r); print r, the tie-adjusted count, and the fraction. Support d-dimensional later if needed (V of ball).
- Both must print intermediate values, not just the result — exam distractors are plausible wrong fractions.

### 1.2 `exam.py` — one interactive driver for geometric questions (−10.5 pts at Q2)

The Q2/Q6-style questions give ~8–19 points on a grid. The blocker in June was data entry + metric selection, not algorithms. Build one entry point:

- Input: labeled points pasted as `A 5 2 / B 1 7 / ...`, metric choice (`man`/`euc`/`sup`), k / ε / MinPts.
- Output in one shot: full distance matrix, kNN outlier scores (dist-to-kth and weighted variants), LOF table (k-dist, neighborhood with ties, lrd, LOF), DBSCAN core/border/noise + cluster labels for each queried (ε, MinPts).
- Add `check_order("C,D,E", scores)` helper that directly answers "is this subset correctly ordered (non-strictly decreasing)?" — the exact form of Q2's subs.

### 1.3 Apriori upgrades (−4 pts + 1 blank at Q5/Q8)

- Un-comment / restore the **pre-prune candidate printout** in the apriori script; print, per level: frequent (k−1)-itemsets → *all* generated candidates → pruned candidates (with the missing subset named) → surviving frequent itemsets with counts. That answers candidate-generation subs (Q8.3) and prune subs (Q5) directly.
- `prunable(candidate, frequent_k_minus_1)` → lists missing subsets (Q5 in one call).
- `rule(db, ante, cons)` → prints support count, relative support, confidence as a fraction, lift. (`freq.py` had support/confidence — they just weren't wired into an obvious one-liner.)

### 1.4 AHC dendrogram matcher (−6.4 pts at Q4)

`cluster.ahc(D, method)` already works from a distance matrix. Add:

- `ahc_all(D)` → run single/complete/average (and ward), print each merge sequence with heights side by side.
- `match_dendrogram(D, merges_heights)` → given the dendrogram's merge levels (e.g. 2, 6, 8, 10), report per linkage: topology match? scale match? This mechanically answers "does the dendrogram correspond to X-linkage" subs.

### 1.5 GMM M-step calculator (Q7 computational subs were fine; make it bulletproof)

- `mstep(xs, gammas)` → per component: Σγ, prior = Σγ/n, μ = Σγx/Σγ, σ² = Σγ(x−μ)²/Σγ. Print numerators/denominators explicitly (exam distractors swap them, exactly as Q7.2 did).
- `param_count(k, d)` → prints the parameter-count breakdown (k means + k variances + (k−1) priors for 1-D) to kill the Q7.4 class of question.

### 1.6 Simplified silhouette (Q9 went fine, but the tool is missing)

`cluster.silhouette` is the full pairwise version. Add per-point **simplified** silhouette (centroid-based a and b) — exam asks about individual observations (Q9.3).

### 1.7 Packaging

- Everything importable from one REPL session: `from exam import *`. Rehearse a 2-minute warm-up: open REPL, paste a dataset, get a distance matrix. Speed is the point.

## 1.8 Borrow from chhan24's code (`chhan24_code/datamining/`)

Analysis 2026-08-03. What his library covers that ours didn't, and what to watch out for:

**Adopt (fills our PLAN gaps directly):**

- `knn_density.py` → covers §1.1: discrete kernel + kNN density with tie-adjusted k and d-dim ball volume (1-D V=2r via the gamma-function formula — verified correct). Missing from his version: fraction output and window/points printout; add those when porting.
- `k_means.py` → covers §1.6 and more: per-point **simplified silhouette**, fixed-point/stability check ("would k-means be trapped here?"), SSE ranking of named partitions, Lloyd simulation with per-iteration printout. Best single file in his repo — adopt nearly verbatim.
- `EM_GMM.py` → covers most of §1.5: full M-step (N_k, π, μ, σ²) with explicit numerator/denominator printout plus a `check_claim()` helper that directly tests exam statements. Add `param_count()` ourselves.
- `Apriori.py` → `can_prune()`/`prune_candidates()` covers §1.3's prunable(); his doesn't name the missing subset — ours should.
- `Distance_mesure.py` / `cosine_check.py` → pattern worth copying: encode a theory claim as a numeric experiment (e.g. Mahalanobis vs Euclidean under a given Σ, cosine under 0-0 padding). Kills Q3-type doubt in seconds.

**Do NOT blindly trust:**

- His `kNN.py` drops ALL zero distances (`if dist != 0`) — silently wrong if the dataset contains duplicate points.
- His `knn_density` counts the query point itself when the query coincides with a data point (distance 0 is ≤ r) — convention differs from "density at x from the sample"; his own `__main__` example prints `Correct = False` because of this.
- His `DBSCAN.py` hardcodes Euclidean — June's exam was Manhattan. Needs a metric parameter (ours has one).
- His `AHC.py` is a scipy plot wrapper — fine for topology, useless for exact merge heights. Our `cluster.ahc` printing heights stays the primary tool; §1.4's `match_dendrogram` is still unbuilt in both repos.
- `Points.py` is 2-D only (x, y attributes).

**Still missing in BOTH repos:** ~~`exam.py` one-shot grid driver (§1.2), dendrogram matcher (§1.4), `param_count()` (§1.5)~~ — all built in `tools/` on 2026-08-03.

**Practice simulator:** his `practice/main.html` (~80 T/F items, MathJax, localStorage). Ours: `practice/simulator.html` — 40 fresh script-verified items with a **BLANK option and real exam ± scoring** plus a counterfactual "score if you had blanked your wrong answers" report. Drills the calibration skill that decided June, not just recall.

## 2. Topics to study hard (ranked)

1. **Non-parametric density estimation** (Q1, −9). Master `f = k/(n·V)` in both directions: kernel (fix V, count k) vs kNN (fix k, find V = 2r), inclusive window boundaries, tie adjustment of k. Redo Q1 by hand until all four subs are automatic, then verify with `density.py`.
2. **LOF pipeline by hand** (Q2, −10.5). k-distance → neighborhood with ties → reach-dist = max(k-dist(o), d(p,o)) → lrd → LOF. Do one full 8-point example on paper once; in the exam, trust the script.
3. **AHC linkages vs dendrogram scale** (Q4, −6.4). Key lesson from June: *check every linkage against the actual merge heights* — topology alone is not "corresponds to". Single/complete/average update rules (Lance-Williams), and which need cluster sizes.
4. **EM-GMM theory** (Q7, −5): hard partition = argmax posterior (posteriors suffice); parameter counting; which quantities the M-step estimates and their exact formulas (watch numerator/denominator swaps).
5. **Apriori theory** (Q5/Q8, −5): anti-monotonicity direction (frequent ⇒ subsets frequent; NEVER the converse), candidate generation = join of frequent (k−1)-itemsets *then* prune, rule support = supp(X∪Y) (count vs fraction — read the question's σ convention), confidence monotonicity when moving items antecedent→consequent.
6. **Distance measures** (Q3, −2.5): Mahalanobis = Euclidean iff Σ = I; positive-definiteness of covariance matrices; SMC vs Jaccard (what gets discarded and when they coincide); cosine ignores 0-0 matches.
7. Low priority (already solid): k-Means mechanics, DBSCAN definitions (keep the "counts itself" convention in mind), basic dendrogram cutting.

## 3. Dry run

Before the re-exam: re-take `failed_first_exam.pdf` cold with the new tools under time pressure, target ≥ 80 with zero guessed answers. Then do the same with `old_cheatsheets/Sample MCQ Questions` and the 250/500 MCQ banks for the theory-only subs, blanking anything not certain, and check the calibration: every answered sub should be right.
