# DM583 re-exam toolkit

Everything from `PLAN.md` §1, importable from one REPL session. Managed with [uv](https://docs.astral.sh/uv/).

## Setup (once)

```
uv sync
```

## Exam warm-up (rehearse this, ~2 minutes)

```
uv run python
>>> from exam import *
>>> res = analyze("A 5 2 / B 1 7 / C 3 3 / D 4 4", metric="man", k=2, db=(3, 2))
>>> check_order("C,D,A", res["lof"])
```

`analyze` prints the full distance matrix, kNN outlier scores (dist-to-kth +
weighted), the complete LOF table (k-dist, tie-inclusive neighbourhood,
reach-dists, lrd, LOF) and DBSCAN core/border/noise per (ε, MinPts).
`check_order` answers "is this subset correctly ordered?" directly.

## Tool map (plan section → call)

| Question type | Call |
|---|---|
| §1.1 kernel density | `discrete_kernel(data, x, h)` — window, points inside, fraction |
| §1.1 kNN density | `knn_density(data, x, k)` — r, tie-adjusted k, fraction |
| §1.2 geometric (Q2/Q6) | `res = analyze("A 5 2 / ...", metric, k=, db=(eps, minpts))` |
| §1.2 order check | `check_order("C,D,E", res["lof"])` |
| §1.3 Apriori levels | `apriori(parse_db("A,B / B,C / ..."), min_sup)` — join → prune (missing subset named) → counts; `apriori_full(...)` adds maximal/closed/rules |
| §1.3 prune check | `prunable(("A","B","C"), [("A","B"), ("A","C")])` |
| §1.3 one rule | `rule(db, "A", "BC")` — support count, rel. support, confidence fraction, lift |
| §1.4 AHC linkages | `ahc_all(proxmat(pts, d))` — all four merge sequences + scipy cross-check |
| §1.4 dendrogram match | `match_dendrogram(D, [2, 6, 8, 10])` — scale + topology verdict per linkage |
| §1.5 GMM M-step | `mstep1d(xs, gammas)` — Σγ, prior, μ, σ² with explicit numerators/denominators |
| §1.5 parameter count | `param_count(k, d)` |
| §1.6 simplified silhouette | `simp_silhouette(data, labels)` — per-point a, b, s |
| MLE Gaussian | `mle(data)` — /n not /(n−1), shown |
| E-step / posteriors | `responsibilities(densities, priors)`, `estep(...)`, `mstep(...)` |
| Distances etc. | `eucd, mand, supd, mink, cosine, smc, jaccard, mahalanobis, proxmat, zscore, ...` |
| k-Means / DBSCAN | `kmeans(data, init)`, `sse(...)`, `dbscan(data, eps, minpts)`, `silhouette(...)` |

Apriori from a CSV (like `data/transactions.csv`): `uv run apriori-csv`.

## Checks

```
uv run pytest
```

Conventions baked in (June's traps): kernel window is **inclusive**; kNN density
tie-adjusts k and uses V = 2r with n = full dataset size; DBSCAN core points
**count themselves**; LOF neighbourhoods include ties at the k-distance;
"corresponds to X-linkage" requires **heights**, not just topology; MLE variance
divides by n.
