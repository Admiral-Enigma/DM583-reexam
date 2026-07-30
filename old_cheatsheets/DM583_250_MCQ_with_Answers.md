# DM583 Data Mining — 250 Multiple-Choice Questions (with answers)

Single-best-answer questions grounded in the lecture slides. Every option is marked **True/False** with a reason; the answer line names the Python toolkit function that computes it (`dist.py`, `cluster.py`, `outliers.py`, `gmm.py`, `freq.py`, `prob.py`) or gives a short justification.

**250 questions.** Topics: Data Representation (52), Partitioning (k-Means) (40), Density-Based (27), Frequent Itemsets (27), Hierarchical (25), Probability & Density (25), EM / GMM (23), Outlier Detection (22), Introduction (9).

---

### Q1 · Density-Based

Run DBSCAN with ε = 2 and MinPts = 3 on the points [[1, 3], [0, 5], [9, 0], [6, 8], [8, 8], [3, 4], [7, 6]]. What is the type of point index 4 = [8, 8]?

- **A)** Cluster centroid — ❌ **False.** DBSCAN has no centroids; points are core/border/noise.
- **B)** Border — ❌ **False.** it is not a border point (< MinPts within ε, but within ε of a core point).
- **C)** Core — ❌ **False.** it is not a core point (≥ MinPts neighbours within ε, incl. itself).
- **D)** Noise — ✅ **True.** it is a noise point (neither core nor within ε of a core point).

**Answer: D.** Use dbscan(data, eps, minpts) → (labels, types).

---

### Q2 · Hierarchical

Which linkage is the 'hierarchical counterpart of k-means' (minimises SSE increase per merge)?

- **A)** Single-linkage — ❌ **False.** MIN linkage, not variance-based.
- **B)** Complete-linkage — ❌ **False.** MAX linkage.
- **C)** Average-linkage — ❌ **False.** UPGMA averages distances.
- **D)** Ward's method — ✅ **True.** Ward merges to minimise the rise in within-cluster variance.

**Answer: D.** Use ahc(D, 'ward').

---

### Q3 · Probability & Density

For the sample [4, 1, 7, 6, 5, 9], what is the **sample variance** (dividing by n−1)?

- **A)** 6.222 — ❌ **False.** this is the population/MLE variance (÷ n).
- **B)** 7.467 — ✅ **True.** this is the sample variance (÷ n−1).
- **C)** 5.333 — ❌ **False.** this is the mean, not a variance.
- **D)** 2.733 — ❌ **False.** this is the standard deviation (√variance).

**Answer: B.** Use var(v) (sample=True); the MLE variance is var(v, sample=False).

---

### Q4 · Frequent Itemsets

For the database below, what is the **confidence of {BUTTER} ⇒ {BREAD}**?

| TID | Items |
| --- | --- |
| 1 | BREAD, BUTTER, DIAPERS, MILK |
| 2 | BREAD, BUTTER, DIAPERS, MILK |
| 3 | DIAPERS, MILK |
| 4 | BUTTER, DIAPERS, MILK |
| 5 | BREAD, BUTTER, DIAPERS, MILK |
| 6 | BUTTER, DIAPERS |
| 7 | BREAD, DIAPERS |
| 8 | BREAD, MILK |
| 9 | BREAD, DIAPERS, MILK |
| 10 | BREAD, BUTTER, DIAPERS, MILK |
| 11 | BREAD, BUTTER, DIAPERS, MILK |
| 12 | BREAD, BUTTER, DIAPERS |

- **A)** 1.0 — ❌ **False.** this is the lift, a different metric.
- **B)** 0.5 — ❌ **False.** this is the rule's support/frequency support(A∪B)/|D|.
- **C)** 0.75 — ✅ **True.** this is confidence = support(A∪B)/support(A).
- **D)** 0.667 — ❌ **False.** this is support(A∪B)/support(B) — wrong denominator.

**Answer: C.** Use confidence(DB, {'BUTTER'}, {'BREAD'}).

---

### Q5 · Hierarchical

For the distance matrix below, what is the **root (final) merge height under Single-Linkage**?

```
[0, 5, 12, 12]
[5, 0, 6, 4]
[12, 6, 0, 11]
[12, 4, 11, 0]
```

- **A)** 9.67 — ❌ **False.** this is the average-linkage root height.
- **B)** 6 — ✅ **True.** this is the single-linkage root height.
- **C)** 12 — ❌ **False.** this is the complete-linkage root height.
- **D)** 7 — ❌ **False.** this is an off value (recompute).

**Answer: B.** Use ahc(D, 'single'); the last merge's height is the root.

---

### Q6 · Probability & Density

A test has sensitivity 0.95, specificity 0.9; prevalence P(D)=0.02. What is **P(D | positive)**?

- **A)** 0.02 — ❌ **False.** this is the prior prevalence P(D), not the posterior.
- **B)** 0.838 — ❌ **False.** this is the complement 1−P(D|+).
- **C)** 0.162 — ✅ **True.** this is the posterior P(D|+) by Bayes' rule.
- **D)** 0.95 — ❌ **False.** this is the sensitivity P(+|D) (likelihood), not the posterior.

**Answer: C.** Use bayes(likelihood, prior, evidence) with evidence = sens·prev + (1−spec)·(1−prev).

---

### Q7 · Partitioning (k-Means)

Run k-means on [[2, 0], [2, 1], [3, 1], [1, 1], [9, 11], [10, 10], [10, 8], [9, 10]] with initial prototypes [[2, 0], [10, 10]]. What is the **final SSE**?

- **A)** 8.5 — ✅ **True.** this is the converged SSE.
- **B)** 17.0 — ❌ **False.** not the converged SSE.
- **C)** 10.5 — ❌ **False.** not the converged SSE.
- **D)** 3.5 — ❌ **False.** not the converged SSE.

**Answer: A.** Use kmeans(data, init) then sse(data, labels, cents).

---

### Q8 · Density-Based

Run DBSCAN with ε = 2 and MinPts = 3 on [[3, 3], [2, 5], [6, 2], [4, 4], [11, 6], [3, 2], [9, 1], [8, 4]]. **How many clusters** result (noise excluded)?

- **A)** 8 — ❌ **False.** DBSCAN does not form 8 clusters here.
- **B)** 0 — ❌ **False.** DBSCAN does not form 0 clusters here.
- **C)** 2 — ❌ **False.** DBSCAN does not form 2 clusters here.
- **D)** 1 — ✅ **True.** DBSCAN forms 1 cluster(s) (5 noise point(s)).

**Answer: D.** Use dbscan(data, eps, minpts); count distinct non-zero labels.

---

### Q9 · Introduction

'Valid' in the KDD definition means the discovered patterns are:

- **A)** Novel to the user — ❌ **False.** That is 'novel', a separate criterion.
- **B)** Immediately understandable — ❌ **False.** That is 'understandable'.
- **C)** Applicable to new data with some degree of reliability — ✅ **True.** Validity is about generalising beyond the sample.
- **D)** Stored in a database — ❌ **False.** Unrelated to validity.

**Answer: C.** Short justification: valid = generalises to new data.

---

### Q10 · Introduction

Supervised learning is characterised by:

- **A)** Having no target variable — ❌ **False.** That is unsupervised.
- **B)** Maximising support — ❌ **False.** That is association mining.
- **C)** Using only a distance matrix — ❌ **False.** That is relational/unsupervised.
- **D)** Learning a mapping from inputs X to a known target Y using (X,Y) examples — ✅ **True.** A 'teacher' (the labels Y) guides training.

**Answer: D.** Short justification: supervised needs labelled (X,Y).

---

### Q11 · Data Representation

For u = [-3, -1, 0] and v = [1, 3, -1], which value is the **Manhattan** distance d(u,v)?

- **A)** 5.05 — ❌ **False.** this is the Minkowski p=3 distance, mink(u,v,3).
- **B)** 5.74 — ❌ **False.** this is the Euclidean distance, eucd(u,v).
- **C)** 9 — ✅ **True.** this is the Manhattan distance, mand(u,v).
- **D)** 4 — ❌ **False.** this is the Suprema/Chebyshev distance, supd(u,v).

**Answer: C.** Use mand(u,v).

---

### Q12 · Data Representation

For u = [2, 5, 2, 1, 1] and v = [2, 1, 2, 2, 3], which value is the **cosine similarity** cos(u,v)?

- **A)** -0.861 — ❌ **False.** this is the Pearson correlation, a different measure.
- **B)** 18.0 — ❌ **False.** this is just the inner product <u,v> (not normalised).
- **C)** 0.023 — ❌ **False.** this is the inner product over ||u||²·||v||² (missing the square root).
- **D)** 0.649 — ✅ **True.** this is the cosine similarity.

**Answer: D.** Use cosine(u,v) = <u,v> / (||u||·||v||).

---

### Q13 · Outlier Detection

For the points [[6, 5], [3, 4], [5, 1], [4, 4], [5, 2], [6, 1], [16, 15]], which has the **highest unweighted KNN outlier score with k=1**?

- **A)** point 1 = [3, 4] — ❌ **False.** its score 1.0 is not the largest.
- **B)** point 4 = [5, 2] — ❌ **False.** its score 1.0 is not the largest.
- **C)** point 0 = [6, 5] — ❌ **False.** its score 2.24 is not the largest.
- **D)** point 6 = [16, 15] — ✅ **True.** largest k=1 NN distance (14.14).

**Answer: D.** Use knn_outlier(data, k) (score = distance to the k-th NN).

---

### Q14 · Data Representation

Which operations are meaningful for an ORDINAL variable (and only these)?

- **A)** = and ≠ only — ❌ **False.** That is nominal.
- **B)** Only arithmetic operations — ❌ **False.** Equality/order also apply, and arithmetic needs numeric.
- **C)** = , ≠ , < , > , ≤ , ≥ — ✅ **True.** Ordinal adds order comparisons to equality.
- **D)** = , ≠ , + , − , × , ÷ — ❌ **False.** Arithmetic needs numerical variables.

**Answer: C.** Short justification: nominal:=,≠ · ordinal:+order · numeric:+arithmetic.

---

### Q15 · Data Representation

For u = [-2, 4, 5] and v = [5, 0, 6], which value is the **Manhattan** distance d(u,v)?

- **A)** 12 — ✅ **True.** this is the Manhattan distance, mand(u,v).
- **B)** 7.42 — ❌ **False.** this is the Minkowski p=3 distance, mink(u,v,3).
- **C)** 7 — ❌ **False.** this is the Suprema/Chebyshev distance, supd(u,v).
- **D)** 8.12 — ❌ **False.** this is the Euclidean distance, eucd(u,v).

**Answer: A.** Use mand(u,v).

---

### Q16 · Density-Based

Run DBSCAN with ε = 3 and MinPts = 3 on the points [[0, 4], [1, 9], [8, 4], [7, 5], [1, 5], [5, 9], [8, 8]]. What is the type of point index 0 = [0, 4]?

- **A)** Core — ❌ **False.** it is not a core point (≥ MinPts neighbours within ε, incl. itself).
- **B)** Border — ❌ **False.** it is not a border point (< MinPts within ε, but within ε of a core point).
- **C)** Noise — ✅ **True.** it is a noise point (neither core nor within ε of a core point).
- **D)** Cluster centroid — ❌ **False.** DBSCAN has no centroids; points are core/border/noise.

**Answer: C.** Use dbscan(data, eps, minpts) → (labels, types).

---

### Q17 · Partitioning (k-Means)

Run k-means on [[1, 0], [2, 0], [1, 0], [10, 8], [10, 8], [10, 10]] with initial prototypes [[1, 0], [10, 8]]. What are the **final cluster labels** (in order)?

- **A)** [0, 0, 0, 1, 1, 1] — ✅ **True.** this is the converged k-means assignment.
- **B)** [0, 1, 0, 1, 0, 1] — ❌ **False.** this is an alternating labelling (not distance-based).
- **C)** [1, 1, 1, 0, 0, 0] — ❌ **False.** this is the same split with labels swapped (not what these inits give).
- **D)** [0, 0, 0, 0, 0, 0] — ❌ **False.** this is everything in one cluster (not a 2-means result).

**Answer: A.** Use kmeans(data, init) → (labels, cents).

---

### Q18 · Frequent Itemsets

For the database below, what is the **lift of {DIAPERS} ⇒ {BUTTER}**?

| TID | Items |
| --- | --- |
| 1 | BUTTER, DIAPERS, EGGS |
| 2 | BUTTER, DIAPERS |
| 3 | BREAD, BUTTER, DIAPERS |
| 4 | BUTTER, EGGS |
| 5 | BREAD, DIAPERS |
| 6 | BREAD, BUTTER, DIAPERS |
| 7 | BUTTER, EGGS |
| 8 | DIAPERS, EGGS |
| 9 | BREAD, DIAPERS, EGGS |
| 10 | BUTTER, DIAPERS |
| 11 | BUTTER, DIAPERS, EGGS |
| 12 | BUTTER, DIAPERS, EGGS |

- **A)** 0.75 — ❌ **False.** this is the frequency f(B) of the consequent.
- **B)** 0.933 — ✅ **True.** this is the lift = conf(A⇒B)/f(B).
- **C)** 0.7 — ❌ **False.** this is the confidence (forgot to divide by f(B)).
- **D)** 0.583 — ❌ **False.** this is the rule support/frequency support(A∪B)/|D|.

**Answer: B.** Use lift(DB, {'DIAPERS'}, {'BUTTER'}) = confidence / f(consequent).

---

### Q19 · Partitioning (k-Means)

Run k-means on [[1, 1], [2, 2], [1, 1], [3, 1], [10, 8], [8, 9], [9, 9], [11, 10]] (init [[1, 1], [8, 9]]), then compute the **Silhouette Width Criterion (SWC)**. Which value is correct?

- **A)** 1.783 — ❌ **False.** this is impossible — the SWC lies in [−1, +1].
- **B)** 0.844 — ✅ **True.** this is the SWC of this partition.
- **C)** 1 — ❌ **False.** this is a slightly off value (recompute).
- **D)** 0.744 — ❌ **False.** this is a slightly off value (recompute).

**Answer: B.** Use silhouette(data, labels); SWC ∈ [−1, +1].

---

### Q20 · Data Representation

A variable is ASYMMETRIC when:

- **A)** It is always continuous — ❌ **False.** Asymmetry concerns which values are informative, not type.
- **B)** It has exactly two categories — ❌ **False.** That is a binary variable, not asymmetric.
- **C)** Its distribution is skewed — ❌ **False.** Skew is unrelated to symmetric/asymmetric encoding.
- **D)** Only certain (typically non-zero) values are informative — ✅ **True.** E.g. presence (1) of a word/item matters; absence (0) does not. Relates to sparse data.

**Answer: D.** Short justification: asymmetric → only non-zero values count (sparse data).

---

### Q21 · Outlier Detection

The Local Outlier Factor (LOF) is fundamentally a:

- **A)** Relative/local density score comparing a point's density to its neighbours' — ✅ **True.** This detects outliers even across clusters of different density.
- **B)** Supervised classifier — ❌ **False.** LOF is unsupervised.
- **C)** Global density score vs the dataset mean — ❌ **False.** LOF is local, not global.
- **D)** Distance to the global centroid — ❌ **False.** Not how LOF works.

**Answer: A.** Use lof(data, k).

---

### Q22 · Probability & Density

The sum (marginalisation) rule states:

- **A)** p(X) = p(X)·p(Y) — ❌ **False.** That is independence, not the sum rule.
- **B)** p(X) = Σ_Y p(X,Y) — ✅ **True.** Marginal of X by summing the joint over Y.
- **C)** p(X) = p(X|Y)/p(Y) — ❌ **False.** Not a valid identity.
- **D)** p(X) = p(Y|X) p(X) — ❌ **False.** That is the product rule for the joint.

**Answer: B.** Use marginal(joint, axis).

---

### Q23 · Partitioning (k-Means)

SSE alone cannot pick the best k across solutions with different k because:

- **A)** SSE ignores the centroids — ❌ **False.** SSE is computed from centroids.
- **B)** SSE is undefined for k>2 — ❌ **False.** SSE is defined for any k.
- **C)** SSE only works for hierarchical methods — ❌ **False.** SSE is the k-means objective.
- **D)** SSE decreases monotonically as k increases (→ 0 at k=N) — ✅ **True.** Hence elbow/silhouette heuristics are used.

**Answer: D.** Short justification: minimise SSE for FIXED k; across k use silhouette/elbow.

---

### Q24 · Data Representation

For u = [2, 2, 4, 0] and v = [6, 5, 1, 2], which value is the **Manhattan** distance d(u,v)?

- **A)** 4 — ❌ **False.** this is the Suprema/Chebyshev distance, supd(u,v).
- **B)** 6.16 — ❌ **False.** this is the Euclidean distance, eucd(u,v).
- **C)** 5.01 — ❌ **False.** this is the Minkowski p=3 distance, mink(u,v,3).
- **D)** 12 — ✅ **True.** this is the Manhattan distance, mand(u,v).

**Answer: D.** Use mand(u,v).

---

### Q25 · Hierarchical

For the distance matrix below, what is the **root (final) merge height under Complete-Linkage**?

```
[0, 4, 8, 5]
[4, 0, 2, 7]
[8, 2, 0, 12]
[5, 7, 12, 0]
```

- **A)** 7.75 — ❌ **False.** this is the average-linkage root height.
- **B)** 12 — ✅ **True.** this is the complete-linkage root height.
- **C)** 5 — ❌ **False.** this is the single-linkage root height.
- **D)** 13 — ❌ **False.** this is an off value (recompute).

**Answer: B.** Use ahc(D, 'complete'); the last merge's height is the root.

---

### Q26 · EM / GMM

The EM E-step computes γ_ij, which is:

- **A)** The mixing weight π_i — ❌ **False.** M-step quantity (π_i = N_i/N).
- **B)** The new cluster mean — ❌ **False.** That is computed in the M-step.
- **C)** The covariance matrix — ❌ **False.** M-step quantity.
- **D)** The posterior probability that point x_j was generated by component i (Bayes' rule) — ✅ **True.** γ_ij = π_i N(x_j|v_i,Σ_i) / Σ_l π_l N(x_j|v_l,Σ_l).

**Answer: D.** Use responsibilities(densities, priors) or estep(...).

---

### Q27 · Data Representation

A dissimilarity is a METRIC if, in addition to non-negativity, identity and symmetry, it satisfies:

- **A)** The triangle inequality d(x,z) ≤ d(x,y)+d(y,z) — ✅ **True.** The triangle inequality is the extra metric axiom.
- **B)** Cosine equal to 1 — ❌ **False.** Unrelated to metric axioms.
- **C)** Zero correlation — ❌ **False.** Correlation is not a metric axiom.
- **D)** Boundedness by 1 — ❌ **False.** Metrics need not be bounded.

**Answer: A.** Short justification: metric = distance + triangle inequality.

---

### Q28 · Data Representation

For u = [5, 3, 4, 5] and v = [1, 3, 5, 2], which value is the **cosine similarity** cos(u,v)?

- **A)** 0.814 — ✅ **True.** this is the cosine similarity.
- **B)** 44.0 — ❌ **False.** this is just the inner product <u,v> (not normalised).
- **C)** 0.015 — ❌ **False.** this is the inner product over ||u||²·||v||² (missing the square root).
- **D)** -0.561 — ❌ **False.** this is the Pearson correlation, a different measure.

**Answer: A.** Use cosine(u,v) = <u,v> / (||u||·||v||).

---

### Q29 · EM / GMM

A Gaussian Mixture Model represents the density as:

- **A)** A uniform distribution — ❌ **False.** Not a GMM.
- **B)** A single Gaussian — ❌ **False.** A mixture has multiple components.
- **C)** A histogram — ❌ **False.** That is non-parametric, not a GMM.
- **D)** Σ_i π_i N(x | v_i, Σ_i) — a weighted sum of k Gaussians — ✅ **True.** π_i are mixing priors, v_i means, Σ_i covariances.

**Answer: D.** Use mvgauss(x, mean, cov) per component; gauss(x,mu,var) in 1-D.

---

### Q30 · Data Representation

For u = [4, -3, 5, 3] and v = [-4, -4, 6, -4], which value is the **Manhattan** distance d(u,v)?

- **A)** 17 — ✅ **True.** this is the Manhattan distance, mand(u,v).
- **B)** 10.72 — ❌ **False.** this is the Euclidean distance, eucd(u,v).
- **C)** 8 — ❌ **False.** this is the Suprema/Chebyshev distance, supd(u,v).
- **D)** 9.5 — ❌ **False.** this is the Minkowski p=3 distance, mink(u,v,3).

**Answer: A.** Use mand(u,v).

---

### Q31 · Partitioning (k-Means)

The hard partition matrix U(X) of k-means satisfies:

- **A)** All entries equal to 1 — ❌ **False.** Each point belongs to one cluster only.
- **B)** β_ij ∈ [0,1] summing to 1 per column — ❌ **False.** That is a fuzzy/probabilistic partition.
- **C)** Rows summing to 1 — ❌ **False.** Columns (objects), not rows, sum to 1.
- **D)** β_ij ∈ {0,1} and each column sums to 1 (each point in exactly one cluster) — ✅ **True.** Hard, non-overlapping assignment.

**Answer: D.** Short justification: hard partition → 0/1 columns summing to 1.

---

### Q32 · Outlier Detection

For the points [[0, 6], [4, 5], [0, 1], [2, 6], [3, 5], [5, 2], [15, 13]], which has the **highest unweighted KNN outlier score with k=2**?

- **A)** point 3 = [2, 6] — ❌ **False.** its score 2.0 is not the largest.
- **B)** point 6 = [15, 13] — ✅ **True.** largest k=2 NN distance (14.42).
- **C)** point 4 = [3, 5] — ❌ **False.** its score 1.41 is not the largest.
- **D)** point 0 = [0, 6] — ❌ **False.** its score 3.16 is not the largest.

**Answer: B.** Use knn_outlier(data, k) (score = distance to the k-th NN).

---

### Q33 · Hierarchical

For the distance matrix below, what is the **root (final) merge height under Single-Linkage**?

```
[0, 11, 6, 12]
[11, 0, 9, 11]
[6, 9, 0, 1]
[12, 11, 1, 0]
```

- **A)** 10 — ❌ **False.** this is an off value (recompute).
- **B)** 12 — ❌ **False.** this is the complete-linkage root height.
- **C)** 9 — ✅ **True.** this is the single-linkage root height.
- **D)** 10.33 — ❌ **False.** this is the average-linkage root height.

**Answer: C.** Use ahc(D, 'single'); the last merge's height is the root.

---

### Q34 · Partitioning (k-Means)

Run k-means on [[3, 3], [3, 2], [2, 0], [10, 9], [9, 8], [8, 9]] with initial prototypes [[3, 3], [10, 9]]. What are the **final cluster labels** (in order)?

- **A)** [1, 1, 1, 0, 0, 0] — ❌ **False.** this is the same split with labels swapped (not what these inits give).
- **B)** [0, 1, 0, 1, 0, 1] — ❌ **False.** this is an alternating labelling (not distance-based).
- **C)** [0, 0, 0, 1, 1, 1] — ✅ **True.** this is the converged k-means assignment.
- **D)** [0, 0, 0, 0, 0, 0] — ❌ **False.** this is everything in one cluster (not a 2-means result).

**Answer: C.** Use kmeans(data, init) → (labels, cents).

---

### Q35 · Data Representation

For binary x1 = [1, 0, 1, 0, 0, 1, 1, 1, 1, 0] and x2 = [1, 0, 0, 1, 0, 1, 0, 0, 0, 1], which value is the **SMC** coefficient?

- **A)** 0.25 — ❌ **False.** this is the Jaccard = n11/(n11+n10+n01).
- **B)** 0.2 — ❌ **False.** this is only n11/n (it omits the other agreements/structure).
- **C)** 0.4 — ✅ **True.** this is the SMC = (n11+n00)/n.
- **D)** 0.6 — ❌ **False.** this is the fraction of disagreements (n10+n01)/n.

**Answer: C.** Use 0.4; contingency(x1,x2)=(n11,n10,n01,n00)=(2,4,2,2).

---

### Q36 · Probability & Density

The log-likelihood is maximised instead of the likelihood because:

- **A)** It changes the optimal θ — ❌ **False.** The optimum is unchanged.
- **B)** It makes the function non-differentiable — ❌ **False.** It remains differentiable.
- **C)** log is monotonic (same optimum) and turns the product over points into a sum — ✅ **True.** Numerically easier and more stable.
- **D)** It removes the need for data — ❌ **False.** Data is still required.

**Answer: C.** Short justification: monotone log → same argmax, easier sums.

---

### Q37 · Introduction

Regression differs from classification in that its dependent variable Y is:

- **A)** Real-valued (numeric, continuous) — ✅ **True.** Regression models a continuous Y = f(X)+ε.
- **B)** Always binary — ❌ **False.** Binary targets are a classification special case.
- **C)** A finite set of nominal class labels — ❌ **False.** That describes classification.
- **D)** Absent (there is no Y) — ❌ **False.** Both regression and classification have a target Y.

**Answer: A.** Short justification: regression → continuous Y, classification → categorical Y.

---

### Q38 · EM / GMM

What is the value of the 1-D Normal density N(x=8 | μ=8, σ²=2)?

- **A)** 1.0 — ❌ **False.** this is only the exponential term, missing the 1/√(2πσ²) normaliser.
- **B)** 0.1995 — ❌ **False.** this is using σ (std) where σ² (variance) was required.
- **C)** 0.1411 — ❌ **False.** this is half the correct density (arithmetic slip).
- **D)** 0.2821 — ✅ **True.** this is the Normal pdf N(x|μ,σ²).

**Answer: D.** Use gauss(x, mu, var) (variance, not std).

---

### Q39 · Density-Based

Run DBSCAN with ε = 3 and MinPts = 2 on [[0, 7], [6, 9], [3, 10], [8, 8], [4, 4], [0, 9], [3, 4], [0, 8]]. **How many clusters** result (noise excluded)?

- **A)** 2 — ❌ **False.** DBSCAN does not form 2 clusters here.
- **B)** 3 — ✅ **True.** DBSCAN forms 3 cluster(s) (1 noise point(s)).
- **C)** 4 — ❌ **False.** DBSCAN does not form 4 clusters here.
- **D)** 8 — ❌ **False.** DBSCAN does not form 8 clusters here.

**Answer: B.** Use dbscan(data, eps, minpts); count distinct non-zero labels.

---

### Q40 · Partitioning (k-Means)

The objective minimised by k-means is the:

- **A)** Sum of Squared Errors (within-cluster variance), SSE — ✅ **True.** SSE = Σ_c Σ_{x∈Cc} ‖x − x̄c‖².
- **B)** Between-cluster distance only — ❌ **False.** k-means minimises within-cluster SSE.
- **C)** Number of clusters k — ❌ **False.** k is an input, not minimised.
- **D)** Silhouette width — ❌ **False.** That is a validation index, not the k-means objective.

**Answer: A.** Use sse(data, labels, cents).

---

### Q41 · Hierarchical

For the distance matrix below, what is the **root (final) merge height under Complete-Linkage**?

```
[0, 8, 9, 5, 1]
[8, 0, 8, 5, 8]
[9, 8, 0, 2, 2]
[5, 5, 2, 0, 1]
[1, 8, 2, 1, 0]
```

- **A)** 9 — ✅ **True.** this is the complete-linkage root height.
- **B)** 7.25 — ❌ **False.** this is the average-linkage root height.
- **C)** 5 — ❌ **False.** this is the single-linkage root height.
- **D)** 11 — ❌ **False.** this is an off value (recompute).

**Answer: A.** Use ahc(D, 'complete'); the last merge's height is the root.

---

### Q42 · Data Representation

One-hot (1-of-n) encoding of a nominal variable is preferred over mapping categories to 1,2,3 because:

- **A)** One-hot is required for ordinal data — ❌ **False.** Ordinal uses order-preserving numeric encoding.
- **B)** Integer codes preserve order best — ❌ **False.** There is no real order to preserve in nominal data.
- **C)** Integer codes invent a fake order and unequal distances between categories — ✅ **True.** One-hot keeps categories equidistant (each value → its own binary).
- **D)** One-hot uses fewer variables — ❌ **False.** It uses more (one per value).

**Answer: C.** Use onehot(cats, levels); ordinal uses ordinal(cats, order).

---

### Q43 · EM / GMM

In the M-step, the updated mean v_i is:

- **A)** Unchanged from the previous step — ❌ **False.** Means are updated each M-step.
- **B)** The densest point — ❌ **False.** Not how EM updates means.
- **C)** A responsibility-weighted average (1/N_i) Σ_j γ_ij x_j — ✅ **True.** Σ_i is the γ-weighted covariance; π_i = N_i/N.
- **D)** The medoid of the cluster — ❌ **False.** GMM uses weighted means.

**Answer: C.** Use mstep(data, gamma).

---

### Q44 · Outlier Detection

For the points [[4, 2], [1, 6], [6, 5], [5, 3], [6, 2], [5, 0], [17, 15]], which has the **highest unweighted KNN outlier score with k=1**?

- **A)** point 4 = [6, 2] — ❌ **False.** its score 1.41 is not the largest.
- **B)** point 2 = [6, 5] — ❌ **False.** its score 2.24 is not the largest.
- **C)** point 5 = [5, 0] — ❌ **False.** its score 2.24 is not the largest.
- **D)** point 6 = [17, 15] — ✅ **True.** largest k=1 NN distance (14.87).

**Answer: D.** Use knn_outlier(data, k) (score = distance to the k-th NN).

---

### Q45 · Outlier Detection

For the points [[4, 0], [3, 4], [4, 1], [1, 3], [0, 1], [2, 6], [13, 17]], which has the **highest unweighted KNN outlier score with k=2**?

- **A)** point 6 = [13, 17] — ✅ **True.** largest k=2 NN distance (16.4).
- **B)** point 3 = [1, 3] — ❌ **False.** its score 2.24 is not the largest.
- **C)** point 1 = [3, 4] — ❌ **False.** its score 2.24 is not the largest.
- **D)** point 0 = [4, 0] — ❌ **False.** its score 4.12 is not the largest.

**Answer: A.** Use knn_outlier(data, k) (score = distance to the k-th NN).

---

### Q46 · Hierarchical

Given the distance matrix (0-based indices), which pair merges **first** under Single-Linkage?

```
[0, 12, 2, 8, 3]
[12, 0, 12, 12, 6]
[2, 12, 0, 2, 5]
[8, 12, 2, 0, 9]
[3, 6, 5, 9, 0]
```

- **A)** objects 1 and 3 (d=12) — ❌ **False.** their distance 12 is not the minimum.
- **B)** objects 2 and 3 (d=2) — ❌ **False.** their distance 2 is not the minimum.
- **C)** objects 0 and 3 (d=8) — ❌ **False.** their distance 8 is not the minimum.
- **D)** objects 0 and 2 (d=2) — ✅ **True.** this is the smallest distance, so they merge first.

**Answer: D.** Use ahc(D,'single'); the closest pair always merges first.

---

### Q47 · Partitioning (k-Means)

Run k-means on [[2, 1], [3, 2], [3, 0], [8, 10], [9, 9], [11, 11]] with initial prototypes [[2, 1], [8, 10]]. What are the **final cluster labels** (in order)?

- **A)** [0, 0, 0, 1, 1, 1] — ✅ **True.** this is the converged k-means assignment.
- **B)** [1, 1, 1, 0, 0, 0] — ❌ **False.** this is the same split with labels swapped (not what these inits give).
- **C)** [0, 1, 0, 1, 0, 1] — ❌ **False.** this is an alternating labelling (not distance-based).
- **D)** [0, 0, 0, 0, 0, 0] — ❌ **False.** this is everything in one cluster (not a 2-means result).

**Answer: A.** Use kmeans(data, init) → (labels, cents).

---

### Q48 · Outlier Detection

For the points [[5, 0], [4, 6], [0, 6], [2, 1], [4, 5], [1, 5], [15, 17]], which has the **highest unweighted KNN outlier score with k=2**?

- **A)** point 2 = [0, 6] — ❌ **False.** its score 4.0 is not the largest.
- **B)** point 4 = [4, 5] — ❌ **False.** its score 3.0 is not the largest.
- **C)** point 3 = [2, 1] — ❌ **False.** its score 4.12 is not the largest.
- **D)** point 6 = [15, 17] — ✅ **True.** largest k=2 NN distance (16.28).

**Answer: D.** Use knn_outlier(data, k) (score = distance to the k-th NN).

---

### Q49 · Data Representation

For binary x1 = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0] and x2 = [0, 1, 0, 0, 0, 0, 1, 1, 1, 0], which value is the **SMC** coefficient?

- **A)** 0.3 — ✅ **True.** this is the SMC = (n11+n00)/n.
- **B)** 0.125 — ❌ **False.** this is the Jaccard = n11/(n11+n10+n01).
- **C)** 0.1 — ❌ **False.** this is only n11/n (it omits the other agreements/structure).
- **D)** 0.7 — ❌ **False.** this is the fraction of disagreements (n10+n01)/n.

**Answer: A.** Use 0.3; contingency(x1,x2)=(n11,n10,n01,n00)=(1,4,3,2).

---

### Q50 · Data Representation

The Suprema (Chebyshev) distance is the Minkowski distance with:

- **A)** p → ∞ — ✅ **True.** As p→∞ the Minkowski limit is max_k|x_k−y_k|.
- **B)** p = 2 — ❌ **False.** p=2 gives Euclidean.
- **C)** p = 1 — ❌ **False.** p=1 gives Manhattan.
- **D)** p = 0 — ❌ **False.** Not a valid Minkowski order here.

**Answer: A.** Use supd(u,v); Manhattan=mink(...,1)=mand, Euclidean=mink(...,2)=eucd.

---

### Q51 · Data Representation

For u = [7, -4, 8, 3] and v = [6, -1, -1, 1], which value is the **Manhattan** distance d(u,v)?

- **A)** 9.15 — ❌ **False.** this is the Minkowski p=3 distance, mink(u,v,3).
- **B)** 9 — ❌ **False.** this is the Suprema/Chebyshev distance, supd(u,v).
- **C)** 15 — ✅ **True.** this is the Manhattan distance, mand(u,v).
- **D)** 9.75 — ❌ **False.** this is the Euclidean distance, eucd(u,v).

**Answer: C.** Use mand(u,v).

---

### Q52 · Hierarchical

Average-linkage (UPGMA) is usually described as:

- **A)** The most sensitive to noise — ❌ **False.** That is single-linkage.
- **B)** Able to follow arbitrary shapes best — ❌ **False.** That is single-linkage.
- **C)** Identical to Ward's method — ❌ **False.** They differ; Ward uses variance.
- **D)** A good practical compromise — fairly robust to noise, but biased to globular clusters — ✅ **True.** It sits between single and complete linkage.

**Answer: D.** Use ahc(D,'average').

---

### Q53 · Frequent Itemsets

The SUPPORT of an itemset X is:

- **A)** The number of items in X — ❌ **False.** That is its length.
- **B)** The number of transactions that contain X (size of its cover) — ✅ **True.** Frequency = support/|D|; X is frequent if support ≥ σ.
- **C)** The fraction of items it covers — ❌ **False.** Support counts transactions, not items.
- **D)** Its confidence times its lift — ❌ **False.** That is not support.

**Answer: B.** Use support(DB, X).

---

### Q54 · Probability & Density

A property required of a probability DENSITY function but NOT of a PMF is:

- **A)** Values sum/integrate to 1 — ❌ **False.** Required of both.
- **B)** Domain is the variable's states — ❌ **False.** Required of both.
- **C)** p(x) ≥ 0 — ❌ **False.** Required of both.
- **D)** p(x) may exceed 1 (it is a density, not a probability) — ✅ **True.** Only ∫p dx = 1 is required; probability = area under the curve.

**Answer: D.** Short justification: pdf can exceed 1; only its integral is 1.

---

### Q55 · Partitioning (k-Means)

Run k-means on [[2, 3], [1, 3], [1, 2], [0, 2], [8, 11], [8, 10], [11, 11], [8, 11]] with initial prototypes [[2, 3], [8, 10]]. What is the **final SSE**?

- **A)** 10.5 — ✅ **True.** this is the converged SSE.
- **B)** 13.5 — ❌ **False.** not the converged SSE.
- **C)** 21.0 — ❌ **False.** not the converged SSE.
- **D)** 7.5 — ❌ **False.** not the converged SSE.

**Answer: A.** Use kmeans(data, init) then sse(data, labels, cents).

---

### Q56 · Partitioning (k-Means)

Run k-means on [[3, 0], [1, 2], [1, 0], [2, 1], [10, 11], [10, 9], [8, 8], [8, 8]] with initial prototypes [[3, 0], [10, 9]]. What is the **final SSE**?

- **A)** 18.5 — ❌ **False.** not the converged SSE.
- **B)** 31.0 — ❌ **False.** not the converged SSE.
- **C)** 15.5 — ✅ **True.** this is the converged SSE.
- **D)** 10.5 — ❌ **False.** not the converged SSE.

**Answer: C.** Use kmeans(data, init) then sse(data, labels, cents).

---

### Q57 · Partitioning (k-Means)

In the silhouette s(i) = (b−a)/max(a,b), the terms a and b are:

- **A)** a = number of clusters; b = points — ❌ **False.** Those are counts, not distances.
- **B)** a = SSE; b = between-cluster variance — ❌ **False.** Not the silhouette definition.
- **C)** a = global mean distance; b = k — ❌ **False.** Incorrect definitions.
- **D)** a = avg distance to OWN cluster; b = avg distance to the NEAREST other cluster — ✅ **True.** Near +1 = well clustered; near −1 = likely misassigned.

**Answer: D.** Use silhouette(data, labels); range is [−1,+1].

---

### Q58 · EM / GMM

If both component covariance matrices are DIAGONAL, the clusters are:

- **A)** Axis-aligned ellipsoids (spherical only if the diagonal entries are equal) — ✅ **True.** Diagonal ≠ spherical in general.
- **B)** Always identical to k-means clusters — ❌ **False.** Only under equal spherical covariances.
- **C)** Necessarily a single point — ❌ **False.** Covariance describes spread, not a point.
- **D)** Necessarily spherical — ❌ **False.** Only when all variances are equal.

**Answer: A.** Short justification: diagonal Σ → axis-aligned ellipses.

---

### Q59 · Density-Based

Run DBSCAN with ε = 3 and MinPts = 2 on the points [[9, 9], [7, 6], [8, 5], [2, 2], [8, 7], [0, 8], [1, 5]]. What is the type of point index 6 = [1, 5]?

- **A)** Core — ❌ **False.** it is not a core point (≥ MinPts neighbours within ε, incl. itself).
- **B)** Border — ❌ **False.** it is not a border point (< MinPts within ε, but within ε of a core point).
- **C)** Cluster centroid — ❌ **False.** DBSCAN has no centroids; points are core/border/noise.
- **D)** Noise — ✅ **True.** it is a noise point (neither core nor within ε of a core point).

**Answer: D.** Use dbscan(data, eps, minpts) → (labels, types).

---

### Q60 · Frequent Itemsets

A CLOSED frequent itemset is one that:

- **A)** Has no frequent superset — ❌ **False.** That defines a MAXIMAL itemset.
- **B)** Has support below the threshold — ❌ **False.** Then it would not be frequent.
- **C)** Has no superset with the SAME support — ✅ **True.** Closed sets compress the frequent set without losing support info.
- **D)** Contains all items — ❌ **False.** Unrelated to closedness.

**Answer: C.** Use is_closed(DB, X).

---

### Q61 · Frequent Itemsets

For the database below, what is the **lift of {MILK} ⇒ {BUTTER}**?

| TID | Items |
| --- | --- |
| 1 | BREAD, BUTTER, DIAPERS |
| 2 | BUTTER, DIAPERS, MILK |
| 3 | BREAD, BUTTER, DIAPERS |
| 4 | BREAD, BUTTER, DIAPERS |
| 5 | BREAD, BUTTER, DIAPERS, MILK |
| 6 | BUTTER, DIAPERS |
| 7 | BREAD, BUTTER, MILK |
| 8 | BREAD, BUTTER |
| 9 | BREAD, MILK |
| 10 | BREAD, BUTTER |
| 11 | BREAD, BUTTER, DIAPERS, MILK |
| 12 | BREAD, BUTTER, DIAPERS, MILK |

- **A)** 0.909 — ✅ **True.** this is the lift = conf(A⇒B)/f(B).
- **B)** 0.417 — ❌ **False.** this is the rule support/frequency support(A∪B)/|D|.
- **C)** 0.833 — ❌ **False.** this is the confidence (forgot to divide by f(B)).
- **D)** 0.917 — ❌ **False.** this is the frequency f(B) of the consequent.

**Answer: A.** Use lift(DB, {'MILK'}, {'BUTTER'}) = confidence / f(consequent).

---

### Q62 · EM / GMM

In an EM-GMM (k=2), the densities at x are 0.0051 and 0.0169 with priors π_C1=0.6, π_C2=0.4. What is the **posterior probability of C1** at x?

- **A)** 0.232 — ❌ **False.** this is the densities normalised WITHOUT the priors.
- **B)** 0.312 — ✅ **True.** this is the posterior (responsibility) of C1 via Bayes.
- **C)** 0.6 — ❌ **False.** this is the PRIOR π_C1, not the posterior.
- **D)** 0.688 — ❌ **False.** this is the posterior of C2, not C1.

**Answer: B.** Use posteriors([d1,d2],[π1,π2]) (E-step, Bayes' rule).

---

### Q63 · Density-Based

Run DBSCAN with ε = 2 and MinPts = 3 on [[5, 11], [8, 10], [9, 5], [3, 4], [6, 8], [3, 7], [4, 9], [9, 1]]. **How many clusters** result (noise excluded)?

- **A)** 2 — ❌ **False.** DBSCAN does not form 2 clusters here.
- **B)** 8 — ❌ **False.** DBSCAN does not form 8 clusters here.
- **C)** 0 — ✅ **True.** DBSCAN forms 0 cluster(s) (8 noise point(s)).
- **D)** 1 — ❌ **False.** DBSCAN does not form 1 clusters here.

**Answer: C.** Use dbscan(data, eps, minpts); count distinct non-zero labels.

---

### Q64 · Data Representation

For u = [-3, 3, -1] and v = [1, 0, -2], which value is the **Manhattan** distance d(u,v)?

- **A)** 4.51 — ❌ **False.** this is the Minkowski p=3 distance, mink(u,v,3).
- **B)** 5.1 — ❌ **False.** this is the Euclidean distance, eucd(u,v).
- **C)** 8 — ✅ **True.** this is the Manhattan distance, mand(u,v).
- **D)** 4 — ❌ **False.** this is the Suprema/Chebyshev distance, supd(u,v).

**Answer: C.** Use mand(u,v).

---

### Q65 · EM / GMM

Inverting each component covariance matrix Σ_i in EM-GMM costs about:

- **A)** O(N) in the number of points — ❌ **False.** Inversion scales with dimensions, not points.
- **B)** O(n) — ❌ **False.** Too low for inversion.
- **C)** O(2^n) — ❌ **False.** Not exponential.
- **D)** O(n³) in the number of dimensions n — ✅ **True.** Matrix inversion is cubic in dimensionality.

**Answer: D.** Short justification: Σ⁻¹ is O(n³); parameters grow with n².

---

### Q66 · Probability & Density

The expectation E[X] of a discrete random variable is:

- **A)** Σ_x P(x) — ❌ **False.** That sums to 1, it is not the mean.
- **B)** Σ_x x · P(x) — ✅ **True.** Probability-weighted average of values.
- **C)** the middle value — ❌ **False.** That is the median.
- **D)** the most frequent value — ❌ **False.** That is the mode.

**Answer: B.** Use expect(vals, probs); for data use mean(v).

---

### Q67 · Data Representation

For u = [6, 7, 5, 5] and v = [0, 5, 5, -1], which value is the **Euclidean** distance d(u,v)?

- **A)** 14 — ❌ **False.** this is the Manhattan distance, mand(u,v).
- **B)** 8.72 — ✅ **True.** this is the Euclidean distance, eucd(u,v).
- **C)** 7.61 — ❌ **False.** this is the Minkowski p=3 distance, mink(u,v,3).
- **D)** 6 — ❌ **False.** this is the Suprema/Chebyshev distance, supd(u,v).

**Answer: B.** Use eucd(u,v).

---

### Q68 · Data Representation

For u = [8, 8, 3] and v = [3, 1, -2], which value is the **Euclidean** distance d(u,v)?

- **A)** 9.95 — ✅ **True.** this is the Euclidean distance, eucd(u,v).
- **B)** 17 — ❌ **False.** this is the Manhattan distance, mand(u,v).
- **C)** 8.4 — ❌ **False.** this is the Minkowski p=3 distance, mink(u,v,3).
- **D)** 7 — ❌ **False.** this is the Suprema/Chebyshev distance, supd(u,v).

**Answer: A.** Use eucd(u,v).

---

### Q69 · Partitioning (k-Means)

Run k-means on [[0, 0], [2, 3], [2, 2], [3, 3], [10, 10], [8, 9], [9, 11], [10, 8]] (init [[0, 0], [8, 9]]), then compute the **Silhouette Width Criterion (SWC)**. Which value is correct?

- **A)** 0.986 — ❌ **False.** this is a slightly off value (recompute).
- **B)** 0.786 — ✅ **True.** this is the SWC of this partition.
- **C)** 1.699 — ❌ **False.** this is impossible — the SWC lies in [−1, +1].
- **D)** 0.586 — ❌ **False.** this is a slightly off value (recompute).

**Answer: B.** Use silhouette(data, labels); SWC ∈ [−1, +1].

---

### Q70 · Data Representation

For binary x1 = [1, 1, 0, 0, 1, 0, 1, 0] and x2 = [0, 0, 0, 1, 0, 0, 1, 1], which value is the **SMC** coefficient?

- **A)** 0.167 — ❌ **False.** this is the Jaccard = n11/(n11+n10+n01).
- **B)** 0.375 — ✅ **True.** this is the SMC = (n11+n00)/n.
- **C)** 0.625 — ❌ **False.** this is the fraction of disagreements (n10+n01)/n.
- **D)** 0.125 — ❌ **False.** this is only n11/n (it omits the other agreements/structure).

**Answer: B.** Use 0.375; contingency(x1,x2)=(n11,n10,n01,n00)=(1,3,2,2).

---

### Q71 · Hierarchical

A key drawback of agglomerative hierarchical clustering is that it is:

- **A)** Only applicable to categorical data — ❌ **False.** It works on numeric/relational data.
- **B)** Always requiring k in advance — ❌ **False.** k can be chosen a posteriori by cutting.
- **C)** Greedy — an early merge cannot be undone, so optimality is not guaranteed — ✅ **True.** Merges are irreversible.
- **D)** Unable to produce a dendrogram — ❌ **False.** It does produce a dendrogram.

**Answer: C.** Short justification: greedy, irreversible merges.

---

### Q72 · Data Representation

For u = [7, 7, 1, 8] and v = [3, 1, 6, -4], which value is the **Euclidean** distance d(u,v)?

- **A)** 12 — ❌ **False.** this is the Suprema/Chebyshev distance, supd(u,v).
- **B)** 12.87 — ❌ **False.** this is the Minkowski p=3 distance, mink(u,v,3).
- **C)** 14.87 — ✅ **True.** this is the Euclidean distance, eucd(u,v).
- **D)** 27 — ❌ **False.** this is the Manhattan distance, mand(u,v).

**Answer: C.** Use eucd(u,v).

---

### Q73 · Frequent Itemsets

An association rule X ⇒ Y expresses:

- **A)** A proven causal link — ❌ **False.** Rules describe co-occurrence, not cause.
- **B)** A co-occurrence (implication), not causality, with X ∩ Y = ∅ — ✅ **True.** Antecedent and consequent are disjoint itemsets.
- **C)** A clustering of transactions — ❌ **False.** Unrelated to clustering.
- **D)** A distance between items — ❌ **False.** No distance is involved.

**Answer: B.** Short justification: co-occurrence, disjoint antecedent/consequent.

---

### Q74 · Data Representation

For binary x1 = [1, 1, 1, 1, 0, 0, 0, 1] and x2 = [0, 0, 0, 0, 1, 0, 1, 1], which value is the **Jaccard** coefficient?

- **A)** 0.75 — ❌ **False.** this is the fraction of disagreements (n10+n01)/n.
- **B)** 0.125 — ❌ **False.** this is only n11/n (it omits the other agreements/structure).
- **C)** 0.143 — ✅ **True.** this is the Jaccard = n11/(n11+n10+n01).
- **D)** 0.25 — ❌ **False.** this is the SMC = (n11+n00)/n.

**Answer: C.** Use 0.143; contingency(x1,x2)=(n11,n10,n01,n00)=(1,4,2,1).

---

### Q75 · Outlier Detection

For the points [[0, 6], [4, 1], [1, 0], [1, 3], [6, 3], [6, 5], [16, 14]], which has the **highest unweighted KNN outlier score with k=1**?

- **A)** point 6 = [16, 14] — ✅ **True.** largest k=1 NN distance (13.45).
- **B)** point 3 = [1, 3] — ❌ **False.** its score 3.0 is not the largest.
- **C)** point 2 = [1, 0] — ❌ **False.** its score 3.0 is not the largest.
- **D)** point 5 = [6, 5] — ❌ **False.** its score 2.0 is not the largest.

**Answer: A.** Use knn_outlier(data, k) (score = distance to the k-th NN).

---

### Q76 · Density-Based

Run DBSCAN with ε = 2 and MinPts = 2 on the points [[0, 7], [4, 0], [4, 8], [4, 1], [5, 2], [5, 0], [4, 2]]. What is the type of point index 5 = [5, 0]?

- **A)** Core — ✅ **True.** it is a core point (≥ MinPts neighbours within ε, incl. itself).
- **B)** Border — ❌ **False.** it is not a border point (< MinPts within ε, but within ε of a core point).
- **C)** Noise — ❌ **False.** it is not a noise point (neither core nor within ε of a core point).
- **D)** Cluster centroid — ❌ **False.** DBSCAN has no centroids; points are core/border/noise.

**Answer: A.** Use dbscan(data, eps, minpts) → (labels, types).

---

### Q77 · Outlier Detection

For the points [[1, 1], [0, 3], [2, 0], [6, 1], [4, 3], [0, 0], [17, 17]], which has the **highest unweighted KNN outlier score with k=1**?

- **A)** point 4 = [4, 3] — ❌ **False.** its score 2.83 is not the largest.
- **B)** point 6 = [17, 17] — ✅ **True.** largest k=1 NN distance (19.1).
- **C)** point 0 = [1, 1] — ❌ **False.** its score 1.41 is not the largest.
- **D)** point 1 = [0, 3] — ❌ **False.** its score 2.24 is not the largest.

**Answer: B.** Use knn_outlier(data, k) (score = distance to the k-th NN).

---

### Q78 · Partitioning (k-Means)

Run k-means on [[1, 0], [3, 1], [1, 2], [10, 11], [8, 10], [9, 10]] with initial prototypes [[1, 0], [10, 11]]. What are the **final cluster labels** (in order)?

- **A)** [0, 0, 0, 0, 0, 0] — ❌ **False.** this is everything in one cluster (not a 2-means result).
- **B)** [1, 1, 1, 0, 0, 0] — ❌ **False.** this is the same split with labels swapped (not what these inits give).
- **C)** [0, 1, 0, 1, 0, 1] — ❌ **False.** this is an alternating labelling (not distance-based).
- **D)** [0, 0, 0, 1, 1, 1] — ✅ **True.** this is the converged k-means assignment.

**Answer: D.** Use kmeans(data, init) → (labels, cents).

---

### Q79 · Frequent Itemsets

For the database below, what is the **support count of {MILK, BUTTER}**?

| TID | Items |
| --- | --- |
| 1 | BEER, BUTTER, DIAPERS, MILK |
| 2 | BREAD, DIAPERS, EGGS, MILK |
| 3 | BEER, BREAD, DIAPERS, EGGS |
| 4 | BREAD, EGGS, MILK |
| 5 | BEER, BREAD, DIAPERS |
| 6 | BEER, BREAD, DIAPERS, MILK |
| 7 | BEER, BREAD, BUTTER, EGGS, MILK |
| 8 | BEER, BREAD, BUTTER |
| 9 | BREAD, BUTTER, DIAPERS, EGGS, MILK |
| 10 | BEER, BUTTER, DIAPERS, EGGS |

- **A)** 5 — ❌ **False.** this is the support of {BUTTER} alone.
- **B)** 3 — ✅ **True.** this is the support of {MILK, BUTTER}.
- **C)** 7 — ❌ **False.** this is the number of transactions NOT containing both.
- **D)** 6 — ❌ **False.** this is the support of {MILK} alone.

**Answer: B.** Use support(DB, {'MILK','BUTTER'}).

---

### Q80 · Hierarchical

For the distance matrix below, what is the **root (final) merge height under Complete-Linkage**?

```
[0, 8, 11, 10, 1]
[8, 0, 2, 9, 9]
[11, 2, 0, 6, 4]
[10, 9, 6, 0, 1]
[1, 9, 4, 1, 0]
```

- **A)** 4 — ❌ **False.** this is the single-linkage root height.
- **B)** 11 — ✅ **True.** this is the complete-linkage root height.
- **C)** 7.83 — ❌ **False.** this is the average-linkage root height.
- **D)** 13 — ❌ **False.** this is an off value (recompute).

**Answer: B.** Use ahc(D, 'complete'); the last merge's height is the root.

---

### Q81 · EM / GMM

Compared with k-means, a genuine ADVANTAGE of EM-GMM is that it:

- **A)** Can model elongated/ellipsoidal clusters and gives posterior probabilities — ✅ **True.** Full covariances + soft memberships carry more information.
- **B)** Needs no number of clusters — ❌ **False.** EM-GMM still needs k.
- **C)** Is immune to local optima — ❌ **False.** It is subject to local optima.
- **D)** Works on nominal data — ❌ **False.** It needs real-valued data.

**Answer: A.** Short justification: ellipsoidal clusters + probabilistic memberships.

---

### Q82 · EM / GMM

What is the value of the 1-D Normal density N(x=4 | μ=6, σ²=4)?

- **A)** 0.088 — ❌ **False.** this is using σ (std) where σ² (variance) was required.
- **B)** 0.0605 — ❌ **False.** this is half the correct density (arithmetic slip).
- **C)** 0.6065 — ❌ **False.** this is only the exponential term, missing the 1/√(2πσ²) normaliser.
- **D)** 0.121 — ✅ **True.** this is the Normal pdf N(x|μ,σ²).

**Answer: D.** Use gauss(x, mu, var) (variance, not std).

---

### Q83 · Data Representation

For binary x1 = [0, 1, 0, 0, 1, 1, 1, 1] and x2 = [0, 0, 1, 0, 0, 0, 0, 1], which value is the **Jaccard** coefficient?

- **A)** 0.167 — ✅ **True.** this is the Jaccard = n11/(n11+n10+n01).
- **B)** 0.375 — ❌ **False.** this is the SMC = (n11+n00)/n.
- **C)** 0.125 — ❌ **False.** this is only n11/n (it omits the other agreements/structure).
- **D)** 0.625 — ❌ **False.** this is the fraction of disagreements (n10+n01)/n.

**Answer: A.** Use 0.167; contingency(x1,x2)=(n11,n10,n01,n00)=(1,4,1,2).

---

### Q84 · Probability & Density

Bayes' theorem can be written as:

- **A)** p(Y|X) = p(X) p(Y) — ❌ **False.** That is independence.
- **B)** p(Y|X) = p(X|Y) + p(Y) — ❌ **False.** Probabilities are multiplied, not added.
- **C)** p(Y|X) = p(X|Y) p(Y) / p(X) — ✅ **True.** posterior = likelihood × prior / evidence.
- **D)** p(Y|X) = p(X|Y) — ❌ **False.** Ignores prior and evidence.

**Answer: C.** Use bayes(likelihood, prior, evidence).

---

### Q85 · Data Representation

Spearman correlation is more robust to outliers than Pearson because it:

- **A)** Adds the covariance to the mean — ❌ **False.** Not how Spearman works.
- **B)** Uses squared values — ❌ **False.** That amplifies outliers.
- **C)** Replaces values by their ranks before computing the correlation — ✅ **True.** Ranking caps the influence of extreme values.
- **D)** Ignores one variable — ❌ **False.** Both variables are used.

**Answer: C.** Use spearman(u,v); Pearson is pearson(u,v).

---

### Q86 · Data Representation

Converting a distance d∈[0,1] to a similarity is done by:

- **A)** s = d² — ❌ **False.** Distorts and does not invert order to a similarity.
- **B)** s = 1 − d — ✅ **True.** Linear flip preserving [0,1] without distortion.
- **C)** s = 1/d — ❌ **False.** Undefined at d=0 and not in [0,1].
- **D)** s = log d — ❌ **False.** Negative/undefined for d≤0.

**Answer: B.** Use sim2dis/dis2sim; for unbounded d use 1/(1+d) or e^(−d).

---

### Q87 · Partitioning (k-Means)

Run k-means on [[2, 0], [1, 1], [3, 1], [3, 0], [8, 11], [9, 8], [11, 11], [11, 8]] (init [[2, 0], [9, 8]]), then compute the **Silhouette Width Criterion (SWC)**. Which value is correct?

- **A)** 1.75 — ❌ **False.** this is impossible — the SWC lies in [−1, +1].
- **B)** 1 — ❌ **False.** this is a slightly off value (recompute).
- **C)** 0.801 — ✅ **True.** this is the SWC of this partition.
- **D)** 0.601 — ❌ **False.** this is a slightly off value (recompute).

**Answer: C.** Use silhouette(data, labels); SWC ∈ [−1, +1].

---

### Q88 · Frequent Itemsets

The anti-monotonicity (downward-closure) property states:

- **A)** Support increases with itemset size — ❌ **False.** Support cannot increase when items are added.
- **B)** Every superset of a frequent itemset is frequent — ❌ **False.** False direction.
- **C)** Confidence is monotone in itemset size — ❌ **False.** Confidence is not monotone.
- **D)** Every subset of a frequent itemset is also frequent — ✅ **True.** Equivalently, any superset of an infrequent set is infrequent — used for pruning.

**Answer: D.** Short justification: Apriori prunes candidates with an infrequent subset.

---

### Q89 · Hierarchical

Cutting a dendrogram horizontally yields:

- **A)** A flat partition whose #clusters equals the number of crossed links — ✅ **True.** Different cut heights give different granularities.
- **B)** The covariance matrix — ❌ **False.** Unrelated.
- **C)** A single cluster always — ❌ **False.** Only at the very top.
- **D)** The SSE of k-means — ❌ **False.** Unrelated.

**Answer: A.** Use cut(merges, n, k).

---

### Q90 · Outlier Detection

The reachability distance used by LOF is:

- **A)** min{k-distance(o), d(p,o)} — ❌ **False.** It is the MAX, not the min.
- **B)** k-distance(o) only — ❌ **False.** That ignores the actual distance.
- **C)** reach_dist_k(p,o) = max{k-distance(o), d(p,o)} — ✅ **True.** The max smooths density fluctuations within a cluster.
- **D)** d(p,o) only — ❌ **False.** That ignores the smoothing term.

**Answer: C.** Use reachdist(data, p, o, k).

---

### Q91 · Partitioning (k-Means)

Run k-means on [[1, 3], [1, 1], [3, 1], [1, 1], [8, 9], [10, 11], [10, 9], [10, 8]] with initial prototypes [[1, 3], [10, 11]]. What is the **final SSE**?

- **A)** 13.75 — ✅ **True.** this is the converged SSE.
- **B)** 15.75 — ❌ **False.** not the converged SSE.
- **C)** 27.5 — ❌ **False.** not the converged SSE.
- **D)** 8.75 — ❌ **False.** not the converged SSE.

**Answer: A.** Use kmeans(data, init) then sse(data, labels, cents).

---

### Q92 · Frequent Itemsets

With n distinct items, the candidate itemset search space has size:

- **A)** n² — ❌ **False.** Counts pairs only.
- **B)** 2^n — ✅ **True.** Each item is in or out → exponential, hence pruning is essential.
- **C)** n! — ❌ **False.** Permutations are irrelevant to sets.
- **D)** n — ❌ **False.** Only counts single items.

**Answer: B.** Short justification: 2^n possible itemsets.

---

### Q93 · Density-Based

Run DBSCAN with ε = 2 and MinPts = 2 on the points [[2, 7], [8, 9], [0, 0], [5, 6], [9, 8], [7, 9], [9, 2]]. What is the type of point index 4 = [9, 8]?

- **A)** Noise — ❌ **False.** it is not a noise point (neither core nor within ε of a core point).
- **B)** Cluster centroid — ❌ **False.** DBSCAN has no centroids; points are core/border/noise.
- **C)** Core — ✅ **True.** it is a core point (≥ MinPts neighbours within ε, incl. itself).
- **D)** Border — ❌ **False.** it is not a border point (< MinPts within ε, but within ε of a core point).

**Answer: C.** Use dbscan(data, eps, minpts) → (labels, types).

---

### Q94 · Outlier Detection

For the points [[0, 6], [5, 0], [6, 0], [1, 1], [1, 6], [1, 4], [16, 15]], which has the **highest unweighted KNN outlier score with k=2**?

- **A)** point 3 = [1, 1] — ❌ **False.** its score 4.12 is not the largest.
- **B)** point 6 = [16, 15] — ✅ **True.** largest k=2 NN distance (18.03).
- **C)** point 2 = [6, 0] — ❌ **False.** its score 5.1 is not the largest.
- **D)** point 4 = [1, 6] — ❌ **False.** its score 2.0 is not the largest.

**Answer: B.** Use knn_outlier(data, k) (score = distance to the k-th NN).

---

### Q95 · Partitioning (k-Means)

Run k-means on [[1, 1], [1, 0], [2, 3], [2, 1], [10, 9], [11, 8], [10, 11], [11, 9]] with initial prototypes [[1, 1], [11, 8]]. What is the **final SSE**?

- **A)** 8.5 — ❌ **False.** not the converged SSE.
- **B)** 23.0 — ❌ **False.** not the converged SSE.
- **C)** 11.5 — ✅ **True.** this is the converged SSE.
- **D)** 14.5 — ❌ **False.** not the converged SSE.

**Answer: C.** Use kmeans(data, init) then sse(data, labels, cents).

---

### Q96 · EM / GMM

What is the value of the 1-D Normal density N(x=2 | μ=2, σ²=2)?

- **A)** 1.0 — ❌ **False.** this is only the exponential term, missing the 1/√(2πσ²) normaliser.
- **B)** 0.1411 — ❌ **False.** this is half the correct density (arithmetic slip).
- **C)** 0.2821 — ✅ **True.** this is the Normal pdf N(x|μ,σ²).
- **D)** 0.1995 — ❌ **False.** this is using σ (std) where σ² (variance) was required.

**Answer: C.** Use gauss(x, mu, var) (variance, not std).

---

### Q97 · Density-Based

DBSCAN works well when it must:

- **A)** Find arbitrarily shaped clusters and resist noise — ✅ **True.** Density-connectivity captures non-convex shapes; noise is its own label.
- **B)** Find strictly spherical clusters — ❌ **False.** That is k-means' strength, not DBSCAN's selling point.
- **C)** Handle very high-dimensional data — ❌ **False.** DBSCAN struggles in high dimensions.
- **D)** Cope with widely varying densities — ❌ **False.** A single global ε fails here.

**Answer: A.** Short justification: arbitrary shapes + noise resistance.

---

### Q98 · Frequent Itemsets

For the database below, what is the **confidence of {EGGS} ⇒ {BUTTER}**?

| TID | Items |
| --- | --- |
| 1 | EGGS, MILK |
| 2 | BREAD, BUTTER, EGGS, MILK |
| 3 | BREAD, BUTTER, EGGS |
| 4 | BREAD, EGGS, MILK |
| 5 | BREAD, BUTTER, EGGS |
| 6 | BREAD, BUTTER, EGGS, MILK |
| 7 | BREAD, BUTTER, MILK |
| 8 | BREAD, BUTTER |
| 9 | BUTTER, EGGS |
| 10 | BREAD, EGGS |
| 11 | BREAD, BUTTER, EGGS, MILK |
| 12 | BUTTER, EGGS |

- **A)** 0.933 — ❌ **False.** this is the lift, a different metric.
- **B)** 0.7 — ✅ **True.** this is confidence = support(A∪B)/support(A).
- **C)** 0.583 — ❌ **False.** this is the rule's support/frequency support(A∪B)/|D|.
- **D)** 0.778 — ❌ **False.** this is support(A∪B)/support(B) — wrong denominator.

**Answer: B.** Use confidence(DB, {'EGGS'}, {'BUTTER'}).

---

### Q99 · Density-Based

Run DBSCAN with ε = 3 and MinPts = 3 on [[8, 5], [9, 4], [4, 0], [0, 2], [8, 6], [11, 6], [2, 7], [8, 9]]. **How many clusters** result (noise excluded)?

- **A)** 2 — ❌ **False.** DBSCAN does not form 2 clusters here.
- **B)** 8 — ❌ **False.** DBSCAN does not form 8 clusters here.
- **C)** 1 — ✅ **True.** DBSCAN forms 1 cluster(s) (3 noise point(s)).
- **D)** 0 — ❌ **False.** DBSCAN does not form 0 clusters here.

**Answer: C.** Use dbscan(data, eps, minpts); count distinct non-zero labels.

---

### Q100 · Density-Based

Run DBSCAN with ε = 3 and MinPts = 3 on the points [[2, 2], [5, 3], [7, 6], [5, 4], [7, 4], [1, 5], [0, 8]]. What is the type of point index 6 = [0, 8]?

- **A)** Border — ❌ **False.** it is not a border point (< MinPts within ε, but within ε of a core point).
- **B)** Noise — ✅ **True.** it is a noise point (neither core nor within ε of a core point).
- **C)** Cluster centroid — ❌ **False.** DBSCAN has no centroids; points are core/border/noise.
- **D)** Core — ❌ **False.** it is not a core point (≥ MinPts neighbours within ε, incl. itself).

**Answer: B.** Use dbscan(data, eps, minpts) → (labels, types).

---

### Q101 · Data Representation

For u = [1, 0, 4, 3, 4] and v = [1, 5, 5, 1, 0], which value is the **cosine similarity** cos(u,v)?

- **A)** 0.011 — ❌ **False.** this is the inner product over ||u||²·||v||² (missing the square root).
- **B)** 0.514 — ✅ **True.** this is the cosine similarity.
- **C)** -0.274 — ❌ **False.** this is the Pearson correlation, a different measure.
- **D)** 24.0 — ❌ **False.** this is just the inner product <u,v> (not normalised).

**Answer: B.** Use cosine(u,v) = <u,v> / (||u||·||v||).

---

### Q102 · Partitioning (k-Means)

Run k-means on [[3, 2], [1, 0], [3, 0], [2, 3], [11, 9], [10, 10], [11, 10], [10, 11]] with initial prototypes [[3, 2], [10, 10]]. What is the **final SSE**?

- **A)** 25.0 — ❌ **False.** not the converged SSE.
- **B)** 15.5 — ❌ **False.** not the converged SSE.
- **C)** 12.5 — ✅ **True.** this is the converged SSE.
- **D)** 7.5 — ❌ **False.** not the converged SSE.

**Answer: C.** Use kmeans(data, init) then sse(data, labels, cents).

---

### Q103 · EM / GMM

What is the value of the 1-D Normal density N(x=8 | μ=9, σ²=4)?

- **A)** 0.0967 — ❌ **False.** this is using σ (std) where σ² (variance) was required.
- **B)** 0.088 — ❌ **False.** this is half the correct density (arithmetic slip).
- **C)** 0.8825 — ❌ **False.** this is only the exponential term, missing the 1/√(2πσ²) normaliser.
- **D)** 0.176 — ✅ **True.** this is the Normal pdf N(x|μ,σ²).

**Answer: D.** Use gauss(x, mu, var) (variance, not std).

---

### Q104 · Partitioning (k-Means)

Run k-means on [[1, 2], [2, 2], [2, 0], [2, 3], [11, 8], [8, 9], [10, 9], [10, 9]] with initial prototypes [[1, 2], [8, 9]]. What is the **final SSE**?

- **A)** 14.0 — ❌ **False.** not the converged SSE.
- **B)** 22.0 — ❌ **False.** not the converged SSE.
- **C)** 6.0 — ❌ **False.** not the converged SSE.
- **D)** 11.0 — ✅ **True.** this is the converged SSE.

**Answer: D.** Use kmeans(data, init) then sse(data, labels, cents).

---

### Q105 · Partitioning (k-Means)

Run k-means on [[2, 0], [1, 3], [0, 3], [3, 3], [11, 10], [8, 10], [8, 11], [9, 11]] (init [[2, 0], [8, 10]]), then compute the **Silhouette Width Criterion (SWC)**. Which value is correct?

- **A)** 0.995 — ❌ **False.** this is a slightly off value (recompute).
- **B)** 0.595 — ❌ **False.** this is a slightly off value (recompute).
- **C)** 1.33 — ❌ **False.** this is impossible — the SWC lies in [−1, +1].
- **D)** 0.795 — ✅ **True.** this is the SWC of this partition.

**Answer: D.** Use silhouette(data, labels); SWC ∈ [−1, +1].

---

### Q106 · Probability & Density

For the sample [7, 4, 7, 2, 2, 5], what is the **sample variance** (dividing by n−1)?

- **A)** 2.258 — ❌ **False.** this is the standard deviation (√variance).
- **B)** 4.25 — ❌ **False.** this is the population/MLE variance (÷ n).
- **C)** 4.5 — ❌ **False.** this is the mean, not a variance.
- **D)** 5.1 — ✅ **True.** this is the sample variance (÷ n−1).

**Answer: D.** Use var(v) (sample=True); the MLE variance is var(v, sample=False).

---

### Q107 · Introduction

Which task is UNSUPERVISED?

- **A)** Classification — ❌ **False.** Classification uses labelled class targets Y — supervised.
- **B)** Clustering — ✅ **True.** Clustering learns groups from inputs X only, with no target variable.
- **C)** Credit-risk prediction from labelled history — ❌ **False.** Uses (X,Y) pairs — supervised.
- **D)** Regression — ❌ **False.** Regression predicts a numeric target Y — supervised.

**Answer: B.** Short justification: clustering/outlier detection/association rules are unsupervised.

---

### Q108 · Frequent Itemsets

For the database below, what is the **support count of {MILK, DIAPERS}**?

| TID | Items |
| --- | --- |
| 1 | BUTTER, MILK |
| 2 | DIAPERS, EGGS, MILK |
| 3 | BREAD, DIAPERS, EGGS |
| 4 | BREAD, BUTTER, DIAPERS, EGGS, MILK |
| 5 | DIAPERS, MILK |
| 6 | BREAD, DIAPERS, EGGS, MILK |
| 7 | DIAPERS, MILK |
| 8 | BREAD, BUTTER, DIAPERS, EGGS, MILK |
| 9 | BREAD, BUTTER, DIAPERS |
| 10 | BREAD, BUTTER, DIAPERS, EGGS, MILK |

- **A)** 7 — ✅ **True.** this is the support of {MILK, DIAPERS}.
- **B)** 3 — ❌ **False.** this is the number of transactions NOT containing both.
- **C)** 8 — ❌ **False.** this is the support of {MILK} alone.
- **D)** 9 — ❌ **False.** this is the support of {DIAPERS} alone.

**Answer: A.** Use support(DB, {'MILK','DIAPERS'}).

---

### Q109 · Outlier Detection

The weighted KNN outlier score differs from the plain kNN score by:

- **A)** Averaging the distances to all 1st…k-th neighbours instead of using only the k-th — ✅ **True.** Aggregation smooths the score.
- **B)** Using Pearson correlation — ❌ **False.** Unrelated.
- **C)** Using the cluster centroid — ❌ **False.** No centroid involved.
- **D)** Using the nearest neighbour only — ❌ **False.** That is k=1 plain kNN.

**Answer: A.** Use wknn_outlier(data, k) vs knn_outlier(data, k).

---

### Q110 · Data Representation

For u = [8, 1, 8, 8] and v = [-3, 5, 7, -1], which value is the **Euclidean** distance d(u,v)?

- **A)** 11 — ❌ **False.** this is the Suprema/Chebyshev distance, supd(u,v).
- **B)** 14.8 — ✅ **True.** this is the Euclidean distance, eucd(u,v).
- **C)** 12.86 — ❌ **False.** this is the Minkowski p=3 distance, mink(u,v,3).
- **D)** 25 — ❌ **False.** this is the Manhattan distance, mand(u,v).

**Answer: B.** Use eucd(u,v).

---

### Q111 · EM / GMM

In an EM-GMM (k=2), the densities at x are 0.0055 and 0.0195 with priors π_C1=0.2, π_C2=0.8. What is the **posterior probability of C1** at x?

- **A)** 0.22 — ❌ **False.** this is the densities normalised WITHOUT the priors.
- **B)** 0.2 — ❌ **False.** this is the PRIOR π_C1, not the posterior.
- **C)** 0.066 — ✅ **True.** this is the posterior (responsibility) of C1 via Bayes.
- **D)** 0.934 — ❌ **False.** this is the posterior of C2, not C1.

**Answer: C.** Use posteriors([d1,d2],[π1,π2]) (E-step, Bayes' rule).

---

### Q112 · Density-Based

HDBSCAN* improves on DBSCAN mainly by:

- **A)** Using squared Euclidean only — ❌ **False.** It works with general distances.
- **B)** Building a density hierarchy over all thresholds and extracting clusters of varying density — ✅ **True.** It yields all DBSCAN* solutions and cuts locally (FOSC).
- **C)** Requiring fewer transactions — ❌ **False.** Transactions are an association-rule concept.
- **D)** Being a supervised method — ❌ **False.** It is unsupervised.

**Answer: B.** Short justification: density hierarchy handles varying densities.

---

### Q113 · Partitioning (k-Means)

Running k-means multiple times for k in [k_min,k_max] and keeping the best-by-criterion result is:

- **A)** A hierarchical method — ❌ **False.** k-means is partitional.
- **B)** A procedure to estimate k while reducing the effect of local minima — ✅ **True.** Multiple restarts + model selection.
- **C)** Unable to change k — ❌ **False.** Its purpose is to compare different k.
- **D)** A way to guarantee the global optimum — ❌ **False.** It only reduces, not removes, local-minima risk.

**Answer: B.** Short justification: multi-run over k + criterion (e.g., silhouette).

---

### Q114 · Density-Based

DBSCAN* (used to define density-connected clusters) differs from DBSCAN by:

- **A)** Treating border points as noise — clusters are maximal sets of density-connected CORE points — ✅ **True.** Borders can be re-attached afterwards if desired.
- **B)** Producing overlapping clusters — ❌ **False.** Clusters remain disjoint.
- **C)** Requiring k in advance — ❌ **False.** It does not need k.
- **D)** Using medoids — ❌ **False.** No medoids involved.

**Answer: A.** Short justification: DBSCAN* drops border points (core-only clusters).

---

### Q115 · Frequent Itemsets

For the database below, what is the **lift of {MILK} ⇒ {BREAD}**?

| TID | Items |
| --- | --- |
| 1 | BUTTER, MILK |
| 2 | BUTTER, MILK |
| 3 | BREAD, MILK |
| 4 | BUTTER, MILK |
| 5 | BUTTER, MILK |
| 6 | BREAD, BUTTER, EGGS |
| 7 | BUTTER, EGGS, MILK |
| 8 | BREAD, BUTTER, EGGS, MILK |
| 9 | EGGS, MILK |
| 10 | BREAD, BUTTER, MILK |
| 11 | BREAD, BUTTER, EGGS, MILK |
| 12 | BREAD, BUTTER, EGGS, MILK |

- **A)** 0.417 — ❌ **False.** this is the rule support/frequency support(A∪B)/|D|.
- **B)** 0.455 — ❌ **False.** this is the confidence (forgot to divide by f(B)).
- **C)** 0.5 — ❌ **False.** this is the frequency f(B) of the consequent.
- **D)** 0.909 — ✅ **True.** this is the lift = conf(A⇒B)/f(B).

**Answer: D.** Use lift(DB, {'MILK'}, {'BREAD'}) = confidence / f(consequent).

---

### Q116 · Data Representation

The Mahalanobis distance generalises Euclidean distance by:

- **A)** Ignoring the data centre — ❌ **False.** It is measured from the centre/mean.
- **B)** Accounting for the covariance of variables (ellipsoidal equidistant sets) — ✅ **True.** It is Euclidean distance on a PCA-whitened space.
- **C)** Working only on binary data — ❌ **False.** It is for numeric multivariate data.
- **D)** Using absolute differences — ❌ **False.** That is Manhattan.

**Answer: B.** Use mahalanobis(x, mean, covmat(data)); square it for R's value.

---

### Q117 · Probability & Density

For the sample [7, 7, 3, 1, 8], what is the **sample variance** (dividing by n−1)?

- **A)** 7.36 — ❌ **False.** this is the population/MLE variance (÷ n).
- **B)** 3.033 — ❌ **False.** this is the standard deviation (√variance).
- **C)** 9.2 — ✅ **True.** this is the sample variance (÷ n−1).
- **D)** 5.2 — ❌ **False.** this is the mean, not a variance.

**Answer: C.** Use var(v) (sample=True); the MLE variance is var(v, sample=False).

---

### Q118 · Probability & Density

For the sample [6, 3, 6, 6, 9, 5], what is the **sample variance** (dividing by n−1)?

- **A)** 1.941 — ❌ **False.** this is the standard deviation (√variance).
- **B)** 3.767 — ✅ **True.** this is the sample variance (÷ n−1).
- **C)** 3.139 — ❌ **False.** this is the population/MLE variance (÷ n).
- **D)** 5.833 — ❌ **False.** this is the mean, not a variance.

**Answer: B.** Use var(v) (sample=True); the MLE variance is var(v, sample=False).

---

### Q119 · Frequent Itemsets

For the database below, what is the **lift of {MILK} ⇒ {BUTTER}**?

| TID | Items |
| --- | --- |
| 1 | BUTTER, DIAPERS, MILK |
| 2 | BUTTER, MILK |
| 3 | BUTTER, MILK |
| 4 | BREAD, BUTTER, MILK |
| 5 | BREAD, BUTTER, MILK |
| 6 | BREAD, DIAPERS, MILK |
| 7 | BREAD, MILK |
| 8 | BUTTER, MILK |
| 9 | BREAD, BUTTER, DIAPERS |
| 10 | DIAPERS, MILK |
| 11 | BUTTER, DIAPERS, MILK |
| 12 | BUTTER, MILK |

- **A)** 0.667 — ❌ **False.** this is the rule support/frequency support(A∪B)/|D|.
- **B)** 0.75 — ❌ **False.** this is the frequency f(B) of the consequent.
- **C)** 0.97 — ✅ **True.** this is the lift = conf(A⇒B)/f(B).
- **D)** 0.727 — ❌ **False.** this is the confidence (forgot to divide by f(B)).

**Answer: C.** Use lift(DB, {'MILK'}, {'BUTTER'}) = confidence / f(consequent).

---

### Q120 · Introduction

In the DM/ML distinction emphasised in the slides, the ML perspective on classification typically:

- **A)** Focuses mainly on predictive power/effectiveness (often black-box) — ✅ **True.** ML prioritises prediction; DM may also seek interpretability.
- **B)** Requires unsupervised data only — ❌ **False.** Classification is supervised.
- **C)** Ignores prediction entirely — ❌ **False.** Prediction is central to ML.
- **D)** Cannot use any training data — ❌ **False.** ML learns from training examples.

**Answer: A.** Short justification: ML → prediction focus; DM → also which/how predictors matter.

---

### Q121 · Hierarchical

Given the distance matrix (0-based indices), which pair merges **first** under Single-Linkage?

```
[0, 8, 7, 10, 6]
[8, 0, 12, 6, 2]
[7, 12, 0, 10, 10]
[10, 6, 10, 0, 3]
[6, 2, 10, 3, 0]
```

- **A)** objects 1 and 4 (d=2) — ✅ **True.** this is the smallest distance, so they merge first.
- **B)** objects 1 and 2 (d=12) — ❌ **False.** their distance 12 is not the minimum.
- **C)** objects 0 and 1 (d=8) — ❌ **False.** their distance 8 is not the minimum.
- **D)** objects 3 and 4 (d=3) — ❌ **False.** their distance 3 is not the minimum.

**Answer: A.** Use ahc(D,'single'); the closest pair always merges first.

---

### Q122 · Probability & Density

A test has sensitivity 0.99, specificity 0.9; prevalence P(D)=0.05. What is **P(D | positive)**?

- **A)** 0.657 — ❌ **False.** this is the complement 1−P(D|+).
- **B)** 0.99 — ❌ **False.** this is the sensitivity P(+|D) (likelihood), not the posterior.
- **C)** 0.05 — ❌ **False.** this is the prior prevalence P(D), not the posterior.
- **D)** 0.343 — ✅ **True.** this is the posterior P(D|+) by Bayes' rule.

**Answer: D.** Use bayes(likelihood, prior, evidence) with evidence = sens·prev + (1−spec)·(1−prev).

---

### Q123 · Partitioning (k-Means)

Run k-means on [[1, 2], [3, 0], [1, 0], [10, 8], [11, 9], [8, 8]] with initial prototypes [[1, 2], [10, 8]]. What are the **final cluster labels** (in order)?

- **A)** [0, 1, 0, 1, 0, 1] — ❌ **False.** this is an alternating labelling (not distance-based).
- **B)** [0, 0, 0, 0, 0, 0] — ❌ **False.** this is everything in one cluster (not a 2-means result).
- **C)** [1, 1, 1, 0, 0, 0] — ❌ **False.** this is the same split with labels swapped (not what these inits give).
- **D)** [0, 0, 0, 1, 1, 1] — ✅ **True.** this is the converged k-means assignment.

**Answer: D.** Use kmeans(data, init) → (labels, cents).

---

### Q124 · Probability & Density

X and Y are independent iff:

- **A)** Cov(X,Y) > 0 — ❌ **False.** Sign of covariance is not independence.
- **B)** p(X,Y) = p(X)·p(Y) for all values — ✅ **True.** Then also p(Y|X) = p(Y).
- **C)** E[X] = E[Y] — ❌ **False.** Equal means do not imply independence.
- **D)** p(X|Y) = p(Y|X) — ❌ **False.** Not the independence condition.

**Answer: B.** Short justification: independence factorises the joint.

---

### Q125 · Data Representation

For u = [1, 1, 3, 5] and v = [4, 0, 2, 1], which value is the **cosine similarity** cos(u,v)?

- **A)** 0.546 — ✅ **True.** this is the cosine similarity.
- **B)** 0.02 — ❌ **False.** this is the inner product over ||u||²·||v||² (missing the square root).
- **C)** 15.0 — ❌ **False.** this is just the inner product <u,v> (not normalised).
- **D)** -0.255 — ❌ **False.** this is the Pearson correlation, a different measure.

**Answer: A.** Use cosine(u,v) = <u,v> / (||u||·||v||).

---

### Q126 · Data Representation

For u = [-2, 2, 3] and v = [4, -4, 4], which value is the **Manhattan** distance d(u,v)?

- **A)** 13 — ✅ **True.** this is the Manhattan distance, mand(u,v).
- **B)** 6 — ❌ **False.** this is the Suprema/Chebyshev distance, supd(u,v).
- **C)** 7.57 — ❌ **False.** this is the Minkowski p=3 distance, mink(u,v,3).
- **D)** 8.54 — ❌ **False.** this is the Euclidean distance, eucd(u,v).

**Answer: A.** Use mand(u,v).

---

### Q127 · EM / GMM

In an EM-GMM (k=2), the densities at x are 0.0061 and 0.0164 with priors π_C1=0.7, π_C2=0.3. What is the **posterior probability of C1** at x?

- **A)** 0.271 — ❌ **False.** this is the densities normalised WITHOUT the priors.
- **B)** 0.7 — ❌ **False.** this is the PRIOR π_C1, not the posterior.
- **C)** 0.535 — ❌ **False.** this is the posterior of C2, not C1.
- **D)** 0.465 — ✅ **True.** this is the posterior (responsibility) of C1 via Bayes.

**Answer: D.** Use posteriors([d1,d2],[π1,π2]) (E-step, Bayes' rule).

---

### Q128 · Data Representation

For u = [4, 2, 5, 0, 4] and v = [5, 3, 3, 1, 4], which value is the **cosine similarity** cos(u,v)?

- **A)** 57.0 — ❌ **False.** this is just the inner product <u,v> (not normalised).
- **B)** 0.758 — ❌ **False.** this is the Pearson correlation, a different measure.
- **C)** 0.942 — ✅ **True.** this is the cosine similarity.
- **D)** 0.016 — ❌ **False.** this is the inner product over ||u||²·||v||² (missing the square root).

**Answer: C.** Use cosine(u,v) = <u,v> / (||u||·||v||).

---

### Q129 · EM / GMM

In an EM-GMM (k=2), the densities at x are 0.0094 and 0.0032 with priors π_C1=0.3, π_C2=0.7. What is the **posterior probability of C1** at x?

- **A)** 0.443 — ❌ **False.** this is the posterior of C2, not C1.
- **B)** 0.3 — ❌ **False.** this is the PRIOR π_C1, not the posterior.
- **C)** 0.557 — ✅ **True.** this is the posterior (responsibility) of C1 via Bayes.
- **D)** 0.746 — ❌ **False.** this is the densities normalised WITHOUT the priors.

**Answer: C.** Use posteriors([d1,d2],[π1,π2]) (E-step, Bayes' rule).

---

### Q130 · Hierarchical

Complete-linkage tends to:

- **A)** Minimise within-cluster variance by design — ❌ **False.** That is Ward's method.
- **B)** Resist noise but split large clusters and favour globular shapes — ✅ **True.** MAX linkage avoids chaining but can fragment elongated clusters.
- **C)** Follow elongated arbitrary shapes well — ❌ **False.** That is single-linkage's strength.
- **D)** Be the most sensitive to single noisy points — ❌ **False.** That is single-linkage.

**Answer: B.** Use ahc(D,'complete').

---

### Q131 · EM / GMM

What is the value of the 1-D Normal density N(x=9 | μ=7, σ²=2)?

- **A)** 0.1038 — ✅ **True.** this is the Normal pdf N(x|μ,σ²).
- **B)** 0.121 — ❌ **False.** this is using σ (std) where σ² (variance) was required.
- **C)** 0.3679 — ❌ **False.** this is only the exponential term, missing the 1/√(2πσ²) normaliser.
- **D)** 0.0519 — ❌ **False.** this is half the correct density (arithmetic slip).

**Answer: A.** Use gauss(x, mu, var) (variance, not std).

---

### Q132 · Partitioning (k-Means)

Which is NOT a limitation of standard k-means?

- **A)** Tends to find globular clusters only — ❌ **False.** True limitation.
- **B)** Mean-based, so sensitive to outliers — ❌ **False.** True limitation.
- **C)** Sensitive to initialisation — ❌ **False.** True limitation.
- **D)** It naturally handles nominal categorical data — ✅ **True.** k-means needs real-valued data (the mean must be defined).

**Answer: D.** Short justification: nominal data is the false claim — k-means needs numeric data.

---

### Q133 · Data Representation

Postal codes stored as numbers should be treated as:

- **A)** Ordinal — ❌ **False.** No inherent order of interest.
- **B)** Nominal (labels; arithmetic is meaningless) — ✅ **True.** Averaging/ordering postal codes is meaningless — they are identifiers.
- **C)** Discrete counts you can sum — ❌ **False.** They are not counts.
- **D)** Continuous numerical — ❌ **False.** No arithmetic meaning.

**Answer: B.** Short justification: numeric-looking IDs are nominal.

---

### Q134 · EM / GMM

In a probabilistic (soft) partition matrix, the membership β_ij is:

- **A)** A binary 0/1 assignment — ❌ **False.** That is a hard partition.
- **B)** The cluster radius — ❌ **False.** Unrelated.
- **C)** A probability/likelihood, with Σ_i β_ij = 1 over clusters per object — ✅ **True.** Hard partitions instead force β_ij ∈ {0,1}.
- **D)** A distance — ❌ **False.** Memberships are probabilities, not distances.

**Answer: C.** Short justification: soft/probabilistic memberships sum to 1 per object.

---

### Q135 · Frequent Itemsets

Apriori builds candidate k-itemsets by:

- **A)** Enumerating all 2^n itemsets and counting each — ❌ **False.** That defeats the purpose of pruning.
- **B)** Keeping only 1-itemsets — ❌ **False.** It grows itemsets level by level.
- **C)** Joining frequent (k−1)-itemsets, then pruning any with an infrequent (k−1)-subset — ✅ **True.** Prune step uses anti-monotonicity BEFORE counting support.
- **D)** Randomly sampling itemsets — ❌ **False.** Apriori is deterministic.

**Answer: C.** Your apriori(DB, max_cat, thresh) implements join+prune.

---

### Q136 · Outlier Detection

Which trio are the main UNSUPERVISED outlier-detection approaches in the slides?

- **A)** Apriori, FP-growth, Eclat — ❌ **False.** Those mine frequent itemsets.
- **B)** Single, complete, average linkage — ❌ **False.** Those are hierarchical linkages.
- **C)** Decision trees, SVMs, neural nets — ❌ **False.** Those are supervised classifiers.
- **D)** Statistical, clustering-based, and non-parametric density-based — ✅ **True.** These are the three families covered.

**Answer: D.** Short justification: statistical / clustering-based / density-based.

---

### Q137 · Data Representation

For u = [5, 0, -3, -2] and v = [0, 5, 8, 6], which value is the **Euclidean** distance d(u,v)?

- **A)** 11 — ❌ **False.** this is the Suprema/Chebyshev distance, supd(u,v).
- **B)** 29 — ❌ **False.** this is the Manhattan distance, mand(u,v).
- **C)** 15.33 — ✅ **True.** this is the Euclidean distance, eucd(u,v).
- **D)** 12.79 — ❌ **False.** this is the Minkowski p=3 distance, mink(u,v,3).

**Answer: C.** Use eucd(u,v).

---

### Q138 · Frequent Itemsets

For the database below, what is the **lift of {BREAD} ⇒ {BUTTER}**?

| TID | Items |
| --- | --- |
| 1 | BREAD, MILK |
| 2 | BREAD, BUTTER, MILK |
| 3 | BREAD, BUTTER, DIAPERS |
| 4 | BREAD, BUTTER, DIAPERS, MILK |
| 5 | BREAD, BUTTER, MILK |
| 6 | BREAD, BUTTER, DIAPERS, MILK |
| 7 | BUTTER, DIAPERS, MILK |
| 8 | BREAD, BUTTER, DIAPERS |
| 9 | BREAD, DIAPERS |
| 10 | BREAD, BUTTER, DIAPERS, MILK |
| 11 | BREAD, DIAPERS, MILK |
| 12 | BREAD, BUTTER, DIAPERS, MILK |

- **A)** 0.667 — ❌ **False.** this is the rule support/frequency support(A∪B)/|D|.
- **B)** 0.97 — ✅ **True.** this is the lift = conf(A⇒B)/f(B).
- **C)** 0.727 — ❌ **False.** this is the confidence (forgot to divide by f(B)).
- **D)** 0.75 — ❌ **False.** this is the frequency f(B) of the consequent.

**Answer: B.** Use lift(DB, {'BREAD'}, {'BUTTER'}) = confidence / f(consequent).

---

### Q139 · Outlier Detection

For the points [[5, 3], [2, 4], [1, 2], [6, 3], [5, 0], [6, 1], [13, 18]], which has the **highest unweighted KNN outlier score with k=1**?

- **A)** point 6 = [13, 18] — ✅ **True.** largest k=1 NN distance (16.55).
- **B)** point 2 = [1, 2] — ❌ **False.** its score 2.24 is not the largest.
- **C)** point 0 = [5, 3] — ❌ **False.** its score 1.0 is not the largest.
- **D)** point 3 = [6, 3] — ❌ **False.** its score 1.0 is not the largest.

**Answer: A.** Use knn_outlier(data, k) (score = distance to the k-th NN).

---

### Q140 · Density-Based

Run DBSCAN with ε = 2 and MinPts = 2 on the points [[4, 2], [7, 0], [4, 1], [0, 0], [8, 4], [4, 0], [8, 6]]. What is the type of point index 0 = [4, 2]?

- **A)** Noise — ❌ **False.** it is not a noise point (neither core nor within ε of a core point).
- **B)** Border — ❌ **False.** it is not a border point (< MinPts within ε, but within ε of a core point).
- **C)** Cluster centroid — ❌ **False.** DBSCAN has no centroids; points are core/border/noise.
- **D)** Core — ✅ **True.** it is a core point (≥ MinPts neighbours within ε, incl. itself).

**Answer: D.** Use dbscan(data, eps, minpts) → (labels, types).

---

### Q141 · Outlier Detection

For the points [[5, 5], [4, 5], [4, 6], [2, 1], [2, 5], [6, 0], [14, 15]], which has the **highest unweighted KNN outlier score with k=2**?

- **A)** point 0 = [5, 5] — ❌ **False.** its score 1.41 is not the largest.
- **B)** point 5 = [6, 0] — ❌ **False.** its score 5.1 is not the largest.
- **C)** point 1 = [4, 5] — ❌ **False.** its score 1.0 is not the largest.
- **D)** point 6 = [14, 15] — ✅ **True.** largest k=2 NN distance (13.45).

**Answer: D.** Use knn_outlier(data, k) (score = distance to the k-th NN).

---

### Q142 · Probability & Density

For the sample [7, 9, 3, 9, 5], what is the **sample variance** (dividing by n−1)?

- **A)** 6.8 — ✅ **True.** this is the sample variance (÷ n−1).
- **B)** 5.44 — ❌ **False.** this is the population/MLE variance (÷ n).
- **C)** 6.6 — ❌ **False.** this is the mean, not a variance.
- **D)** 2.608 — ❌ **False.** this is the standard deviation (√variance).

**Answer: A.** Use var(v) (sample=True); the MLE variance is var(v, sample=False).

---

### Q143 · Density-Based

Run DBSCAN with ε = 2 and MinPts = 3 on [[10, 7], [7, 1], [4, 3], [1, 10], [4, 6], [6, 11], [10, 5], [5, 8]]. **How many clusters** result (noise excluded)?

- **A)** 0 — ✅ **True.** DBSCAN forms 0 cluster(s) (8 noise point(s)).
- **B)** 2 — ❌ **False.** DBSCAN does not form 2 clusters here.
- **C)** 8 — ❌ **False.** DBSCAN does not form 8 clusters here.
- **D)** 1 — ❌ **False.** DBSCAN does not form 1 clusters here.

**Answer: A.** Use dbscan(data, eps, minpts); count distinct non-zero labels.

---

### Q144 · Density-Based

In DBSCAN, a CORE point:

- **A)** Has at least MinPts points within radius ε (including itself) — ✅ **True.** Core points sit in the interior of a dense region.
- **B)** Is the cluster centroid — ❌ **False.** DBSCAN has no centroids.
- **C)** Lies on the convex hull — ❌ **False.** Geometry of the hull is irrelevant.
- **D)** Has fewer than MinPts within ε — ❌ **False.** That may be border or noise.

**Answer: A.** Use dbscan(data, eps, minpts) → types include 'core'.

---

### Q145 · Partitioning (k-Means)

Run k-means on [[1, 0], [0, 0], [0, 2], [8, 11], [11, 11], [8, 8]] with initial prototypes [[1, 0], [8, 11]]. What are the **final cluster labels** (in order)?

- **A)** [0, 0, 0, 0, 0, 0] — ❌ **False.** this is everything in one cluster (not a 2-means result).
- **B)** [0, 1, 0, 1, 0, 1] — ❌ **False.** this is an alternating labelling (not distance-based).
- **C)** [1, 1, 1, 0, 0, 0] — ❌ **False.** this is the same split with labels swapped (not what these inits give).
- **D)** [0, 0, 0, 1, 1, 1] — ✅ **True.** this is the converged k-means assignment.

**Answer: D.** Use kmeans(data, init) → (labels, cents).

---

### Q146 · Introduction

The KDD cycle places data-mining/modelling at which stage?

- **A)** Before any data is collected — ❌ **False.** Data must be acquired and prepared first.
- **B)** Only after the final decision is made — ❌ **False.** Decisions come after interpretation.
- **C)** It replaces pre-processing entirely — ❌ **False.** Pre-processing precedes mining.
- **D)** After data acquisition, pre-processing and selection (on the target data) — ✅ **True.** Mining/modelling acts on the prepared target data, then validation/interpretation follow.

**Answer: D.** Short justification: KDD = acquire → preprocess → select → mine → validate/interpret.

---

### Q147 · Partitioning (k-Means)

Per-iteration k-means cost is:

- **A)** O(N³) — ❌ **False.** That is naive hierarchical time cost.
- **B)** O(N²) — ❌ **False.** That is hierarchical memory/comparison cost.
- **C)** O(N·n·k) — ✅ **True.** N points × k centroids × n dimensions.
- **D)** O(2^N) — ❌ **False.** Exponential — not k-means.

**Answer: C.** Short justification: linear in N → k-means scales well.

---

### Q148 · Density-Based

Run DBSCAN with ε = 3 and MinPts = 3 on the points [[9, 8], [3, 0], [9, 1], [7, 9], [9, 7], [3, 8], [2, 2]]. What is the type of point index 6 = [2, 2]?

- **A)** Cluster centroid — ❌ **False.** DBSCAN has no centroids; points are core/border/noise.
- **B)** Border — ❌ **False.** it is not a border point (< MinPts within ε, but within ε of a core point).
- **C)** Noise — ✅ **True.** it is a noise point (neither core nor within ε of a core point).
- **D)** Core — ❌ **False.** it is not a core point (≥ MinPts neighbours within ε, incl. itself).

**Answer: C.** Use dbscan(data, eps, minpts) → (labels, types).

---

### Q149 · Outlier Detection

For the points [[3, 6], [3, 4], [6, 1], [0, 0], [1, 2], [3, 2], [18, 14]], which has the **highest unweighted KNN outlier score with k=2**?

- **A)** point 1 = [3, 4] — ❌ **False.** its score 2.0 is not the largest.
- **B)** point 2 = [6, 1] — ❌ **False.** its score 4.24 is not the largest.
- **C)** point 3 = [0, 0] — ❌ **False.** its score 3.61 is not the largest.
- **D)** point 6 = [18, 14] — ✅ **True.** largest k=2 NN distance (17.69).

**Answer: D.** Use knn_outlier(data, k) (score = distance to the k-th NN).

---

### Q150 · EM / GMM

What is the value of the 1-D Normal density N(x=11 | μ=9, σ²=2)?

- **A)** 0.121 — ❌ **False.** this is using σ (std) where σ² (variance) was required.
- **B)** 0.1038 — ✅ **True.** this is the Normal pdf N(x|μ,σ²).
- **C)** 0.0519 — ❌ **False.** this is half the correct density (arithmetic slip).
- **D)** 0.3679 — ❌ **False.** this is only the exponential term, missing the 1/√(2πσ²) normaliser.

**Answer: B.** Use gauss(x, mu, var) (variance, not std).

---

### Q151 · Partitioning (k-Means)

Run k-means on [[3, 1], [1, 2], [0, 2], [0, 0], [10, 8], [8, 11], [11, 8], [10, 10]] with initial prototypes [[3, 1], [8, 11]]. What is the **final SSE**?

- **A)** 25.25 — ❌ **False.** not the converged SSE.
- **B)** 17.25 — ❌ **False.** not the converged SSE.
- **C)** 40.5 — ❌ **False.** not the converged SSE.
- **D)** 20.25 — ✅ **True.** this is the converged SSE.

**Answer: D.** Use kmeans(data, init) then sse(data, labels, cents).

---

### Q152 · Probability & Density

For the sample [6, 2, 2, 4, 5, 5], what is the **sample variance** (dividing by n−1)?

- **A)** 2.8 — ✅ **True.** this is the sample variance (÷ n−1).
- **B)** 1.673 — ❌ **False.** this is the standard deviation (√variance).
- **C)** 4.0 — ❌ **False.** this is the mean, not a variance.
- **D)** 2.333 — ❌ **False.** this is the population/MLE variance (÷ n).

**Answer: A.** Use var(v) (sample=True); the MLE variance is var(v, sample=False).

---

### Q153 · EM / GMM

In an EM-GMM (k=2), the densities at x are 0.0104 and 0.0044 with priors π_C1=0.6, π_C2=0.4. What is the **posterior probability of C1** at x?

- **A)** 0.6 — ❌ **False.** this is the PRIOR π_C1, not the posterior.
- **B)** 0.703 — ❌ **False.** this is the densities normalised WITHOUT the priors.
- **C)** 0.22 — ❌ **False.** this is the posterior of C2, not C1.
- **D)** 0.78 — ✅ **True.** this is the posterior (responsibility) of C1 via Bayes.

**Answer: D.** Use posteriors([d1,d2],[π1,π2]) (E-step, Bayes' rule).

---

### Q154 · Data Representation

For u = [7, 7, -1, -3] and v = [-1, -3, 0, 0], which value is the **Manhattan** distance d(u,v)?

- **A)** 11.55 — ❌ **False.** this is the Minkowski p=3 distance, mink(u,v,3).
- **B)** 22 — ✅ **True.** this is the Manhattan distance, mand(u,v).
- **C)** 10 — ❌ **False.** this is the Suprema/Chebyshev distance, supd(u,v).
- **D)** 13.19 — ❌ **False.** this is the Euclidean distance, eucd(u,v).

**Answer: B.** Use mand(u,v).

---

### Q155 · Hierarchical

Given the distance matrix (0-based indices), which pair merges **first** under Single-Linkage?

```
[0, 12, 9, 3]
[12, 0, 11, 9]
[9, 11, 0, 1]
[3, 9, 1, 0]
```

- **A)** objects 0 and 3 (d=3) — ❌ **False.** their distance 3 is not the minimum.
- **B)** objects 0 and 1 (d=12) — ❌ **False.** their distance 12 is not the minimum.
- **C)** objects 2 and 3 (d=1) — ✅ **True.** this is the smallest distance, so they merge first.
- **D)** objects 1 and 3 (d=9) — ❌ **False.** their distance 9 is not the minimum.

**Answer: C.** Use ahc(D,'single'); the closest pair always merges first.

---

### Q156 · Data Representation

For u = [-2, -1, 4, 7] and v = [-1, 1, 3, 7], which value is the **Euclidean** distance d(u,v)?

- **A)** 2.15 — ❌ **False.** this is the Minkowski p=3 distance, mink(u,v,3).
- **B)** 4 — ❌ **False.** this is the Manhattan distance, mand(u,v).
- **C)** 2 — ❌ **False.** this is the Suprema/Chebyshev distance, supd(u,v).
- **D)** 2.45 — ✅ **True.** this is the Euclidean distance, eucd(u,v).

**Answer: D.** Use eucd(u,v).

---

### Q157 · Probability & Density

For the sample [7, 3, 5, 1, 7], what is the **sample variance** (dividing by n−1)?

- **A)** 5.44 — ❌ **False.** this is the population/MLE variance (÷ n).
- **B)** 6.8 — ✅ **True.** this is the sample variance (÷ n−1).
- **C)** 4.6 — ❌ **False.** this is the mean, not a variance.
- **D)** 2.608 — ❌ **False.** this is the standard deviation (√variance).

**Answer: B.** Use var(v) (sample=True); the MLE variance is var(v, sample=False).

---

### Q158 · Outlier Detection

Hawkins' classic definition of an outlier is an observation that:

- **A)** Has zero variance — ❌ **False.** Unrelated to the definition.
- **B)** Has the largest value in the data — ❌ **False.** Magnitude alone is not the definition.
- **C)** Deviates so much it seems generated by a different mechanism — ✅ **True.** Normal points follow one generating process; outliers do not.
- **D)** Belongs to the majority class — ❌ **False.** That describes inliers.

**Answer: C.** Short justification: Hawkins (1980) — 'different mechanism'.

---

### Q159 · Data Representation

For u = [7, 3, 2, 2] and v = [3, 5, 5, -1], which value is the **Euclidean** distance d(u,v)?

- **A)** 4 — ❌ **False.** this is the Suprema/Chebyshev distance, supd(u,v).
- **B)** 5.01 — ❌ **False.** this is the Minkowski p=3 distance, mink(u,v,3).
- **C)** 6.16 — ✅ **True.** this is the Euclidean distance, eucd(u,v).
- **D)** 12 — ❌ **False.** this is the Manhattan distance, mand(u,v).

**Answer: C.** Use eucd(u,v).

---

### Q160 · Frequent Itemsets

For the database below, what is the **support count of {DIAPERS, BREAD}**?

| TID | Items |
| --- | --- |
| 1 | BEER, BREAD, BUTTER, DIAPERS, EGGS, MILK |
| 2 | BREAD, DIAPERS, EGGS |
| 3 | BEER, BUTTER, DIAPERS, EGGS, MILK |
| 4 | BEER, EGGS |
| 5 | BEER, BREAD, BUTTER, DIAPERS, EGGS, MILK |
| 6 | BEER, BREAD, BUTTER, DIAPERS, EGGS, MILK |
| 7 | BREAD, DIAPERS |
| 8 | BREAD, BUTTER, EGGS, MILK |
| 9 | BEER, BREAD, DIAPERS, EGGS |
| 10 | BREAD, BUTTER, DIAPERS, EGGS, MILK |
| 11 | BEER, BREAD, BUTTER, DIAPERS, EGGS, MILK |
| 12 | BEER, BUTTER, DIAPERS, EGGS, MILK |

- **A)** 9 — ❌ **False.** this is the support of {BREAD} alone.
- **B)** 10 — ❌ **False.** this is the support of {DIAPERS} alone.
- **C)** 8 — ✅ **True.** this is the support of {DIAPERS, BREAD}.
- **D)** 4 — ❌ **False.** this is the number of transactions NOT containing both.

**Answer: C.** Use support(DB, {'DIAPERS','BREAD'}).

---

### Q161 · Data Representation

For u = [0, 8, 2, 5] and v = [3, 7, 6, -1], which value is the **Euclidean** distance d(u,v)?

- **A)** 7.87 — ✅ **True.** this is the Euclidean distance, eucd(u,v).
- **B)** 6.75 — ❌ **False.** this is the Minkowski p=3 distance, mink(u,v,3).
- **C)** 14 — ❌ **False.** this is the Manhattan distance, mand(u,v).
- **D)** 6 — ❌ **False.** this is the Suprema/Chebyshev distance, supd(u,v).

**Answer: A.** Use eucd(u,v).

---

### Q162 · Outlier Detection

For the points [[3, 0], [0, 1], [1, 2], [3, 5], [1, 4], [1, 3], [18, 16]], which has the **highest unweighted KNN outlier score with k=2**?

- **A)** point 4 = [1, 4] — ❌ **False.** its score 2.0 is not the largest.
- **B)** point 0 = [3, 0] — ❌ **False.** its score 3.16 is not the largest.
- **C)** point 6 = [18, 16] — ✅ **True.** largest k=2 NN distance (20.81).
- **D)** point 3 = [3, 5] — ❌ **False.** its score 2.83 is not the largest.

**Answer: C.** Use knn_outlier(data, k) (score = distance to the k-th NN).

---

### Q163 · Probability & Density

A test has sensitivity 0.99, specificity 0.9; prevalence P(D)=0.01. What is **P(D | positive)**?

- **A)** 0.01 — ❌ **False.** this is the prior prevalence P(D), not the posterior.
- **B)** 0.091 — ✅ **True.** this is the posterior P(D|+) by Bayes' rule.
- **C)** 0.909 — ❌ **False.** this is the complement 1−P(D|+).
- **D)** 0.99 — ❌ **False.** this is the sensitivity P(+|D) (likelihood), not the posterior.

**Answer: B.** Use bayes(likelihood, prior, evidence) with evidence = sens·prev + (1−spec)·(1−prev).

---

### Q164 · Data Representation

For u = [2, 1, 3, 1, 3] and v = [3, 3, 0, 2, 5], which value is the **cosine similarity** cos(u,v)?

- **A)** 0.0 — ❌ **False.** this is the Pearson correlation, a different measure.
- **B)** 0.023 — ❌ **False.** this is the inner product over ||u||²·||v||² (missing the square root).
- **C)** 26.0 — ❌ **False.** this is just the inner product <u,v> (not normalised).
- **D)** 0.774 — ✅ **True.** this is the cosine similarity.

**Answer: D.** Use cosine(u,v) = <u,v> / (||u||·||v||).

---

### Q165 · Outlier Detection

For the points [[6, 2], [0, 0], [3, 5], [1, 1], [2, 1], [1, 5], [18, 14]], which has the **highest unweighted KNN outlier score with k=1**?

- **A)** point 4 = [2, 1] — ❌ **False.** its score 1.0 is not the largest.
- **B)** point 6 = [18, 14] — ✅ **True.** largest k=1 NN distance (16.97).
- **C)** point 1 = [0, 0] — ❌ **False.** its score 1.41 is not the largest.
- **D)** point 5 = [1, 5] — ❌ **False.** its score 2.0 is not the largest.

**Answer: B.** Use knn_outlier(data, k) (score = distance to the k-th NN).

---

### Q166 · Data Representation

For u = [1, -1, 0] and v = [1, 3, 1], which value is the **Euclidean** distance d(u,v)?

- **A)** 4.02 — ❌ **False.** this is the Minkowski p=3 distance, mink(u,v,3).
- **B)** 4 — ❌ **False.** this is the Suprema/Chebyshev distance, supd(u,v).
- **C)** 4.12 — ✅ **True.** this is the Euclidean distance, eucd(u,v).
- **D)** 5 — ❌ **False.** this is the Manhattan distance, mand(u,v).

**Answer: C.** Use eucd(u,v).

---

### Q167 · Partitioning (k-Means)

Run k-means on [[1, 3], [3, 2], [1, 0], [8, 11], [11, 8], [8, 11]] with initial prototypes [[1, 3], [8, 11]]. What are the **final cluster labels** (in order)?

- **A)** [0, 0, 0, 0, 0, 0] — ❌ **False.** this is everything in one cluster (not a 2-means result).
- **B)** [0, 1, 0, 1, 0, 1] — ❌ **False.** this is an alternating labelling (not distance-based).
- **C)** [1, 1, 1, 0, 0, 0] — ❌ **False.** this is the same split with labels swapped (not what these inits give).
- **D)** [0, 0, 0, 1, 1, 1] — ✅ **True.** this is the converged k-means assignment.

**Answer: D.** Use kmeans(data, init) → (labels, cents).

---

### Q168 · Density-Based

Run DBSCAN with ε = 3 and MinPts = 2 on [[10, 10], [3, 9], [5, 11], [5, 8], [5, 6], [4, 2], [9, 10], [5, 0]]. **How many clusters** result (noise excluded)?

- **A)** 4 — ❌ **False.** DBSCAN does not form 4 clusters here.
- **B)** 2 — ❌ **False.** DBSCAN does not form 2 clusters here.
- **C)** 8 — ❌ **False.** DBSCAN does not form 8 clusters here.
- **D)** 3 — ✅ **True.** DBSCAN forms 3 cluster(s) (0 noise point(s)).

**Answer: D.** Use dbscan(data, eps, minpts); count distinct non-zero labels.

---

### Q169 · Frequent Itemsets

For the database below, what is the **lift of {EGGS} ⇒ {BUTTER}**?

| TID | Items |
| --- | --- |
| 1 | BREAD, BUTTER, EGGS, MILK |
| 2 | BREAD, BUTTER, EGGS, MILK |
| 3 | BUTTER, EGGS, MILK |
| 4 | BREAD, BUTTER, EGGS, MILK |
| 5 | BREAD, BUTTER, EGGS, MILK |
| 6 | BREAD, EGGS |
| 7 | BREAD, BUTTER, EGGS, MILK |
| 8 | BREAD, BUTTER, EGGS, MILK |
| 9 | BREAD, BUTTER, EGGS |
| 10 | BREAD, EGGS |
| 11 | BUTTER, MILK |
| 12 | BUTTER, EGGS |

- **A)** 0.75 — ❌ **False.** this is the rule support/frequency support(A∪B)/|D|.
- **B)** 0.818 — ❌ **False.** this is the confidence (forgot to divide by f(B)).
- **C)** 0.982 — ✅ **True.** this is the lift = conf(A⇒B)/f(B).
- **D)** 0.833 — ❌ **False.** this is the frequency f(B) of the consequent.

**Answer: C.** Use lift(DB, {'EGGS'}, {'BUTTER'}) = confidence / f(consequent).

---

### Q170 · Hierarchical

Given the distance matrix (0-based indices), which pair merges **first** under Single-Linkage?

```
[0, 6, 1, 8, 6]
[6, 0, 1, 1, 9]
[1, 1, 0, 1, 10]
[8, 1, 1, 0, 3]
[6, 9, 10, 3, 0]
```

- **A)** objects 1 and 2 (d=1) — ❌ **False.** their distance 1 is not the minimum.
- **B)** objects 0 and 2 (d=1) — ✅ **True.** this is the smallest distance, so they merge first.
- **C)** objects 0 and 1 (d=6) — ❌ **False.** their distance 6 is not the minimum.
- **D)** objects 2 and 4 (d=10) — ❌ **False.** their distance 10 is not the minimum.

**Answer: B.** Use ahc(D,'single'); the closest pair always merges first.

---

### Q171 · Probability & Density

Zero covariance between X and Y means they are:

- **A)** Always independent — ❌ **False.** Zero cov is necessary, not sufficient.
- **B)** Perfectly correlated — ❌ **False.** Opposite of zero covariance.
- **C)** Identical — ❌ **False.** Unrelated.
- **D)** Uncorrelated (no linear relationship), but not necessarily independent — ✅ **True.** A nonlinear dependence can remain.

**Answer: D.** Use cov(u,v); independence needs the full joint to factorise.

---

### Q172 · Hierarchical

For the distance matrix below, what is the **root (final) merge height under Complete-Linkage**?

```
[0, 2, 5, 2]
[2, 0, 6, 7]
[5, 6, 0, 6]
[2, 7, 6, 0]
```

- **A)** 7 — ✅ **True.** this is the complete-linkage root height.
- **B)** 5.67 — ❌ **False.** this is the average-linkage root height.
- **C)** 5 — ❌ **False.** this is the single-linkage root height.
- **D)** 9 — ❌ **False.** this is an off value (recompute).

**Answer: A.** Use ahc(D, 'complete'); the last merge's height is the root.

---

### Q173 · Hierarchical

For the distance matrix below, what is the **root (final) merge height under Single-Linkage**?

```
[0, 10, 9, 4]
[10, 0, 12, 5]
[9, 12, 0, 4]
[4, 5, 4, 0]
```

- **A)** 9.0 — ❌ **False.** this is the average-linkage root height.
- **B)** 5 — ✅ **True.** this is the single-linkage root height.
- **C)** 8 — ❌ **False.** this is an off value (recompute).
- **D)** 12 — ❌ **False.** this is the complete-linkage root height.

**Answer: B.** Use ahc(D, 'single'); the last merge's height is the root.

---

### Q174 · Data Representation

For binary x1 = [0, 1, 1, 0, 0, 1, 0, 1] and x2 = [0, 1, 0, 0, 1, 1, 0, 0], which value is the **Jaccard** coefficient?

- **A)** 0.375 — ❌ **False.** this is the fraction of disagreements (n10+n01)/n.
- **B)** 0.4 — ✅ **True.** this is the Jaccard = n11/(n11+n10+n01).
- **C)** 0.25 — ❌ **False.** this is only n11/n (it omits the other agreements/structure).
- **D)** 0.625 — ❌ **False.** this is the SMC = (n11+n00)/n.

**Answer: B.** Use 0.4; contingency(x1,x2)=(n11,n10,n01,n00)=(2,2,1,3).

---

### Q175 · Frequent Itemsets

For the database below, what is the **confidence of {EGGS} ⇒ {BUTTER}**?

| TID | Items |
| --- | --- |
| 1 | BREAD, BUTTER |
| 2 | BREAD, BUTTER, DIAPERS, EGGS |
| 3 | BREAD, BUTTER, DIAPERS |
| 4 | BREAD, DIAPERS |
| 5 | BREAD, BUTTER, EGGS |
| 6 | BREAD, DIAPERS |
| 7 | BREAD, BUTTER, DIAPERS, EGGS |
| 8 | BREAD, BUTTER, DIAPERS, EGGS |
| 9 | BUTTER, EGGS |
| 10 | BREAD, DIAPERS |
| 11 | BUTTER, DIAPERS |
| 12 | BREAD, DIAPERS |

- **A)** 1.5 — ❌ **False.** this is the lift, a different metric.
- **B)** 1.0 — ✅ **True.** this is confidence = support(A∪B)/support(A).
- **C)** 0.417 — ❌ **False.** this is the rule's support/frequency support(A∪B)/|D|.
- **D)** 0.625 — ❌ **False.** this is support(A∪B)/support(B) — wrong denominator.

**Answer: B.** Use confidence(DB, {'EGGS'}, {'BUTTER'}).

---

### Q176 · EM / GMM

In an EM-GMM (k=2), the densities at x are 0.0106 and 0.0098 with priors π_C1=0.6, π_C2=0.4. What is the **posterior probability of C1** at x?

- **A)** 0.381 — ❌ **False.** this is the posterior of C2, not C1.
- **B)** 0.52 — ❌ **False.** this is the densities normalised WITHOUT the priors.
- **C)** 0.619 — ✅ **True.** this is the posterior (responsibility) of C1 via Bayes.
- **D)** 0.6 — ❌ **False.** this is the PRIOR π_C1, not the posterior.

**Answer: C.** Use posteriors([d1,d2],[π1,π2]) (E-step, Bayes' rule).

---

### Q177 · Frequent Itemsets

A MAXIMAL frequent itemset is one that:

- **A)** Has the largest support — ❌ **False.** Support size is unrelated to maximality.
- **B)** Has no superset of equal support — ❌ **False.** That is CLOSED.
- **C)** Is a singleton — ❌ **False.** Maximal sets are usually larger.
- **D)** Has no frequent superset — ✅ **True.** Maximal ⊆ closed ⊆ frequent.

**Answer: D.** Use is_maximal(DB, X, thresh).

---

### Q178 · Data Representation

For u = [-2, 7, 4, -4] and v = [0, 5, -1, -1], which value is the **Manhattan** distance d(u,v)?

- **A)** 5.52 — ❌ **False.** this is the Minkowski p=3 distance, mink(u,v,3).
- **B)** 5 — ❌ **False.** this is the Suprema/Chebyshev distance, supd(u,v).
- **C)** 12 — ✅ **True.** this is the Manhattan distance, mand(u,v).
- **D)** 6.48 — ❌ **False.** this is the Euclidean distance, eucd(u,v).

**Answer: C.** Use mand(u,v).

---

### Q179 · Data Representation

For u = [5, 2, 1, 2] and v = [5, 5, 1, 1], which value is the **cosine similarity** cos(u,v)?

- **A)** 38.0 — ❌ **False.** this is just the inner product <u,v> (not normalised).
- **B)** 0.667 — ❌ **False.** this is the Pearson correlation, a different measure.
- **C)** 0.021 — ❌ **False.** this is the inner product over ||u||²·||v||² (missing the square root).
- **D)** 0.904 — ✅ **True.** this is the cosine similarity.

**Answer: D.** Use cosine(u,v) = <u,v> / (||u||·||v||).

---

### Q180 · Hierarchical

Given the distance matrix (0-based indices), which pair merges **first** under Single-Linkage?

```
[0, 11, 5, 9]
[11, 0, 6, 12]
[5, 6, 0, 10]
[9, 12, 10, 0]
```

- **A)** objects 0 and 2 (d=5) — ✅ **True.** this is the smallest distance, so they merge first.
- **B)** objects 1 and 3 (d=12) — ❌ **False.** their distance 12 is not the minimum.
- **C)** objects 2 and 3 (d=10) — ❌ **False.** their distance 10 is not the minimum.
- **D)** objects 1 and 2 (d=6) — ❌ **False.** their distance 6 is not the minimum.

**Answer: A.** Use ahc(D,'single'); the closest pair always merges first.

---

### Q181 · Data Representation

For binary x1 = [0, 0, 1, 1, 1, 1, 0, 1] and x2 = [0, 1, 1, 1, 0, 1, 0, 1], which value is the **SMC** coefficient?

- **A)** 0.5 — ❌ **False.** this is only n11/n (it omits the other agreements/structure).
- **B)** 0.25 — ❌ **False.** this is the fraction of disagreements (n10+n01)/n.
- **C)** 0.667 — ❌ **False.** this is the Jaccard = n11/(n11+n10+n01).
- **D)** 0.75 — ✅ **True.** this is the SMC = (n11+n00)/n.

**Answer: D.** Use 0.75; contingency(x1,x2)=(n11,n10,n01,n00)=(4,1,1,2).

---

### Q182 · Probability & Density

For the sample [4, 2, 6, 5, 2], what is the **sample variance** (dividing by n−1)?

- **A)** 2.56 — ❌ **False.** this is the population/MLE variance (÷ n).
- **B)** 3.8 — ❌ **False.** this is the mean, not a variance.
- **C)** 1.789 — ❌ **False.** this is the standard deviation (√variance).
- **D)** 3.2 — ✅ **True.** this is the sample variance (÷ n−1).

**Answer: D.** Use var(v) (sample=True); the MLE variance is var(v, sample=False).

---

### Q183 · Outlier Detection

A core problem of the STATISTICAL (parametric) outlier approach is:

- **A)** It needs no distribution at all — ❌ **False.** It assumes a parametric distribution.
- **B)** A distribution must be assumed and its estimates can be skewed by the very outliers sought — ✅ **True.** True distributions are rarely known; estimates need robustness.
- **C)** It cannot produce any score — ❌ **False.** It can produce probabilities/scores.
- **D)** It works only on text — ❌ **False.** It is general-purpose.

**Answer: B.** Short justification: parametric assumption + estimate robustness issues.

---

### Q184 · EM / GMM

Which statement about EM-GMM is TRUE?

- **A)** It is hierarchical and finds k automatically — ❌ **False.** It is non-hierarchical; k is given.
- **B)** It works directly on nominal data — ❌ **False.** It needs real-valued data.
- **C)** It is parametric, needs k as input, and converges only to a local optimum — ✅ **True.** Often initialised with k-means.
- **D)** It is non-parametric — ❌ **False.** It is a parametric (Gaussian) model.

**Answer: C.** Short justification: parametric, k-input, local optima, real-valued.

---

### Q185 · Hierarchical

Single-linkage is characterised by:

- **A)** Detecting arbitrarily shaped clusters but being sensitive to noise (chaining) — ✅ **True.** Nearby noise points can bridge clusters.
- **B)** Requiring real-valued vectors only — ❌ **False.** It works from a distance matrix alone.
- **C)** Being the most robust to outliers — ❌ **False.** Single-linkage is the least robust.
- **D)** Producing only globular clusters — ❌ **False.** That is complete/average/Ward.

**Answer: A.** Use ahc(D, 'single'); compare with 'complete'/'average'.

---

### Q186 · Density-Based

Run DBSCAN with ε = 2 and MinPts = 2 on [[6, 0], [9, 1], [2, 1], [5, 2], [0, 6], [0, 8], [6, 2], [9, 2]]. **How many clusters** result (noise excluded)?

- **A)** 4 — ❌ **False.** DBSCAN does not form 4 clusters here.
- **B)** 2 — ❌ **False.** DBSCAN does not form 2 clusters here.
- **C)** 3 — ✅ **True.** DBSCAN forms 3 cluster(s) (1 noise point(s)).
- **D)** 8 — ❌ **False.** DBSCAN does not form 8 clusters here.

**Answer: C.** Use dbscan(data, eps, minpts); count distinct non-zero labels.

---

### Q187 · Probability & Density

For the sample [3, 2, 4, 4, 1], what is the **sample variance** (dividing by n−1)?

- **A)** 1.7 — ✅ **True.** this is the sample variance (÷ n−1).
- **B)** 1.36 — ❌ **False.** this is the population/MLE variance (÷ n).
- **C)** 1.304 — ❌ **False.** this is the standard deviation (√variance).
- **D)** 2.8 — ❌ **False.** this is the mean, not a variance.

**Answer: A.** Use var(v) (sample=True); the MLE variance is var(v, sample=False).

---

### Q188 · Data Representation

For u = [3, 4, 8] and v = [5, 8, 1], which value is the **Euclidean** distance d(u,v)?

- **A)** 13 — ❌ **False.** this is the Manhattan distance, mand(u,v).
- **B)** 7.46 — ❌ **False.** this is the Minkowski p=3 distance, mink(u,v,3).
- **C)** 7 — ❌ **False.** this is the Suprema/Chebyshev distance, supd(u,v).
- **D)** 8.31 — ✅ **True.** this is the Euclidean distance, eucd(u,v).

**Answer: D.** Use eucd(u,v).

---

### Q189 · Frequent Itemsets

For the database below, what is the **confidence of {BREAD} ⇒ {MILK}**?

| TID | Items |
| --- | --- |
| 1 | BREAD, BUTTER, DIAPERS, MILK |
| 2 | BUTTER, DIAPERS, MILK |
| 3 | BUTTER, DIAPERS |
| 4 | BUTTER, DIAPERS, MILK |
| 5 | BUTTER, MILK |
| 6 | BREAD, DIAPERS |
| 7 | BUTTER, DIAPERS |
| 8 | BREAD, DIAPERS, MILK |
| 9 | BREAD, BUTTER, DIAPERS, MILK |
| 10 | BREAD, DIAPERS |
| 11 | BREAD, BUTTER, DIAPERS, MILK |
| 12 | BREAD, BUTTER, DIAPERS, MILK |

- **A)** 0.625 — ❌ **False.** this is support(A∪B)/support(B) — wrong denominator.
- **B)** 1.071 — ❌ **False.** this is the lift, a different metric.
- **C)** 0.417 — ❌ **False.** this is the rule's support/frequency support(A∪B)/|D|.
- **D)** 0.714 — ✅ **True.** this is confidence = support(A∪B)/support(A).

**Answer: D.** Use confidence(DB, {'BREAD'}, {'MILK'}).

---

### Q190 · Partitioning (k-Means)

Run k-means on [[0, 0], [0, 2], [2, 0], [11, 10], [10, 11], [11, 9]] with initial prototypes [[0, 0], [11, 10]]. What are the **final cluster labels** (in order)?

- **A)** [0, 0, 0, 1, 1, 1] — ✅ **True.** this is the converged k-means assignment.
- **B)** [0, 1, 0, 1, 0, 1] — ❌ **False.** this is an alternating labelling (not distance-based).
- **C)** [1, 1, 1, 0, 0, 0] — ❌ **False.** this is the same split with labels swapped (not what these inits give).
- **D)** [0, 0, 0, 0, 0, 0] — ❌ **False.** this is everything in one cluster (not a 2-means result).

**Answer: A.** Use kmeans(data, init) → (labels, cents).

---

### Q191 · Frequent Itemsets

For the database below, what is the **confidence of {EGGS} ⇒ {MILK}**?

| TID | Items |
| --- | --- |
| 1 | DIAPERS, EGGS, MILK |
| 2 | BREAD, DIAPERS, MILK |
| 3 | BREAD, EGGS, MILK |
| 4 | BREAD, DIAPERS, EGGS, MILK |
| 5 | BREAD, DIAPERS, EGGS, MILK |
| 6 | DIAPERS, EGGS, MILK |
| 7 | DIAPERS, EGGS, MILK |
| 8 | BREAD, DIAPERS |
| 9 | DIAPERS, EGGS, MILK |
| 10 | BREAD, DIAPERS, EGGS, MILK |
| 11 | BREAD, DIAPERS, EGGS, MILK |
| 12 | BREAD, DIAPERS, MILK |

- **A)** 0.75 — ❌ **False.** this is the rule's support/frequency support(A∪B)/|D|.
- **B)** 1.091 — ❌ **False.** this is the lift, a different metric.
- **C)** 1.0 — ✅ **True.** this is confidence = support(A∪B)/support(A).
- **D)** 0.818 — ❌ **False.** this is support(A∪B)/support(B) — wrong denominator.

**Answer: C.** Use confidence(DB, {'EGGS'}, {'MILK'}).

---

### Q192 · Partitioning (k-Means)

Classic k-means represents a cluster by its ___ and assigns points using ___.

- **A)** random member ; cosine similarity — ❌ **False.** Not k-means.
- **B)** densest point ; Mahalanobis distance — ❌ **False.** Not k-means.
- **C)** medoid ; Manhattan distance — ❌ **False.** That is k-medoids/PAM.
- **D)** centroid (mean) ; squared Euclidean distance — ✅ **True.** It is a prototype-based, mean-based, hard partitioning method.

**Answer: D.** Use kmeans(data, init); centroid via centroid(pts).

---

### Q193 · Data Representation

For u = [3, 3, 2, -1] and v = [-2, -2, -1, 7], which value is the **Euclidean** distance d(u,v)?

- **A)** 21 — ❌ **False.** this is the Manhattan distance, mand(u,v).
- **B)** 9.24 — ❌ **False.** this is the Minkowski p=3 distance, mink(u,v,3).
- **C)** 8 — ❌ **False.** this is the Suprema/Chebyshev distance, supd(u,v).
- **D)** 11.09 — ✅ **True.** this is the Euclidean distance, eucd(u,v).

**Answer: D.** Use eucd(u,v).

---

### Q194 · Probability & Density

For a Normal distribution, the MLE estimates of mean and variance are:

- **A)** The sample mean and the sample variance (variance dividing by n) — ✅ **True.** The MLE for a Gaussian is intuitive.
- **B)** Always 0 and 1 — ❌ **False.** Only for a standardised special case.
- **C)** The median and the range — ❌ **False.** Not the MLE.
- **D)** The mode and the IQR — ❌ **False.** Not the MLE.

**Answer: A.** Use MLE_uni(v) → (sample mean, MLE variance).

---

### Q195 · Probability & Density

Parametric vs non-parametric density estimation — which pairing is correct?

- **A)** Parametric → MLE / method of moments; non-parametric → KDE and kNN density — ✅ **True.** Parametric assumes a known form; non-parametric does not.
- **B)** Both are only histograms — ❌ **False.** KDE/kNN/MLE are distinct methods.
- **C)** Parametric → KDE; non-parametric → MLE — ❌ **False.** Reversed.
- **D)** Non-parametric assumes a Gaussian — ❌ **False.** Non-parametric assumes no fixed form.

**Answer: A.** Use MLE_uni(v) (parametric) or kde(x, data, h) (non-parametric).

---

### Q196 · Frequent Itemsets

Lift(A ⇒ B) equals:

- **A)** support(A ∪ B) — ❌ **False.** That is the rule support.
- **B)** 1 − conf(A⇒B) — ❌ **False.** That is part of conviction, not lift.
- **C)** conf(A⇒B) × support(A) — ❌ **False.** Equals support(A∪B), not lift.
- **D)** conf(A⇒B) / f(B) — ✅ **True.** Lift>1 positive assoc., =1 independent, <1 negative.

**Answer: D.** Use lift(DB, A, B).

---

### Q197 · Density-Based

Run DBSCAN with ε = 2 and MinPts = 3 on the points [[6, 7], [4, 6], [7, 5], [6, 0], [7, 4], [9, 5], [2, 0]]. What is the type of point index 2 = [7, 5]?

- **A)** Cluster centroid — ❌ **False.** DBSCAN has no centroids; points are core/border/noise.
- **B)** Border — ❌ **False.** it is not a border point (< MinPts within ε, but within ε of a core point).
- **C)** Core — ✅ **True.** it is a core point (≥ MinPts neighbours within ε, incl. itself).
- **D)** Noise — ❌ **False.** it is not a noise point (neither core nor within ε of a core point).

**Answer: C.** Use dbscan(data, eps, minpts) → (labels, types).

---

### Q198 · Outlier Detection

In the DB(ε, π)-outlier model, a point p is an outlier if:

- **A)** It has the highest density — ❌ **False.** Outliers have low density.
- **B)** It is the cluster centroid — ❌ **False.** No centroids in this model.
- **C)** More than π points lie within ε — ❌ **False.** That would make it an inlier.
- **D)** At most a fraction π of the other points lie within distance ε of p — ✅ **True.** A distance-based notion of low local density.

**Answer: D.** Use db_outlier(data, eps, pi).

---

### Q199 · Frequent Itemsets

For the database below, what is the **confidence of {EGGS} ⇒ {MILK}**?

| TID | Items |
| --- | --- |
| 1 | BUTTER, EGGS |
| 2 | BREAD, BUTTER, EGGS, MILK |
| 3 | BUTTER, EGGS, MILK |
| 4 | BREAD, BUTTER, EGGS, MILK |
| 5 | BREAD, EGGS, MILK |
| 6 | BREAD, BUTTER, EGGS, MILK |
| 7 | BREAD, EGGS |
| 8 | BUTTER, EGGS |
| 9 | BUTTER, EGGS, MILK |
| 10 | BREAD, BUTTER |
| 11 | BREAD, EGGS, MILK |
| 12 | BREAD, EGGS |

- **A)** 1.091 — ❌ **False.** this is the lift, a different metric.
- **B)** 1.0 — ❌ **False.** this is support(A∪B)/support(B) — wrong denominator.
- **C)** 0.583 — ❌ **False.** this is the rule's support/frequency support(A∪B)/|D|.
- **D)** 0.636 — ✅ **True.** this is confidence = support(A∪B)/support(A).

**Answer: D.** Use confidence(DB, {'EGGS'}, {'MILK'}).

---

### Q200 · Density-Based

DBSCAN's two parameters are:

- **A)** support and confidence — ❌ **False.** Those are association-rule metrics.
- **B)** ε (radius) and MinPts — ✅ **True.** They define the density threshold via an ε-neighbourhood count.
- **C)** k and the iteration count — ❌ **False.** Those are k-means-like settings.
- **D)** centroid and variance — ❌ **False.** DBSCAN is non-parametric, no centroids.

**Answer: B.** Use dbscan(data, eps, minpts).

---

### Q201 · Partitioning (k-Means)

Run k-means on [[2, 3], [3, 1], [1, 1], [11, 9], [8, 9], [8, 9]] with initial prototypes [[2, 3], [11, 9]]. What are the **final cluster labels** (in order)?

- **A)** [0, 1, 0, 1, 0, 1] — ❌ **False.** this is an alternating labelling (not distance-based).
- **B)** [0, 0, 0, 0, 0, 0] — ❌ **False.** this is everything in one cluster (not a 2-means result).
- **C)** [0, 0, 0, 1, 1, 1] — ✅ **True.** this is the converged k-means assignment.
- **D)** [1, 1, 1, 0, 0, 0] — ❌ **False.** this is the same split with labels swapped (not what these inits give).

**Answer: C.** Use kmeans(data, init) → (labels, cents).

---

### Q202 · Probability & Density

A test has sensitivity 0.95, specificity 0.95; prevalence P(D)=0.01. What is **P(D | positive)**?

- **A)** 0.161 — ✅ **True.** this is the posterior P(D|+) by Bayes' rule.
- **B)** 0.839 — ❌ **False.** this is the complement 1−P(D|+).
- **C)** 0.01 — ❌ **False.** this is the prior prevalence P(D), not the posterior.
- **D)** 0.95 — ❌ **False.** this is the sensitivity P(+|D) (likelihood), not the posterior.

**Answer: A.** Use bayes(likelihood, prior, evidence) with evidence = sens·prev + (1−spec)·(1−prev).

---

### Q203 · Density-Based

Typical DBSCAN runtime is:

- **A)** O(2^n) — ❌ **False.** Not exponential.
- **B)** O(N) always — ❌ **False.** Range searches cost more than O(1) each.
- **C)** O(n²) in general, O(n log n) with spatial indexes in low dimensions — ✅ **True.** Cost is n × ε-range-search; indexes (kd-/R*-trees) speed it up.
- **D)** O(N³) like hierarchical — ❌ **False.** DBSCAN is cheaper.

**Answer: C.** Short justification: O(n²), O(n log n) with indexing; O(n) memory.

---

### Q204 · Outlier Detection

For LOF values, which interpretation is correct?

- **A)** LOF is always within [0,1] — ❌ **False.** LOF can exceed 1.
- **B)** LOF ≈ 1 → strong outlier — ❌ **False.** Reversed.
- **C)** LOF < 0 → inlier — ❌ **False.** LOF is non-negative.
- **D)** LOF ≈ 1 → inlier (homogeneous density); LOF ≫ 1 → outlier — ✅ **True.** Ratio of neighbours' densities to the point's own density.

**Answer: D.** Use lof(data, k); compare values to ~1.

---

### Q205 · Frequent Itemsets

Confidence of the rule X ⇒ Y is:

- **A)** support(X ∪ Y) / support(X) — ✅ **True.** Among transactions with X, the fraction also containing Y.
- **B)** support(X ∪ Y) / |D| — ❌ **False.** That is the rule's support/frequency.
- **C)** support(X) / support(Y) — ❌ **False.** Not a defined rule metric.
- **D)** support(X ∪ Y) / support(Y) — ❌ **False.** Wrong denominator (that is closer to a 'recall').

**Answer: A.** Use confidence(DB, X, Y).

---

### Q206 · Density-Based

Run DBSCAN with ε = 3 and MinPts = 2 on the points [[7, 5], [8, 6], [5, 0], [4, 7], [4, 6], [1, 7], [7, 6]]. What is the type of point index 4 = [4, 6]?

- **A)** Border — ❌ **False.** it is not a border point (< MinPts within ε, but within ε of a core point).
- **B)** Noise — ❌ **False.** it is not a noise point (neither core nor within ε of a core point).
- **C)** Core — ✅ **True.** it is a core point (≥ MinPts neighbours within ε, incl. itself).
- **D)** Cluster centroid — ❌ **False.** DBSCAN has no centroids; points are core/border/noise.

**Answer: C.** Use dbscan(data, eps, minpts) → (labels, types).

---

### Q207 · Frequent Itemsets

For the database below, what is the **confidence of {BREAD} ⇒ {EGGS}**?

| TID | Items |
| --- | --- |
| 1 | BREAD, BUTTER, EGGS, MILK |
| 2 | BUTTER, EGGS |
| 3 | BREAD, BUTTER, MILK |
| 4 | BREAD, EGGS |
| 5 | BUTTER, EGGS, MILK |
| 6 | BREAD, BUTTER, MILK |
| 7 | BREAD, BUTTER |
| 8 | BREAD, BUTTER, EGGS, MILK |
| 9 | BREAD, EGGS |
| 10 | BREAD, BUTTER, EGGS, MILK |
| 11 | BREAD, BUTTER |
| 12 | BUTTER, MILK |

- **A)** 0.952 — ❌ **False.** this is the lift, a different metric.
- **B)** 0.417 — ❌ **False.** this is the rule's support/frequency support(A∪B)/|D|.
- **C)** 0.714 — ❌ **False.** this is support(A∪B)/support(B) — wrong denominator.
- **D)** 0.556 — ✅ **True.** this is confidence = support(A∪B)/support(A).

**Answer: D.** Use confidence(DB, {'BREAD'}, {'EGGS'}).

---

### Q208 · EM / GMM

What is the value of the 1-D Normal density N(x=1 | μ=1, σ²=2)?

- **A)** 1.0 — ❌ **False.** this is only the exponential term, missing the 1/√(2πσ²) normaliser.
- **B)** 0.2821 — ✅ **True.** this is the Normal pdf N(x|μ,σ²).
- **C)** 0.1995 — ❌ **False.** this is using σ (std) where σ² (variance) was required.
- **D)** 0.1411 — ❌ **False.** this is half the correct density (arithmetic slip).

**Answer: B.** Use gauss(x, mu, var) (variance, not std).

---

### Q209 · Data Representation

For u = [5, -2, -1] and v = [-4, 5, 2], which value is the **Manhattan** distance d(u,v)?

- **A)** 11.79 — ❌ **False.** this is the Euclidean distance, eucd(u,v).
- **B)** 9 — ❌ **False.** this is the Suprema/Chebyshev distance, supd(u,v).
- **C)** 19 — ✅ **True.** this is the Manhattan distance, mand(u,v).
- **D)** 10.32 — ❌ **False.** this is the Minkowski p=3 distance, mink(u,v,3).

**Answer: C.** Use mand(u,v).

---

### Q210 · Partitioning (k-Means)

Run k-means on [[3, 2], [3, 0], [1, 0], [8, 11], [8, 10], [8, 11]] with initial prototypes [[3, 2], [8, 11]]. What are the **final cluster labels** (in order)?

- **A)** [0, 1, 0, 1, 0, 1] — ❌ **False.** this is an alternating labelling (not distance-based).
- **B)** [1, 1, 1, 0, 0, 0] — ❌ **False.** this is the same split with labels swapped (not what these inits give).
- **C)** [0, 0, 0, 1, 1, 1] — ✅ **True.** this is the converged k-means assignment.
- **D)** [0, 0, 0, 0, 0, 0] — ❌ **False.** this is everything in one cluster (not a 2-means result).

**Answer: C.** Use kmeans(data, init) → (labels, cents).

---

### Q211 · Partitioning (k-Means)

Run k-means on [[1, 1], [0, 2], [0, 2], [1, 0], [11, 11], [10, 11], [9, 9], [8, 9]] with initial prototypes [[1, 1], [10, 11]]. What is the **final SSE**?

- **A)** 25.5 — ❌ **False.** not the converged SSE.
- **B)** 17.75 — ❌ **False.** not the converged SSE.
- **C)** 12.75 — ✅ **True.** this is the converged SSE.
- **D)** 9.75 — ❌ **False.** not the converged SSE.

**Answer: C.** Use kmeans(data, init) then sse(data, labels, cents).

---

### Q212 · Data Representation

The Simple Matching Coefficient (SMC) is appropriate for ___ binary variables, whereas Jaccard suits ___ ones.

- **A)** asymmetric ; symmetric — ❌ **False.** Reversed.
- **B)** ordinal ; nominal — ❌ **False.** Both coefficients are for binary data.
- **C)** symmetric ; asymmetric — ✅ **True.** SMC counts 0-0 matches (symmetric); Jaccard drops them (asymmetric).
- **D)** continuous ; discrete — ❌ **False.** Both are for binary/categorical data.

**Answer: C.** Use smc(u,v) and jaccard(u,v); contingency(u,v) gives (n11,n10,n01,n00).

---

### Q213 · Hierarchical

For the distance matrix below, what is the **root (final) merge height under Complete-Linkage**?

```
[0, 4, 4, 6]
[4, 0, 7, 9]
[4, 7, 0, 1]
[6, 9, 1, 0]
```

- **A)** 10 — ❌ **False.** this is an off value (recompute).
- **B)** 4 — ❌ **False.** this is the single-linkage root height.
- **C)** 6.5 — ❌ **False.** this is the average-linkage root height.
- **D)** 9 — ✅ **True.** this is the complete-linkage root height.

**Answer: D.** Use ahc(D, 'complete'); the last merge's height is the root.

---

### Q214 · Partitioning (k-Means)

Run k-means on [[0, 0], [3, 2], [2, 3], [10, 9], [8, 11], [10, 9]] with initial prototypes [[0, 0], [10, 9]]. What are the **final cluster labels** (in order)?

- **A)** [0, 1, 0, 1, 0, 1] — ❌ **False.** this is an alternating labelling (not distance-based).
- **B)** [0, 0, 0, 1, 1, 1] — ✅ **True.** this is the converged k-means assignment.
- **C)** [1, 1, 1, 0, 0, 0] — ❌ **False.** this is the same split with labels swapped (not what these inits give).
- **D)** [0, 0, 0, 0, 0, 0] — ❌ **False.** this is everything in one cluster (not a 2-means result).

**Answer: B.** Use kmeans(data, init) → (labels, cents).

---

### Q215 · Frequent Itemsets

For the database below, what is the **lift of {DIAPERS} ⇒ {MILK}**?

| TID | Items |
| --- | --- |
| 1 | DIAPERS, MILK |
| 2 | BREAD, BUTTER, DIAPERS, MILK |
| 3 | BREAD, BUTTER |
| 4 | BREAD, DIAPERS |
| 5 | BUTTER, DIAPERS, MILK |
| 6 | BUTTER, MILK |
| 7 | BREAD, MILK |
| 8 | BREAD, BUTTER, DIAPERS |
| 9 | BUTTER, DIAPERS |
| 10 | BREAD, BUTTER, DIAPERS, MILK |
| 11 | BREAD, BUTTER, DIAPERS, MILK |
| 12 | BREAD, BUTTER, DIAPERS |

- **A)** 0.417 — ❌ **False.** this is the rule support/frequency support(A∪B)/|D|.
- **B)** 0.952 — ✅ **True.** this is the lift = conf(A⇒B)/f(B).
- **C)** 0.556 — ❌ **False.** this is the confidence (forgot to divide by f(B)).
- **D)** 0.583 — ❌ **False.** this is the frequency f(B) of the consequent.

**Answer: B.** Use lift(DB, {'DIAPERS'}, {'MILK'}) = confidence / f(consequent).

---

### Q216 · Partitioning (k-Means)

Run k-means on [[0, 0], [1, 2], [1, 1], [1, 2], [9, 11], [9, 9], [9, 9], [8, 11]] (init [[0, 0], [9, 9]]), then compute the **Silhouette Width Criterion (SWC)**. Which value is correct?

- **A)** 0.879 — ✅ **True.** this is the SWC of this partition.
- **B)** 1.238 — ❌ **False.** this is impossible — the SWC lies in [−1, +1].
- **C)** 0.779 — ❌ **False.** this is a slightly off value (recompute).
- **D)** 0.979 — ❌ **False.** this is a slightly off value (recompute).

**Answer: A.** Use silhouette(data, labels); SWC ∈ [−1, +1].

---

### Q217 · Introduction

Which is a specialised DM task mentioned beyond the core ones?

- **A)** Matrix inversion — ❌ **False.** A linear-algebra routine.
- **B)** Compiling code — ❌ **False.** Unrelated.
- **C)** Sorting an array — ❌ **False.** A generic algorithm, not a DM task.
- **D)** Recommendation / community detection / sentiment analysis — ✅ **True.** These are listed as specialised tasks.

**Answer: D.** Short justification: recommendation, link/sentiment analysis are specialised DM tasks.

---

### Q218 · Data Representation

For u = [2, -1, 7, 2] and v = [8, 1, 1, 8], which value is the **Euclidean** distance d(u,v)?

- **A)** 8.69 — ❌ **False.** this is the Minkowski p=3 distance, mink(u,v,3).
- **B)** 20 — ❌ **False.** this is the Manhattan distance, mand(u,v).
- **C)** 6 — ❌ **False.** this is the Suprema/Chebyshev distance, supd(u,v).
- **D)** 10.58 — ✅ **True.** this is the Euclidean distance, eucd(u,v).

**Answer: D.** Use eucd(u,v).

---

### Q219 · Data Representation

Re-scaling or z-score standardisation is used mainly to:

- **A)** Guarantee the triangle inequality — ❌ **False.** Distances already satisfy it; scaling is unrelated.
- **B)** Remove the need for a distance function — ❌ **False.** A distance is still required.
- **C)** Remove the implicit pre-weighting by which wide-range variables dominate distances — ✅ **True.** Different units/ranges otherwise dominate Minkowski/Mahalanobis distances.
- **D)** Make data categorical — ❌ **False.** It keeps data numeric.

**Answer: C.** Use zscore(col) or rescale(col).

---

### Q220 · Partitioning (k-Means)

Run k-means on [[2, 1], [2, 1], [1, 2], [3, 2], [11, 11], [10, 10], [8, 10], [10, 10]] with initial prototypes [[2, 1], [10, 10]]. What is the **final SSE**?

- **A)** 3.5 — ❌ **False.** not the converged SSE.
- **B)** 8.5 — ✅ **True.** this is the converged SSE.
- **C)** 11.5 — ❌ **False.** not the converged SSE.
- **D)** 17.0 — ❌ **False.** not the converged SSE.

**Answer: B.** Use kmeans(data, init) then sse(data, labels, cents).

---

### Q221 · Partitioning (k-Means)

Run k-means on [[2, 0], [1, 1], [0, 0], [2, 0], [11, 11], [9, 9], [8, 9], [8, 9]] with initial prototypes [[2, 0], [9, 9]]. What is the **final SSE**?

- **A)** 10.5 — ❌ **False.** not the converged SSE.
- **B)** 17.5 — ❌ **False.** not the converged SSE.
- **C)** 25.0 — ❌ **False.** not the converged SSE.
- **D)** 12.5 — ✅ **True.** this is the converged SSE.

**Answer: D.** Use kmeans(data, init) then sse(data, labels, cents).

---

### Q222 · Hierarchical

Typical complexity of agglomerative hierarchical clustering:

- **A)** O(2^N) time — ❌ **False.** Exponential — incorrect.
- **B)** O(N) time and O(1) space — ❌ **False.** Far too low.
- **C)** O(N log N) always — ❌ **False.** Only achievable for some linkages.
- **D)** O(N²) memory and about O(N³) time — ✅ **True.** Stores the N×N proximity matrix; N merges each search/update it.

**Answer: D.** Short justification: proximity matrix → O(N²) space, ~O(N³) time.

---

### Q223 · Probability & Density

For the sample [8, 7, 9, 6, 6], what is the **sample variance** (dividing by n−1)?

- **A)** 7.2 — ❌ **False.** this is the mean, not a variance.
- **B)** 1.7 — ✅ **True.** this is the sample variance (÷ n−1).
- **C)** 1.304 — ❌ **False.** this is the standard deviation (√variance).
- **D)** 1.36 — ❌ **False.** this is the population/MLE variance (÷ n).

**Answer: B.** Use var(v) (sample=True); the MLE variance is var(v, sample=False).

---

### Q224 · Hierarchical

Given the distance matrix (0-based indices), which pair merges **first** under Single-Linkage?

```
[0, 9, 5, 7, 3]
[9, 0, 4, 4, 7]
[5, 4, 0, 12, 11]
[7, 4, 12, 0, 4]
[3, 7, 11, 4, 0]
```

- **A)** objects 0 and 3 (d=7) — ❌ **False.** their distance 7 is not the minimum.
- **B)** objects 1 and 2 (d=4) — ❌ **False.** their distance 4 is not the minimum.
- **C)** objects 2 and 3 (d=12) — ❌ **False.** their distance 12 is not the minimum.
- **D)** objects 0 and 4 (d=3) — ✅ **True.** this is the smallest distance, so they merge first.

**Answer: D.** Use ahc(D,'single'); the closest pair always merges first.

---

### Q225 · Density-Based

Run DBSCAN with ε = 3 and MinPts = 3 on [[9, 1], [10, 7], [4, 0], [7, 0], [7, 9], [10, 2], [2, 5], [10, 4]]. **How many clusters** result (noise excluded)?

- **A)** 1 — ✅ **True.** DBSCAN forms 1 cluster(s) (2 noise point(s)).
- **B)** 0 — ❌ **False.** DBSCAN does not form 0 clusters here.
- **C)** 2 — ❌ **False.** DBSCAN does not form 2 clusters here.
- **D)** 8 — ❌ **False.** DBSCAN does not form 8 clusters here.

**Answer: A.** Use dbscan(data, eps, minpts); count distinct non-zero labels.

---

### Q226 · Hierarchical

Given the distance matrix (0-based indices), which pair merges **first** under Single-Linkage?

```
[0, 3, 5, 11, 10]
[3, 0, 8, 10, 3]
[5, 8, 0, 9, 12]
[11, 10, 9, 0, 5]
[10, 3, 12, 5, 0]
```

- **A)** objects 2 and 3 (d=9) — ❌ **False.** their distance 9 is not the minimum.
- **B)** objects 0 and 1 (d=3) — ✅ **True.** this is the smallest distance, so they merge first.
- **C)** objects 1 and 4 (d=3) — ❌ **False.** their distance 3 is not the minimum.
- **D)** objects 2 and 4 (d=12) — ❌ **False.** their distance 12 is not the minimum.

**Answer: B.** Use ahc(D,'single'); the closest pair always merges first.

---

### Q227 · Partitioning (k-Means)

Run k-means on [[1, 3], [1, 0], [1, 1], [11, 9], [10, 10], [10, 10]] with initial prototypes [[1, 3], [11, 9]]. What are the **final cluster labels** (in order)?

- **A)** [0, 0, 0, 0, 0, 0] — ❌ **False.** this is everything in one cluster (not a 2-means result).
- **B)** [0, 1, 0, 1, 0, 1] — ❌ **False.** this is an alternating labelling (not distance-based).
- **C)** [0, 0, 0, 1, 1, 1] — ✅ **True.** this is the converged k-means assignment.
- **D)** [1, 1, 1, 0, 0, 0] — ❌ **False.** this is the same split with labels swapped (not what these inits give).

**Answer: C.** Use kmeans(data, init) → (labels, cents).

---

### Q228 · Partitioning (k-Means)

Run k-means on [[3, 2], [1, 1], [0, 1], [1, 1], [10, 11], [10, 9], [9, 11], [10, 11]] (init [[3, 2], [10, 9]]), then compute the **Silhouette Width Criterion (SWC)**. Which value is correct?

- **A)** 0.879 — ✅ **True.** this is the SWC of this partition.
- **B)** 0.979 — ❌ **False.** this is a slightly off value (recompute).
- **C)** 0.679 — ❌ **False.** this is a slightly off value (recompute).
- **D)** 1.399 — ❌ **False.** this is impossible — the SWC lies in [−1, +1].

**Answer: A.** Use silhouette(data, labels); SWC ∈ [−1, +1].

---

### Q229 · Partitioning (k-Means)

Run k-means on [[2, 0], [0, 1], [0, 0], [3, 0], [9, 8], [10, 8], [11, 8], [9, 9]] (init [[2, 0], [10, 8]]), then compute the **Silhouette Width Criterion (SWC)**. Which value is correct?

- **A)** 0.85 — ✅ **True.** this is the SWC of this partition.
- **B)** 1.639 — ❌ **False.** this is impossible — the SWC lies in [−1, +1].
- **C)** 0.75 — ❌ **False.** this is a slightly off value (recompute).
- **D)** 1 — ❌ **False.** this is a slightly off value (recompute).

**Answer: A.** Use silhouette(data, labels); SWC ∈ [−1, +1].

---

### Q230 · Data Representation

Cosine similarity is the preferred proximity for:

- **A)** Ordinal survey scales — ❌ **False.** Use order-aware encodings, not cosine.
- **B)** Sparse, asymmetric numeric data such as bag-of-words text — ✅ **True.** Cosine ignores zeros (absent terms) and compares direction, not magnitude.
- **C)** A single binary variable — ❌ **False.** Cosine is for vectors, not one bit.
- **D)** Time-series needing alignment — ❌ **False.** Use elastic measures like DTW.

**Answer: B.** Use cosine(u,v).

---

### Q231 · Hierarchical

Given the distance matrix (0-based indices), which pair merges **first** under Single-Linkage?

```
[0, 2, 9, 12]
[2, 0, 3, 1]
[9, 3, 0, 5]
[12, 1, 5, 0]
```

- **A)** objects 1 and 3 (d=1) — ✅ **True.** this is the smallest distance, so they merge first.
- **B)** objects 2 and 3 (d=5) — ❌ **False.** their distance 5 is not the minimum.
- **C)** objects 0 and 1 (d=2) — ❌ **False.** their distance 2 is not the minimum.
- **D)** objects 0 and 3 (d=12) — ❌ **False.** their distance 12 is not the minimum.

**Answer: A.** Use ahc(D,'single'); the closest pair always merges first.

---

### Q232 · EM / GMM

What is the value of the 1-D Normal density N(x=0 | μ=1, σ²=4)?

- **A)** 0.0967 — ❌ **False.** this is using σ (std) where σ² (variance) was required.
- **B)** 0.8825 — ❌ **False.** this is only the exponential term, missing the 1/√(2πσ²) normaliser.
- **C)** 0.088 — ❌ **False.** this is half the correct density (arithmetic slip).
- **D)** 0.176 — ✅ **True.** this is the Normal pdf N(x|μ,σ²).

**Answer: D.** Use gauss(x, mu, var) (variance, not std).

---

### Q233 · Data Representation

For u = [8, -1, 2] and v = [1, 0, 7], which value is the **Manhattan** distance d(u,v)?

- **A)** 7 — ❌ **False.** this is the Suprema/Chebyshev distance, supd(u,v).
- **B)** 13 — ✅ **True.** this is the Manhattan distance, mand(u,v).
- **C)** 7.77 — ❌ **False.** this is the Minkowski p=3 distance, mink(u,v,3).
- **D)** 8.66 — ❌ **False.** this is the Euclidean distance, eucd(u,v).

**Answer: B.** Use mand(u,v).

---

### Q234 · Data Representation

For u = [5, 2, 0, 3, 1] and v = [2, 0, 4, 1, 5], which value is the **cosine similarity** cos(u,v)?

- **A)** 0.425 — ✅ **True.** this is the cosine similarity.
- **B)** 0.01 — ❌ **False.** this is the inner product over ||u||²·||v||² (missing the square root).
- **C)** -0.526 — ❌ **False.** this is the Pearson correlation, a different measure.
- **D)** 18.0 — ❌ **False.** this is just the inner product <u,v> (not normalised).

**Answer: A.** Use cosine(u,v) = <u,v> / (||u||·||v||).

---

### Q235 · Partitioning (k-Means)

k-means is guaranteed to find:

- **A)** The correct k automatically — ❌ **False.** k must be supplied.
- **B)** Only a local optimum (depends on initialisation) — ✅ **True.** Different seeds give different partitions; multiple restarts mitigate this.
- **C)** The global optimum always — ❌ **False.** Not guaranteed.
- **D)** A medoid-based solution — ❌ **False.** k-means uses means, not medoids.

**Answer: B.** Short justification: k-means → local optimum; rerun with several inits.

---

### Q236 · Introduction

Clustering is sometimes called:

- **A)** Hypothesis testing — ❌ **False.** That is classical confirmatory statistics.
- **B)** Dimensionality reduction — ❌ **False.** That maps to fewer features, a different task.
- **C)** Unsupervised classification — ✅ **True.** It groups similar observations without using labels.
- **D)** Supervised regression — ❌ **False.** Regression is supervised and predicts numbers.

**Answer: C.** Short justification: clustering = unsupervised classification.

---

### Q237 · Probability & Density

For the sample [5, 1, 4, 8, 5], what is the **sample variance** (dividing by n−1)?

- **A)** 2.51 — ❌ **False.** this is the standard deviation (√variance).
- **B)** 6.3 — ✅ **True.** this is the sample variance (÷ n−1).
- **C)** 4.6 — ❌ **False.** this is the mean, not a variance.
- **D)** 5.04 — ❌ **False.** this is the population/MLE variance (÷ n).

**Answer: B.** Use var(v) (sample=True); the MLE variance is var(v, sample=False).

---

### Q238 · Frequent Itemsets

For the database below, what is the **lift of {BREAD} ⇒ {EGGS}**?

| TID | Items |
| --- | --- |
| 1 | BUTTER, EGGS, MILK |
| 2 | BUTTER, EGGS, MILK |
| 3 | BUTTER, EGGS, MILK |
| 4 | BREAD, BUTTER, EGGS, MILK |
| 5 | BREAD, BUTTER, EGGS, MILK |
| 6 | BUTTER, EGGS |
| 7 | BREAD, BUTTER |
| 8 | BREAD, BUTTER, MILK |
| 9 | EGGS, MILK |
| 10 | BREAD, BUTTER, EGGS |
| 11 | BREAD, BUTTER, EGGS, MILK |
| 12 | BREAD, BUTTER, EGGS, MILK |

- **A)** 0.833 — ❌ **False.** this is the frequency f(B) of the consequent.
- **B)** 0.714 — ❌ **False.** this is the confidence (forgot to divide by f(B)).
- **C)** 0.857 — ✅ **True.** this is the lift = conf(A⇒B)/f(B).
- **D)** 0.417 — ❌ **False.** this is the rule support/frequency support(A∪B)/|D|.

**Answer: C.** Use lift(DB, {'BREAD'}, {'EGGS'}) = confidence / f(consequent).

---

### Q239 · Density-Based

A BORDER point in DBSCAN:

- **A)** Is a dense core point on the edge — ❌ **False.** Border points are not core.
- **B)** Has < MinPts within ε but lies within ε of a core point — ✅ **True.** It is attached to a core point's cluster.
- **C)** Has more neighbours than a core point — ❌ **False.** Then it would be core.
- **D)** Is always labelled noise — ❌ **False.** Only if not reachable from a core point.

**Answer: B.** Use dbscan(...); 'border' in the returned types.

---

### Q240 · Density-Based

Why do clusters of VARYING density challenge DBSCAN?

- **A)** The triangle inequality fails — ❌ **False.** Distances still satisfy it.
- **B)** Centroids cannot be computed — ❌ **False.** DBSCAN uses no centroids.
- **C)** It needs labelled data — ❌ **False.** DBSCAN is unsupervised.
- **D)** A single global (ε, MinPts) cannot fit both dense and sparse clusters — ✅ **True.** Tuning for one density misses the other; HDBSCAN* addresses this.

**Answer: D.** Short justification: one global ε can't fit multiple densities → HDBSCAN*.

---

### Q241 · Density-Based

Run DBSCAN with ε = 3 and MinPts = 2 on [[3, 3], [9, 11], [4, 11], [5, 4], [1, 10], [6, 0], [10, 8], [2, 9]]. **How many clusters** result (noise excluded)?

- **A)** 3 — ❌ **False.** DBSCAN does not form 3 clusters here.
- **B)** 1 — ❌ **False.** DBSCAN does not form 1 clusters here.
- **C)** 2 — ✅ **True.** DBSCAN forms 2 cluster(s) (3 noise point(s)).
- **D)** 8 — ❌ **False.** DBSCAN does not form 8 clusters here.

**Answer: C.** Use dbscan(data, eps, minpts); count distinct non-zero labels.

---

### Q242 · Data Representation

For u = [2, 2, 3, 4] and v = [-2, 8, 8, 5], which value is the **Manhattan** distance d(u,v)?

- **A)** 8.83 — ❌ **False.** this is the Euclidean distance, eucd(u,v).
- **B)** 6 — ❌ **False.** this is the Suprema/Chebyshev distance, supd(u,v).
- **C)** 16 — ✅ **True.** this is the Manhattan distance, mand(u,v).
- **D)** 7.4 — ❌ **False.** this is the Minkowski p=3 distance, mink(u,v,3).

**Answer: C.** Use mand(u,v).

---

### Q243 · Introduction

According to Fayyad et al. (1996), KDD is best described as:

- **A)** The physical storage of large datasets — ❌ **False.** That is data management, not knowledge discovery.
- **B)** A supervised method that always needs labelled data — ❌ **False.** KDD spans supervised and unsupervised methods.
- **C)** A single SQL query that retrieves records from a database — ❌ **False.** KDD is a multi-step process, not a query.
- **D)** The nontrivial process of identifying valid, novel, potentially useful and ultimately understandable patterns in data — ✅ **True.** This is the textbook KDD definition; 'nontrivial' rules out plain search/aggregation.

**Answer: D.** Short justification: KDD = process of finding valid/novel/useful/understandable patterns.

---

### Q244 · Probability & Density

A test has sensitivity 0.99, specificity 0.95; prevalence P(D)=0.01. What is **P(D | positive)**?

- **A)** 0.99 — ❌ **False.** this is the sensitivity P(+|D) (likelihood), not the posterior.
- **B)** 0.833 — ❌ **False.** this is the complement 1−P(D|+).
- **C)** 0.167 — ✅ **True.** this is the posterior P(D|+) by Bayes' rule.
- **D)** 0.01 — ❌ **False.** this is the prior prevalence P(D), not the posterior.

**Answer: C.** Use bayes(likelihood, prior, evidence) with evidence = sens·prev + (1−spec)·(1−prev).

---

### Q245 · Data Representation

For binary x1 = [1, 1, 0, 0, 0, 1, 0, 1, 1, 0] and x2 = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0], which value is the **Jaccard** coefficient?

- **A)** 0.4 — ❌ **False.** this is only n11/n (it omits the other agreements/structure).
- **B)** 0.2 — ❌ **False.** this is the fraction of disagreements (n10+n01)/n.
- **C)** 0.667 — ✅ **True.** this is the Jaccard = n11/(n11+n10+n01).
- **D)** 0.8 — ❌ **False.** this is the SMC = (n11+n00)/n.

**Answer: C.** Use 0.667; contingency(x1,x2)=(n11,n10,n01,n00)=(4,1,1,4).

---

### Q246 · Outlier Detection

The simple kNN outlier score of a point is:

- **A)** Its distance to the k-th nearest neighbour — ✅ **True.** Weighted-kNN instead averages the 1..k NN distances.
- **B)** Its Pearson correlation — ❌ **False.** Unrelated.
- **C)** Its cluster label — ❌ **False.** kNN outlier gives a score, not a label.
- **D)** The number of clusters — ❌ **False.** Unrelated.

**Answer: A.** Use knn_outlier(data, k); weighted = wknn_outlier(data, k).

---

### Q247 · Partitioning (k-Means)

Run k-means on [[2, 1], [0, 2], [0, 2], [0, 0], [10, 9], [11, 11], [11, 8], [8, 11]] (init [[2, 1], [11, 11]]), then compute the **Silhouette Width Criterion (SWC)**. Which value is correct?

- **A)** 0.922 — ❌ **False.** this is a slightly off value (recompute).
- **B)** 0.822 — ✅ **True.** this is the SWC of this partition.
- **C)** 0.722 — ❌ **False.** this is a slightly off value (recompute).
- **D)** 1.569 — ❌ **False.** this is impossible — the SWC lies in [−1, +1].

**Answer: B.** Use silhouette(data, labels); SWC ∈ [−1, +1].

---

### Q248 · Hierarchical

Single-linkage defines the distance between two clusters as the:

- **A)** Average pairwise distance — ❌ **False.** That is average-linkage (UPGMA).
- **B)** Increase in within-cluster SSE — ❌ **False.** That is Ward's method.
- **C)** Minimum distance between any two of their points — ✅ **True.** MIN linkage → chaining, detects arbitrary shapes, noise-sensitive.
- **D)** Maximum pairwise distance — ❌ **False.** That is complete-linkage.

**Answer: C.** Use ahc(D, 'single').

---

### Q249 · Hierarchical

Agglomerative hierarchical clustering is 'relational' because it:

- **A)** Can run from a (dis)similarity matrix alone, without the original vectors — ✅ **True.** Only pairwise distances are needed.
- **B)** Requires a relational SQL database — ❌ **False.** Unrelated to databases.
- **C)** Works only on graphs — ❌ **False.** It works on any distance matrix.
- **D)** Needs class labels — ❌ **False.** It is unsupervised.

**Answer: A.** Use ahc(D, ...) — input is the distance matrix D.

---

### Q250 · EM / GMM

EM fits a GMM by:

- **A)** Maximising the silhouette — ❌ **False.** That is a validation index.
- **B)** Minimising the SSE — ❌ **False.** That is k-means' objective.
- **C)** Maximising support — ❌ **False.** That is association-rule mining.
- **D)** Maximising the (log-)likelihood of the data (MLE) — ✅ **True.** Log turns the product over points into a sum.

**Answer: D.** Short justification: EM is a Maximum-Likelihood procedure.

---
