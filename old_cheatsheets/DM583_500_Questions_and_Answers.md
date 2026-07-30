# DM583 Data Mining — 500 Sample MCQ Questions & Answers

Each question gives a scenario, then several statements; for each statement decide **True** or **False**. Numeric values were computed with the course Python toolkit; conceptual statements cite the relevant lecture in brackets. The correct answer and a short justification follow every statement.

**Contents:** 500 questions, 2500 statements (1338 True / 1162 False). Topic breakdown: Data Representation (122), Partitioning (k-Means) (71), 1-D Dataset (mixed) (66), Probability & Density (62), EM / GMM (51), Hierarchical (47), Frequent Itemsets (45), Outlier Detection (36).

---

## Question 1 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0096 and 0.0146, with priors π_C1 = 0.4 and π_C2 = 0.6. Which statements are correct?

**1.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**2.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**3.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

**4.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

**5.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

---

## Question 2 · Data Representation

Two objects are described by 8 binary (asymmetric/symmetric) variables: x1 = [0, 0, 1, 0, 0, 0, 1, 0] and x2 = [0, 0, 1, 1, 1, 1, 1, 0]. Which statements are correct?

**1.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.775.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.625, not 0.775.

**2.** The count of disagreements n10 + n01 is approximately 4.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 3, not 4.

**3.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**4.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**5.** The count of 1–1 matches n11 is approximately 2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 2.

---

## Question 3 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 6). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, DIAPERS, EGGS |
| 2 | BEER, BUTTER, DIAPERS |
| 3 | DIAPERS, EGGS, MILK |
| 4 | BEER, BUTTER, DIAPERS, EGGS, JAM, MILK |
| 5 | BEER, BUTTER, DIAPERS, EGGS, JAM, MILK |
| 6 | BUTTER, DIAPERS, EGGS |
| 7 | BEER, BUTTER, DIAPERS, EGGS, JAM, MILK |
| 8 | BEER, BUTTER, DIAPERS, EGGS, MILK |
| 9 | BEER, BUTTER, DIAPERS, EGGS, MILK |
| 10 | BEER, BUTTER, DIAPERS, EGGS, JAM, MILK |

**1.** The lift of the rule {MILK} ⇒ {EGGS} is approximately 1.311.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 1.111, not 1.311.

**2.** The support count of the itemset {MILK, EGGS} is approximately 7.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 7.

**3.** With n distinct items the candidate search space contains 2^n possible itemsets.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Each item is in or out, giving 2^n itemsets — hence Apriori pruning is essential.

**4.** The frequent itemset {DIAPERS} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

**5.** Confidence of X ⇒ Y is defined as support(X ∪ Y) / support(Y).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Confidence = support(X∪Y)/support(X) (divide by the antecedent's support).

---

## Question 4 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 5). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, BREAD, CRACKERS, JAM, MILK |
| 2 | BEER, JAM, MILK |
| 3 | BEER, BREAD, JAM, MILK |
| 4 | BEER, JAM, MILK |
| 5 | BREAD, CRACKERS |
| 6 | BEER, BREAD, CRACKERS, JAM, MILK |
| 7 | BEER, JAM, MILK |
| 8 | BEER, BREAD, JAM, MILK |
| 9 | BEER, BREAD, MILK |
| 10 | BEER, BREAD, CRACKERS, JAM, MILK |
| 11 | BREAD, CRACKERS, MILK |
| 12 | BEER, CRACKERS, MILK |

**1.** With n distinct items the candidate search space contains 2^n possible itemsets.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Each item is in or out, giving 2^n itemsets — hence Apriori pruning is essential.

**2.** Confidence of X ⇒ Y is defined as support(X ∪ Y) / support(Y).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Confidence = support(X∪Y)/support(X) (divide by the antecedent's support).

**3.** The support count of {BEER} is approximately 10.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 10.

**4.** The confidence of the rule {BREAD} ⇒ {MILK} is approximately 1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 0.875, not 1.

**5.** The support count of the itemset {BREAD, MILK} is approximately 7.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 7.

---

## Question 5 · Data Representation

Two objects are described by 10 binary (asymmetric/symmetric) variables: x1 = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] and x2 = [1, 0, 0, 0, 0, 0, 1, 1, 0, 1]. Which statements are correct?

**1.** The count of 1–1 matches n11 is approximately 2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 2.

**2.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**3.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**4.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**5.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.5.

---

## Question 6 · Data Representation

Two objects are described by 8 binary (asymmetric/symmetric) variables: x1 = [0, 1, 0, 1, 1, 1, 0, 1] and x2 = [0, 0, 0, 0, 1, 0, 0, 1]. Which statements are correct?

**1.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**2.** The count of disagreements n10 + n01 is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 3, not 6.

**3.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**4.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.625.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.625.

**5.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

---

## Question 7 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 4). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, BREAD, BUTTER, JAM |
| 2 | BUTTER, CRACKERS |
| 3 | BEER, BREAD, BUTTER, JAM |
| 4 | BEER, BREAD, CRACKERS, JAM |
| 5 | BEER, BUTTER, CRACKERS, JAM |
| 6 | BREAD, BUTTER |
| 7 | BEER, BREAD, BUTTER, CRACKERS, JAM |
| 8 | BEER, BREAD, BUTTER, CRACKERS, JAM |
| 9 | BEER, BUTTER, JAM |
| 10 | BEER, CRACKERS, JAM |
| 11 | BEER, BUTTER, CRACKERS, JAM |
| 12 | BEER, BREAD, BUTTER, CRACKERS, JAM |

**1.** The support count of {JAM} is approximately 10.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 10.

**2.** The confidence of the rule {BEER} ⇒ {BREAD} is approximately 0.75.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 0.6, not 0.75.

**3.** The lift of the rule {BEER} ⇒ {BREAD} is approximately 1.029.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 1.029.

**4.** The frequent itemset {JAM} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

**5.** The support count of the itemset {BEER, BREAD} is approximately 8.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 6, not 8.

---

## Question 8 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-28, -10, -7, 19, 26, 38, 74, 85}. Which statements are correct?

**1.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**2.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**3.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 24.62, σ̂² = (1/n)Σ(x−μ̂)² ≈ 1407.98.

**4.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**5.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [18, 3, 3, 11, 7, 12, 11, 7].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [18, 3, 3, 7, 7, 12, 11, 11], not [18, 3, 3, 11, 7, 12, 11, 7].

---

## Question 9 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 5). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, CRACKERS |
| 2 | BEER, BREAD, BUTTER, CRACKERS, JAM, MILK |
| 3 | BEER, BUTTER |
| 4 | JAM, MILK |
| 5 | BEER, BUTTER, CRACKERS, JAM, MILK |
| 6 | BEER, BREAD, CRACKERS, JAM |
| 7 | BUTTER, JAM, MILK |
| 8 | BEER, BUTTER, CRACKERS, JAM, MILK |
| 9 | BUTTER, CRACKERS, JAM, MILK |
| 10 | BREAD, BUTTER, CRACKERS, MILK |
| 11 | BEER, BREAD, BUTTER, JAM, MILK |
| 12 | BEER, BREAD, BUTTER, JAM, MILK |
| 13 | CRACKERS, MILK |
| 14 | BREAD, JAM, MILK |

**1.** By anti-monotonicity (downward closure), every subset of a frequent itemset is also frequent.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Apriori prunes any candidate having an infrequent subset before counting support.

**2.** The support count of the itemset {BUTTER, JAM} is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 7, not 6.

**3.** The support count of {MILK} is approximately 11.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 11.

**4.** The frequent itemset {BUTTER} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

**5.** With n distinct items the candidate search space contains 2^n possible itemsets.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Each item is in or out, giving 2^n itemsets — hence Apriori pruning is essential.

---

## Question 10 · Probability & Density

A test has sensitivity P(+|D)=0.9 and specificity 0.95; disease prevalence is P(D)=0.01. Also consider the sample [3, 3, 4, 4, 5]. Which statements are correct?

**1.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**2.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**3.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**4.** The sample mean of the listed sample is approximately 4.0.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 3.8, not 4.0.

**5.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

---

## Question 11 · Hierarchical

Consider 5 objects with the symmetric distance matrix (0-based indices):

```
[0, 11, 11, 4, 4]
[11, 0, 7, 7, 5]
[11, 7, 0, 12, 10]
[4, 7, 12, 0, 5]
[4, 5, 10, 5, 0]
```

Which statements are correct?

**1.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**2.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**3.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**4.** Using Single-Linkage, the height of the final (root) merge is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 7, not 6.

**5.** Using Complete-Linkage, the height of the final (root) merge is approximately 12.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 12.

---

## Question 12 · Data Representation

Two objects are described by 12 binary (asymmetric/symmetric) variables: x1 = [1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1] and x2 = [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1]. Which statements are correct?

**1.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**2.** The count of disagreements n10 + n01 is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 7, not 6.

**3.** The Jaccard coefficient Jc(x1,x2) is approximately 0.3.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.3.

**4.** The count of 1–1 matches n11 is approximately 0.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 3, not 0.

**5.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.617.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.417, not 0.617.

---

## Question 13 · Data Representation

Consider two records described by 4 numerical variables: u = [3, 8, -3, 6] and v = [5, -4, -4, -3]. Which statements are correct?

**1.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

**2.** The cosine similarity cos(u,v) is approximately 0.239.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ -0.261, not 0.239.

**3.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

**4.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

**5.** The Suprema (Chebyshev) distance d(u,v) is approximately 12.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 12.

---

## Question 14 · Probability & Density

A test has sensitivity P(+|D)=0.99 and specificity 0.99; disease prevalence is P(D)=0.01. Also consider the sample [1, 6, 4, 4, 6]. Which statements are correct?

**1.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**2.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**3.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**4.** The posterior P(D | +) by Bayes' rule is approximately 0.2.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.5, not 0.2.

**5.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

---

## Question 15 · Outlier Detection

Consider the 2-D points [[6, 0], [3, 4], [6, 5], [1, 4], [3, 6], [3, 5], [12, 12]]. Which statements are correct?

**1.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

**2.** The weighted KNN outlier score averages a point's distances to all its 1st…k-th nearest neighbours.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] Weighted-kNN aggregates (averages) the 1..k NN distances; plain kNN uses only the k-th.

**3.** Point 6 (the far point) receives the largest LOF, consistent with being an outlier.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF values ≈ [2.24, 0.95, 1.8, 1.14, 0.8, 1.24, 4.95]; the isolated point has LOF ≫ 1.

**4.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

**5.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

---

## Question 16 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[3, 1], [2, 2], [3, 0], [1, 0], [11, 9], [8, 10], [10, 9], [10, 10]] with initial prototypes [[3, 1], [8, 10]]. Which statements are correct?

**1.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**2.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**3.** The final cluster labels (one per point, in order) are [0, 0, 1, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 0, 1, 0, 1, 1, 1, 1].

**4.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**5.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.642.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.842, not 0.642.

---

## Question 17 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-28, -22, -7, 11, 46, 47, 51, 57}. Which statements are correct?

**1.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**2.** With ε = 15 and MinPts = 2, DBSCAN groups the data into the clusters [[-28, -22, -7], [46, 47, 51, 57]] with [11] as noise.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=15, MinPts=2) gives clusters [[-28, -22, -7], [46, 47, 51, 57]]; noise = [11].

**3.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [6, 6, 15, 18, 1, 1, 4, 6].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] The values are [6, 6, 15, 18, 1, 1, 4, 6].

**4.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**5.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

---

## Question 18 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-9, 23, 32, 34, 59, 61, 79}. Which statements are correct?

**1.** The MLE estimate of the mean μ is approximately 40.36.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 39.86, not 40.36.

**2.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**3.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**4.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 39.86, σ̂² = (1/n)Σ(x−μ̂)² ≈ 730.41.

**5.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

---

## Question 19 · Data Representation

Consider two records described by 5 numerical variables: u = [8, 0, 1, -3, 3] and v = [2, 8, -5, 6, -5]. Which statements are correct?

**1.** The Manhattan (city-block) distance d(u,v) is approximately 37.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 37.

**2.** The Euclidean distance d(u,v) is approximately 16.76.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 16.76.

**3.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

**4.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

**5.** The inner product <u,v> is approximately -21.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ -22, not -21.

---

## Question 20 · Data Representation

Consider two records described by 4 numerical variables: u = [0, -4, -5, 1] and v = [5, 0, 0, -2]. Which statements are correct?

**1.** The inner product <u,v> is approximately -2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ -2.

**2.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

**3.** The cosine similarity cos(u,v) is approximately -0.057.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ -0.057.

**4.** The Minkowski distance of order p=3 between u and v is approximately 6.99.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 6.99.

**5.** The Manhattan (city-block) distance d(u,v) is approximately 16.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 17, not 16.

---

## Question 21 · Data Representation

Two objects are described by 12 binary (asymmetric/symmetric) variables: x1 = [1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0] and x2 = [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1]. Which statements are correct?

**1.** The Jaccard coefficient Jc(x1,x2) is approximately 0.182.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.182.

**2.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**3.** The count of 1–1 matches n11 is approximately 2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 2.

**4.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**5.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.25.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.25.

---

## Question 22 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-5, 10, 58, 78, 81, 87}. Which statements are correct?

**1.** With ε = 15 and MinPts = 1, DBSCAN groups the data into the clusters [[-5, 10], [58], [78, 81, 87]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=15, MinPts=1) gives clusters [[-5, 10], [58], [78, 81, 87]]; no noise.

**2.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**3.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**4.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 51.5, σ̂² = (1/n)Σ(x−μ̂)² ≈ 1298.25.

**5.** The MLE estimate of the variance σ² (dividing by n) is approximately 1298.25.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 1298.25.

---

## Question 23 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 5). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BREAD, BUTTER, DIAPERS, JAM, MILK |
| 2 | EGGS, MILK |
| 3 | BREAD, DIAPERS, EGGS |
| 4 | BREAD, BUTTER, DIAPERS, JAM, MILK |
| 5 | BREAD, DIAPERS, MILK |
| 6 | BREAD, BUTTER, DIAPERS, EGGS, JAM, MILK |
| 7 | BREAD, BUTTER |
| 8 | BUTTER, DIAPERS, JAM |
| 9 | BREAD, BUTTER, DIAPERS, JAM |
| 10 | JAM, MILK |
| 11 | DIAPERS, EGGS, JAM |
| 12 | BREAD, BUTTER, JAM, MILK |

**1.** Apriori must scan the database to count the support of a candidate even when one of its subsets is already known to be infrequent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The prune step removes such candidates first, so no database scan is needed for them.

**2.** The frequent itemset {MILK} is maximal (it has no frequent superset).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Maximal = no superset reaches support 5.

**3.** The lift of the rule {BUTTER} ⇒ {DIAPERS} is approximately 1.221.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 1.071, not 1.221.

**4.** The support count of the itemset {BUTTER, DIAPERS} is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 5.

**5.** The frequent itemset {MILK} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

---

## Question 24 · Probability & Density

A test has sensitivity P(+|D)=0.95 and specificity 0.9; disease prevalence is P(D)=0.02. Also consider the sample [4, 2, 2, 5, 2]. Which statements are correct?

**1.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**2.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**3.** The sample mean of the listed sample is approximately 3.0.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 3.0.

**4.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**5.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

---

## Question 25 · Data Representation

Two objects are described by 10 binary (asymmetric/symmetric) variables: x1 = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1] and x2 = [1, 1, 0, 1, 0, 1, 1, 1, 1, 1]. Which statements are correct?

**1.** The Jaccard coefficient Jc(x1,x2) is approximately 0.5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.5.

**2.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.5.

**3.** The count of 1–1 matches n11 is approximately 7.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 5, not 7.

**4.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**5.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

---

## Question 26 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[3, 3], [1, 0], [2, 3], [1, 0], [11, 9], [8, 11], [10, 11], [8, 10]] with initial prototypes [[3, 3], [8, 11]]. Which statements are correct?

**1.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**2.** The final cluster labels (one per point, in order) are [1, 0, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [1, 0, 0, 0, 1, 1, 1, 1].

**3.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**4.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.64.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.79, not 0.64.

**5.** The final SSE (sum of squared errors) of the partition is approximately 21.25.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 21.25.

---

## Question 27 · Data Representation

Consider two records described by 5 numerical variables: u = [-2, -3, 1, 3, -2] and v = [1, -4, -2, 2, 7]. Which statements are correct?

**1.** The Suprema (Chebyshev) distance d(u,v) is approximately 8.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 9, not 8.

**2.** The Euclidean distance d(u,v) is approximately 10.05.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 10.05.

**3.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

**4.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

**5.** The Manhattan (city-block) distance d(u,v) is approximately 17.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 17.

---

## Question 28 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 4). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BUTTER, CRACKERS, DIAPERS, JAM |
| 2 | BREAD, BUTTER, CRACKERS, DIAPERS, JAM, MILK |
| 3 | CRACKERS, DIAPERS, JAM, MILK |
| 4 | BREAD, BUTTER, CRACKERS, DIAPERS, JAM, MILK |
| 5 | CRACKERS, DIAPERS, JAM, MILK |
| 6 | BREAD, BUTTER, CRACKERS, DIAPERS, JAM |
| 7 | BUTTER, CRACKERS, JAM |
| 8 | BREAD, BUTTER, CRACKERS, DIAPERS, JAM, MILK |
| 9 | BREAD, BUTTER, CRACKERS, DIAPERS, JAM, MILK |
| 10 | BREAD, BUTTER, DIAPERS |
| 11 | BREAD, BUTTER, CRACKERS, DIAPERS, JAM, MILK |
| 12 | DIAPERS, JAM |

**1.** By anti-monotonicity (downward closure), every subset of a frequent itemset is also frequent.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Apriori prunes any candidate having an infrequent subset before counting support.

**2.** Apriori must scan the database to count the support of a candidate even when one of its subsets is already known to be infrequent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The prune step removes such candidates first, so no database scan is needed for them.

**3.** With n distinct items the candidate search space contains 2^n possible itemsets.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Each item is in or out, giving 2^n itemsets — hence Apriori pruning is essential.

**4.** The support count of the itemset {BUTTER, BREAD} is approximately 10.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 7, not 10.

**5.** The lift of the rule {BUTTER} ⇒ {BREAD} is approximately 1.483.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 1.333, not 1.483.

---

## Question 29 · Data Representation

Consider two records described by 5 numerical variables: u = [1, 5, 9, -3, -2] and v = [1, -4, -2, -2, 3]. Which statements are correct?

**1.** The Euclidean distance d(u,v) is approximately 14.95.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 15.1, not 14.95.

**2.** The Manhattan (city-block) distance d(u,v) is approximately 28.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 26, not 28.

**3.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**4.** The cosine similarity cos(u,v) is approximately -0.879.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ -0.579, not -0.879.

**5.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

---

## Question 30 · Hierarchical

Consider 4 objects with the symmetric distance matrix (0-based indices):

```
[0, 1, 10, 8]
[1, 0, 7, 2]
[10, 7, 0, 4]
[8, 2, 4, 0]
```

Which statements are correct?

**1.** Using Single-Linkage, the height of the final (root) merge is approximately 4.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 4.

**2.** Using Complete-Linkage, the height of the final (root) merge is approximately 10.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 10.

**3.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

**4.** Using Single-Linkage, the first merge joins objects 0 and 1 at height 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (0,)+(1,) at 1.

**5.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

---

## Question 31 · Hierarchical

Consider 5 objects with the symmetric distance matrix (0-based indices):

```
[0, 12, 5, 5, 9]
[12, 0, 9, 7, 5]
[5, 9, 0, 12, 11]
[5, 7, 12, 0, 11]
[9, 5, 11, 11, 0]
```

Which statements are correct?

**1.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

**2.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**3.** Using Single-Linkage, the height of the final (root) merge is approximately 7.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 7.

**4.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**5.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

---

## Question 32 · Probability & Density

A test has sensitivity P(+|D)=0.99 and specificity 0.99; disease prevalence is P(D)=0.05. Also consider the sample [3, 2, 2, 3, 2]. Which statements are correct?

**1.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**2.** The sample variance (÷ n−1) of the listed sample is approximately 0.3.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 0.3.

**3.** The sample mean of the listed sample is approximately 2.4.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 2.4.

**4.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**5.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

---

## Question 33 · Data Representation

Consider two records described by 3 numerical variables: u = [1, 1, -3] and v = [-4, -1, 9]. Which statements are correct?

**1.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**2.** The inner product <u,v> is approximately -32.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ -32.

**3.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

**4.** The Minkowski distance of order p=3 between u and v is approximately 12.4.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 12.3, not 12.4.

**5.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

---

## Question 34 · Data Representation

Consider two records described by 4 numerical variables: u = [9, -1, 7, 9] and v = [-4, 7, -4, 2]. Which statements are correct?

**1.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

**2.** The Manhattan (city-block) distance d(u,v) is approximately 39.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 39.

**3.** The cosine similarity cos(u,v) is approximately -0.195.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ -0.395, not -0.195.

**4.** The inner product <u,v> is approximately -53.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ -53.

**5.** The Suprema (Chebyshev) distance d(u,v) is approximately 15.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 13, not 15.

---

## Question 35 · Data Representation

Two objects are described by 8 binary (asymmetric/symmetric) variables: x1 = [1, 1, 1, 0, 1, 1, 0, 1] and x2 = [1, 0, 1, 0, 1, 1, 1, 0]. Which statements are correct?

**1.** The count of disagreements n10 + n01 is approximately 3.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 3.

**2.** The count of 1–1 matches n11 is approximately 4.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 4.

**3.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.125.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.625, not 0.125.

**4.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**5.** The Jaccard coefficient Jc(x1,x2) is approximately 0.571.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.571.

---

## Question 36 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-10, 1, 32, 40, 41, 68, 107}. Which statements are correct?

**1.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**2.** The MLE estimate of the variance σ² (dividing by n) is approximately 1337.28.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 1336.98, not 1337.28.

**3.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**4.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 39.86, σ̂² = (1/n)Σ(x−μ̂)² ≈ 1336.98.

**5.** With ε = 20 and MinPts = 1, DBSCAN groups the data into the clusters [[-10, 1], [32, 40, 41], [68], [107]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=20, MinPts=1) gives clusters [[-10, 1], [32, 40, 41], [68], [107]]; no noise.

---

## Question 37 · Data Representation

Consider two records described by 3 numerical variables: u = [3, 7, -5] and v = [4, 5, 8]. Which statements are correct?

**1.** The cosine similarity cos(u,v) is approximately 0.075.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.075.

**2.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

**3.** The Manhattan (city-block) distance d(u,v) is approximately 13.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 16, not 13.

**4.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**5.** The Minkowski distance of order p=3 between u and v is approximately 13.02.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 13.02.

---

## Question 38 · Outlier Detection

Consider the 2-D points [[7, 4], [1, 2], [4, 2], [6, 0], [6, 3], [4, 7], [12, 12]]. Which statements are correct?

**1.** Point 6 (the far point) receives the largest LOF, consistent with being an outlier.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF values ≈ [1.01, 1.4, 0.86, 1.01, 1.17, 1.42, 2.7]; the isolated point has LOF ≫ 1.

**2.** The weighted KNN outlier score averages a point's distances to all its 1st…k-th nearest neighbours.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] Weighted-kNN aggregates (averages) the 1..k NN distances; plain kNN uses only the k-th.

**3.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

**4.** The unweighted KNN outlier scores with k=2 (per point, in order) are [3.61, 5.1, 2.83, 3.0, 2.24, 4.47, 10.43].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [3.61, 5.1, 2.83, 3.0, 2.24, 4.47, 9.43], not [3.61, 5.1, 2.83, 3.0, 2.24, 4.47, 10.43].

**5.** LOF is a global density score that compares each point's density to the dataset-wide average density.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] LOF is a LOCAL/relative score: density vs the point's own neighbours.

---

## Question 39 · Data Representation

Two objects are described by 10 binary (asymmetric/symmetric) variables: x1 = [0, 0, 1, 0, 1, 0, 0, 1, 0, 1] and x2 = [0, 0, 0, 0, 0, 1, 1, 0, 1, 0]. Which statements are correct?

**1.** The Jaccard coefficient Jc(x1,x2) is approximately 0.15.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.0, not 0.15.

**2.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.3.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.3.

**3.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**4.** The count of disagreements n10 + n01 is approximately 9.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 7, not 9.

**5.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

---

## Question 40 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[1, 3], [3, 0], [3, 2], [0, 1], [8, 9], [9, 9], [11, 11], [11, 9]] with initial prototypes [[1, 3], [9, 9]]. Which statements are correct?

**1.** The final SSE (sum of squared errors) of the partition is approximately 21.5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 21.5.

**2.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] The values are [0, 0, 0, 0, 1, 1, 1, 1].

**3.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**4.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**5.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

---

## Question 41 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-21, -7, -1, 29, 43, 51, 65, 80}. Which statements are correct?

**1.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**2.** The MLE estimate of the mean μ is approximately 29.88.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 29.88.

**3.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**4.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [15, 6, 6, 14, 8, 8, 14, 15].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [14, 6, 6, 14, 8, 8, 14, 15], not [15, 6, 6, 14, 8, 8, 14, 15].

**5.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 29.88, σ̂² = (1/n)Σ(x−μ̂)² ≈ 1158.36.

---

## Question 42 · Probability & Density

A test has sensitivity P(+|D)=0.99 and specificity 0.9; disease prevalence is P(D)=0.01. Also consider the sample [3, 4, 5, 3, 3]. Which statements are correct?

**1.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**2.** The posterior P(D | +) by Bayes' rule is approximately 0.091.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 0.091.

**3.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**4.** The sample mean of the listed sample is approximately 3.45.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 3.6, not 3.45.

**5.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

---

## Question 43 · Data Representation

Consider two records described by 5 numerical variables: u = [7, -2, -1, 4, 7] and v = [4, 4, -1, -1, 4]. Which statements are correct?

**1.** The inner product <u,v> is approximately 46.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 45, not 46.

**2.** The cosine similarity cos(u,v) is approximately 0.583.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.583.

**3.** The Manhattan (city-block) distance d(u,v) is approximately 17.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 17.

**4.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

**5.** The Suprema (Chebyshev) distance d(u,v) is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 6.

---

## Question 44 · Hierarchical

Consider 5 objects with the symmetric distance matrix (0-based indices):

```
[0, 2, 12, 1, 12]
[2, 0, 7, 7, 12]
[12, 7, 0, 10, 7]
[1, 7, 10, 0, 1]
[12, 12, 7, 1, 0]
```

Which statements are correct?

**1.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**2.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**3.** Using Complete-Linkage, the height of the final (root) merge is approximately 9.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 12, not 9.

**4.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

**5.** Using Single-Linkage, the first merge joins objects 0 and 3 at height 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (0,)+(3,) at 1.

---

## Question 45 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-21, 11, 24, 29, 67, 82, 86, 90}. Which statements are correct?

**1.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 46.0, σ̂² = (1/n)Σ(x−μ̂)² ≈ 1470.0.

**2.** The MLE estimate of the mean μ is approximately 46.0.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 46.0.

**3.** The MLE estimate of the variance σ² (dividing by n) is approximately 1469.8.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 1470.0, not 1469.8.

**4.** With ε = 25 and MinPts = 1, DBSCAN groups the data into the clusters [[-21], [11, 24, 29], [67, 82, 86, 90]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=25, MinPts=1) gives clusters [[-21], [11, 24, 29], [67, 82, 86, 90]]; no noise.

**5.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

---

## Question 46 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-24, -23, -3, 14, 15, 29, 80, 84}. Which statements are correct?

**1.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 21.5, σ̂² = (1/n)Σ(x−μ̂)² ≈ 1516.75.

**2.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**3.** The MLE estimate of the mean μ is approximately 21.2.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 21.5, not 21.2.

**4.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [4, 1, 17, 1, 1, 14, 1, 4].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [1, 1, 17, 1, 1, 14, 4, 4], not [4, 1, 17, 1, 1, 14, 1, 4].

**5.** The MLE estimate of the variance σ² (dividing by n) is approximately 1516.75.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 1516.75.

---

## Question 47 · Hierarchical

Consider 4 objects with the symmetric distance matrix (0-based indices):

```
[0, 3, 7, 4]
[3, 0, 10, 10]
[7, 10, 0, 12]
[4, 10, 12, 0]
```

Which statements are correct?

**1.** Using Single-Linkage, the first merge joins objects 0 and 1 at height 3.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (0,)+(1,) at 3.

**2.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**3.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**4.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**5.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

---

## Question 48 · Outlier Detection

Consider the 2-D points [[2, 4], [3, 4], [7, 0], [0, 6], [7, 2], [6, 6], [13, 15]]. Which statements are correct?

**1.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

**2.** LOF is a global density score that compares each point's density to the dataset-wide average density.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] LOF is a LOCAL/relative score: density vs the point's own neighbours.

**3.** Point 6 (the far point) receives the largest LOF, consistent with being an outlier.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF values ≈ [1.07, 0.99, 1.19, 0.9, 1.13, 0.94, 2.98]; the isolated point has LOF ≫ 1.

**4.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

**5.** The weighted KNN outlier score averages a point's distances to all its 1st…k-th nearest neighbours.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] Weighted-kNN aggregates (averages) the 1..k NN distances; plain kNN uses only the k-th.

---

## Question 49 · Probability & Density

A test has sensitivity P(+|D)=0.9 and specificity 0.9; disease prevalence is P(D)=0.05. Also consider the sample [1, 1, 5, 2, 3]. Which statements are correct?

**1.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**2.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**3.** The sample mean of the listed sample is approximately 2.2.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 2.4, not 2.2.

**4.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**5.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

---

## Question 50 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-18, -15, -3, 0, 24, 42, 53, 79}. Which statements are correct?

**1.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 20.25, σ̂² = (1/n)Σ(x−μ̂)² ≈ 1083.44.

**2.** The MLE estimate of the mean μ is approximately 19.75.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 20.25, not 19.75.

**3.** The MLE estimate of the variance σ² (dividing by n) is approximately 1083.24.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 1083.44, not 1083.24.

**4.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**5.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

---

## Question 51 · Data Representation

Consider two records described by 5 numerical variables: u = [6, -1, 0, 4, 4] and v = [2, 0, -1, -2, 4]. Which statements are correct?

**1.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

**2.** The Manhattan (city-block) distance d(u,v) is approximately 14.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 12, not 14.

**3.** The Suprema (Chebyshev) distance d(u,v) is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 6, not 5.

**4.** The inner product <u,v> is approximately 20.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 20.

**5.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

---

## Question 52 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[3, 3], [2, 2], [1, 3], [1, 2], [9, 11], [11, 8], [8, 8], [8, 10]] with initial prototypes [[3, 3], [11, 8]]. Which statements are correct?

**1.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**2.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**3.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**4.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 2, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 0, 0, 0, 2, 1, 1, 1].

**5.** The final SSE (sum of squared errors) of the partition is approximately 16.5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 16.5.

---

## Question 53 · Data Representation

Two objects are described by 8 binary (asymmetric/symmetric) variables: x1 = [1, 0, 1, 0, 0, 0, 0, 1] and x2 = [0, 0, 1, 0, 1, 1, 0, 1]. Which statements are correct?

**1.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**2.** The count of 1–1 matches n11 is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 2, not 5.

**3.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**4.** The Jaccard coefficient Jc(x1,x2) is approximately 0.7.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.4, not 0.7.

**5.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.625.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.625.

---

## Question 54 · Data Representation

Consider two records described by 5 numerical variables: u = [8, 1, -4, 2, 1] and v = [-2, -4, 0, 5, -1]. Which statements are correct?

**1.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**2.** The Suprema (Chebyshev) distance d(u,v) is approximately 10.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 10.

**3.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

**4.** The Euclidean distance d(u,v) is approximately 12.41.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 12.41.

**5.** The Manhattan (city-block) distance d(u,v) is approximately 27.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 24, not 27.

---

## Question 55 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0024 and 0.0088, with priors π_C1 = 0.4 and π_C2 = 0.6. Which statements are correct?

**1.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**2.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

**3.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

**4.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**5.** The posterior probability (responsibility) of C1 at x is approximately 0.004.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The correct value is ≈ 0.154, not 0.004.

---

## Question 56 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0059 and 0.0163, with priors π_C1 = 0.4 and π_C2 = 0.6. Which statements are correct?

**1.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

**2.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**3.** The posterior probability (responsibility) of C2 at x is approximately 0.806.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.806.

**4.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**5.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

---

## Question 57 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[0, 0], [1, 3], [3, 1], [0, 1], [9, 11], [10, 10], [11, 8], [11, 8]] with initial prototypes [[0, 0], [10, 10]]. Which statements are correct?

**1.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**2.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**3.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 1, 1, 1, 2].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 0, 0, 0, 1, 1, 1, 2].

**4.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**5.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

---

## Question 58 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-22, 14, 42, 55, 64, 78}. Which statements are correct?

**1.** The MLE estimate of the variance σ² (dividing by n) is approximately 1125.82.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 1125.92, not 1125.82.

**2.** The MLE estimate of the mean μ is approximately 38.5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 38.5.

**3.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**4.** With ε = 10 and MinPts = 1, DBSCAN groups the data into the clusters [[-22], [14], [42], [55, 64], [78]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=10, MinPts=1) gives clusters [[-22], [14], [42], [55, 64], [78]]; no noise.

**5.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [36, 28, 13, 9, 9, 14].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] The values are [36, 28, 13, 9, 9, 14].

---

## Question 59 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0055 and 0.0188, with priors π_C1 = 0.7 and π_C2 = 0.3. Which statements are correct?

**1.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**2.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

**3.** The posterior probability (responsibility) of C1 at x is approximately 0.306.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The correct value is ≈ 0.406, not 0.306.

**4.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**5.** The posterior probability (responsibility) of C2 at x is approximately 0.694.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The correct value is ≈ 0.594, not 0.694.

---

## Question 60 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 4). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, EGGS |
| 2 | BEER, CRACKERS |
| 3 | CRACKERS, DIAPERS, EGGS, MILK |
| 4 | EGGS, MILK |
| 5 | BEER, CRACKERS, DIAPERS, MILK |
| 6 | CRACKERS, EGGS |
| 7 | BEER, CRACKERS, DIAPERS, EGGS, MILK |
| 8 | BEER, DIAPERS, EGGS, MILK |
| 9 | BEER, CRACKERS, DIAPERS, EGGS, MILK |
| 10 | BEER, CRACKERS, DIAPERS, EGGS, MILK |

**1.** The lift of the rule {DIAPERS} ⇒ {BEER} is approximately 1.04.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 1.19, not 1.04.

**2.** The frequent itemset {EGGS} is maximal (it has no frequent superset).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Maximal = no superset reaches support 4.

**3.** Confidence of X ⇒ Y is defined as support(X ∪ Y) / support(Y).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Confidence = support(X∪Y)/support(X) (divide by the antecedent's support).

**4.** The frequent itemset {EGGS} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

**5.** Apriori must scan the database to count the support of a candidate even when one of its subsets is already known to be infrequent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The prune step removes such candidates first, so no database scan is needed for them.

---

## Question 61 · Probability & Density

A test has sensitivity P(+|D)=0.95 and specificity 0.9; disease prevalence is P(D)=0.1. Also consider the sample [6, 6, 6, 5, 4]. Which statements are correct?

**1.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**2.** The sample mean of the listed sample is approximately 5.4.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 5.4.

**3.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**4.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**5.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

---

## Question 62 · Probability & Density

A test has sensitivity P(+|D)=0.9 and specificity 0.99; disease prevalence is P(D)=0.05. Also consider the sample [5, 2, 2, 1, 5]. Which statements are correct?

**1.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**2.** The sample variance (÷ n−1) of the listed sample is approximately 3.35.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 3.5, not 3.35.

**3.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**4.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**5.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

---

## Question 63 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[2, 1], [0, 2], [1, 1], [0, 3], [9, 8], [9, 9], [10, 11], [8, 9]] with initial prototypes [[2, 1], [9, 9]]. Which statements are correct?

**1.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**2.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.834.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 0.834.

**3.** The final cluster labels (one per point, in order) are [1, 0, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [1, 0, 0, 0, 1, 1, 1, 1].

**4.** The final SSE (sum of squared errors) of the partition is approximately 12.15.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 12.25, not 12.15.

**5.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

---

## Question 64 · Data Representation

Consider two records described by 4 numerical variables: u = [-1, -5, 0, 7] and v = [7, -1, 6, 8]. Which statements are correct?

**1.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

**2.** The inner product <u,v> is approximately 54.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 54.

**3.** The cosine similarity cos(u,v) is approximately 0.209.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.509, not 0.209.

**4.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

**5.** The Suprema (Chebyshev) distance d(u,v) is approximately 10.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 8, not 10.

---

## Question 65 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 5). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, CRACKERS, DIAPERS, EGGS, JAM, MILK |
| 2 | BEER, CRACKERS, EGGS, JAM, MILK |
| 3 | BEER, DIAPERS, JAM |
| 4 | BEER, MILK |
| 5 | BEER, DIAPERS, JAM, MILK |
| 6 | BEER, CRACKERS, DIAPERS, EGGS, JAM |
| 7 | BEER, MILK |
| 8 | BEER, CRACKERS, DIAPERS, EGGS |
| 9 | DIAPERS, JAM, MILK |
| 10 | DIAPERS, JAM, MILK |
| 11 | BEER, CRACKERS |
| 12 | CRACKERS, DIAPERS, EGGS, JAM, MILK |

**1.** With n distinct items the candidate search space contains 2^n possible itemsets.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Each item is in or out, giving 2^n itemsets — hence Apriori pruning is essential.

**2.** The support count of {JAM} is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 8, not 6.

**3.** Apriori must scan the database to count the support of a candidate even when one of its subsets is already known to be infrequent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The prune step removes such candidates first, so no database scan is needed for them.

**4.** By anti-monotonicity (downward closure), every subset of a frequent itemset is also frequent.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Apriori prunes any candidate having an infrequent subset before counting support.

**5.** The lift of the rule {EGGS} ⇒ {BEER} is approximately 1.067.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 1.067.

---

## Question 66 · Probability & Density

A test has sensitivity P(+|D)=0.9 and specificity 0.99; disease prevalence is P(D)=0.1. Also consider the sample [2, 3, 6, 1, 5]. Which statements are correct?

**1.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**2.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**3.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**4.** The posterior P(D | +) by Bayes' rule is approximately 0.709.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.909, not 0.709.

**5.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

---

## Question 67 · Outlier Detection

Consider the 2-D points [[5, 5], [4, 3], [2, 3], [6, 7], [7, 5], [4, 7], [15, 15]]. Which statements are correct?

**1.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

**2.** The unweighted KNN outlier scores with k=1 (per point, in order) are [2.0, 2.0, 2.0, 2.0, 3.0, 2.0, 12.04].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 12.04], not [2.0, 2.0, 2.0, 2.0, 3.0, 2.0, 12.04].

**3.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

**4.** Point 6 (the far point) receives the largest LOF, consistent with being an outlier.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF values ≈ [0.94, 1.15, 1.15, 1.0, 1.0, 1.0, 5.56]; the isolated point has LOF ≫ 1.

**5.** LOF is a global density score that compares each point's density to the dataset-wide average density.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] LOF is a LOCAL/relative score: density vs the point's own neighbours.

---

## Question 68 · Data Representation

Consider two records described by 5 numerical variables: u = [2, 2, 0, 6, -3] and v = [4, 2, -1, -1, -5]. Which statements are correct?

**1.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

**2.** The Euclidean distance d(u,v) is approximately 7.92.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 7.62, not 7.92.

**3.** The Manhattan (city-block) distance d(u,v) is approximately 12.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 12.

**4.** The inner product <u,v> is approximately 21.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 21.

**5.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

---

## Question 69 · Hierarchical

Consider 4 objects with the symmetric distance matrix (0-based indices):

```
[0, 11, 6, 10]
[11, 0, 1, 1]
[6, 1, 0, 2]
[10, 1, 2, 0]
```

Which statements are correct?

**1.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**2.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**3.** Using Single-Linkage, the height of the final (root) merge is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 6.

**4.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**5.** Using Complete-Linkage, the height of the final (root) merge is approximately 11.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 11.

---

## Question 70 · Hierarchical

Consider 4 objects with the symmetric distance matrix (0-based indices):

```
[0, 4, 12, 3]
[4, 0, 2, 4]
[12, 2, 0, 2]
[3, 4, 2, 0]
```

Which statements are correct?

**1.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**2.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**3.** Using Single-Linkage, the first merge joins objects 1 and 2 at height 2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (1,)+(2,) at 2.

**4.** Using Complete-Linkage, the height of the final (root) merge is approximately 11.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 12, not 11.

**5.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

---

## Question 71 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[0, 2], [3, 1], [1, 3], [0, 2], [10, 9], [8, 10], [8, 8], [11, 8]] with initial prototypes [[0, 2], [8, 10]]. Which statements are correct?

**1.** The final SSE (sum of squared errors) of the partition is approximately 17.5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 17.5.

**2.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**3.** The final cluster labels (one per point, in order) are [0, 0, 1, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 0, 1, 0, 1, 1, 1, 1].

**4.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**5.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

---

## Question 72 · Outlier Detection

Consider the 2-D points [[4, 4], [7, 4], [6, 0], [3, 6], [1, 6], [2, 5], [15, 12]]. Which statements are correct?

**1.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

**2.** LOF is a global density score that compares each point's density to the dataset-wide average density.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] LOF is a LOCAL/relative score: density vs the point's own neighbours.

**3.** Point 6 (the far point) receives the largest LOF, consistent with being an outlier.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF values ≈ [1.21, 1.27, 1.54, 0.93, 0.93, 1.17, 5.28]; the isolated point has LOF ≫ 1.

**4.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

**5.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

---

## Question 73 · Data Representation

Two objects are described by 8 binary (asymmetric/symmetric) variables: x1 = [0, 0, 1, 1, 0, 1, 1, 1] and x2 = [1, 0, 0, 1, 1, 1, 1, 1]. Which statements are correct?

**1.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**2.** The Jaccard coefficient Jc(x1,x2) is approximately 0.571.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.571.

**3.** The count of disagreements n10 + n01 is approximately 3.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 3.

**4.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**5.** The count of 1–1 matches n11 is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 4, not 5.

---

## Question 74 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[0, 3], [3, 2], [2, 1], [0, 1], [10, 8], [9, 10], [11, 8], [11, 8]] with initial prototypes [[0, 3], [9, 10]]. Which statements are correct?

**1.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**2.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.819.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 0.819.

**3.** The final SSE (sum of squared errors) of the partition is approximately 15.1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 15.25, not 15.1.

**4.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**5.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

---

## Question 75 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0022 and 0.0047, with priors π_C1 = 0.3 and π_C2 = 0.7. Which statements are correct?

**1.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**2.** The posterior probability (responsibility) of C1 at x is approximately 0.167.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.167.

**3.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**4.** The posterior probability (responsibility) of C2 at x is approximately 0.833.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.833.

**5.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

---

## Question 76 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-24, -20, -3, 6, 17, 18, 83, 99}. Which statements are correct?

**1.** With ε = 15 and MinPts = 2, DBSCAN groups the data into the clusters [[-24, -20], [-3, 6, 17, 18]] with [83, 99] as noise.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=15, MinPts=2) gives clusters [[-24, -20], [-3, 6, 17, 18]]; noise = [83, 99].

**2.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**3.** The MLE estimate of the variance σ² (dividing by n) is approximately 1806.5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 1806.5.

**4.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**5.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 22.0, σ̂² = (1/n)Σ(x−μ̂)² ≈ 1806.5.

---

## Question 77 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {23, 29, 30, 73, 75, 89}. Which statements are correct?

**1.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**2.** The MLE estimate of the variance σ² (dividing by n) is approximately 697.47.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 697.47.

**3.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**4.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**5.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 53.17, σ̂² = (1/n)Σ(x−μ̂)² ≈ 697.47.

---

## Question 78 · Probability & Density

A test has sensitivity P(+|D)=0.99 and specificity 0.95; disease prevalence is P(D)=0.05. Also consider the sample [5, 6, 2, 5, 1]. Which statements are correct?

**1.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**2.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**3.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**4.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**5.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

---

## Question 79 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-7, 38, 81, 99, 102, 103, 108}. Which statements are correct?

**1.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**2.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**3.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 74.86, σ̂² = (1/n)Σ(x−μ̂)² ≈ 1615.27.

**4.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**5.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [45, 43, 18, 3, 5, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [45, 43, 18, 3, 1, 1, 5], not [45, 43, 18, 3, 5, 1, 1].

---

## Question 80 · Hierarchical

Consider 5 objects with the symmetric distance matrix (0-based indices):

```
[0, 10, 6, 7, 3]
[10, 0, 3, 3, 5]
[6, 3, 0, 9, 6]
[7, 3, 9, 0, 11]
[3, 5, 6, 11, 0]
```

Which statements are correct?

**1.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**2.** Using Single-Linkage, the height of the final (root) merge is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 5.

**3.** Using Complete-Linkage, the height of the final (root) merge is approximately 12.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 11, not 12.

**4.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**5.** Using Single-Linkage, the first merge joins objects 0 and 4 at height 3.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (0,)+(4,) at 3.

---

## Question 81 · Hierarchical

Consider 4 objects with the symmetric distance matrix (0-based indices):

```
[0, 1, 5, 8]
[1, 0, 8, 10]
[5, 8, 0, 6]
[8, 10, 6, 0]
```

Which statements are correct?

**1.** Using Single-Linkage, the first merge joins objects 0 and 1 at height 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (0,)+(1,) at 1.

**2.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

**3.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**4.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**5.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

---

## Question 82 · Data Representation

Consider two records described by 4 numerical variables: u = [5, 1, -3, 9] and v = [-5, 8, 3, 4]. Which statements are correct?

**1.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**2.** The inner product <u,v> is approximately 7.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 10, not 7.

**3.** The Euclidean distance d(u,v) is approximately 14.49.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 14.49.

**4.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

**5.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

---

## Question 83 · Data Representation

Two objects are described by 12 binary (asymmetric/symmetric) variables: x1 = [0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1] and x2 = [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0]. Which statements are correct?

**1.** The count of disagreements n10 + n01 is approximately 7.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 7.

**2.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**3.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.417.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.417.

**4.** The Jaccard coefficient Jc(x1,x2) is approximately 0.3.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.3.

**5.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

---

## Question 84 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[2, 1], [1, 2], [2, 2], [2, 1], [9, 9], [9, 8], [11, 9], [10, 10]] with initial prototypes [[2, 1], [9, 8]]. Which statements are correct?

**1.** The final SSE (sum of squared errors) of the partition is approximately 6.7.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 6.5, not 6.7.

**2.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**3.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 2, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 0, 0, 0, 2, 1, 1, 1].

**4.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.877, not 1.

**5.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

---

## Question 85 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[3, 3], [3, 2], [1, 2], [0, 0], [10, 11], [8, 10], [9, 11], [9, 9]] with initial prototypes [[3, 3], [8, 10]]. Which statements are correct?

**1.** The final cluster labels (one per point, in order) are [0, 0, 0, 1, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 0, 0, 1, 1, 1, 1, 1].

**2.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**3.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**4.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**5.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

---

## Question 86 · Probability & Density

A test has sensitivity P(+|D)=0.99 and specificity 0.9; disease prevalence is P(D)=0.1. Also consider the sample [2, 3, 2, 3, 4]. Which statements are correct?

**1.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**2.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**3.** The sample mean of the listed sample is approximately 3.0.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 2.8, not 3.0.

**4.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**5.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

---

## Question 87 · Hierarchical

Consider 4 objects with the symmetric distance matrix (0-based indices):

```
[0, 9, 4, 9]
[9, 0, 9, 5]
[4, 9, 0, 12]
[9, 5, 12, 0]
```

Which statements are correct?

**1.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

**2.** Using Single-Linkage, the first merge joins objects 0 and 2 at height 4.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (0,)+(2,) at 4.

**3.** Using Complete-Linkage, the height of the final (root) merge is approximately 12.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 12.

**4.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**5.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

---

## Question 88 · Hierarchical

Consider 5 objects with the symmetric distance matrix (0-based indices):

```
[0, 1, 7, 11, 5]
[1, 0, 1, 11, 11]
[7, 1, 0, 2, 2]
[11, 11, 2, 0, 11]
[5, 11, 2, 11, 0]
```

Which statements are correct?

**1.** Using Single-Linkage, the first merge joins objects 0 and 1 at height 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (0,)+(1,) at 1.

**2.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

**3.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**4.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**5.** Using Complete-Linkage, the height of the final (root) merge is approximately 11.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 11.

---

## Question 89 · Outlier Detection

Consider the 2-D points [[5, 5], [7, 0], [6, 7], [7, 2], [3, 2], [6, 3], [17, 15]]. Which statements are correct?

**1.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

**2.** The unweighted KNN outlier scores with k=2 (per point, in order) are [2.24, 3.16, 4.0, 2.0, 3.61, 2.24, 15.62].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] The values are [2.24, 3.16, 4.0, 2.0, 3.61, 2.24, 15.62].

**3.** The weighted KNN outlier score averages a point's distances to all its 1st…k-th nearest neighbours.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] Weighted-kNN aggregates (averages) the 1..k NN distances; plain kNN uses only the k-th.

**4.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

**5.** LOF is a global density score that compares each point's density to the dataset-wide average density.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] LOF is a LOCAL/relative score: density vs the point's own neighbours.

---

## Question 90 · Outlier Detection

Consider the 2-D points [[5, 5], [0, 4], [5, 7], [3, 0], [4, 2], [6, 6], [17, 13]]. Which statements are correct?

**1.** LOF is a global density score that compares each point's density to the dataset-wide average density.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] LOF is a LOCAL/relative score: density vs the point's own neighbours.

**2.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

**3.** Point 6 (the far point) receives the largest LOF, consistent with being an outlier.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF values ≈ [0.93, 1.16, 0.93, 0.93, 1.7, 1.17, 7.18]; the isolated point has LOF ≫ 1.

**4.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

**5.** The unweighted KNN outlier scores with k=1 (per point, in order) are [2.41, 4.47, 1.41, 2.24, 2.24, 1.41, 13.04].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [1.41, 4.47, 1.41, 2.24, 2.24, 1.41, 13.04], not [2.41, 4.47, 1.41, 2.24, 2.24, 1.41, 13.04].

---

## Question 91 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0034 and 0.0139, with priors π_C1 = 0.7 and π_C2 = 0.3. Which statements are correct?

**1.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

**2.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**3.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**4.** The posterior probability (responsibility) of C1 at x is approximately 0.213.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The correct value is ≈ 0.363, not 0.213.

**5.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

---

## Question 92 · Hierarchical

Consider 4 objects with the symmetric distance matrix (0-based indices):

```
[0, 6, 11, 6]
[6, 0, 7, 5]
[11, 7, 0, 5]
[6, 5, 5, 0]
```

Which statements are correct?

**1.** Using Complete-Linkage, the height of the final (root) merge is approximately 14.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 11, not 14.

**2.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**3.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**4.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**5.** Using Single-Linkage, the height of the final (root) merge is approximately 4.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 6, not 4.

---

## Question 93 · Data Representation

Consider two records described by 4 numerical variables: u = [-2, 3, 3, 9] and v = [7, -1, -3, -2]. Which statements are correct?

**1.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

**2.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

**3.** The Euclidean distance d(u,v) is approximately 15.44.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 15.94, not 15.44.

**4.** The inner product <u,v> is approximately -44.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ -44.

**5.** The Suprema (Chebyshev) distance d(u,v) is approximately 11.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 11.

---

## Question 94 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[2, 0], [0, 2], [3, 3], [2, 3], [10, 8], [11, 10], [10, 10], [11, 10]] with initial prototypes [[2, 0], [11, 10]]. Which statements are correct?

**1.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**2.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**3.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.526.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.826, not 0.526.

**4.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**5.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

---

## Question 95 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[2, 3], [0, 3], [2, 1], [0, 1], [9, 8], [8, 10], [10, 8], [10, 10]] with initial prototypes [[2, 3], [8, 10]]. Which statements are correct?

**1.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**2.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.801.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 0.801.

**3.** The final SSE (sum of squared errors) of the partition is approximately 14.75.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 14.75.

**4.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**5.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

---

## Question 96 · Data Representation

Two objects are described by 10 binary (asymmetric/symmetric) variables: x1 = [1, 0, 0, 0, 0, 1, 0, 1, 0, 1] and x2 = [0, 1, 1, 1, 1, 0, 1, 0, 0, 1]. Which statements are correct?

**1.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.35.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.2, not 0.35.

**2.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**3.** The count of 1–1 matches n11 is approximately 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 1.

**4.** The Jaccard coefficient Jc(x1,x2) is approximately 0.111.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.111.

**5.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

---

## Question 97 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-2, 2, 4, 17, 18, 44, 47}. Which statements are correct?

**1.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**2.** The MLE estimate of the mean μ is approximately 18.47.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 18.57, not 18.47.

**3.** With ε = 25 and MinPts = 2, DBSCAN groups the data into the clusters [[-2, 2, 4, 17, 18], [44, 47]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=25, MinPts=2) gives clusters [[-2, 2, 4, 17, 18], [44, 47]]; no noise.

**4.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 18.57, σ̂² = (1/n)Σ(x−μ̂)² ≈ 338.24.

**5.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [5, 2, 2, 1, 1, 3, 3].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [4, 2, 2, 1, 1, 3, 3], not [5, 2, 2, 1, 1, 3, 3].

---

## Question 98 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[1, 1], [0, 1], [3, 0], [0, 2], [10, 11], [11, 11], [8, 11], [9, 10]] with initial prototypes [[1, 1], [11, 11]]. Which statements are correct?

**1.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**2.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.849.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 0.849.

**3.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] The values are [0, 0, 0, 0, 1, 1, 1, 1].

**4.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**5.** The final SSE (sum of squared errors) of the partition is approximately 13.95.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 13.75, not 13.95.

---

## Question 99 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[0, 3], [2, 0], [2, 3], [0, 1], [11, 11], [10, 10], [10, 11], [11, 9]] with initial prototypes [[0, 3], [10, 10]]. Which statements are correct?

**1.** The final SSE (sum of squared errors) of the partition is approximately 14.5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 14.5.

**2.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.838, not 1.

**3.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 2, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 0, 0, 0, 2, 1, 1, 1].

**4.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**5.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

---

## Question 100 · Data Representation

Two objects are described by 8 binary (asymmetric/symmetric) variables: x1 = [0, 0, 0, 0, 1, 0, 0, 0] and x2 = [0, 0, 1, 1, 0, 0, 1, 1]. Which statements are correct?

**1.** The count of 1–1 matches n11 is approximately 0.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.

**2.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.375.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.375.

**3.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**4.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**5.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

---

## Question 101 · Data Representation

Two objects are described by 10 binary (asymmetric/symmetric) variables: x1 = [0, 0, 0, 0, 0, 1, 0, 0, 1, 0] and x2 = [0, 0, 0, 1, 1, 1, 1, 0, 0, 1]. Which statements are correct?

**1.** The count of 1–1 matches n11 is approximately 0.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 1, not 0.

**2.** The count of disagreements n10 + n01 is approximately 2.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 5, not 2.

**3.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**4.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**5.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.2.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.5, not 0.2.

---

## Question 102 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[2, 3], [0, 1], [2, 1], [3, 1], [11, 9], [9, 11], [11, 11], [8, 8]] with initial prototypes [[2, 3], [9, 11]]. Which statements are correct?

**1.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**2.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**3.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.275.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.775, not 0.275.

**4.** The final SSE (sum of squared errors) of the partition is approximately 20.95.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 21.25, not 20.95.

**5.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

---

## Question 103 · Hierarchical

Consider 5 objects with the symmetric distance matrix (0-based indices):

```
[0, 7, 6, 12, 8]
[7, 0, 11, 11, 12]
[6, 11, 0, 5, 11]
[12, 11, 5, 0, 3]
[8, 12, 11, 3, 0]
```

Which statements are correct?

**1.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**2.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**3.** Using Single-Linkage, the height of the final (root) merge is approximately 7.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 7.

**4.** Using Single-Linkage, the first merge joins objects 3 and 4 at height 3.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (3,)+(4,) at 3.

**5.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

---

## Question 104 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 6). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BREAD, BUTTER, CRACKERS, DIAPERS, JAM, MILK |
| 2 | CRACKERS, MILK |
| 3 | BUTTER, CRACKERS, DIAPERS |
| 4 | BREAD, JAM |
| 5 | BREAD, BUTTER, DIAPERS, MILK |
| 6 | CRACKERS, MILK |
| 7 | BREAD, CRACKERS |
| 8 | BREAD, BUTTER, DIAPERS, JAM, MILK |
| 9 | BREAD, BUTTER, CRACKERS, DIAPERS |
| 10 | BREAD, CRACKERS, DIAPERS, JAM, MILK |

**1.** By anti-monotonicity (downward closure), every subset of a frequent itemset is also frequent.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Apriori prunes any candidate having an infrequent subset before counting support.

**2.** Confidence of X ⇒ Y is defined as support(X ∪ Y) / support(Y).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Confidence = support(X∪Y)/support(X) (divide by the antecedent's support).

**3.** Apriori must scan the database to count the support of a candidate even when one of its subsets is already known to be infrequent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The prune step removes such candidates first, so no database scan is needed for them.

**4.** The support count of the itemset {CRACKERS, MILK} is approximately 1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 4, not 1.

**5.** The confidence of the rule {CRACKERS} ⇒ {MILK} is approximately 0.071.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 0.571, not 0.071.

---

## Question 105 · Probability & Density

A test has sensitivity P(+|D)=0.95 and specificity 0.9; disease prevalence is P(D)=0.01. Also consider the sample [6, 5, 5, 2, 3]. Which statements are correct?

**1.** The sample variance (÷ n−1) of the listed sample is approximately 2.7.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 2.7.

**2.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**3.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**4.** The sample mean of the listed sample is approximately 4.4.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 4.2, not 4.4.

**5.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

---

## Question 106 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 6). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, BREAD, MILK |
| 2 | BREAD, BUTTER, MILK |
| 3 | BREAD, CRACKERS, MILK |
| 4 | CRACKERS, DIAPERS, MILK |
| 5 | BEER, BREAD, BUTTER, CRACKERS, DIAPERS, MILK |
| 6 | BEER, BUTTER, CRACKERS, DIAPERS, MILK |
| 7 | BEER, CRACKERS |
| 8 | BEER, BUTTER, CRACKERS, DIAPERS |
| 9 | BEER, BREAD, BUTTER, CRACKERS, DIAPERS, MILK |
| 10 | BEER, BREAD, BUTTER, CRACKERS, MILK |
| 11 | BEER, BREAD, CRACKERS, DIAPERS, MILK |
| 12 | BUTTER, DIAPERS |
| 13 | BREAD, CRACKERS |
| 14 | BEER, DIAPERS |

**1.** Apriori must scan the database to count the support of a candidate even when one of its subsets is already known to be infrequent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The prune step removes such candidates first, so no database scan is needed for them.

**2.** The frequent itemset {BEER} is maximal (it has no frequent superset).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Maximal = no superset reaches support 6.

**3.** With n distinct items the candidate search space contains 2^n possible itemsets.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Each item is in or out, giving 2^n itemsets — hence Apriori pruning is essential.

**4.** The frequent itemset {BEER} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

**5.** The confidence of the rule {BUTTER} ⇒ {BEER} is approximately 0.714.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 0.714.

---

## Question 107 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 4). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BREAD, CRACKERS, DIAPERS, EGGS, JAM, MILK |
| 2 | BREAD, CRACKERS, EGGS, JAM |
| 3 | CRACKERS, DIAPERS, EGGS, JAM, MILK |
| 4 | BREAD, CRACKERS, DIAPERS, EGGS, JAM, MILK |
| 5 | CRACKERS, DIAPERS, EGGS |
| 6 | BREAD, DIAPERS, EGGS, MILK |
| 7 | BREAD, CRACKERS, DIAPERS, MILK |
| 8 | DIAPERS, EGGS, JAM, MILK |
| 9 | DIAPERS, JAM, MILK |
| 10 | BREAD, CRACKERS, DIAPERS, EGGS, MILK |
| 11 | BREAD, CRACKERS, DIAPERS, EGGS, JAM, MILK |
| 12 | BREAD, CRACKERS, DIAPERS, EGGS, JAM, MILK |

**1.** The support count of {EGGS} is approximately 10.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 10.

**2.** The support count of the itemset {EGGS, BREAD} is approximately 7.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 7.

**3.** Confidence of X ⇒ Y is defined as support(X ∪ Y) / support(Y).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Confidence = support(X∪Y)/support(X) (divide by the antecedent's support).

**4.** By anti-monotonicity (downward closure), every subset of a frequent itemset is also frequent.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Apriori prunes any candidate having an infrequent subset before counting support.

**5.** The lift of the rule {EGGS} ⇒ {BREAD} is approximately 0.55.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 1.05, not 0.55.

---

## Question 108 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0167 and 0.0193, with priors π_C1 = 0.7 and π_C2 = 0.3. Which statements are correct?

**1.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**2.** The posterior probability (responsibility) of C2 at x is approximately 0.331.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.331.

**3.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**4.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**5.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

---

## Question 109 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-28, -12, 14, 47, 71, 106}. Which statements are correct?

**1.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [16, 16, 26, 24, 24, 35].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] The values are [16, 16, 26, 24, 24, 35].

**2.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 33.0, σ̂² = (1/n)Σ(x−μ̂)² ≈ 2179.33.

**3.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**4.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**5.** The MLE estimate of the mean μ is approximately 33.0.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 33.0.

---

## Question 110 · Data Representation

Two objects are described by 8 binary (asymmetric/symmetric) variables: x1 = [1, 0, 0, 1, 1, 0, 1, 1] and x2 = [1, 0, 0, 0, 0, 1, 0, 0]. Which statements are correct?

**1.** The Jaccard coefficient Jc(x1,x2) is approximately 0.267.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.167, not 0.267.

**2.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**3.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**4.** The count of 1–1 matches n11 is approximately 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 1.

**5.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.375.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.375.

---

## Question 111 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-27, -25, -13, 5, 68, 101, 109}. Which statements are correct?

**1.** With ε = 20 and MinPts = 2, DBSCAN groups the data into the clusters [[-27, -25, -13, 5], [101, 109]] with [68] as noise.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=20, MinPts=2) gives clusters [[-27, -25, -13, 5], [101, 109]]; noise = [68].

**2.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [2, 2, 12, 18, 33, 8, 8].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] The values are [2, 2, 12, 18, 33, 8, 8].

**3.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 31.14, σ̂² = (1/n)Σ(x−μ̂)² ≈ 3066.41.

**4.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**5.** The MLE estimate of the mean μ is approximately 30.99.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 31.14, not 30.99.

---

## Question 112 · Probability & Density

A test has sensitivity P(+|D)=0.99 and specificity 0.99; disease prevalence is P(D)=0.05. Also consider the sample [5, 2, 4, 5, 3]. Which statements are correct?

**1.** The sample variance (÷ n−1) of the listed sample is approximately 1.8.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 1.7, not 1.8.

**2.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**3.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**4.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**5.** The sample mean of the listed sample is approximately 3.7.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 3.8, not 3.7.

---

## Question 113 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.009 and 0.0056, with priors π_C1 = 0.7 and π_C2 = 0.3. Which statements are correct?

**1.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**2.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**3.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**4.** The posterior probability (responsibility) of C1 at x is approximately 0.789.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.789.

**5.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

---

## Question 114 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[2, 2], [0, 1], [2, 0], [0, 2], [10, 8], [11, 8], [8, 10], [8, 11]] with initial prototypes [[2, 2], [11, 8]]. Which statements are correct?

**1.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**2.** The final SSE (sum of squared errors) of the partition is approximately 20.25.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 20.25.

**3.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**4.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**5.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

---

## Question 115 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-15, -7, 27, 36, 95, 102}. Which statements are correct?

**1.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**2.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 39.67, σ̂² = (1/n)Σ(x−μ̂)² ≈ 2047.89.

**3.** With ε = 10 and MinPts = 2, DBSCAN groups the data into the clusters [[-15, -7], [27, 36], [95, 102]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=10, MinPts=2) gives clusters [[-15, -7], [27, 36], [95, 102]]; no noise.

**4.** The MLE estimate of the mean μ is approximately 39.87.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 39.67, not 39.87.

**5.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [9, 8, 9, 9, 7, 7].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [8, 8, 9, 9, 7, 7], not [9, 8, 9, 9, 7, 7].

---

## Question 116 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[2, 1], [1, 2], [3, 1], [2, 0], [9, 9], [9, 11], [10, 11], [9, 11]] with initial prototypes [[2, 1], [9, 11]]. Which statements are correct?

**1.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.577.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.877, not 0.577.

**2.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 2, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 0, 0, 0, 2, 1, 1, 1].

**3.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**4.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**5.** The final SSE (sum of squared errors) of the partition is approximately 7.75.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 7.75.

---

## Question 117 · Hierarchical

Consider 4 objects with the symmetric distance matrix (0-based indices):

```
[0, 9, 2, 9]
[9, 0, 1, 5]
[2, 1, 0, 12]
[9, 5, 12, 0]
```

Which statements are correct?

**1.** Using Single-Linkage, the height of the final (root) merge is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 5.

**2.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**3.** Using Single-Linkage, the first merge joins objects 1 and 2 at height 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (1,)+(2,) at 1.

**4.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**5.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

---

## Question 118 · Outlier Detection

Consider the 2-D points [[4, 4], [4, 0], [5, 4], [7, 0], [6, 4], [1, 3], [16, 15]]. Which statements are correct?

**1.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

**2.** The unweighted KNN outlier scores with k=2 (per point, in order) are [2.0, 4.0, 1.0, 4.12, 2.0, 4.12, 15.56].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] The values are [2.0, 4.0, 1.0, 4.12, 2.0, 4.12, 15.56].

**3.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

**4.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

**5.** Point 6 (the far point) receives the largest LOF, consistent with being an outlier.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF values ≈ [0.87, 1.85, 1.33, 1.85, 0.87, 2.12, 8.87]; the isolated point has LOF ≫ 1.

---

## Question 119 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[0, 1], [2, 1], [2, 0], [1, 1], [9, 8], [8, 11], [10, 8], [8, 8]] with initial prototypes [[0, 1], [8, 11]]. Which statements are correct?

**1.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.832.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 0.832.

**2.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**3.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**4.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 1, 2, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 0, 0, 0, 1, 2, 1, 1].

**5.** The final SSE (sum of squared errors) of the partition is approximately 13.0.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 13.0.

---

## Question 120 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[2, 2], [1, 2], [1, 2], [2, 3], [11, 9], [9, 11], [9, 10], [10, 9]] with initial prototypes [[2, 2], [9, 11]]. Which statements are correct?

**1.** The final cluster labels (one per point, in order) are [1, 0, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [1, 0, 0, 0, 1, 1, 1, 1].

**2.** The final SSE (sum of squared errors) of the partition is approximately 6.75.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 7.25, not 6.75.

**3.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**4.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**5.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

---

## Question 121 · Data Representation

Two objects are described by 10 binary (asymmetric/symmetric) variables: x1 = [0, 0, 1, 1, 0, 0, 0, 1, 0, 0] and x2 = [1, 0, 0, 0, 1, 0, 0, 1, 0, 0]. Which statements are correct?

**1.** The count of disagreements n10 + n01 is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 4, not 6.

**2.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**3.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**4.** The Jaccard coefficient Jc(x1,x2) is approximately 0.2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.2.

**5.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

---

## Question 122 · Outlier Detection

Consider the 2-D points [[0, 1], [4, 0], [0, 3], [5, 1], [4, 1], [5, 2], [16, 14]]. Which statements are correct?

**1.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

**2.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

**3.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

**4.** LOF is a global density score that compares each point's density to the dataset-wide average density.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] LOF is a LOCAL/relative score: density vs the point's own neighbours.

**5.** The unweighted KNN outlier scores with k=2 (per point, in order) are [4.0, 1.41, 4.47, 2.0, 1.0, 1.41, 17.03].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [4.0, 1.41, 4.47, 1.0, 1.0, 1.41, 17.03], not [4.0, 1.41, 4.47, 2.0, 1.0, 1.41, 17.03].

---

## Question 123 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-23, -16, -11, 21, 39, 57, 79}. Which statements are correct?

**1.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**2.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**3.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [7, 5, 5, 18, 18, 18, 22].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] The values are [7, 5, 5, 18, 18, 18, 22].

**4.** The MLE estimate of the mean μ is approximately 20.86.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 20.86.

**5.** The MLE estimate of the variance σ² (dividing by n) is approximately 1330.41.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 1330.41.

---

## Question 124 · Data Representation

Two objects are described by 10 binary (asymmetric/symmetric) variables: x1 = [1, 1, 0, 1, 1, 0, 1, 1, 0, 0] and x2 = [1, 1, 0, 1, 0, 0, 0, 1, 0, 1]. Which statements are correct?

**1.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**2.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**3.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**4.** The count of 1–1 matches n11 is approximately 7.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 4, not 7.

**5.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.4.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.7, not 0.4.

---

## Question 125 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 4). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, BREAD, BUTTER, DIAPERS, EGGS, MILK |
| 2 | BEER, BREAD, EGGS, MILK |
| 3 | BREAD, BUTTER, EGGS, MILK |
| 4 | BEER, BREAD, BUTTER, DIAPERS, EGGS, MILK |
| 5 | BEER, BREAD, BUTTER, DIAPERS, EGGS, MILK |
| 6 | BUTTER, DIAPERS |
| 7 | BEER, BUTTER |
| 8 | BEER, BREAD, BUTTER, EGGS |
| 9 | BEER, BREAD, BUTTER, DIAPERS, EGGS, MILK |
| 10 | BEER, BREAD, BUTTER, DIAPERS, EGGS, MILK |
| 11 | BEER, BREAD, EGGS, MILK |
| 12 | BEER, BREAD, BUTTER, DIAPERS, EGGS |

**1.** The frequent itemset {BUTTER} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

**2.** The confidence of the rule {BREAD} ⇒ {BEER} is approximately 0.8.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 0.9, not 0.8.

**3.** The support count of {BREAD} is approximately 9.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 10, not 9.

**4.** By anti-monotonicity (downward closure), every subset of a frequent itemset is also frequent.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Apriori prunes any candidate having an infrequent subset before counting support.

**5.** The support count of the itemset {BREAD, BEER} is approximately 7.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 9, not 7.

---

## Question 126 · Outlier Detection

Consider the 2-D points [[0, 4], [0, 0], [4, 2], [2, 6], [3, 2], [3, 5], [12, 16]]. Which statements are correct?

**1.** The weighted KNN outlier score averages a point's distances to all its 1st…k-th nearest neighbours.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] Weighted-kNN aggregates (averages) the 1..k NN distances; plain kNN uses only the k-th.

**2.** Point 6 (the far point) receives the largest LOF, consistent with being an outlier.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF values ≈ [1.0, 1.25, 1.03, 1.04, 1.03, 0.95, 4.73]; the isolated point has LOF ≫ 1.

**3.** LOF is a global density score that compares each point's density to the dataset-wide average density.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] LOF is a LOCAL/relative score: density vs the point's own neighbours.

**4.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

**5.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

---

## Question 127 · Probability & Density

A test has sensitivity P(+|D)=0.9 and specificity 0.95; disease prevalence is P(D)=0.02. Also consider the sample [1, 1, 4, 1, 5]. Which statements are correct?

**1.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**2.** The sample variance (÷ n−1) of the listed sample is approximately 3.8.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 3.8.

**3.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**4.** The sample mean of the listed sample is approximately 2.2.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 2.4, not 2.2.

**5.** The posterior P(D | +) by Bayes' rule is approximately 0.769.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.269, not 0.769.

---

## Question 128 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[3, 1], [1, 3], [2, 1], [0, 1], [10, 9], [8, 8], [10, 11], [8, 8]] with initial prototypes [[3, 1], [8, 8]]. Which statements are correct?

**1.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.789.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 0.789.

**2.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] The values are [0, 0, 0, 0, 1, 1, 1, 1].

**3.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**4.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**5.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

---

## Question 129 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0195 and 0.0125, with priors π_C1 = 0.5 and π_C2 = 0.5. Which statements are correct?

**1.** The posterior probability (responsibility) of C2 at x is approximately 0.391.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.391.

**2.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**3.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**4.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

**5.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

---

## Question 130 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[0, 3], [2, 3], [3, 0], [2, 2], [11, 10], [10, 10], [9, 9], [9, 10]] with initial prototypes [[0, 3], [10, 10]]. Which statements are correct?

**1.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**2.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.826, not 1.

**3.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**4.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**5.** The final SSE (sum of squared errors) of the partition is approximately 14.25.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 14.25.

---

## Question 131 · Data Representation

Consider two records described by 4 numerical variables: u = [1, 7, -2, -2] and v = [0, 4, 6, -1]. Which statements are correct?

**1.** The Minkowski distance of order p=3 between u and v is approximately 8.15.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 8.15.

**2.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

**3.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**4.** The inner product <u,v> is approximately 18.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 18.

**5.** The cosine similarity cos(u,v) is approximately 0.425.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.325, not 0.425.

---

## Question 132 · Hierarchical

Consider 5 objects with the symmetric distance matrix (0-based indices):

```
[0, 4, 1, 5, 12]
[4, 0, 5, 4, 1]
[1, 5, 0, 1, 3]
[5, 4, 1, 0, 1]
[12, 1, 3, 1, 0]
```

Which statements are correct?

**1.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**2.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**3.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**4.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

**5.** Using Single-Linkage, the first merge joins objects 0 and 2 at height 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (0,)+(2,) at 1.

---

## Question 133 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-16, 32, 60, 64, 74, 105, 108}. Which statements are correct?

**1.** The MLE estimate of the mean μ is approximately 61.0.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 61.0.

**2.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**3.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**4.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 61.0, σ̂² = (1/n)Σ(x−μ̂)² ≈ 1584.86.

**5.** With ε = 25 and MinPts = 1, DBSCAN groups the data into the clusters [[-16], [32], [60, 64, 74], [105, 108]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=25, MinPts=1) gives clusters [[-16], [32], [60, 64, 74], [105, 108]]; no noise.

---

## Question 134 · Hierarchical

Consider 5 objects with the symmetric distance matrix (0-based indices):

```
[0, 8, 1, 1, 11]
[8, 0, 3, 7, 4]
[1, 3, 0, 7, 6]
[1, 7, 7, 0, 12]
[11, 4, 6, 12, 0]
```

Which statements are correct?

**1.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**2.** Using Complete-Linkage, the height of the final (root) merge is approximately 12.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 12.

**3.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**4.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

**5.** Using Single-Linkage, the height of the final (root) merge is approximately 2.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 4, not 2.

---

## Question 135 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[3, 2], [1, 0], [3, 3], [0, 0], [11, 9], [11, 10], [9, 10], [9, 9]] with initial prototypes [[3, 2], [11, 10]]. Which statements are correct?

**1.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.606.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.806, not 0.606.

**2.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**3.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**4.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**5.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 1, 1, 1, 2].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 0, 0, 0, 1, 1, 1, 2].

---

## Question 136 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[2, 0], [0, 1], [1, 3], [1, 2], [11, 9], [8, 9], [10, 11], [11, 10]] with initial prototypes [[2, 0], [8, 9]]. Which statements are correct?

**1.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**2.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**3.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.821.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 0.821.

**4.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**5.** The final cluster labels (one per point, in order) are [0, 1, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 1, 0, 0, 1, 1, 1, 1].

---

## Question 137 · Outlier Detection

Consider the 2-D points [[2, 4], [6, 1], [5, 7], [2, 6], [5, 6], [2, 5], [14, 16]]. Which statements are correct?

**1.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

**2.** The weighted KNN outlier score averages a point's distances to all its 1st…k-th nearest neighbours.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] Weighted-kNN aggregates (averages) the 1..k NN distances; plain kNN uses only the k-th.

**3.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

**4.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

**5.** LOF is a global density score that compares each point's density to the dataset-wide average density.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] LOF is a LOCAL/relative score: density vs the point's own neighbours.

---

## Question 138 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[2, 2], [2, 1], [1, 1], [3, 3], [11, 8], [11, 11], [10, 8], [10, 10]] with initial prototypes [[2, 2], [11, 11]]. Which statements are correct?

**1.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**2.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.832, not 1.

**3.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**4.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**5.** The final SSE (sum of squared errors) of the partition is approximately 12.5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 12.5.

---

## Question 139 · Hierarchical

Consider 5 objects with the symmetric distance matrix (0-based indices):

```
[0, 8, 1, 4, 7]
[8, 0, 4, 1, 4]
[1, 4, 0, 12, 12]
[4, 1, 12, 0, 11]
[7, 4, 12, 11, 0]
```

Which statements are correct?

**1.** Using Single-Linkage, the first merge joins objects 0 and 2 at height 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (0,)+(2,) at 1.

**2.** Using Complete-Linkage, the height of the final (root) merge is approximately 9.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 12, not 9.

**3.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

**4.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**5.** Using Single-Linkage, the height of the final (root) merge is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 4, not 6.

---

## Question 140 · Data Representation

Two objects are described by 8 binary (asymmetric/symmetric) variables: x1 = [0, 1, 0, 0, 0, 0, 1, 1] and x2 = [1, 0, 1, 0, 1, 1, 1, 1]. Which statements are correct?

**1.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**2.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.375.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.375.

**3.** The count of disagreements n10 + n01 is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 5.

**4.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**5.** The Jaccard coefficient Jc(x1,x2) is approximately 0.136.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.286, not 0.136.

---

## Question 141 · Outlier Detection

Consider the 2-D points [[4, 4], [3, 4], [4, 6], [4, 2], [7, 2], [3, 5], [13, 17]]. Which statements are correct?

**1.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

**2.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

**3.** Point 6 (the far point) receives the largest LOF, consistent with being an outlier.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF values ≈ [0.84, 1.07, 1.29, 1.63, 2.15, 1.04, 9.44]; the isolated point has LOF ≫ 1.

**4.** The weighted KNN outlier score averages a point's distances to all its 1st…k-th nearest neighbours.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] Weighted-kNN aggregates (averages) the 1..k NN distances; plain kNN uses only the k-th.

**5.** The unweighted KNN outlier scores with k=1 (per point, in order) are [1.0, 1.0, 2.41, 2.0, 3.0, 1.0, 14.21].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [1.0, 1.0, 1.41, 2.0, 3.0, 1.0, 14.21], not [1.0, 1.0, 2.41, 2.0, 3.0, 1.0, 14.21].

---

## Question 142 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[0, 1], [0, 0], [0, 2], [3, 1], [10, 8], [9, 11], [9, 11], [10, 8]] with initial prototypes [[0, 1], [9, 11]]. Which statements are correct?

**1.** The final SSE (sum of squared errors) of the partition is approximately 18.75.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 18.75.

**2.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**3.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**4.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.822, not 1.

**5.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

---

## Question 143 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[2, 3], [1, 1], [2, 2], [3, 0], [10, 8], [10, 8], [10, 8], [11, 9]] with initial prototypes [[2, 3], [10, 8]]. Which statements are correct?

**1.** The final cluster labels (one per point, in order) are [0, 1, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 1, 0, 0, 1, 1, 1, 1].

**2.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.772.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.872, not 0.772.

**3.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**4.** The final SSE (sum of squared errors) of the partition is approximately 8.5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 8.5.

**5.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

---

## Question 144 · Data Representation

Consider two records described by 4 numerical variables: u = [-2, 0, 8, 3] and v = [2, -4, -3, -5]. Which statements are correct?

**1.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

**2.** The Manhattan (city-block) distance d(u,v) is approximately 26.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 27, not 26.

**3.** The Euclidean distance d(u,v) is approximately 14.73.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 14.73.

**4.** The inner product <u,v> is approximately -42.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ -43, not -42.

**5.** The Minkowski distance of order p=3 between u and v is approximately 12.54.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 12.54.

---

## Question 145 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0191 and 0.0042, with priors π_C1 = 0.2 and π_C2 = 0.8. Which statements are correct?

**1.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**2.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**3.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**4.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

**5.** The posterior probability (responsibility) of C2 at x is approximately 0.468.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.468.

---

## Question 146 · Outlier Detection

Consider the 2-D points [[1, 1], [7, 3], [5, 0], [1, 0], [1, 6], [3, 5], [16, 16]]. Which statements are correct?

**1.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

**2.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

**3.** Point 6 (the far point) receives the largest LOF, consistent with being an outlier.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF values ≈ [0.98, 0.96, 1.02, 0.98, 1.09, 1.07, 3.7]; the isolated point has LOF ≫ 1.

**4.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

**5.** The unweighted KNN outlier scores with k=2 (per point, in order) are [5.12, 4.47, 4.0, 4.0, 5.0, 4.47, 17.03].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [4.12, 4.47, 4.0, 4.0, 5.0, 4.47, 17.03], not [5.12, 4.47, 4.0, 4.0, 5.0, 4.47, 17.03].

---

## Question 147 · Data Representation

Consider two records described by 3 numerical variables: u = [6, -2, -2] and v = [-3, -1, 6]. Which statements are correct?

**1.** The Euclidean distance d(u,v) is approximately 12.08.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 12.08.

**2.** The Minkowski distance of order p=3 between u and v is approximately 10.75.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 10.75.

**3.** The cosine similarity cos(u,v) is approximately -0.622.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ -0.622.

**4.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

**5.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

---

## Question 148 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-26, -23, -20, 58, 65, 73, 77, 89}. Which statements are correct?

**1.** The MLE estimate of the mean μ is approximately 36.62.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 36.62.

**2.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [3, 3, 3, 7, 7, 4, 4, 12].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] The values are [3, 3, 3, 7, 7, 4, 4, 12].

**3.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**4.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 36.62, σ̂² = (1/n)Σ(x−μ̂)² ≈ 2205.23.

**5.** The MLE estimate of the variance σ² (dividing by n) is approximately 2205.08.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 2205.23, not 2205.08.

---

## Question 149 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 6). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BREAD, CRACKERS |
| 2 | BEER, CRACKERS |
| 3 | BEER, BREAD, BUTTER, CRACKERS, EGGS |
| 4 | CRACKERS, EGGS |
| 5 | BEER, BREAD, BUTTER, CRACKERS, EGGS |
| 6 | BEER, BREAD, EGGS |
| 7 | BEER, BREAD, CRACKERS, JAM |
| 8 | BREAD, EGGS, JAM |
| 9 | BREAD, BUTTER |
| 10 | BEER, BREAD, BUTTER, CRACKERS, EGGS |

**1.** The frequent itemset {CRACKERS} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

**2.** The support count of {BUTTER} is approximately 4.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 4.

**3.** The lift of the rule {CRACKERS} ⇒ {BEER} is approximately 1.39.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 1.19, not 1.39.

**4.** The support count of the itemset {CRACKERS, BEER} is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 5, not 6.

**5.** With n distinct items the candidate search space contains 2^n possible itemsets.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Each item is in or out, giving 2^n itemsets — hence Apriori pruning is essential.

---

## Question 150 · Hierarchical

Consider 5 objects with the symmetric distance matrix (0-based indices):

```
[0, 2, 7, 4, 1]
[2, 0, 7, 3, 10]
[7, 7, 0, 4, 8]
[4, 3, 4, 0, 3]
[1, 10, 8, 3, 0]
```

Which statements are correct?

**1.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**2.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**3.** Using Single-Linkage, the first merge joins objects 0 and 4 at height 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (0,)+(4,) at 1.

**4.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**5.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

---

## Question 151 · Probability & Density

A test has sensitivity P(+|D)=0.95 and specificity 0.99; disease prevalence is P(D)=0.01. Also consider the sample [1, 6, 4, 6, 1]. Which statements are correct?

**1.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**2.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**3.** The sample variance (÷ n−1) of the listed sample is approximately 6.15.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 6.3, not 6.15.

**4.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**5.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

---

## Question 152 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 4). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | CRACKERS, EGGS, MILK |
| 2 | BREAD, CRACKERS, DIAPERS, MILK |
| 3 | BREAD, CRACKERS, DIAPERS, EGGS |
| 4 | BREAD, DIAPERS, EGGS |
| 5 | CRACKERS, EGGS |
| 6 | DIAPERS, EGGS, MILK |
| 7 | CRACKERS, EGGS |
| 8 | BREAD, CRACKERS, DIAPERS, EGGS, MILK |
| 9 | BREAD, CRACKERS, DIAPERS, EGGS, MILK |
| 10 | CRACKERS, DIAPERS |
| 11 | BREAD, CRACKERS, DIAPERS, EGGS, MILK |
| 12 | BREAD, CRACKERS, DIAPERS, MILK |
| 13 | BREAD, CRACKERS, DIAPERS, EGGS, MILK |
| 14 | DIAPERS, EGGS, MILK |

**1.** The lift of the rule {BREAD} ⇒ {MILK} is approximately 1.167.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 1.167.

**2.** By anti-monotonicity (downward closure), every subset of a frequent itemset is also frequent.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Apriori prunes any candidate having an infrequent subset before counting support.

**3.** The support count of the itemset {BREAD, MILK} is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 6.

**4.** The frequent itemset {CRACKERS} is maximal (it has no frequent superset).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Maximal = no superset reaches support 4.

**5.** The confidence of the rule {BREAD} ⇒ {MILK} is approximately 0.9.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 0.75, not 0.9.

---

## Question 153 · Hierarchical

Consider 4 objects with the symmetric distance matrix (0-based indices):

```
[0, 3, 2, 7]
[3, 0, 11, 10]
[2, 11, 0, 8]
[7, 10, 8, 0]
```

Which statements are correct?

**1.** Using Complete-Linkage, the height of the final (root) merge is approximately 8.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 11, not 8.

**2.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**3.** Using Single-Linkage, the height of the final (root) merge is approximately 9.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 7, not 9.

**4.** Using Single-Linkage, the first merge joins objects 0 and 2 at height 2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (0,)+(2,) at 2.

**5.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

---

## Question 154 · Probability & Density

A test has sensitivity P(+|D)=0.99 and specificity 0.9; disease prevalence is P(D)=0.02. Also consider the sample [2, 2, 3, 2, 2]. Which statements are correct?

**1.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**2.** The posterior P(D | +) by Bayes' rule is approximately 0.068.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.168, not 0.068.

**3.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**4.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**5.** The sample variance (÷ n−1) of the listed sample is approximately 0.1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.2, not 0.1.

---

## Question 155 · Outlier Detection

Consider the 2-D points [[2, 4], [5, 5], [1, 4], [6, 7], [6, 6], [1, 6], [15, 13]]. Which statements are correct?

**1.** The weighted KNN outlier score averages a point's distances to all its 1st…k-th nearest neighbours.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] Weighted-kNN aggregates (averages) the 1..k NN distances; plain kNN uses only the k-th.

**2.** The unweighted KNN outlier scores with k=2 (per point, in order) are [2.24, 2.24, 2.0, 3.24, 1.41, 2.24, 11.4].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [2.24, 2.24, 2.0, 2.24, 1.41, 2.24, 11.4], not [2.24, 2.24, 2.0, 3.24, 1.41, 2.24, 11.4].

**3.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

**4.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

**5.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

---

## Question 156 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 4). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BUTTER, DIAPERS, MILK |
| 2 | BEER, BUTTER, DIAPERS |
| 3 | BUTTER, CRACKERS, MILK |
| 4 | BEER, BREAD, BUTTER, CRACKERS, DIAPERS, MILK |
| 5 | BEER, BREAD, BUTTER, CRACKERS, DIAPERS, MILK |
| 6 | BREAD, MILK |
| 7 | BEER, BREAD, CRACKERS, MILK |
| 8 | BEER, BREAD, BUTTER, CRACKERS, DIAPERS, MILK |
| 9 | BEER, BREAD, CRACKERS, MILK |
| 10 | BEER, DIAPERS |
| 11 | BEER, BREAD, CRACKERS, DIAPERS, MILK |
| 12 | BEER, BREAD, BUTTER, CRACKERS, DIAPERS, MILK |

**1.** Apriori must scan the database to count the support of a candidate even when one of its subsets is already known to be infrequent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The prune step removes such candidates first, so no database scan is needed for them.

**2.** By anti-monotonicity (downward closure), every subset of a frequent itemset is also frequent.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Apriori prunes any candidate having an infrequent subset before counting support.

**3.** The confidence of the rule {DIAPERS} ⇒ {BEER} is approximately 0.975.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 0.875, not 0.975.

**4.** The support count of {BUTTER} is approximately 8.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 7, not 8.

**5.** The support count of the itemset {DIAPERS, BEER} is approximately 9.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 7, not 9.

---

## Question 157 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[2, 1], [2, 1], [2, 1], [1, 3], [9, 8], [9, 11], [10, 8], [8, 10]] with initial prototypes [[2, 1], [9, 11]]. Which statements are correct?

**1.** The final cluster labels (one per point, in order) are [0, 0, 0, 1, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 0, 0, 1, 1, 1, 1, 1].

**2.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**3.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.741.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.841, not 0.741.

**4.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**5.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

---

## Question 158 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 6). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, BREAD, DIAPERS, JAM, MILK |
| 2 | BEER, BREAD, BUTTER, JAM, MILK |
| 3 | BEER, BREAD, BUTTER, DIAPERS, JAM, MILK |
| 4 | BREAD, BUTTER |
| 5 | BEER, BREAD, BUTTER |
| 6 | BEER, BREAD, DIAPERS, JAM, MILK |
| 7 | BEER, BREAD, MILK |
| 8 | BUTTER, DIAPERS, JAM, MILK |
| 9 | BUTTER, DIAPERS, JAM |
| 10 | BEER, DIAPERS |

**1.** By anti-monotonicity (downward closure), every subset of a frequent itemset is also frequent.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Apriori prunes any candidate having an infrequent subset before counting support.

**2.** The frequent itemset {DIAPERS} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

**3.** Confidence of X ⇒ Y is defined as support(X ∪ Y) / support(Y).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Confidence = support(X∪Y)/support(X) (divide by the antecedent's support).

**4.** The frequent itemset {DIAPERS} is maximal (it has no frequent superset).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Maximal = no superset reaches support 6.

**5.** With n distinct items the candidate search space contains 2^n possible itemsets.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Each item is in or out, giving 2^n itemsets — hence Apriori pruning is essential.

---

## Question 159 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-28, -16, -3, -2, 0, 70, 83}. Which statements are correct?

**1.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**2.** The MLE estimate of the variance σ² (dividing by n) is approximately 1613.84.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 1613.84.

**3.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 14.86, σ̂² = (1/n)Σ(x−μ̂)² ≈ 1613.84.

**4.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**5.** The MLE estimate of the mean μ is approximately 14.36.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 14.86, not 14.36.

---

## Question 160 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.02 and 0.0104, with priors π_C1 = 0.6 and π_C2 = 0.4. Which statements are correct?

**1.** The posterior probability (responsibility) of C2 at x is approximately 0.257.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.257.

**2.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**3.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

**4.** The posterior probability (responsibility) of C1 at x is approximately 0.643.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The correct value is ≈ 0.743, not 0.643.

**5.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

---

## Question 161 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0074 and 0.0177, with priors π_C1 = 0.2 and π_C2 = 0.8. Which statements are correct?

**1.** The posterior probability (responsibility) of C1 at x is approximately 0.095.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.095.

**2.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**3.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

**4.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**5.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

---

## Question 162 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[1, 3], [3, 1], [0, 1], [2, 0], [10, 8], [10, 9], [8, 8], [9, 9]] with initial prototypes [[1, 3], [10, 9]]. Which statements are correct?

**1.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 1, 2, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 0, 0, 0, 1, 2, 1, 1].

**2.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**3.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**4.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.811.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 0.811.

**5.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

---

## Question 163 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[2, 2], [0, 3], [3, 2], [2, 0], [11, 10], [9, 10], [8, 11], [10, 8]] with initial prototypes [[2, 2], [9, 10]]. Which statements are correct?

**1.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.887.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.787, not 0.887.

**2.** The final SSE (sum of squared errors) of the partition is approximately 18.95.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 19.25, not 18.95.

**3.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**4.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**5.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

---

## Question 164 · Probability & Density

A test has sensitivity P(+|D)=0.99 and specificity 0.9; disease prevalence is P(D)=0.01. Also consider the sample [4, 2, 4, 5, 6]. Which statements are correct?

**1.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**2.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**3.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**4.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**5.** The sample mean of the listed sample is approximately 4.7.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 4.2, not 4.7.

---

## Question 165 · Hierarchical

Consider 5 objects with the symmetric distance matrix (0-based indices):

```
[0, 1, 3, 2, 10]
[1, 0, 2, 12, 8]
[3, 2, 0, 1, 6]
[2, 12, 1, 0, 9]
[10, 8, 6, 9, 0]
```

Which statements are correct?

**1.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**2.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**3.** Using Single-Linkage, the first merge joins objects 0 and 1 at height 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (0,)+(1,) at 1.

**4.** Using Complete-Linkage, the height of the final (root) merge is approximately 12.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 12.

**5.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

---

## Question 166 · Probability & Density

A test has sensitivity P(+|D)=0.95 and specificity 0.9; disease prevalence is P(D)=0.1. Also consider the sample [1, 3, 5, 3, 3]. Which statements are correct?

**1.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**2.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**3.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**4.** The sample mean of the listed sample is approximately 2.5.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 3.0, not 2.5.

**5.** The posterior P(D | +) by Bayes' rule is approximately 1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.514, not 1.

---

## Question 167 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-24, 15, 26, 66, 71, 85}. Which statements are correct?

**1.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**2.** With ε = 25 and MinPts = 2, DBSCAN groups the data into the clusters [[15, 26], [66, 71, 85]] with [-24] as noise.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=25, MinPts=2) gives clusters [[15, 26], [66, 71, 85]]; noise = [-24].

**3.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**4.** The MLE estimate of the mean μ is approximately 39.63.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 39.83, not 39.63.

**5.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

---

## Question 168 · Hierarchical

Consider 5 objects with the symmetric distance matrix (0-based indices):

```
[0, 10, 7, 10, 6]
[10, 0, 12, 10, 8]
[7, 12, 0, 2, 5]
[10, 10, 2, 0, 8]
[6, 8, 5, 8, 0]
```

Which statements are correct?

**1.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

**2.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**3.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**4.** Using Single-Linkage, the height of the final (root) merge is approximately 8.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 8.

**5.** Using Complete-Linkage, the height of the final (root) merge is approximately 10.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 12, not 10.

---

## Question 169 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-29, -13, 6, 29, 32, 48, 64, 109}. Which statements are correct?

**1.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**2.** With ε = 25 and MinPts = 2, DBSCAN groups the data into the clusters [[-29, -13, 6, 29, 32, 48, 64]] with [109] as noise.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=25, MinPts=2) gives clusters [[-29, -13, 6, 29, 32, 48, 64]]; noise = [109].

**3.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**4.** The MLE estimate of the variance σ² (dividing by n) is approximately 1703.29.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 1703.44, not 1703.29.

**5.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [16, 16, 3, 19, 3, 16, 16, 45].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [16, 16, 19, 3, 3, 16, 16, 45], not [16, 16, 3, 19, 3, 16, 16, 45].

---

## Question 170 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[0, 2], [1, 3], [3, 1], [3, 3], [8, 10], [11, 9], [10, 10], [11, 8]] with initial prototypes [[0, 2], [11, 9]]. Which statements are correct?

**1.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**2.** The final cluster labels (one per point, in order) are [0, 1, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 1, 0, 0, 1, 1, 1, 1].

**3.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**4.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**5.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.785.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 0.785.

---

## Question 171 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 6). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, BUTTER, CRACKERS, MILK |
| 2 | BEER, BUTTER, CRACKERS, JAM, MILK |
| 3 | CRACKERS, JAM |
| 4 | BUTTER, JAM, MILK |
| 5 | BEER, CRACKERS, JAM, MILK |
| 6 | BEER, CRACKERS, JAM, MILK |
| 7 | BEER, BUTTER, CRACKERS, MILK |
| 8 | BUTTER, CRACKERS, JAM, MILK |
| 9 | BEER, CRACKERS, MILK |
| 10 | BUTTER, CRACKERS, JAM |

**1.** With n distinct items the candidate search space contains 2^n possible itemsets.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Each item is in or out, giving 2^n itemsets — hence Apriori pruning is essential.

**2.** The support count of {JAM} is approximately 8.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 7, not 8.

**3.** Apriori must scan the database to count the support of a candidate even when one of its subsets is already known to be infrequent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The prune step removes such candidates first, so no database scan is needed for them.

**4.** The confidence of the rule {MILK} ⇒ {CRACKERS} is approximately 1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 0.875, not 1.

**5.** The frequent itemset {BUTTER} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

---

## Question 172 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[0, 3], [2, 0], [1, 1], [0, 2], [11, 8], [10, 8], [8, 8], [11, 11]] with initial prototypes [[0, 3], [10, 8]]. Which statements are correct?

**1.** The final cluster labels (one per point, in order) are [0, 0, 1, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 0, 1, 0, 1, 1, 1, 1].

**2.** The final SSE (sum of squared errors) of the partition is approximately 20.5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 20.5.

**3.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.796.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 0.796.

**4.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**5.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

---

## Question 173 · Outlier Detection

Consider the 2-D points [[2, 1], [3, 7], [5, 4], [7, 3], [2, 3], [1, 6], [17, 16]]. Which statements are correct?

**1.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

**2.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

**3.** LOF is a global density score that compares each point's density to the dataset-wide average density.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] LOF is a LOCAL/relative score: density vs the point's own neighbours.

**4.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

**5.** The unweighted KNN outlier scores with k=1 (per point, in order) are [3.0, 2.24, 2.24, 2.24, 2.0, 2.24, 16.4].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [2.0, 2.24, 2.24, 2.24, 2.0, 2.24, 16.4], not [3.0, 2.24, 2.24, 2.24, 2.0, 2.24, 16.4].

---

## Question 174 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0121 and 0.004, with priors π_C1 = 0.7 and π_C2 = 0.3. Which statements are correct?

**1.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

**2.** The posterior probability (responsibility) of C1 at x is approximately 0.576.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The correct value is ≈ 0.876, not 0.576.

**3.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**4.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**5.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

---

## Question 175 · Probability & Density

A test has sensitivity P(+|D)=0.9 and specificity 0.99; disease prevalence is P(D)=0.05. Also consider the sample [1, 2, 3, 1, 3]. Which statements are correct?

**1.** The sample mean of the listed sample is approximately 2.5.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 2.0, not 2.5.

**2.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**3.** The sample variance (÷ n−1) of the listed sample is approximately 1.15.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 1.0, not 1.15.

**4.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**5.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

---

## Question 176 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0054 and 0.0107, with priors π_C1 = 0.7 and π_C2 = 0.3. Which statements are correct?

**1.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

**2.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**3.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**4.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

**5.** The posterior probability (responsibility) of C1 at x is approximately 0.241.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The correct value is ≈ 0.541, not 0.241.

---

## Question 177 · Probability & Density

A test has sensitivity P(+|D)=0.95 and specificity 0.95; disease prevalence is P(D)=0.02. Also consider the sample [2, 1, 6, 6, 6]. Which statements are correct?

**1.** The sample mean of the listed sample is approximately 4.2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 4.2.

**2.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**3.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**4.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**5.** The sample variance (÷ n−1) of the listed sample is approximately 6.5.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 6.2, not 6.5.

---

## Question 178 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[2, 1], [0, 3], [3, 3], [2, 1], [8, 11], [10, 9], [11, 10], [9, 8]] with initial prototypes [[2, 1], [10, 9]]. Which statements are correct?

**1.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**2.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**3.** The final SSE (sum of squared errors) of the partition is approximately 18.75.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 18.75.

**4.** The final cluster labels (one per point, in order) are [1, 0, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [1, 0, 0, 0, 1, 1, 1, 1].

**5.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.784.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 0.784.

---

## Question 179 · Data Representation

Consider two records described by 5 numerical variables: u = [7, 1, 7, 2, 9] and v = [8, 6, 9, 8, -4]. Which statements are correct?

**1.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

**2.** The Manhattan (city-block) distance d(u,v) is approximately 26.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 27, not 26.

**3.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

**4.** The inner product <u,v> is approximately 105.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 105.

**5.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

---

## Question 180 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-4, -2, 3, 13, 63, 78}. Which statements are correct?

**1.** The MLE estimate of the variance σ² (dividing by n) is approximately 1075.14.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 1075.14.

**2.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**3.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**4.** The MLE estimate of the mean μ is approximately 25.07.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 25.17, not 25.07.

**5.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 25.17, σ̂² = (1/n)Σ(x−μ̂)² ≈ 1075.14.

---

## Question 181 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-3, 0, 36, 47, 71, 84}. Which statements are correct?

**1.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**2.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**3.** The MLE estimate of the mean μ is approximately 39.17.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 39.17.

**4.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**5.** The MLE estimate of the variance σ² (dividing by n) is approximately 1067.81.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 1067.81.

---

## Question 182 · Outlier Detection

Consider the 2-D points [[6, 2], [6, 5], [7, 6], [0, 5], [1, 6], [7, 5], [14, 15]]. Which statements are correct?

**1.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

**2.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

**3.** Point 6 (the far point) receives the largest LOF, consistent with being an outlier.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF values ≈ [2.37, 0.93, 0.93, 2.8, 2.8, 1.17, 9.06]; the isolated point has LOF ≫ 1.

**4.** LOF is a global density score that compares each point's density to the dataset-wide average density.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] LOF is a LOCAL/relative score: density vs the point's own neighbours.

**5.** The unweighted KNN outlier scores with k=1 (per point, in order) are [3.0, 1.0, 1.0, 1.41, 1.41, 1.0, 11.4].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] The values are [3.0, 1.0, 1.0, 1.41, 1.41, 1.0, 11.4].

---

## Question 183 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0055 and 0.0195, with priors π_C1 = 0.2 and π_C2 = 0.8. Which statements are correct?

**1.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**2.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

**3.** The posterior probability (responsibility) of C2 at x is approximately 0.784.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The correct value is ≈ 0.934, not 0.784.

**4.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**5.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

---

## Question 184 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0127 and 0.0048, with priors π_C1 = 0.3 and π_C2 = 0.7. Which statements are correct?

**1.** The posterior probability (responsibility) of C1 at x is approximately 0.831.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The correct value is ≈ 0.531, not 0.831.

**2.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**3.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

**4.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**5.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

---

## Question 185 · Outlier Detection

Consider the 2-D points [[0, 7], [5, 5], [7, 1], [4, 6], [1, 7], [4, 7], [17, 14]]. Which statements are correct?

**1.** The unweighted KNN outlier scores with k=1 (per point, in order) are [1.0, 1.41, 4.47, 1.0, 1.0, 1.0, 14.76].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] The values are [1.0, 1.41, 4.47, 1.0, 1.0, 1.0, 14.76].

**2.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

**3.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

**4.** The weighted KNN outlier score averages a point's distances to all its 1st…k-th nearest neighbours.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] Weighted-kNN aggregates (averages) the 1..k NN distances; plain kNN uses only the k-th.

**5.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

---

## Question 186 · Hierarchical

Consider 4 objects with the symmetric distance matrix (0-based indices):

```
[0, 3, 3, 5]
[3, 0, 3, 4]
[3, 3, 0, 7]
[5, 4, 7, 0]
```

Which statements are correct?

**1.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

**2.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**3.** Using Single-Linkage, the height of the final (root) merge is approximately 4.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 4.

**4.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**5.** Using Single-Linkage, the first merge joins objects 0 and 1 at height 3.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (0,)+(1,) at 3.

---

## Question 187 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-25, -11, 6, 24, 28, 82, 106}. Which statements are correct?

**1.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**2.** The MLE estimate of the variance σ² (dividing by n) is approximately 1971.71.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 1971.71.

**3.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**4.** With ε = 10 and MinPts = 2, DBSCAN groups the data into the clusters [[24, 28]] with [-25, -11, 6, 82, 106] as noise.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=10, MinPts=2) gives clusters [[24, 28]]; noise = [-25, -11, 6, 82, 106].

**5.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

---

## Question 188 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0042 and 0.0106, with priors π_C1 = 0.6 and π_C2 = 0.4. Which statements are correct?

**1.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

**2.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

**3.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**4.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

**5.** The posterior probability (responsibility) of C2 at x is approximately 0.627.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.627.

---

## Question 189 · Hierarchical

Consider 4 objects with the symmetric distance matrix (0-based indices):

```
[0, 10, 1, 10]
[10, 0, 3, 5]
[1, 3, 0, 12]
[10, 5, 12, 0]
```

Which statements are correct?

**1.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

**2.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**3.** Using Single-Linkage, the height of the final (root) merge is approximately 2.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 5, not 2.

**4.** Using Single-Linkage, the first merge joins objects 0 and 2 at height 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (0,)+(2,) at 1.

**5.** Using Complete-Linkage, the height of the final (root) merge is approximately 12.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 12.

---

## Question 190 · Outlier Detection

Consider the 2-D points [[7, 4], [0, 4], [3, 1], [5, 4], [2, 6], [7, 2], [12, 15]]. Which statements are correct?

**1.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

**2.** LOF is a global density score that compares each point's density to the dataset-wide average density.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] LOF is a LOCAL/relative score: density vs the point's own neighbours.

**3.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

**4.** The weighted KNN outlier score averages a point's distances to all its 1st…k-th nearest neighbours.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] Weighted-kNN aggregates (averages) the 1..k NN distances; plain kNN uses only the k-th.

**5.** The unweighted KNN outlier scores with k=2 (per point, in order) are [2.0, 4.24, 4.12, 2.83, 3.61, 2.83, 13.04].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] The values are [2.0, 4.24, 4.12, 2.83, 3.61, 2.83, 13.04].

---

## Question 191 · Probability & Density

A test has sensitivity P(+|D)=0.9 and specificity 0.95; disease prevalence is P(D)=0.05. Also consider the sample [3, 1, 4, 5, 1]. Which statements are correct?

**1.** The sample variance (÷ n−1) of the listed sample is approximately 3.4.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 3.2, not 3.4.

**2.** The posterior P(D | +) by Bayes' rule is approximately 0.186.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.486, not 0.186.

**3.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**4.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**5.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

---

## Question 192 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-20, 27, 54, 57, 73, 98}. Which statements are correct?

**1.** The MLE estimate of the mean μ is approximately 48.27.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 48.17, not 48.27.

**2.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 48.17, σ̂² = (1/n)Σ(x−μ̂)² ≈ 1384.47.

**3.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**4.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**5.** With ε = 20 and MinPts = 2, DBSCAN groups the data into the clusters [[54, 57, 73]] with [-20, 27, 98] as noise.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=20, MinPts=2) gives clusters [[54, 57, 73]]; noise = [-20, 27, 98].

---

## Question 193 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 4). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BREAD, DIAPERS, EGGS, MILK |
| 2 | EGGS, JAM, MILK |
| 3 | DIAPERS, EGGS |
| 4 | BEER, BREAD, EGGS, JAM, MILK |
| 5 | DIAPERS, EGGS |
| 6 | BREAD, DIAPERS, EGGS, JAM |
| 7 | BEER, BREAD, MILK |
| 8 | BEER, BREAD, DIAPERS, EGGS, JAM, MILK |
| 9 | BEER, DIAPERS, EGGS |
| 10 | BEER, BREAD, DIAPERS, EGGS, JAM, MILK |
| 11 | BEER, BREAD, DIAPERS, EGGS, JAM, MILK |
| 12 | BEER, DIAPERS, EGGS |

**1.** By anti-monotonicity (downward closure), every subset of a frequent itemset is also frequent.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Apriori prunes any candidate having an infrequent subset before counting support.

**2.** The lift of the rule {BREAD} ⇒ {DIAPERS} is approximately 0.652.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 0.952, not 0.652.

**3.** Confidence of X ⇒ Y is defined as support(X ∪ Y) / support(Y).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Confidence = support(X∪Y)/support(X) (divide by the antecedent's support).

**4.** With n distinct items the candidate search space contains 2^n possible itemsets.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Each item is in or out, giving 2^n itemsets — hence Apriori pruning is essential.

**5.** Apriori must scan the database to count the support of a candidate even when one of its subsets is already known to be infrequent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The prune step removes such candidates first, so no database scan is needed for them.

---

## Question 194 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[1, 1], [0, 2], [2, 2], [1, 2], [11, 8], [11, 11], [11, 8], [8, 8]] with initial prototypes [[1, 1], [11, 11]]. Which statements are correct?

**1.** The final SSE (sum of squared errors) of the partition is approximately 16.55.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 16.25, not 16.55.

**2.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**3.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.925.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.825, not 0.925.

**4.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**5.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

---

## Question 195 · Probability & Density

A test has sensitivity P(+|D)=0.95 and specificity 0.99; disease prevalence is P(D)=0.1. Also consider the sample [1, 6, 6, 4, 5]. Which statements are correct?

**1.** The posterior P(D | +) by Bayes' rule is approximately 1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.913, not 1.

**2.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**3.** The sample mean of the listed sample is approximately 4.4.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 4.4.

**4.** The sample variance (÷ n−1) of the listed sample is approximately 4.3.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 4.3.

**5.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

---

## Question 196 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0174 and 0.0142, with priors π_C1 = 0.2 and π_C2 = 0.8. Which statements are correct?

**1.** The posterior probability (responsibility) of C1 at x is approximately 0.235.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.235.

**2.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**3.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

**4.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**5.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

---

## Question 197 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-30, 2, 4, 17, 59, 70, 76}. Which statements are correct?

**1.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**2.** With ε = 20 and MinPts = 1, DBSCAN groups the data into the clusters [[-30], [2, 4, 17], [59, 70, 76]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=20, MinPts=1) gives clusters [[-30], [2, 4, 17], [59, 70, 76]]; no noise.

**3.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**4.** The MLE estimate of the mean μ is approximately 28.29.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 28.29.

**5.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 28.29, σ̂² = (1/n)Σ(x−μ̂)² ≈ 1395.06.

---

## Question 198 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0132 and 0.0096, with priors π_C1 = 0.7 and π_C2 = 0.3. Which statements are correct?

**1.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**2.** The posterior probability (responsibility) of C1 at x is approximately 0.762.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.762.

**3.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**4.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

**5.** The posterior probability (responsibility) of C2 at x is approximately 0.238.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.238.

---

## Question 199 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {67, 80, 81, 86, 87, 88}. Which statements are correct?

**1.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**2.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**3.** With ε = 20 and MinPts = 1, DBSCAN groups the data into the clusters [[67, 80, 81, 86, 87, 88]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=20, MinPts=1) gives clusters [[67, 80, 81, 86, 87, 88]]; no noise.

**4.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**5.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 81.5, σ̂² = (1/n)Σ(x−μ̂)² ≈ 50.92.

---

## Question 200 · Hierarchical

Consider 5 objects with the symmetric distance matrix (0-based indices):

```
[0, 3, 6, 4, 2]
[3, 0, 6, 4, 2]
[6, 6, 0, 7, 6]
[4, 4, 7, 0, 1]
[2, 2, 6, 1, 0]
```

Which statements are correct?

**1.** Using Single-Linkage, the height of the final (root) merge is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 6.

**2.** Using Complete-Linkage, the height of the final (root) merge is approximately 9.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 7, not 9.

**3.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**4.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**5.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

---

## Question 201 · Data Representation

Consider two records described by 4 numerical variables: u = [4, -3, 3, -1] and v = [7, 3, 5, 6]. Which statements are correct?

**1.** The cosine similarity cos(u,v) is approximately 0.434.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.434.

**2.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

**3.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

**4.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

**5.** The inner product <u,v> is approximately 28.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 28.

---

## Question 202 · Data Representation

Two objects are described by 8 binary (asymmetric/symmetric) variables: x1 = [0, 0, 1, 0, 0, 0, 0, 1] and x2 = [0, 0, 1, 1, 1, 1, 0, 0]. Which statements are correct?

**1.** The count of 1–1 matches n11 is approximately 2.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 1, not 2.

**2.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**3.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**4.** The Simple Matching Coefficient SMC(x1,x2) is approximately 1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.5, not 1.

**5.** The Jaccard coefficient Jc(x1,x2) is approximately 0.2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.2.

---

## Question 203 · Data Representation

Consider two records described by 3 numerical variables: u = [-3, -1, 0] and v = [6, -4, -5]. Which statements are correct?

**1.** The Suprema (Chebyshev) distance d(u,v) is approximately 9.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 9.

**2.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**3.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

**4.** The Minkowski distance of order p=3 between u and v is approximately 9.44.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 9.59, not 9.44.

**5.** The Manhattan (city-block) distance d(u,v) is approximately 17.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 17.

---

## Question 204 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-14, -13, 46, 50, 52, 79, 84}. Which statements are correct?

**1.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**2.** The MLE estimate of the variance σ² (dividing by n) is approximately 1351.39.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 1351.39.

**3.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [1, 1, 4, 2, 2, 5, 5].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] The values are [1, 1, 4, 2, 2, 5, 5].

**4.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**5.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

---

## Question 205 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[0, 3], [2, 3], [0, 2], [1, 3], [11, 8], [10, 11], [10, 9], [9, 9]] with initial prototypes [[0, 3], [10, 11]]. Which statements are correct?

**1.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**2.** The final SSE (sum of squared errors) of the partition is approximately 10.25.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 10.25.

**3.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**4.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**5.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

---

## Question 206 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[0, 0], [3, 2], [0, 1], [1, 0], [8, 8], [9, 10], [8, 11], [8, 9]] with initial prototypes [[0, 0], [9, 10]]. Which statements are correct?

**1.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**2.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**3.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**4.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.819.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 0.819.

**5.** The final SSE (sum of squared errors) of the partition is approximately 14.5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 14.5.

---

## Question 207 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {18, 44, 54, 64, 94, 108}. Which statements are correct?

**1.** The MLE estimate of the mean μ is approximately 63.67.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 63.67.

**2.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [14, 10, 10, 10, 26, 14].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [26, 10, 10, 10, 14, 14], not [14, 10, 10, 10, 26, 14].

**3.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**4.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**5.** With ε = 15 and MinPts = 1, DBSCAN groups the data into the clusters [[18], [44, 54, 64], [94, 108]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=15, MinPts=1) gives clusters [[18], [44, 54, 64], [94, 108]]; no noise.

---

## Question 208 · Data Representation

Consider two records described by 5 numerical variables: u = [-5, 3, 8, 0, 4] and v = [-1, 6, -5, 0, 1]. Which statements are correct?

**1.** The Euclidean distance d(u,v) is approximately 14.35.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 14.25, not 14.35.

**2.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**3.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

**4.** The Manhattan (city-block) distance d(u,v) is approximately 23.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 23.

**5.** The Suprema (Chebyshev) distance d(u,v) is approximately 13.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 13.

---

## Question 209 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 5). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, BREAD, CRACKERS, MILK |
| 2 | BEER, BREAD, CRACKERS, MILK |
| 3 | BEER, BREAD, BUTTER, CRACKERS, DIAPERS, MILK |
| 4 | BEER, BREAD, BUTTER, DIAPERS |
| 5 | BREAD, CRACKERS |
| 6 | BEER, BREAD, BUTTER, CRACKERS, DIAPERS |
| 7 | BEER, BREAD, BUTTER, CRACKERS, DIAPERS, MILK |
| 8 | BEER, BREAD |
| 9 | BREAD, CRACKERS, DIAPERS, MILK |
| 10 | BREAD, BUTTER, DIAPERS |
| 11 | BREAD, BUTTER, CRACKERS, DIAPERS, MILK |
| 12 | BEER, BREAD, CRACKERS, DIAPERS |
| 13 | BEER, BREAD, CRACKERS, DIAPERS |
| 14 | BEER, BREAD, BUTTER |

**1.** The lift of the rule {BUTTER} ⇒ {BREAD} is approximately 0.8.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 1.0, not 0.8.

**2.** Apriori must scan the database to count the support of a candidate even when one of its subsets is already known to be infrequent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The prune step removes such candidates first, so no database scan is needed for them.

**3.** The frequent itemset {CRACKERS} is maximal (it has no frequent superset).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Maximal = no superset reaches support 5.

**4.** The frequent itemset {CRACKERS} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

**5.** The support count of {BUTTER} is approximately 7.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 7.

---

## Question 210 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-22, -20, 2, 15, 33, 45, 99}. Which statements are correct?

**1.** The MLE estimate of the mean μ is approximately 21.71.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 21.71.

**2.** The MLE estimate of the variance σ² (dividing by n) is approximately 1532.49.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 1532.49.

**3.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**4.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [3, 2, 13, 13, 12, 12, 54].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [2, 2, 13, 13, 12, 12, 54], not [3, 2, 13, 13, 12, 12, 54].

**5.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 21.71, σ̂² = (1/n)Σ(x−μ̂)² ≈ 1532.49.

---

## Question 211 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[1, 3], [3, 3], [2, 1], [1, 0], [11, 8], [9, 10], [9, 8], [11, 9]] with initial prototypes [[1, 3], [9, 10]]. Which statements are correct?

**1.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.793.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 0.793.

**2.** The final SSE (sum of squared errors) of the partition is approximately 16.25.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 16.25.

**3.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] The values are [0, 0, 0, 0, 1, 1, 1, 1].

**4.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**5.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

---

## Question 212 · Data Representation

Two objects are described by 12 binary (asymmetric/symmetric) variables: x1 = [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0] and x2 = [1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0]. Which statements are correct?

**1.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**2.** The Jaccard coefficient Jc(x1,x2) is approximately 0.429.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.429.

**3.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.567.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.667, not 0.567.

**4.** The count of disagreements n10 + n01 is approximately 7.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 4, not 7.

**5.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

---

## Question 213 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[3, 0], [1, 0], [1, 0], [1, 3], [9, 8], [9, 9], [8, 10], [10, 8]] with initial prototypes [[3, 0], [9, 9]]. Which statements are correct?

**1.** The final cluster labels (one per point, in order) are [0, 1, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 1, 0, 0, 1, 1, 1, 1].

**2.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.321.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.821, not 0.321.

**3.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**4.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**5.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

---

## Question 214 · Outlier Detection

Consider the 2-D points [[0, 7], [0, 0], [6, 1], [6, 4], [6, 3], [4, 7], [13, 15]]. Which statements are correct?

**1.** Point 6 (the far point) receives the largest LOF, consistent with being an outlier.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF values ≈ [1.59, 2.35, 0.92, 0.92, 1.2, 1.51, 3.72]; the isolated point has LOF ≫ 1.

**2.** The weighted KNN outlier score averages a point's distances to all its 1st…k-th nearest neighbours.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] Weighted-kNN aggregates (averages) the 1..k NN distances; plain kNN uses only the k-th.

**3.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

**4.** LOF is a global density score that compares each point's density to the dataset-wide average density.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] LOF is a LOCAL/relative score: density vs the point's own neighbours.

**5.** The unweighted KNN outlier scores with k=2 (per point, in order) are [6.71, 6.71, 3.0, 3.0, 2.0, 4.0, 13.04].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] The values are [6.71, 6.71, 3.0, 3.0, 2.0, 4.0, 13.04].

---

## Question 215 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[1, 0], [1, 2], [1, 3], [2, 3], [10, 11], [8, 11], [9, 9], [11, 11]] with initial prototypes [[1, 0], [8, 11]]. Which statements are correct?

**1.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 1, 2, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 0, 0, 0, 1, 2, 1, 1].

**2.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**3.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**4.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**5.** The final SSE (sum of squared errors) of the partition is approximately 14.9.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 14.75, not 14.9.

---

## Question 216 · Data Representation

Two objects are described by 8 binary (asymmetric/symmetric) variables: x1 = [1, 1, 1, 0, 0, 1, 0, 0] and x2 = [1, 1, 0, 0, 0, 1, 0, 1]. Which statements are correct?

**1.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.95.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.75, not 0.95.

**2.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**3.** The count of disagreements n10 + n01 is approximately 0.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 2, not 0.

**4.** The Jaccard coefficient Jc(x1,x2) is approximately 0.45.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.6, not 0.45.

**5.** The count of 1–1 matches n11 is approximately 0.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 3, not 0.

---

## Question 217 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {9, 44, 57, 63, 75, 76, 98}. Which statements are correct?

**1.** The MLE estimate of the mean μ is approximately 60.29.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 60.29.

**2.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**3.** With ε = 15 and MinPts = 2, DBSCAN groups the data into the clusters [[44, 57, 63, 75, 76]] with [9, 98] as noise.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=15, MinPts=2) gives clusters [[44, 57, 63, 75, 76]]; noise = [9, 98].

**4.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**5.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

---

## Question 218 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-4, 30, 77, 79, 91, 95}. Which statements are correct?

**1.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**2.** The MLE estimate of the variance σ² (dividing by n) is approximately 1303.06.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 1303.56, not 1303.06.

**3.** The MLE estimate of the mean μ is approximately 61.33.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 61.33.

**4.** With ε = 25 and MinPts = 2, DBSCAN groups the data into the clusters [[77, 79, 91, 95]] with [-4, 30] as noise.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=25, MinPts=2) gives clusters [[77, 79, 91, 95]]; noise = [-4, 30].

**5.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

---

## Question 219 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 5). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | DIAPERS, MILK |
| 2 | BEER, MILK |
| 3 | BEER, BREAD, DIAPERS, JAM |
| 4 | BEER, BREAD, DIAPERS, JAM |
| 5 | BREAD, DIAPERS, JAM |
| 6 | BEER, DIAPERS, JAM, MILK |
| 7 | BEER, DIAPERS |
| 8 | BEER, BREAD, DIAPERS |
| 9 | BEER, DIAPERS, JAM, MILK |
| 10 | BEER, BREAD, DIAPERS, JAM, MILK |

**1.** Apriori must scan the database to count the support of a candidate even when one of its subsets is already known to be infrequent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The prune step removes such candidates first, so no database scan is needed for them.

**2.** The support count of the itemset {BEER, MILK} is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 4, not 6.

**3.** The frequent itemset {DIAPERS} is maximal (it has no frequent superset).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Maximal = no superset reaches support 5.

**4.** The support count of {BREAD} is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 5.

**5.** By anti-monotonicity (downward closure), every subset of a frequent itemset is also frequent.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Apriori prunes any candidate having an infrequent subset before counting support.

---

## Question 220 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-14, -4, 9, 21, 39, 41, 71, 85}. Which statements are correct?

**1.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**2.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**3.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**4.** The MLE estimate of the mean μ is approximately 30.8.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 31.0, not 30.8.

**5.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [10, 10, 12, 14, 2, 2, 14, 12].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [10, 10, 12, 12, 2, 2, 14, 14], not [10, 10, 12, 14, 2, 2, 14, 12].

---

## Question 221 · Probability & Density

A test has sensitivity P(+|D)=0.95 and specificity 0.99; disease prevalence is P(D)=0.05. Also consider the sample [3, 3, 2, 2, 6]. Which statements are correct?

**1.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**2.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**3.** The sample variance (÷ n−1) of the listed sample is approximately 2.8.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 2.7, not 2.8.

**4.** The posterior P(D | +) by Bayes' rule is approximately 0.333.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.833, not 0.333.

**5.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

---

## Question 222 · Data Representation

Consider two records described by 5 numerical variables: u = [7, 4, 6, -4, 1] and v = [-4, 1, 9, -5, 6]. Which statements are correct?

**1.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

**2.** The Minkowski distance of order p=3 between u and v is approximately 11.48.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 11.48.

**3.** The inner product <u,v> is approximately 58.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 56, not 58.

**4.** The Manhattan (city-block) distance d(u,v) is approximately 26.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 23, not 26.

**5.** The Suprema (Chebyshev) distance d(u,v) is approximately 8.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 11, not 8.

---

## Question 223 · Probability & Density

A test has sensitivity P(+|D)=0.95 and specificity 0.95; disease prevalence is P(D)=0.01. Also consider the sample [6, 6, 5, 4, 2]. Which statements are correct?

**1.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**2.** The posterior P(D | +) by Bayes' rule is approximately 0.161.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 0.161.

**3.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**4.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**5.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

---

## Question 224 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 6). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, BREAD, BUTTER, DIAPERS, MILK |
| 2 | BEER, BUTTER, DIAPERS, MILK |
| 3 | BEER, BREAD, DIAPERS, MILK |
| 4 | BEER, BREAD, BUTTER, DIAPERS, MILK |
| 5 | BEER, BREAD, BUTTER, DIAPERS |
| 6 | BEER, BREAD, BUTTER |
| 7 | BEER, DIAPERS, MILK |
| 8 | BEER, BUTTER, DIAPERS, MILK |
| 9 | BUTTER, DIAPERS, MILK |
| 10 | BEER, BREAD, BUTTER, MILK |
| 11 | BEER, DIAPERS |
| 12 | BREAD, BUTTER, DIAPERS, MILK |
| 13 | BEER, BREAD, BUTTER, DIAPERS, MILK |
| 14 | BEER, BREAD, BUTTER, MILK |

**1.** By anti-monotonicity (downward closure), every subset of a frequent itemset is also frequent.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Apriori prunes any candidate having an infrequent subset before counting support.

**2.** Confidence of X ⇒ Y is defined as support(X ∪ Y) / support(Y).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Confidence = support(X∪Y)/support(X) (divide by the antecedent's support).

**3.** The confidence of the rule {MILK} ⇒ {DIAPERS} is approximately 0.818.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 0.818.

**4.** The frequent itemset {MILK} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

**5.** The frequent itemset {MILK} is maximal (it has no frequent superset).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Maximal = no superset reaches support 6.

---

## Question 225 · Probability & Density

A test has sensitivity P(+|D)=0.9 and specificity 0.9; disease prevalence is P(D)=0.05. Also consider the sample [1, 1, 1, 6, 4]. Which statements are correct?

**1.** The sample mean of the listed sample is approximately 2.8.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 2.6, not 2.8.

**2.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**3.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**4.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**5.** The posterior P(D | +) by Bayes' rule is approximately 0.421.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.321, not 0.421.

---

## Question 226 · Probability & Density

A test has sensitivity P(+|D)=0.95 and specificity 0.9; disease prevalence is P(D)=0.02. Also consider the sample [1, 1, 5, 6, 6]. Which statements are correct?

**1.** The posterior P(D | +) by Bayes' rule is approximately 0.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.162, not 0.

**2.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**3.** The sample mean of the listed sample is approximately 3.9.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 3.8, not 3.9.

**4.** The sample variance (÷ n−1) of the listed sample is approximately 6.7.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 6.7.

**5.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

---

## Question 227 · Outlier Detection

Consider the 2-D points [[1, 1], [2, 0], [7, 6], [3, 2], [2, 5], [4, 1], [16, 14]]. Which statements are correct?

**1.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

**2.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

**3.** The weighted KNN outlier score averages a point's distances to all its 1st…k-th nearest neighbours.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] Weighted-kNN aggregates (averages) the 1..k NN distances; plain kNN uses only the k-th.

**4.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

**5.** The unweighted KNN outlier scores with k=2 (per point, in order) are [2.24, 2.24, 5.66, 2.24, 4.12, 2.24, 16.64].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] The values are [2.24, 2.24, 5.66, 2.24, 4.12, 2.24, 16.64].

---

## Question 228 · Data Representation

Two objects are described by 10 binary (asymmetric/symmetric) variables: x1 = [0, 1, 0, 1, 1, 1, 1, 0, 1, 0] and x2 = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0]. Which statements are correct?

**1.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.2.

**2.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**3.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**4.** The count of disagreements n10 + n01 is approximately 8.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 8.

**5.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

---

## Question 229 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[0, 0], [1, 2], [2, 1], [0, 3], [11, 9], [8, 10], [8, 9], [9, 11]] with initial prototypes [[0, 0], [8, 10]]. Which statements are correct?

**1.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.811.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 0.811.

**2.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**3.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**4.** The final cluster labels (one per point, in order) are [0, 0, 0, 1, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 0, 0, 1, 1, 1, 1, 1].

**5.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

---

## Question 230 · Probability & Density

A test has sensitivity P(+|D)=0.95 and specificity 0.9; disease prevalence is P(D)=0.05. Also consider the sample [1, 1, 2, 5, 5]. Which statements are correct?

**1.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**2.** The sample variance (÷ n−1) of the listed sample is approximately 4.2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 4.2.

**3.** The sample mean of the listed sample is approximately 3.3.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 2.8, not 3.3.

**4.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**5.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

---

## Question 231 · Data Representation

Consider two records described by 5 numerical variables: u = [-2, -2, 2, 2, 5] and v = [4, -5, 4, -1, 0]. Which statements are correct?

**1.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**2.** The Manhattan (city-block) distance d(u,v) is approximately 19.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 19.

**3.** The cosine similarity cos(u,v) is approximately -0.036.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.164, not -0.036.

**4.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

**5.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

---

## Question 232 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 4). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, DIAPERS, JAM |
| 2 | DIAPERS, MILK |
| 3 | BEER, DIAPERS, JAM, MILK |
| 4 | CRACKERS, DIAPERS |
| 5 | DIAPERS, MILK |
| 6 | CRACKERS, DIAPERS, JAM |
| 7 | BEER, DIAPERS, JAM, MILK |
| 8 | CRACKERS, MILK |
| 9 | CRACKERS, JAM, MILK |
| 10 | BEER, DIAPERS, MILK |
| 11 | BEER, CRACKERS, DIAPERS |
| 12 | BEER, JAM, MILK |
| 13 | CRACKERS, DIAPERS, JAM, MILK |
| 14 | BEER, CRACKERS, DIAPERS, JAM, MILK |

**1.** By anti-monotonicity (downward closure), every subset of a frequent itemset is also frequent.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Apriori prunes any candidate having an infrequent subset before counting support.

**2.** The confidence of the rule {BEER} ⇒ {DIAPERS} is approximately 0.957.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 0.857, not 0.957.

**3.** The support count of the itemset {BEER, DIAPERS} is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 6.

**4.** With n distinct items the candidate search space contains 2^n possible itemsets.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Each item is in or out, giving 2^n itemsets — hence Apriori pruning is essential.

**5.** The frequent itemset {DIAPERS} is maximal (it has no frequent superset).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Maximal = no superset reaches support 4.

---

## Question 233 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[1, 3], [1, 0], [2, 3], [2, 2], [11, 8], [8, 10], [9, 8], [9, 11]] with initial prototypes [[1, 3], [8, 10]]. Which statements are correct?

**1.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**2.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**3.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 2, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 0, 0, 0, 2, 1, 1, 1].

**4.** The final SSE (sum of squared errors) of the partition is approximately 18.0.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 18.5, not 18.0.

**5.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

---

## Question 234 · Hierarchical

Consider 5 objects with the symmetric distance matrix (0-based indices):

```
[0, 2, 2, 8, 8]
[2, 0, 10, 2, 9]
[2, 10, 0, 7, 6]
[8, 2, 7, 0, 7]
[8, 9, 6, 7, 0]
```

Which statements are correct?

**1.** Using Single-Linkage, the first merge joins objects 0 and 1 at height 2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (0,)+(1,) at 2.

**2.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**3.** Using Complete-Linkage, the height of the final (root) merge is approximately 10.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 10.

**4.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**5.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

---

## Question 235 · Data Representation

Two objects are described by 12 binary (asymmetric/symmetric) variables: x1 = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0] and x2 = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]. Which statements are correct?

**1.** The Jaccard coefficient Jc(x1,x2) is approximately 0.375.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.375.

**2.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**3.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**4.** The count of 1–1 matches n11 is approximately 3.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 3.

**5.** The Simple Matching Coefficient SMC(x1,x2) is approximately 1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.583, not 1.

---

## Question 236 · Data Representation

Consider two records described by 5 numerical variables: u = [-2, 3, 7, 2, 9] and v = [-1, -1, 4, 4, 0]. Which statements are correct?

**1.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

**2.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**3.** The Euclidean distance d(u,v) is approximately 10.69.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 10.54, not 10.69.

**4.** The inner product <u,v> is approximately 33.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 35, not 33.

**5.** The Manhattan (city-block) distance d(u,v) is approximately 19.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 19.

---

## Question 237 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 6). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, BREAD, CRACKERS, EGGS |
| 2 | CRACKERS, DIAPERS |
| 3 | BEER, BREAD, BUTTER, CRACKERS, DIAPERS, EGGS |
| 4 | BREAD, CRACKERS, DIAPERS, EGGS |
| 5 | BREAD, EGGS |
| 6 | BEER, BREAD, BUTTER, CRACKERS, DIAPERS, EGGS |
| 7 | BEER, BUTTER, DIAPERS |
| 8 | BUTTER, CRACKERS, EGGS |
| 9 | BEER, BREAD, BUTTER, CRACKERS, EGGS |
| 10 | BREAD, DIAPERS |
| 11 | BEER, BREAD, BUTTER, CRACKERS, DIAPERS, EGGS |
| 12 | BEER, BREAD, BUTTER, CRACKERS, DIAPERS, EGGS |

**1.** With n distinct items the candidate search space contains 2^n possible itemsets.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Each item is in or out, giving 2^n itemsets — hence Apriori pruning is essential.

**2.** The confidence of the rule {BUTTER} ⇒ {EGGS} is approximately 0.757.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 0.857, not 0.757.

**3.** The support count of the itemset {BUTTER, EGGS} is approximately 7.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 6, not 7.

**4.** Apriori must scan the database to count the support of a candidate even when one of its subsets is already known to be infrequent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The prune step removes such candidates first, so no database scan is needed for them.

**5.** The frequent itemset {CRACKERS} is maximal (it has no frequent superset).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Maximal = no superset reaches support 6.

---

## Question 238 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0122 and 0.004, with priors π_C1 = 0.7 and π_C2 = 0.3. Which statements are correct?

**1.** The posterior probability (responsibility) of C1 at x is approximately 0.877.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.877.

**2.** The posterior probability (responsibility) of C2 at x is approximately 0.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The correct value is ≈ 0.123, not 0.

**3.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**4.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**5.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

---

## Question 239 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 5). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BREAD, DIAPERS, EGGS, MILK |
| 2 | BREAD, EGGS |
| 3 | BEER, BREAD, CRACKERS, DIAPERS |
| 4 | BEER, DIAPERS, MILK |
| 5 | BEER, DIAPERS, EGGS, MILK |
| 6 | BEER, BREAD, CRACKERS, EGGS, MILK |
| 7 | BEER, BREAD, CRACKERS, DIAPERS, EGGS, MILK |
| 8 | CRACKERS, MILK |
| 9 | BREAD, CRACKERS, DIAPERS, MILK |
| 10 | BEER, BREAD, CRACKERS, DIAPERS, EGGS, MILK |

**1.** The confidence of the rule {EGGS} ⇒ {CRACKERS} is approximately 0.35.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 0.5, not 0.35.

**2.** The frequent itemset {EGGS} is maximal (it has no frequent superset).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Maximal = no superset reaches support 5.

**3.** The lift of the rule {EGGS} ⇒ {CRACKERS} is approximately 0.833.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 0.833.

**4.** Apriori must scan the database to count the support of a candidate even when one of its subsets is already known to be infrequent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The prune step removes such candidates first, so no database scan is needed for them.

**5.** The support count of the itemset {EGGS, CRACKERS} is approximately 3.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 3.

---

## Question 240 · Probability & Density

A test has sensitivity P(+|D)=0.99 and specificity 0.95; disease prevalence is P(D)=0.05. Also consider the sample [2, 2, 5, 5, 5]. Which statements are correct?

**1.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**2.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**3.** The sample variance (÷ n−1) of the listed sample is approximately 3.0.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 2.7, not 3.0.

**4.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**5.** The posterior P(D | +) by Bayes' rule is approximately 0.41.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.51, not 0.41.

---

## Question 241 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[0, 2], [1, 2], [3, 3], [3, 3], [9, 8], [10, 11], [8, 11], [10, 11]] with initial prototypes [[0, 2], [10, 11]]. Which statements are correct?

**1.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] The values are [0, 0, 0, 0, 1, 1, 1, 1].

**2.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**3.** The final SSE (sum of squared errors) of the partition is approximately 17.25.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 17.25.

**4.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**5.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

---

## Question 242 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0126 and 0.0167, with priors π_C1 = 0.2 and π_C2 = 0.8. Which statements are correct?

**1.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

**2.** The posterior probability (responsibility) of C1 at x is approximately 0.659.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The correct value is ≈ 0.159, not 0.659.

**3.** The posterior probability (responsibility) of C2 at x is approximately 0.941.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The correct value is ≈ 0.841, not 0.941.

**4.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**5.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

---

## Question 243 · Data Representation

Two objects are described by 8 binary (asymmetric/symmetric) variables: x1 = [1, 0, 0, 0, 1, 0, 1, 1] and x2 = [1, 0, 0, 0, 0, 0, 1, 0]. Which statements are correct?

**1.** The count of 1–1 matches n11 is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 2, not 5.

**2.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**3.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**4.** The count of disagreements n10 + n01 is approximately 2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 2.

**5.** The Jaccard coefficient Jc(x1,x2) is approximately 0.35.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.5, not 0.35.

---

## Question 244 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-15, 14, 19, 64, 107, 108}. Which statements are correct?

**1.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**2.** The MLE estimate of the mean μ is approximately 49.5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 49.5.

**3.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**4.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 49.5, σ̂² = (1/n)Σ(x−μ̂)² ≈ 2214.92.

**5.** With ε = 10 and MinPts = 1, DBSCAN groups the data into the clusters [[-15], [14, 19], [64], [107, 108]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=10, MinPts=1) gives clusters [[-15], [14, 19], [64], [107, 108]]; no noise.

---

## Question 245 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-18, 7, 10, 43, 60, 65, 107}. Which statements are correct?

**1.** The MLE estimate of the mean μ is approximately 39.29.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 39.14, not 39.29.

**2.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [25, 3, 3, 5, 17, 5, 42].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [25, 3, 3, 17, 5, 5, 42], not [25, 3, 3, 5, 17, 5, 42].

**3.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**4.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 39.14, σ̂² = (1/n)Σ(x−μ̂)² ≈ 1552.98.

**5.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

---

## Question 246 · Hierarchical

Consider 4 objects with the symmetric distance matrix (0-based indices):

```
[0, 12, 6, 9]
[12, 0, 1, 2]
[6, 1, 0, 2]
[9, 2, 2, 0]
```

Which statements are correct?

**1.** Using Complete-Linkage, the height of the final (root) merge is approximately 12.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 12.

**2.** Using Single-Linkage, the height of the final (root) merge is approximately 4.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 6, not 4.

**3.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**4.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**5.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

---

## Question 247 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 5). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | JAM, MILK |
| 2 | DIAPERS, EGGS, JAM |
| 3 | JAM, MILK |
| 4 | BEER, DIAPERS, JAM |
| 5 | BEER, CRACKERS, DIAPERS, EGGS, JAM, MILK |
| 6 | CRACKERS, MILK |
| 7 | BEER, CRACKERS, DIAPERS, JAM, MILK |
| 8 | CRACKERS, EGGS |
| 9 | BEER, CRACKERS, DIAPERS, EGGS, JAM |
| 10 | BEER, CRACKERS, DIAPERS, EGGS, JAM, MILK |

**1.** The frequent itemset {CRACKERS} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

**2.** With n distinct items the candidate search space contains 2^n possible itemsets.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Each item is in or out, giving 2^n itemsets — hence Apriori pruning is essential.

**3.** By anti-monotonicity (downward closure), every subset of a frequent itemset is also frequent.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Apriori prunes any candidate having an infrequent subset before counting support.

**4.** Apriori must scan the database to count the support of a candidate even when one of its subsets is already known to be infrequent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The prune step removes such candidates first, so no database scan is needed for them.

**5.** The frequent itemset {CRACKERS} is maximal (it has no frequent superset).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Maximal = no superset reaches support 5.

---

## Question 248 · Probability & Density

A test has sensitivity P(+|D)=0.95 and specificity 0.9; disease prevalence is P(D)=0.05. Also consider the sample [1, 4, 3, 5, 6]. Which statements are correct?

**1.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**2.** The posterior P(D | +) by Bayes' rule is approximately 0.333.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 0.333.

**3.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**4.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**5.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

---

## Question 249 · Data Representation

Two objects are described by 10 binary (asymmetric/symmetric) variables: x1 = [1, 0, 1, 1, 0, 1, 0, 1, 0, 1] and x2 = [1, 1, 1, 0, 0, 1, 1, 1, 0, 1]. Which statements are correct?

**1.** The count of disagreements n10 + n01 is approximately 3.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 3.

**2.** The count of 1–1 matches n11 is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 5.

**3.** The Jaccard coefficient Jc(x1,x2) is approximately 0.525.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.625, not 0.525.

**4.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**5.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

---

## Question 250 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0073 and 0.0098, with priors π_C1 = 0.2 and π_C2 = 0.8. Which statements are correct?

**1.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

**2.** The posterior probability (responsibility) of C1 at x is approximately 0.157.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.157.

**3.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

**4.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**5.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

---

## Question 251 · Data Representation

Two objects are described by 12 binary (asymmetric/symmetric) variables: x1 = [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0] and x2 = [1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1]. Which statements are correct?

**1.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**2.** The count of 1–1 matches n11 is approximately 3.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 2, not 3.

**3.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**4.** The Jaccard coefficient Jc(x1,x2) is approximately 0.35.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.2, not 0.35.

**5.** The count of disagreements n10 + n01 is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 8, not 5.

---

## Question 252 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[2, 0], [3, 2], [3, 0], [3, 1], [10, 9], [8, 8], [9, 9], [10, 10]] with initial prototypes [[2, 0], [8, 8]]. Which statements are correct?

**1.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**2.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**3.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**4.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.851.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 0.851.

**5.** The final cluster labels (one per point, in order) are [0, 0, 0, 1, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 0, 0, 1, 1, 1, 1, 1].

---

## Question 253 · Probability & Density

A test has sensitivity P(+|D)=0.9 and specificity 0.9; disease prevalence is P(D)=0.01. Also consider the sample [3, 3, 6, 4, 5]. Which statements are correct?

**1.** The sample variance (÷ n−1) of the listed sample is approximately 1.9.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 1.7, not 1.9.

**2.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**3.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**4.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**5.** The posterior P(D | +) by Bayes' rule is approximately 0.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.083, not 0.

---

## Question 254 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 4). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BUTTER, CRACKERS, DIAPERS, EGGS, JAM, MILK |
| 2 | BUTTER, CRACKERS, DIAPERS, EGGS, JAM, MILK |
| 3 | CRACKERS, DIAPERS |
| 4 | BUTTER, MILK |
| 5 | DIAPERS, MILK |
| 6 | BUTTER, CRACKERS, DIAPERS, EGGS, JAM, MILK |
| 7 | BUTTER, CRACKERS, DIAPERS, EGGS |
| 8 | BUTTER, DIAPERS, EGGS, JAM, MILK |
| 9 | CRACKERS, DIAPERS, EGGS, JAM |
| 10 | BUTTER, DIAPERS, JAM, MILK |

**1.** The frequent itemset {JAM} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

**2.** By anti-monotonicity (downward closure), every subset of a frequent itemset is also frequent.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Apriori prunes any candidate having an infrequent subset before counting support.

**3.** The confidence of the rule {DIAPERS} ⇒ {JAM} is approximately 0.667.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 0.667.

**4.** The frequent itemset {JAM} is maximal (it has no frequent superset).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Maximal = no superset reaches support 4.

**5.** Apriori must scan the database to count the support of a candidate even when one of its subsets is already known to be infrequent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The prune step removes such candidates first, so no database scan is needed for them.

---

## Question 255 · Outlier Detection

Consider the 2-D points [[2, 4], [4, 0], [3, 1], [3, 7], [7, 0], [6, 7], [16, 13]]. Which statements are correct?

**1.** LOF is a global density score that compares each point's density to the dataset-wide average density.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] LOF is a LOCAL/relative score: density vs the point's own neighbours.

**2.** The unweighted KNN outlier scores with k=1 (per point, in order) are [3.16, 1.41, 1.41, 4.0, 3.0, 3.0, 11.66].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [3.16, 1.41, 1.41, 3.0, 3.0, 3.0, 11.66], not [3.16, 1.41, 1.41, 4.0, 3.0, 3.0, 11.66].

**3.** Point 6 (the far point) receives the largest LOF, consistent with being an outlier.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF values ≈ [0.9, 1.1, 0.91, 1.15, 1.07, 1.15, 3.18]; the isolated point has LOF ≫ 1.

**4.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

**5.** The weighted KNN outlier score averages a point's distances to all its 1st…k-th nearest neighbours.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] Weighted-kNN aggregates (averages) the 1..k NN distances; plain kNN uses only the k-th.

---

## Question 256 · Outlier Detection

Consider the 2-D points [[1, 3], [6, 1], [4, 6], [6, 6], [2, 5], [4, 1], [12, 17]]. Which statements are correct?

**1.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

**2.** Point 6 (the far point) receives the largest LOF, consistent with being an outlier.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF values ≈ [0.84, 1.18, 1.04, 1.04, 0.96, 1.24, 4.11]; the isolated point has LOF ≫ 1.

**3.** The unweighted KNN outlier scores with k=1 (per point, in order) are [2.24, 2.0, 2.0, 2.0, 2.24, 3.0, 12.53].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [2.24, 2.0, 2.0, 2.0, 2.24, 2.0, 12.53], not [2.24, 2.0, 2.0, 2.0, 2.24, 3.0, 12.53].

**4.** The weighted KNN outlier score averages a point's distances to all its 1st…k-th nearest neighbours.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] Weighted-kNN aggregates (averages) the 1..k NN distances; plain kNN uses only the k-th.

**5.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

---

## Question 257 · Data Representation

Two objects are described by 8 binary (asymmetric/symmetric) variables: x1 = [1, 1, 0, 0, 0, 0, 1, 1] and x2 = [0, 1, 1, 1, 0, 0, 0, 1]. Which statements are correct?

**1.** The count of 1–1 matches n11 is approximately 0.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 2, not 0.

**2.** The Jaccard coefficient Jc(x1,x2) is approximately 0.333.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.333.

**3.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**4.** The count of disagreements n10 + n01 is approximately 1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 4, not 1.

**5.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.65.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.5, not 0.65.

---

## Question 258 · Hierarchical

Consider 5 objects with the symmetric distance matrix (0-based indices):

```
[0, 6, 5, 2, 7]
[6, 0, 8, 1, 8]
[5, 8, 0, 10, 1]
[2, 1, 10, 0, 7]
[7, 8, 1, 7, 0]
```

Which statements are correct?

**1.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

**2.** Using Single-Linkage, the height of the final (root) merge is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 5, not 6.

**3.** Using Complete-Linkage, the height of the final (root) merge is approximately 10.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 10.

**4.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**5.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

---

## Question 259 · Probability & Density

A test has sensitivity P(+|D)=0.95 and specificity 0.99; disease prevalence is P(D)=0.01. Also consider the sample [4, 2, 2, 3, 4]. Which statements are correct?

**1.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**2.** The sample variance (÷ n−1) of the listed sample is approximately 1.3.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 1.0, not 1.3.

**3.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**4.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**5.** The posterior P(D | +) by Bayes' rule is approximately 0.79.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.49, not 0.79.

---

## Question 260 · Data Representation

Two objects are described by 12 binary (asymmetric/symmetric) variables: x1 = [0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1] and x2 = [1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0]. Which statements are correct?

**1.** The count of 1–1 matches n11 is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 3, not 5.

**2.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.417.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.417.

**3.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**4.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**5.** The count of disagreements n10 + n01 is approximately 7.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 7.

---

## Question 261 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[2, 2], [2, 3], [3, 1], [1, 2], [9, 8], [10, 11], [8, 10], [11, 8]] with initial prototypes [[2, 2], [10, 11]]. Which statements are correct?

**1.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**2.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**3.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**4.** The final SSE (sum of squared errors) of the partition is approximately 15.9.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 15.75, not 15.9.

**5.** The final cluster labels (one per point, in order) are [0, 1, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 1, 0, 0, 1, 1, 1, 1].

---

## Question 262 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0034 and 0.0064, with priors π_C1 = 0.5 and π_C2 = 0.5. Which statements are correct?

**1.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**2.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

**3.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**4.** The posterior probability (responsibility) of C1 at x is approximately 0.347.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.347.

**5.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

---

## Question 263 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-4, 9, 21, 31, 42, 75, 81}. Which statements are correct?

**1.** With ε = 25 and MinPts = 2, DBSCAN groups the data into the clusters [[-4, 9, 21, 31, 42], [75, 81]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=25, MinPts=2) gives clusters [[-4, 9, 21, 31, 42], [75, 81]]; no noise.

**2.** The MLE estimate of the mean μ is approximately 36.43.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 36.43.

**3.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**4.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [13, 12, 6, 10, 11, 10, 6].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [13, 12, 10, 10, 11, 6, 6], not [13, 12, 6, 10, 11, 10, 6].

**5.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

---

## Question 264 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0124 and 0.0094, with priors π_C1 = 0.7 and π_C2 = 0.3. Which statements are correct?

**1.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**2.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

**3.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

**4.** The posterior probability (responsibility) of C2 at x is approximately 0.245.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.245.

**5.** The posterior probability (responsibility) of C1 at x is approximately 0.755.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.755.

---

## Question 265 · Data Representation

Consider two records described by 5 numerical variables: u = [-4, -5, 5, 9, -3] and v = [-3, 5, 8, -1, 4]. Which statements are correct?

**1.** The cosine similarity cos(u,v) is approximately 0.045.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.045.

**2.** The Euclidean distance d(u,v) is approximately 16.39.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 16.09, not 16.39.

**3.** The Manhattan (city-block) distance d(u,v) is approximately 29.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 31, not 29.

**4.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

**5.** The Minkowski distance of order p=3 between u and v is approximately 13.33.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 13.33.

---

## Question 266 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0163 and 0.0182, with priors π_C1 = 0.5 and π_C2 = 0.5. Which statements are correct?

**1.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

**2.** The posterior probability (responsibility) of C2 at x is approximately 0.528.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.528.

**3.** The posterior probability (responsibility) of C1 at x is approximately 0.472.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.472.

**4.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**5.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

---

## Question 267 · Probability & Density

A test has sensitivity P(+|D)=0.99 and specificity 0.95; disease prevalence is P(D)=0.02. Also consider the sample [6, 2, 6, 3, 2]. Which statements are correct?

**1.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**2.** The sample mean of the listed sample is approximately 3.8.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 3.8.

**3.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**4.** The sample variance (÷ n−1) of the listed sample is approximately 4.7.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 4.2, not 4.7.

**5.** The posterior P(D | +) by Bayes' rule is approximately 0.288.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 0.288.

---

## Question 268 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 4). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BREAD, BUTTER, DIAPERS, EGGS, JAM |
| 2 | BREAD, BUTTER, DIAPERS, EGGS, JAM |
| 3 | BREAD, BUTTER, DIAPERS, EGGS |
| 4 | BREAD, BUTTER, DIAPERS, EGGS |
| 5 | BREAD, BUTTER |
| 6 | BREAD, BUTTER, EGGS |
| 7 | BREAD, BUTTER, DIAPERS, EGGS, JAM |
| 8 | EGGS, JAM |
| 9 | BUTTER, DIAPERS, JAM |
| 10 | BREAD, BUTTER, DIAPERS, EGGS, JAM |
| 11 | EGGS, JAM |
| 12 | BREAD, BUTTER, DIAPERS, JAM |

**1.** The confidence of the rule {DIAPERS} ⇒ {JAM} is approximately 0.55.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 0.75, not 0.55.

**2.** The support count of the itemset {DIAPERS, JAM} is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 6.

**3.** Apriori must scan the database to count the support of a candidate even when one of its subsets is already known to be infrequent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The prune step removes such candidates first, so no database scan is needed for them.

**4.** With n distinct items the candidate search space contains 2^n possible itemsets.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Each item is in or out, giving 2^n itemsets — hence Apriori pruning is essential.

**5.** The support count of {JAM} is approximately 10.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 8, not 10.

---

## Question 269 · Data Representation

Consider two records described by 4 numerical variables: u = [-1, -5, 4, 2] and v = [9, -2, -1, 0]. Which statements are correct?

**1.** The inner product <u,v> is approximately -6.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ -3, not -6.

**2.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

**3.** The cosine similarity cos(u,v) is approximately 0.102.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ -0.048, not 0.102.

**4.** The Minkowski distance of order p=3 between u and v is approximately 10.41.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 10.51, not 10.41.

**5.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

---

## Question 270 · Data Representation

Consider two records described by 3 numerical variables: u = [-4, 7, 0] and v = [9, -5, 6]. Which statements are correct?

**1.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

**2.** The Manhattan (city-block) distance d(u,v) is approximately 28.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 31, not 28.

**3.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

**4.** The Euclidean distance d(u,v) is approximately 19.18.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 18.68, not 19.18.

**5.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

---

## Question 271 · Hierarchical

Consider 4 objects with the symmetric distance matrix (0-based indices):

```
[0, 11, 2, 10]
[11, 0, 3, 6]
[2, 3, 0, 1]
[10, 6, 1, 0]
```

Which statements are correct?

**1.** Using Single-Linkage, the height of the final (root) merge is approximately 3.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 3.

**2.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**3.** Using Single-Linkage, the first merge joins objects 2 and 3 at height 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (2,)+(3,) at 1.

**4.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**5.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

---

## Question 272 · Data Representation

Two objects are described by 8 binary (asymmetric/symmetric) variables: x1 = [0, 0, 1, 0, 1, 1, 1, 0] and x2 = [0, 0, 0, 0, 1, 0, 0, 1]. Which statements are correct?

**1.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**2.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**3.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.7.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.5, not 0.7.

**4.** The count of disagreements n10 + n01 is approximately 4.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 4.

**5.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

---

## Question 273 · Data Representation

Two objects are described by 8 binary (asymmetric/symmetric) variables: x1 = [0, 0, 1, 1, 1, 0, 0, 0] and x2 = [0, 0, 0, 1, 0, 1, 1, 0]. Which statements are correct?

**1.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**2.** The Jaccard coefficient Jc(x1,x2) is approximately 0.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.2, not 0.

**3.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.5.

**4.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**5.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

---

## Question 274 · Data Representation

Consider two records described by 3 numerical variables: u = [5, 4, 5] and v = [8, 8, -2]. Which statements are correct?

**1.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**2.** The Manhattan (city-block) distance d(u,v) is approximately 16.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 14, not 16.

**3.** The Euclidean distance d(u,v) is approximately 8.6.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 8.6.

**4.** The inner product <u,v> is approximately 64.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 62, not 64.

**5.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

---

## Question 275 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-20, -15, 33, 36, 50, 53, 76, 97}. Which statements are correct?

**1.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**2.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**3.** The MLE estimate of the variance σ² (dividing by n) is approximately 1436.54.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 1436.44, not 1436.54.

**4.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**5.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [5, 5, 3, 3, 3, 3, 21, 21].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] The values are [5, 5, 3, 3, 3, 3, 21, 21].

---

## Question 276 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-24, -15, -8, 16, 63, 66, 104, 105}. Which statements are correct?

**1.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [9, 7, 24, 7, 3, 3, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [9, 7, 7, 24, 3, 3, 1, 1], not [9, 7, 24, 7, 3, 3, 1, 1].

**2.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**3.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**4.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**5.** The MLE estimate of the variance σ² (dividing by n) is approximately 2437.73.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 2438.23, not 2437.73.

---

## Question 277 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0047 and 0.0077, with priors π_C1 = 0.7 and π_C2 = 0.3. Which statements are correct?

**1.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**2.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

**3.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**4.** The posterior probability (responsibility) of C2 at x is approximately 0.412.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.412.

**5.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

---

## Question 278 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 6). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, CRACKERS |
| 2 | BREAD, CRACKERS, EGGS |
| 3 | BEER, BREAD, CRACKERS, EGGS |
| 4 | BEER, BREAD |
| 5 | BEER, BREAD, EGGS |
| 6 | BREAD, EGGS, MILK |
| 7 | BEER, CRACKERS |
| 8 | BEER, BREAD, EGGS, MILK |
| 9 | BEER, BREAD, CRACKERS, MILK |
| 10 | BREAD, EGGS |

**1.** Confidence of X ⇒ Y is defined as support(X ∪ Y) / support(Y).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Confidence = support(X∪Y)/support(X) (divide by the antecedent's support).

**2.** Apriori must scan the database to count the support of a candidate even when one of its subsets is already known to be infrequent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The prune step removes such candidates first, so no database scan is needed for them.

**3.** The frequent itemset {EGGS} is maximal (it has no frequent superset).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Maximal = no superset reaches support 6.

**4.** The lift of the rule {BREAD} ⇒ {BEER} is approximately 1.043.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 0.893, not 1.043.

**5.** The support count of the itemset {BREAD, BEER} is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 5.

---

## Question 279 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0087 and 0.0181, with priors π_C1 = 0.4 and π_C2 = 0.6. Which statements are correct?

**1.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

**2.** The posterior probability (responsibility) of C1 at x is approximately 0.093.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The correct value is ≈ 0.243, not 0.093.

**3.** The posterior probability (responsibility) of C2 at x is approximately 0.857.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The correct value is ≈ 0.757, not 0.857.

**4.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**5.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

---

## Question 280 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[3, 1], [2, 3], [1, 1], [2, 1], [9, 11], [8, 9], [10, 11], [10, 11]] with initial prototypes [[3, 1], [8, 9]]. Which statements are correct?

**1.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**2.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**3.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] The values are [0, 0, 0, 0, 1, 1, 1, 1].

**4.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**5.** The final SSE (sum of squared errors) of the partition is approximately 10.75.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 10.75.

---

## Question 281 · Data Representation

Two objects are described by 12 binary (asymmetric/symmetric) variables: x1 = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0] and x2 = [0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0]. Which statements are correct?

**1.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.5.

**2.** The count of disagreements n10 + n01 is approximately 4.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 6, not 4.

**3.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**4.** The count of 1–1 matches n11 is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 2, not 5.

**5.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

---

## Question 282 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 6). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, JAM |
| 2 | BEER, BUTTER, DIAPERS, EGGS, JAM |
| 3 | BREAD, BUTTER |
| 4 | BREAD, BUTTER, JAM |
| 5 | BEER, BREAD, BUTTER, EGGS |
| 6 | BEER, BREAD, BUTTER, DIAPERS, EGGS, JAM |
| 7 | BUTTER, JAM |
| 8 | BREAD, BUTTER, JAM |
| 9 | BREAD, BUTTER, DIAPERS, EGGS, JAM |
| 10 | BEER, BREAD, BUTTER, DIAPERS, EGGS, JAM |
| 11 | BREAD, BUTTER, DIAPERS, EGGS |
| 12 | BEER, BREAD, BUTTER, DIAPERS, EGGS, JAM |

**1.** The support count of the itemset {BEER, BUTTER} is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 5.

**2.** By anti-monotonicity (downward closure), every subset of a frequent itemset is also frequent.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Apriori prunes any candidate having an infrequent subset before counting support.

**3.** The frequent itemset {JAM} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

**4.** Confidence of X ⇒ Y is defined as support(X ∪ Y) / support(Y).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Confidence = support(X∪Y)/support(X) (divide by the antecedent's support).

**5.** The lift of the rule {BEER} ⇒ {BUTTER} is approximately 1.009.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 0.909, not 1.009.

---

## Question 283 · Probability & Density

A test has sensitivity P(+|D)=0.9 and specificity 0.99; disease prevalence is P(D)=0.05. Also consider the sample [1, 1, 2, 1, 4]. Which statements are correct?

**1.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**2.** The posterior P(D | +) by Bayes' rule is approximately 0.976.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.826, not 0.976.

**3.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**4.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**5.** The sample mean of the listed sample is approximately 1.8.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 1.8.

---

## Question 284 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0101 and 0.016, with priors π_C1 = 0.7 and π_C2 = 0.3. Which statements are correct?

**1.** The posterior probability (responsibility) of C2 at x is approximately 0.554.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The correct value is ≈ 0.404, not 0.554.

**2.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**3.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

**4.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**5.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

---

## Question 285 · Probability & Density

A test has sensitivity P(+|D)=0.95 and specificity 0.99; disease prevalence is P(D)=0.1. Also consider the sample [5, 5, 2, 3, 3]. Which statements are correct?

**1.** The sample variance (÷ n−1) of the listed sample is approximately 2.1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 1.8, not 2.1.

**2.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**3.** The posterior P(D | +) by Bayes' rule is approximately 0.913.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 0.913.

**4.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**5.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

---

## Question 286 · Data Representation

Two objects are described by 10 binary (asymmetric/symmetric) variables: x1 = [0, 0, 0, 0, 1, 0, 1, 0, 0, 1] and x2 = [1, 0, 0, 0, 1, 1, 0, 0, 1, 1]. Which statements are correct?

**1.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**2.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**3.** The count of disagreements n10 + n01 is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 4, not 5.

**4.** The count of 1–1 matches n11 is approximately 2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 2.

**5.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.6.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.6.

---

## Question 287 · Probability & Density

A test has sensitivity P(+|D)=0.99 and specificity 0.99; disease prevalence is P(D)=0.05. Also consider the sample [4, 1, 5, 2, 6]. Which statements are correct?

**1.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**2.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**3.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**4.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**5.** The posterior P(D | +) by Bayes' rule is approximately 0.639.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.839, not 0.639.

---

## Question 288 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[2, 0], [0, 0], [1, 0], [3, 3], [8, 10], [10, 11], [9, 9], [9, 10]] with initial prototypes [[2, 0], [10, 11]]. Which statements are correct?

**1.** The final SSE (sum of squared errors) of the partition is approximately 15.75.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 15.75.

**2.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**3.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.674.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.824, not 0.674.

**4.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**5.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

---

## Question 289 · Data Representation

Consider two records described by 4 numerical variables: u = [-2, 1, 0, 8] and v = [-5, -2, -5, 6]. Which statements are correct?

**1.** The Manhattan (city-block) distance d(u,v) is approximately 15.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 13, not 15.

**2.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

**3.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**4.** The Suprema (Chebyshev) distance d(u,v) is approximately 3.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 5, not 3.

**5.** The Euclidean distance d(u,v) is approximately 7.01.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 6.86, not 7.01.

---

## Question 290 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 4). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, BREAD, DIAPERS, JAM, MILK |
| 2 | BREAD, JAM, MILK |
| 3 | BREAD, DIAPERS, EGGS, JAM, MILK |
| 4 | BEER, DIAPERS, JAM |
| 5 | BREAD, DIAPERS, EGGS, JAM, MILK |
| 6 | DIAPERS, EGGS, JAM, MILK |
| 7 | BEER, BREAD, DIAPERS, EGGS, JAM, MILK |
| 8 | BEER, BREAD, DIAPERS, MILK |
| 9 | BREAD, DIAPERS |
| 10 | BREAD, JAM, MILK |
| 11 | BREAD, EGGS, MILK |
| 12 | BEER, BREAD, DIAPERS, EGGS, JAM, MILK |

**1.** The lift of the rule {BREAD} ⇒ {MILK} is approximately 1.58.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 1.08, not 1.58.

**2.** Confidence of X ⇒ Y is defined as support(X ∪ Y) / support(Y).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Confidence = support(X∪Y)/support(X) (divide by the antecedent's support).

**3.** With n distinct items the candidate search space contains 2^n possible itemsets.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Each item is in or out, giving 2^n itemsets — hence Apriori pruning is essential.

**4.** The support count of the itemset {BREAD, MILK} is approximately 8.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 9, not 8.

**5.** The frequent itemset {BEER} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

---

## Question 291 · Outlier Detection

Consider the 2-D points [[4, 4], [3, 4], [2, 3], [1, 7], [6, 0], [2, 5], [17, 14]]. Which statements are correct?

**1.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

**2.** Point 6 (the far point) receives the largest LOF, consistent with being an outlier.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF values ≈ [1.08, 1.16, 0.91, 1.56, 2.54, 0.91, 8.32]; the isolated point has LOF ≫ 1.

**3.** The weighted KNN outlier score averages a point's distances to all its 1st…k-th nearest neighbours.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] Weighted-kNN aggregates (averages) the 1..k NN distances; plain kNN uses only the k-th.

**4.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

**5.** The unweighted KNN outlier scores with k=2 (per point, in order) are [2.24, 1.41, 2.0, 3.61, 6.0, 2.0, 17.2].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [2.24, 1.41, 2.0, 3.61, 5.0, 2.0, 17.2], not [2.24, 1.41, 2.0, 3.61, 6.0, 2.0, 17.2].

---

## Question 292 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {23, 28, 51, 70, 105, 109}. Which statements are correct?

**1.** The MLE estimate of the variance σ² (dividing by n) is approximately 1147.89.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 1147.89.

**2.** The MLE estimate of the mean μ is approximately 64.13.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 64.33, not 64.13.

**3.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [5, 5, 19, 19, 4, 4].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] The values are [5, 5, 19, 19, 4, 4].

**4.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**5.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

---

## Question 293 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 5). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, BUTTER, CRACKERS |
| 2 | BEER, BUTTER, CRACKERS, DIAPERS, EGGS |
| 3 | BEER, BUTTER, CRACKERS, DIAPERS |
| 4 | BEER, BUTTER, CRACKERS, EGGS |
| 5 | BEER, BUTTER, CRACKERS, DIAPERS, EGGS |
| 6 | BEER, BUTTER, CRACKERS, DIAPERS, EGGS |
| 7 | BEER, BUTTER, CRACKERS, DIAPERS, EGGS |
| 8 | BEER, BUTTER, DIAPERS, EGGS |
| 9 | BEER, BUTTER, CRACKERS, DIAPERS, EGGS |
| 10 | BUTTER, CRACKERS, DIAPERS |

**1.** By anti-monotonicity (downward closure), every subset of a frequent itemset is also frequent.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Apriori prunes any candidate having an infrequent subset before counting support.

**2.** The lift of the rule {CRACKERS} ⇒ {BEER} is approximately 0.688.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 0.988, not 0.688.

**3.** The frequent itemset {CRACKERS} is maximal (it has no frequent superset).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Maximal = no superset reaches support 5.

**4.** The support count of {DIAPERS} is approximately 11.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 8, not 11.

**5.** Confidence of X ⇒ Y is defined as support(X ∪ Y) / support(Y).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Confidence = support(X∪Y)/support(X) (divide by the antecedent's support).

---

## Question 294 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[1, 1], [1, 3], [1, 3], [0, 3], [8, 8], [8, 8], [9, 11], [10, 8]] with initial prototypes [[1, 1], [8, 8]]. Which statements are correct?

**1.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**2.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**3.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**4.** The final cluster labels (one per point, in order) are [1, 0, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [1, 0, 0, 0, 1, 1, 1, 1].

**5.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.826.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 0.826.

---

## Question 295 · Probability & Density

A test has sensitivity P(+|D)=0.9 and specificity 0.99; disease prevalence is P(D)=0.01. Also consider the sample [4, 1, 3, 2, 3]. Which statements are correct?

**1.** The posterior P(D | +) by Bayes' rule is approximately 0.476.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 0.476.

**2.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**3.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**4.** The sample variance (÷ n−1) of the listed sample is approximately 1.0.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 1.3, not 1.0.

**5.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

---

## Question 296 · Hierarchical

Consider 5 objects with the symmetric distance matrix (0-based indices):

```
[0, 8, 6, 4, 9]
[8, 0, 6, 7, 9]
[6, 6, 0, 9, 12]
[4, 7, 9, 0, 5]
[9, 9, 12, 5, 0]
```

Which statements are correct?

**1.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**2.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**3.** Using Complete-Linkage, the height of the final (root) merge is approximately 11.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 12, not 11.

**4.** Using Single-Linkage, the first merge joins objects 0 and 3 at height 4.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (0,)+(3,) at 4.

**5.** Using Single-Linkage, the height of the final (root) merge is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 6.

---

## Question 297 · Probability & Density

A test has sensitivity P(+|D)=0.99 and specificity 0.99; disease prevalence is P(D)=0.02. Also consider the sample [3, 5, 2, 5, 5]. Which statements are correct?

**1.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**2.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**3.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**4.** The sample variance (÷ n−1) of the listed sample is approximately 2.0.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 2.0.

**5.** The posterior P(D | +) by Bayes' rule is approximately 0.669.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 0.669.

---

## Question 298 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 4). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, CRACKERS, DIAPERS, JAM, MILK |
| 2 | BEER, CRACKERS, DIAPERS, JAM, MILK |
| 3 | BEER, DIAPERS, MILK |
| 4 | BEER, CRACKERS, DIAPERS, EGGS, JAM, MILK |
| 5 | DIAPERS, EGGS |
| 6 | BEER, CRACKERS, EGGS, MILK |
| 7 | BEER, CRACKERS, DIAPERS, EGGS, JAM |
| 8 | BEER, DIAPERS, EGGS, JAM, MILK |
| 9 | CRACKERS, JAM, MILK |
| 10 | BEER, CRACKERS, DIAPERS, EGGS, JAM, MILK |
| 11 | BEER, DIAPERS, EGGS, JAM |
| 12 | CRACKERS, DIAPERS, EGGS |

**1.** The frequent itemset {BEER} is maximal (it has no frequent superset).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Maximal = no superset reaches support 4.

**2.** The confidence of the rule {CRACKERS} ⇒ {JAM} is approximately 0.75.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 0.75.

**3.** Confidence of X ⇒ Y is defined as support(X ∪ Y) / support(Y).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Confidence = support(X∪Y)/support(X) (divide by the antecedent's support).

**4.** Apriori must scan the database to count the support of a candidate even when one of its subsets is already known to be infrequent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The prune step removes such candidates first, so no database scan is needed for them.

**5.** With n distinct items the candidate search space contains 2^n possible itemsets.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Each item is in or out, giving 2^n itemsets — hence Apriori pruning is essential.

---

## Question 299 · Data Representation

Two objects are described by 8 binary (asymmetric/symmetric) variables: x1 = [0, 0, 0, 0, 0, 1, 1, 0] and x2 = [1, 1, 0, 0, 0, 1, 1, 1]. Which statements are correct?

**1.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**2.** The count of disagreements n10 + n01 is approximately 3.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 3.

**3.** The Jaccard coefficient Jc(x1,x2) is approximately 0.4.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.4.

**4.** The count of 1–1 matches n11 is approximately 2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 2.

**5.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

---

## Question 300 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0164 and 0.0191, with priors π_C1 = 0.3 and π_C2 = 0.7. Which statements are correct?

**1.** The posterior probability (responsibility) of C2 at x is approximately 0.731.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.731.

**2.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**3.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

**4.** The posterior probability (responsibility) of C1 at x is approximately 0.569.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The correct value is ≈ 0.269, not 0.569.

**5.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

---

## Question 301 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[2, 0], [3, 3], [1, 0], [2, 1], [9, 8], [11, 10], [10, 11], [9, 9]] with initial prototypes [[2, 0], [11, 10]]. Which statements are correct?

**1.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**2.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.812.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 0.812.

**3.** The final SSE (sum of squared errors) of the partition is approximately 15.25.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 15.75, not 15.25.

**4.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**5.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] The values are [0, 0, 0, 0, 1, 1, 1, 1].

---

## Question 302 · Data Representation

Two objects are described by 10 binary (asymmetric/symmetric) variables: x1 = [0, 0, 1, 1, 0, 1, 0, 0, 1, 0] and x2 = [1, 1, 1, 0, 1, 0, 1, 0, 1, 1]. Which statements are correct?

**1.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**2.** The count of disagreements n10 + n01 is approximately 7.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 7.

**3.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.2.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.3, not 0.2.

**4.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**5.** The Jaccard coefficient Jc(x1,x2) is approximately 0.222.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.222.

---

## Question 303 · Outlier Detection

Consider the 2-D points [[2, 7], [1, 1], [4, 6], [3, 0], [5, 0], [0, 5], [16, 14]]. Which statements are correct?

**1.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

**2.** LOF is a global density score that compares each point's density to the dataset-wide average density.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] LOF is a LOCAL/relative score: density vs the point's own neighbours.

**3.** The unweighted KNN outlier scores with k=2 (per point, in order) are [2.83, 4.12, 5.12, 2.24, 4.12, 4.12, 15.65].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [2.83, 4.12, 4.12, 2.24, 4.12, 4.12, 15.65], not [2.83, 4.12, 5.12, 2.24, 4.12, 4.12, 15.65].

**4.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

**5.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

---

## Question 304 · Probability & Density

A test has sensitivity P(+|D)=0.9 and specificity 0.95; disease prevalence is P(D)=0.02. Also consider the sample [3, 4, 5, 4, 5]. Which statements are correct?

**1.** The sample mean of the listed sample is approximately 4.2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 4.2.

**2.** The sample variance (÷ n−1) of the listed sample is approximately 0.9.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.7, not 0.9.

**3.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**4.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**5.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

---

## Question 305 · Probability & Density

A test has sensitivity P(+|D)=0.99 and specificity 0.95; disease prevalence is P(D)=0.01. Also consider the sample [6, 3, 5, 6, 1]. Which statements are correct?

**1.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**2.** The sample variance (÷ n−1) of the listed sample is approximately 4.7.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 4.7.

**3.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**4.** The sample mean of the listed sample is approximately 4.5.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 4.2, not 4.5.

**5.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

---

## Question 306 · Outlier Detection

Consider the 2-D points [[0, 4], [1, 5], [6, 1], [4, 6], [6, 4], [5, 3], [12, 17]]. Which statements are correct?

**1.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

**2.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

**3.** The weighted KNN outlier score averages a point's distances to all its 1st…k-th nearest neighbours.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] Weighted-kNN aggregates (averages) the 1..k NN distances; plain kNN uses only the k-th.

**4.** LOF is a global density score that compares each point's density to the dataset-wide average density.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] LOF is a LOCAL/relative score: density vs the point's own neighbours.

**5.** The unweighted KNN outlier scores with k=1 (per point, in order) are [1.41, 1.41, 2.24, 2.83, 1.41, 1.41, 13.6].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] The values are [1.41, 1.41, 2.24, 2.83, 1.41, 1.41, 13.6].

---

## Question 307 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {11, 29, 34, 39, 59, 61, 63, 93}. Which statements are correct?

**1.** The MLE estimate of the mean μ is approximately 49.12.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 48.62, not 49.12.

**2.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**3.** The MLE estimate of the variance σ² (dividing by n) is approximately 568.48.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 567.98, not 568.48.

**4.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**5.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

---

## Question 308 · Outlier Detection

Consider the 2-D points [[7, 4], [1, 2], [0, 0], [7, 0], [1, 7], [0, 5], [15, 16]]. Which statements are correct?

**1.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

**2.** Point 6 (the far point) receives the largest LOF, consistent with being an outlier.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF values ≈ [1.27, 1.0, 1.0, 1.27, 1.0, 1.0, 3.13]; the isolated point has LOF ≫ 1.

**3.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

**4.** The unweighted KNN outlier scores with k=2 (per point, in order) are [6.32, 3.16, 5.0, 6.32, 5.0, 4.16, 16.64].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [6.32, 3.16, 5.0, 6.32, 5.0, 3.16, 16.64], not [6.32, 3.16, 5.0, 6.32, 5.0, 4.16, 16.64].

**5.** The weighted KNN outlier score averages a point's distances to all its 1st…k-th nearest neighbours.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] Weighted-kNN aggregates (averages) the 1..k NN distances; plain kNN uses only the k-th.

---

## Question 309 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 4). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, BUTTER, JAM |
| 2 | BEER, BREAD, BUTTER, DIAPERS |
| 3 | BREAD, DIAPERS, MILK |
| 4 | BREAD, BUTTER, DIAPERS, JAM, MILK |
| 5 | BEER, BREAD, BUTTER, DIAPERS, JAM, MILK |
| 6 | BUTTER, MILK |
| 7 | BEER, BUTTER, DIAPERS, JAM, MILK |
| 8 | BEER, BREAD, BUTTER, DIAPERS |
| 9 | BEER, BUTTER, MILK |
| 10 | BEER, BREAD, BUTTER, DIAPERS, MILK |
| 11 | BEER, BREAD, DIAPERS, JAM, MILK |
| 12 | BEER, BREAD, BUTTER, DIAPERS, JAM, MILK |
| 13 | BEER, BREAD, BUTTER, DIAPERS, JAM, MILK |
| 14 | BEER, BREAD, BUTTER, JAM, MILK |

**1.** Apriori must scan the database to count the support of a candidate even when one of its subsets is already known to be infrequent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The prune step removes such candidates first, so no database scan is needed for them.

**2.** The lift of the rule {BREAD} ⇒ {MILK} is approximately 0.918.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 1.018, not 0.918.

**3.** The frequent itemset {BUTTER} is maximal (it has no frequent superset).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Maximal = no superset reaches support 4.

**4.** Confidence of X ⇒ Y is defined as support(X ∪ Y) / support(Y).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Confidence = support(X∪Y)/support(X) (divide by the antecedent's support).

**5.** The frequent itemset {BUTTER} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

---

## Question 310 · Probability & Density

A test has sensitivity P(+|D)=0.9 and specificity 0.99; disease prevalence is P(D)=0.05. Also consider the sample [5, 6, 2, 4, 4]. Which statements are correct?

**1.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**2.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**3.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**4.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**5.** The posterior P(D | +) by Bayes' rule is approximately 0.626.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.826, not 0.626.

---

## Question 311 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 6). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, BREAD, CRACKERS, DIAPERS, EGGS, MILK |
| 2 | BEER, BREAD, CRACKERS, DIAPERS |
| 3 | BREAD, CRACKERS, DIAPERS, EGGS, MILK |
| 4 | BEER, BREAD, CRACKERS, DIAPERS, EGGS, MILK |
| 5 | BEER, BREAD, CRACKERS, DIAPERS, MILK |
| 6 | BEER, BREAD, CRACKERS, DIAPERS, EGGS, MILK |
| 7 | BEER, BREAD, CRACKERS, DIAPERS, EGGS |
| 8 | BEER, BREAD, CRACKERS, DIAPERS |
| 9 | BEER, BREAD |
| 10 | BREAD, CRACKERS, EGGS |
| 11 | BEER, BREAD, CRACKERS, DIAPERS, EGGS, MILK |
| 12 | CRACKERS, EGGS |
| 13 | BEER, BREAD, CRACKERS, DIAPERS, MILK |
| 14 | BEER, BREAD, DIAPERS, EGGS, MILK |

**1.** With n distinct items the candidate search space contains 2^n possible itemsets.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Each item is in or out, giving 2^n itemsets — hence Apriori pruning is essential.

**2.** By anti-monotonicity (downward closure), every subset of a frequent itemset is also frequent.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Apriori prunes any candidate having an infrequent subset before counting support.

**3.** The support count of {CRACKERS} is approximately 11.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 12, not 11.

**4.** The frequent itemset {EGGS} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

**5.** The confidence of the rule {BEER} ⇒ {CRACKERS} is approximately 0.968.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 0.818, not 0.968.

---

## Question 312 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0146 and 0.0162, with priors π_C1 = 0.3 and π_C2 = 0.7. Which statements are correct?

**1.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

**2.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

**3.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**4.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**5.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

---

## Question 313 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {9, 13, 23, 40, 45, 68, 102}. Which statements are correct?

**1.** The MLE estimate of the mean μ is approximately 42.66.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 42.86, not 42.66.

**2.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [4, 5, 10, 5, 4, 23, 34].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [4, 4, 10, 5, 5, 23, 34], not [4, 5, 10, 5, 4, 23, 34].

**3.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**4.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**5.** With ε = 25 and MinPts = 1, DBSCAN groups the data into the clusters [[9, 13, 23, 40, 45, 68], [102]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=25, MinPts=1) gives clusters [[9, 13, 23, 40, 45, 68], [102]]; no noise.

---

## Question 314 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[3, 1], [3, 3], [1, 2], [0, 0], [11, 9], [11, 11], [11, 10], [10, 9]] with initial prototypes [[3, 1], [11, 11]]. Which statements are correct?

**1.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**2.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**3.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**4.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] The values are [0, 0, 0, 0, 1, 1, 1, 1].

**5.** The final SSE (sum of squared errors) of the partition is approximately 15.25.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 15.25.

---

## Question 315 · Data Representation

Two objects are described by 10 binary (asymmetric/symmetric) variables: x1 = [0, 0, 1, 0, 0, 0, 1, 0, 0, 0] and x2 = [1, 1, 0, 1, 1, 0, 0, 0, 0, 1]. Which statements are correct?

**1.** The Jaccard coefficient Jc(x1,x2) is approximately 0.0.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.0.

**2.** The count of 1–1 matches n11 is approximately 0.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.

**3.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**4.** The count of disagreements n10 + n01 is approximately 7.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 7.

**5.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.3, not 0.

---

## Question 316 · Data Representation

Two objects are described by 10 binary (asymmetric/symmetric) variables: x1 = [1, 1, 0, 0, 0, 0, 1, 0, 1, 1] and x2 = [1, 1, 0, 0, 1, 1, 1, 1, 1, 0]. Which statements are correct?

**1.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**2.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**3.** The Jaccard coefficient Jc(x1,x2) is approximately 0.5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.5.

**4.** The count of 1–1 matches n11 is approximately 4.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 4.

**5.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.6.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.6.

---

## Question 317 · Outlier Detection

Consider the 2-D points [[1, 1], [4, 5], [0, 2], [3, 2], [4, 1], [3, 5], [16, 12]]. Which statements are correct?

**1.** The unweighted KNN outlier scores with k=2 (per point, in order) are [2.24, 3.16, 4.0, 2.24, 3.0, 3.0, 14.76].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [2.24, 3.16, 3.0, 2.24, 3.0, 3.0, 14.76], not [2.24, 3.16, 4.0, 2.24, 3.0, 3.0, 14.76].

**2.** Point 6 (the far point) receives the largest LOF, consistent with being an outlier.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF values ≈ [1.0, 1.09, 1.0, 1.0, 1.0, 1.09, 4.65]; the isolated point has LOF ≫ 1.

**3.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

**4.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

**5.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

---

## Question 318 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[1, 2], [0, 1], [2, 0], [3, 3], [8, 10], [9, 9], [8, 8], [10, 11]] with initial prototypes [[1, 2], [9, 9]]. Which statements are correct?

**1.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**2.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**3.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.782.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 0.782.

**4.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**5.** The final SSE (sum of squared errors) of the partition is approximately 17.6.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 17.75, not 17.6.

---

## Question 319 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[0, 2], [0, 2], [2, 3], [1, 3], [9, 11], [11, 9], [8, 9], [11, 10]] with initial prototypes [[0, 2], [11, 9]]. Which statements are correct?

**1.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**2.** The final cluster labels (one per point, in order) are [0, 1, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 1, 0, 0, 1, 1, 1, 1].

**3.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**4.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**5.** The final SSE (sum of squared errors) of the partition is approximately 12.75.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 13.25, not 12.75.

---

## Question 320 · Outlier Detection

Consider the 2-D points [[6, 2], [7, 7], [2, 3], [1, 6], [3, 2], [4, 1], [17, 15]]. Which statements are correct?

**1.** Point 6 (the far point) receives the largest LOF, consistent with being an outlier.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF values ≈ [1.11, 1.8, 0.9, 1.65, 1.17, 0.86, 4.18]; the isolated point has LOF ≫ 1.

**2.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

**3.** LOF is a global density score that compares each point's density to the dataset-wide average density.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] LOF is a LOCAL/relative score: density vs the point's own neighbours.

**4.** The weighted KNN outlier score averages a point's distances to all its 1st…k-th nearest neighbours.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] Weighted-kNN aggregates (averages) the 1..k NN distances; plain kNN uses only the k-th.

**5.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

---

## Question 321 · Probability & Density

A test has sensitivity P(+|D)=0.95 and specificity 0.95; disease prevalence is P(D)=0.01. Also consider the sample [5, 4, 3, 6, 6]. Which statements are correct?

**1.** The sample mean of the listed sample is approximately 4.8.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 4.8.

**2.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**3.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**4.** The posterior P(D | +) by Bayes' rule is approximately 0.161.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 0.161.

**5.** The sample variance (÷ n−1) of the listed sample is approximately 1.7.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 1.7.

---

## Question 322 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0146 and 0.014, with priors π_C1 = 0.5 and π_C2 = 0.5. Which statements are correct?

**1.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

**2.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**3.** The posterior probability (responsibility) of C1 at x is approximately 0.51.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.51.

**4.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

**5.** The posterior probability (responsibility) of C2 at x is approximately 0.49.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.49.

---

## Question 323 · Outlier Detection

Consider the 2-D points [[0, 0], [6, 4], [3, 0], [2, 2], [2, 5], [4, 7], [17, 16]]. Which statements are correct?

**1.** The weighted KNN outlier score averages a point's distances to all its 1st…k-th nearest neighbours.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] Weighted-kNN aggregates (averages) the 1..k NN distances; plain kNN uses only the k-th.

**2.** The unweighted KNN outlier scores with k=2 (per point, in order) are [3.0, 4.12, 4.0, 2.83, 3.0, 3.61, 16.28].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [3.0, 4.12, 3.0, 2.83, 3.0, 3.61, 16.28], not [3.0, 4.12, 4.0, 2.83, 3.0, 3.61, 16.28].

**3.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

**4.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

**5.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

---

## Question 324 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0198 and 0.0192, with priors π_C1 = 0.6 and π_C2 = 0.4. Which statements are correct?

**1.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**2.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

**3.** The posterior probability (responsibility) of C2 at x is approximately 0.393.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.393.

**4.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

**5.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

---

## Question 325 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0074 and 0.018, with priors π_C1 = 0.6 and π_C2 = 0.4. Which statements are correct?

**1.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

**2.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

**3.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**4.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

**5.** The posterior probability (responsibility) of C1 at x is approximately 0.381.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.381.

---

## Question 326 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-30, 6, 18, 19, 63, 64, 99, 103}. Which statements are correct?

**1.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 42.75, σ̂² = (1/n)Σ(x−μ̂)² ≈ 1934.44.

**2.** The MLE estimate of the variance σ² (dividing by n) is approximately 1934.44.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 1934.44.

**3.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [36, 12, 1, 1, 4, 1, 4, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [36, 12, 1, 1, 1, 1, 4, 4], not [36, 12, 1, 1, 4, 1, 4, 1].

**4.** With ε = 25 and MinPts = 1, DBSCAN groups the data into the clusters [[-30], [6, 18, 19], [63, 64], [99, 103]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=25, MinPts=1) gives clusters [[-30], [6, 18, 19], [63, 64], [99, 103]]; no noise.

**5.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

---

## Question 327 · Hierarchical

Consider 4 objects with the symmetric distance matrix (0-based indices):

```
[0, 5, 3, 3]
[5, 0, 7, 8]
[3, 7, 0, 4]
[3, 8, 4, 0]
```

Which statements are correct?

**1.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**2.** Using Single-Linkage, the first merge joins objects 0 and 2 at height 3.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (0,)+(2,) at 3.

**3.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**4.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**5.** Using Complete-Linkage, the height of the final (root) merge is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 8, not 5.

---

## Question 328 · Data Representation

Two objects are described by 12 binary (asymmetric/symmetric) variables: x1 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1] and x2 = [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0]. Which statements are correct?

**1.** The count of disagreements n10 + n01 is approximately 9.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 8, not 9.

**2.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.033.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.333, not 0.033.

**3.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**4.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**5.** The count of 1–1 matches n11 is approximately 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 1.

---

## Question 329 · Probability & Density

A test has sensitivity P(+|D)=0.95 and specificity 0.9; disease prevalence is P(D)=0.1. Also consider the sample [6, 1, 3, 5, 6]. Which statements are correct?

**1.** The sample mean of the listed sample is approximately 4.2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 4.2.

**2.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**3.** The posterior P(D | +) by Bayes' rule is approximately 0.814.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.514, not 0.814.

**4.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**5.** The sample variance (÷ n−1) of the listed sample is approximately 4.4.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 4.7, not 4.4.

---

## Question 330 · Data Representation

Consider two records described by 4 numerical variables: u = [8, 6, 8, -4] and v = [-2, 9, -3, -2]. Which statements are correct?

**1.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

**2.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

**3.** The inner product <u,v> is approximately 20.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 22, not 20.

**4.** The Manhattan (city-block) distance d(u,v) is approximately 26.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 26.

**5.** The cosine similarity cos(u,v) is approximately 0.166.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.166.

---

## Question 331 · Data Representation

Two objects are described by 12 binary (asymmetric/symmetric) variables: x1 = [1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1] and x2 = [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]. Which statements are correct?

**1.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**2.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**3.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.667.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.667.

**4.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**5.** The count of disagreements n10 + n01 is approximately 3.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 4, not 3.

---

## Question 332 · Data Representation

Consider two records described by 3 numerical variables: u = [9, 9, 3] and v = [4, 9, 5]. Which statements are correct?

**1.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

**2.** The Euclidean distance d(u,v) is approximately 5.19.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 5.39, not 5.19.

**3.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

**4.** The cosine similarity cos(u,v) is approximately 0.914.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.914.

**5.** The Minkowski distance of order p=3 between u and v is approximately 5.0.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 5.1, not 5.0.

---

## Question 333 · Data Representation

Consider two records described by 3 numerical variables: u = [-5, -2, 4] and v = [-3, 7, -2]. Which statements are correct?

**1.** The Suprema (Chebyshev) distance d(u,v) is approximately 7.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 9, not 7.

**2.** The inner product <u,v> is approximately -9.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ -7, not -9.

**3.** The Euclidean distance d(u,v) is approximately 11.3.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 11.0, not 11.3.

**4.** The cosine similarity cos(u,v) is approximately -0.133.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ -0.133.

**5.** The Manhattan (city-block) distance d(u,v) is approximately 18.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 17, not 18.

---

## Question 334 · Hierarchical

Consider 4 objects with the symmetric distance matrix (0-based indices):

```
[0, 10, 11, 4]
[10, 0, 12, 12]
[11, 12, 0, 8]
[4, 12, 8, 0]
```

Which statements are correct?

**1.** Using Single-Linkage, the first merge joins objects 0 and 3 at height 4.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (0,)+(3,) at 4.

**2.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**3.** Using Complete-Linkage, the height of the final (root) merge is approximately 14.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 12, not 14.

**4.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

**5.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

---

## Question 335 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.015 and 0.0143, with priors π_C1 = 0.2 and π_C2 = 0.8. Which statements are correct?

**1.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

**2.** The posterior probability (responsibility) of C2 at x is approximately 0.792.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.792.

**3.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**4.** The posterior probability (responsibility) of C1 at x is approximately 0.208.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.208.

**5.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

---

## Question 336 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0153 and 0.0023, with priors π_C1 = 0.5 and π_C2 = 0.5. Which statements are correct?

**1.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**2.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**3.** The posterior probability (responsibility) of C1 at x is approximately 0.869.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.869.

**4.** The posterior probability (responsibility) of C2 at x is approximately 0.131.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.131.

**5.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

---

## Question 337 · Hierarchical

Consider 5 objects with the symmetric distance matrix (0-based indices):

```
[0, 10, 12, 6, 10]
[10, 0, 9, 3, 6]
[12, 9, 0, 7, 5]
[6, 3, 7, 0, 5]
[10, 6, 5, 5, 0]
```

Which statements are correct?

**1.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**2.** Using Single-Linkage, the first merge joins objects 1 and 3 at height 3.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (1,)+(3,) at 3.

**3.** Using Complete-Linkage, the height of the final (root) merge is approximately 12.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 12.

**4.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**5.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

---

## Question 338 · Data Representation

Two objects are described by 12 binary (asymmetric/symmetric) variables: x1 = [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1] and x2 = [1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1]. Which statements are correct?

**1.** The count of 1–1 matches n11 is approximately 3.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 3.

**2.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**3.** The count of disagreements n10 + n01 is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 6, not 5.

**4.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**5.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

---

## Question 339 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[0, 1], [1, 1], [3, 0], [1, 1], [10, 9], [10, 9], [9, 8], [8, 9]] with initial prototypes [[0, 1], [10, 9]]. Which statements are correct?

**1.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**2.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.868, not 1.

**3.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**4.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**5.** The final SSE (sum of squared errors) of the partition is approximately 9.0.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 9.0.

---

## Question 340 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0034 and 0.0083, with priors π_C1 = 0.3 and π_C2 = 0.7. Which statements are correct?

**1.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**2.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**3.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**4.** The posterior probability (responsibility) of C2 at x is approximately 0.651.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The correct value is ≈ 0.851, not 0.651.

**5.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

---

## Question 341 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[1, 0], [2, 0], [0, 0], [1, 3], [10, 11], [11, 11], [8, 11], [11, 9]] with initial prototypes [[1, 0], [11, 11]]. Which statements are correct?

**1.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**2.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**3.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**4.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 1, 1, 1, 2].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 0, 0, 0, 1, 1, 1, 2].

**5.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.328.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.828, not 0.328.

---

## Question 342 · Data Representation

Two objects are described by 10 binary (asymmetric/symmetric) variables: x1 = [0, 0, 1, 0, 1, 0, 1, 0, 1, 0] and x2 = [1, 0, 0, 1, 0, 0, 0, 0, 0, 1]. Which statements are correct?

**1.** The count of disagreements n10 + n01 is approximately 10.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 7, not 10.

**2.** The count of 1–1 matches n11 is approximately 2.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0, not 2.

**3.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**4.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.3.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.3.

**5.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

---

## Question 343 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-28, -26, 1, 47, 52, 90}. Which statements are correct?

**1.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [2, 2, 38, 5, 5, 27].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [2, 2, 27, 5, 5, 38], not [2, 2, 38, 5, 5, 27].

**2.** The MLE estimate of the mean μ is approximately 22.67.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 22.67.

**3.** The MLE estimate of the variance σ² (dividing by n) is approximately 1898.46.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 1898.56, not 1898.46.

**4.** With ε = 15 and MinPts = 1, DBSCAN groups the data into the clusters [[-28, -26], [1], [47, 52], [90]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=15, MinPts=1) gives clusters [[-28, -26], [1], [47, 52], [90]]; no noise.

**5.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

---

## Question 344 · Outlier Detection

Consider the 2-D points [[4, 0], [7, 7], [5, 4], [2, 0], [5, 6], [6, 6], [16, 14]]. Which statements are correct?

**1.** LOF is a global density score that compares each point's density to the dataset-wide average density.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] LOF is a LOCAL/relative score: density vs the point's own neighbours.

**2.** The unweighted KNN outlier scores with k=1 (per point, in order) are [2.0, 1.41, 2.0, 3.0, 1.0, 1.0, 11.4].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [2.0, 1.41, 2.0, 2.0, 1.0, 1.0, 11.4], not [2.0, 1.41, 2.0, 3.0, 1.0, 1.0, 11.4].

**3.** Point 6 (the far point) receives the largest LOF, consistent with being an outlier.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF values ≈ [1.58, 0.93, 1.08, 1.58, 0.86, 1.16, 6.17]; the isolated point has LOF ≫ 1.

**4.** The weighted KNN outlier score averages a point's distances to all its 1st…k-th nearest neighbours.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] Weighted-kNN aggregates (averages) the 1..k NN distances; plain kNN uses only the k-th.

**5.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

---

## Question 345 · Probability & Density

A test has sensitivity P(+|D)=0.9 and specificity 0.95; disease prevalence is P(D)=0.02. Also consider the sample [6, 6, 3, 4, 5]. Which statements are correct?

**1.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**2.** The posterior P(D | +) by Bayes' rule is approximately 0.419.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.269, not 0.419.

**3.** The sample variance (÷ n−1) of the listed sample is approximately 1.55.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 1.7, not 1.55.

**4.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**5.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

---

## Question 346 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {2, 29, 39, 66, 77, 95}. Which statements are correct?

**1.** With ε = 15 and MinPts = 1, DBSCAN groups the data into the clusters [[2], [29, 39], [66, 77], [95]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=15, MinPts=1) gives clusters [[2], [29, 39], [66, 77], [95]]; no noise.

**2.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [27, 10, 10, 11, 18, 11].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [27, 10, 10, 11, 11, 18], not [27, 10, 10, 11, 18, 11].

**3.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**4.** The MLE estimate of the mean μ is approximately 51.43.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 51.33, not 51.43.

**5.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

---

## Question 347 · Data Representation

Two objects are described by 12 binary (asymmetric/symmetric) variables: x1 = [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0] and x2 = [1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1]. Which statements are correct?

**1.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**2.** The count of 1–1 matches n11 is approximately 3.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 3.

**3.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**4.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**5.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.5.

---

## Question 348 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-12, 6, 15, 19, 61, 96, 98, 99}. Which statements are correct?

**1.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [18, 9, 4, 4, 35, 2, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] The values are [18, 9, 4, 4, 35, 2, 1, 1].

**2.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**3.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**4.** The MLE estimate of the mean μ is approximately 47.6.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 47.75, not 47.6.

**5.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

---

## Question 349 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[3, 3], [3, 2], [2, 0], [0, 1], [10, 11], [9, 9], [8, 10], [11, 9]] with initial prototypes [[3, 3], [9, 9]]. Which statements are correct?

**1.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**2.** The final SSE (sum of squared errors) of the partition is approximately 18.6.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 18.75, not 18.6.

**3.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] The values are [0, 0, 0, 0, 1, 1, 1, 1].

**4.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**5.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

---

## Question 350 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0156 and 0.0162, with priors π_C1 = 0.4 and π_C2 = 0.6. Which statements are correct?

**1.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**2.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**3.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

**4.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

**5.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

---

## Question 351 · Data Representation

Two objects are described by 8 binary (asymmetric/symmetric) variables: x1 = [0, 1, 1, 1, 1, 1, 0, 1] and x2 = [1, 0, 0, 1, 0, 0, 1, 0]. Which statements are correct?

**1.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**2.** The count of 1–1 matches n11 is approximately 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 1.

**3.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**4.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.125.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.125.

**5.** The count of disagreements n10 + n01 is approximately 7.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 7.

---

## Question 352 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {8, 17, 34, 80, 86, 89}. Which statements are correct?

**1.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**2.** With ε = 10 and MinPts = 1, DBSCAN groups the data into the clusters [[8, 17], [34], [80, 86, 89]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=10, MinPts=1) gives clusters [[8, 17], [34], [80, 86, 89]]; no noise.

**3.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**4.** The MLE estimate of the variance σ² (dividing by n) is approximately 1132.12.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 1132.22, not 1132.12.

**5.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 52.33, σ̂² = (1/n)Σ(x−μ̂)² ≈ 1132.22.

---

## Question 353 · Data Representation

Two objects are described by 12 binary (asymmetric/symmetric) variables: x1 = [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0] and x2 = [1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0]. Which statements are correct?

**1.** The count of 1–1 matches n11 is approximately 4.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 2, not 4.

**2.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**3.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**4.** The count of disagreements n10 + n01 is approximately 8.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 6, not 8.

**5.** The Jaccard coefficient Jc(x1,x2) is approximately 0.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.25, not 0.

---

## Question 354 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-22, -21, 39, 68, 82, 105}. Which statements are correct?

**1.** The MLE estimate of the mean μ is approximately 42.03.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 41.83, not 42.03.

**2.** With ε = 10 and MinPts = 1, DBSCAN groups the data into the clusters [[-22, -21], [39], [68], [82], [105]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=10, MinPts=1) gives clusters [[-22, -21], [39], [68], [82], [105]]; no noise.

**3.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**4.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**5.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

---

## Question 355 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[3, 1], [3, 3], [0, 1], [2, 1], [11, 11], [10, 8], [11, 10], [8, 9]] with initial prototypes [[3, 1], [10, 8]]. Which statements are correct?

**1.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**2.** The final SSE (sum of squared errors) of the partition is approximately 20.3.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 20.0, not 20.3.

**3.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.782.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 0.782.

**4.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**5.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] The values are [0, 0, 0, 0, 1, 1, 1, 1].

---

## Question 356 · Probability & Density

A test has sensitivity P(+|D)=0.99 and specificity 0.95; disease prevalence is P(D)=0.05. Also consider the sample [2, 6, 4, 4, 2]. Which statements are correct?

**1.** The sample mean of the listed sample is approximately 3.6.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 3.6.

**2.** The posterior P(D | +) by Bayes' rule is approximately 0.01.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.51, not 0.01.

**3.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**4.** The sample variance (÷ n−1) of the listed sample is approximately 2.8.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 2.8.

**5.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

---

## Question 357 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[1, 0], [0, 2], [0, 3], [2, 0], [11, 8], [9, 11], [10, 9], [9, 8]] with initial prototypes [[1, 0], [9, 11]]. Which statements are correct?

**1.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**2.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**3.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**4.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**5.** The final cluster labels (one per point, in order) are [1, 0, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [1, 0, 0, 0, 1, 1, 1, 1].

---

## Question 358 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0157 and 0.0127, with priors π_C1 = 0.4 and π_C2 = 0.6. Which statements are correct?

**1.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

**2.** The posterior probability (responsibility) of C2 at x is approximately 0.848.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The correct value is ≈ 0.548, not 0.848.

**3.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

**4.** The posterior probability (responsibility) of C1 at x is approximately 0.452.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.452.

**5.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

---

## Question 359 · Data Representation

Consider two records described by 5 numerical variables: u = [-1, 9, 0, -2, -1] and v = [5, 1, 7, -3, -5]. Which statements are correct?

**1.** The inner product <u,v> is approximately 15.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 15.

**2.** The Minkowski distance of order p=3 between u and v is approximately 10.58.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 10.43, not 10.58.

**3.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**4.** The Euclidean distance d(u,v) is approximately 13.18.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 12.88, not 13.18.

**5.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

---

## Question 360 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-28, -11, 34, 42, 67, 76, 92}. Which statements are correct?

**1.** With ε = 15 and MinPts = 1, DBSCAN groups the data into the clusters [[-28], [-11], [34, 42], [67, 76], [92]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=15, MinPts=1) gives clusters [[-28], [-11], [34, 42], [67, 76], [92]]; no noise.

**2.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**3.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**4.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [17, 17, 8, 8, 9, 9, 16].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] The values are [17, 17, 8, 8, 9, 9, 16].

**5.** The MLE estimate of the mean μ is approximately 38.86.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 38.86.

---

## Question 361 · Hierarchical

Consider 4 objects with the symmetric distance matrix (0-based indices):

```
[0, 1, 12, 4]
[1, 0, 1, 6]
[12, 1, 0, 7]
[4, 6, 7, 0]
```

Which statements are correct?

**1.** Using Complete-Linkage, the height of the final (root) merge is approximately 14.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 12, not 14.

**2.** Using Single-Linkage, the height of the final (root) merge is approximately 4.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 4.

**3.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

**4.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**5.** Using Single-Linkage, the first merge joins objects 0 and 1 at height 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (0,)+(1,) at 1.

---

## Question 362 · Probability & Density

A test has sensitivity P(+|D)=0.9 and specificity 0.9; disease prevalence is P(D)=0.01. Also consider the sample [2, 5, 3, 1, 2]. Which statements are correct?

**1.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**2.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**3.** The posterior P(D | +) by Bayes' rule is approximately 0.083.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 0.083.

**4.** The sample mean of the listed sample is approximately 2.6.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 2.6.

**5.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

---

## Question 363 · Data Representation

Consider two records described by 5 numerical variables: u = [4, 8, 1, 3, 2] and v = [2, 3, 6, 5, -5]. Which statements are correct?

**1.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

**2.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**3.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

**4.** The Manhattan (city-block) distance d(u,v) is approximately 20.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 21, not 20.

**5.** The inner product <u,v> is approximately 44.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 43, not 44.

---

## Question 364 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0067 and 0.0111, with priors π_C1 = 0.5 and π_C2 = 0.5. Which statements are correct?

**1.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

**2.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

**3.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**4.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

**5.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

---

## Question 365 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0041 and 0.0026, with priors π_C1 = 0.2 and π_C2 = 0.8. Which statements are correct?

**1.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**2.** The posterior probability (responsibility) of C2 at x is approximately 1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The correct value is ≈ 0.717, not 1.

**3.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**4.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

**5.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

---

## Question 366 · Data Representation

Two objects are described by 8 binary (asymmetric/symmetric) variables: x1 = [0, 1, 0, 1, 0, 1, 1, 1] and x2 = [0, 1, 0, 0, 1, 0, 1, 1]. Which statements are correct?

**1.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.325.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.625, not 0.325.

**2.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**3.** The count of disagreements n10 + n01 is approximately 3.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 3.

**4.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**5.** The Jaccard coefficient Jc(x1,x2) is approximately 0.5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.5.

---

## Question 367 · Data Representation

Two objects are described by 12 binary (asymmetric/symmetric) variables: x1 = [1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1] and x2 = [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0]. Which statements are correct?

**1.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**2.** The count of disagreements n10 + n01 is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 5.

**3.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**4.** The count of 1–1 matches n11 is approximately 4.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 2, not 4.

**5.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

---

## Question 368 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 5). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, BUTTER, EGGS |
| 2 | BEER, BUTTER, EGGS |
| 3 | BEER, BUTTER, EGGS |
| 4 | BEER, BUTTER, DIAPERS, EGGS, MILK |
| 5 | BEER, BUTTER, DIAPERS, EGGS, MILK |
| 6 | BUTTER, EGGS, MILK |
| 7 | BEER, BUTTER, DIAPERS, EGGS, MILK |
| 8 | BEER, BUTTER, DIAPERS, EGGS, MILK |
| 9 | BUTTER, DIAPERS, EGGS, MILK |
| 10 | BEER, EGGS, MILK |

**1.** The lift of the rule {BUTTER} ⇒ {DIAPERS} is approximately 1.111.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 1.111.

**2.** The frequent itemset {BUTTER} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

**3.** The support count of the itemset {BUTTER, DIAPERS} is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 5.

**4.** The support count of {EGGS} is approximately 10.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 10.

**5.** By anti-monotonicity (downward closure), every subset of a frequent itemset is also frequent.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Apriori prunes any candidate having an infrequent subset before counting support.

---

## Question 369 · Hierarchical

Consider 4 objects with the symmetric distance matrix (0-based indices):

```
[0, 4, 9, 11]
[4, 0, 10, 8]
[9, 10, 0, 6]
[11, 8, 6, 0]
```

Which statements are correct?

**1.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**2.** Using Complete-Linkage, the height of the final (root) merge is approximately 9.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 11, not 9.

**3.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

**4.** Using Single-Linkage, the height of the final (root) merge is approximately 8.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 8.

**5.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

---

## Question 370 · Data Representation

Consider two records described by 4 numerical variables: u = [6, -3, 2, 7] and v = [5, -5, -5, 7]. Which statements are correct?

**1.** The inner product <u,v> is approximately 84.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 84.

**2.** The Manhattan (city-block) distance d(u,v) is approximately 10.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 10.

**3.** The Minkowski distance of order p=3 between u and v is approximately 6.91.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 7.06, not 6.91.

**4.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

**5.** The Suprema (Chebyshev) distance d(u,v) is approximately 7.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 7.

---

## Question 371 · Data Representation

Two objects are described by 12 binary (asymmetric/symmetric) variables: x1 = [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0] and x2 = [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1]. Which statements are correct?

**1.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**2.** The Jaccard coefficient Jc(x1,x2) is approximately 0.643.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.143, not 0.643.

**3.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.3.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.5, not 0.3.

**4.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**5.** The count of disagreements n10 + n01 is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 6.

---

## Question 372 · Data Representation

Consider two records described by 4 numerical variables: u = [-1, 5, 9, 5] and v = [-5, 7, -4, -1]. Which statements are correct?

**1.** The Minkowski distance of order p=3 between u and v is approximately 13.04.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 13.54, not 13.04.

**2.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

**3.** The Euclidean distance d(u,v) is approximately 15.0.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 15.0.

**4.** The Suprema (Chebyshev) distance d(u,v) is approximately 14.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 13, not 14.

**5.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

---

## Question 373 · Outlier Detection

Consider the 2-D points [[7, 1], [7, 7], [4, 3], [1, 1], [4, 2], [0, 2], [15, 17]]. Which statements are correct?

**1.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

**2.** LOF is a global density score that compares each point's density to the dataset-wide average density.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] LOF is a LOCAL/relative score: density vs the point's own neighbours.

**3.** The unweighted KNN outlier scores with k=2 (per point, in order) are [3.61, 5.83, 3.61, 3.16, 3.16, 4.0, 17.8].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] The values are [3.61, 5.83, 3.61, 3.16, 3.16, 4.0, 17.8].

**4.** Point 6 (the far point) receives the largest LOF, consistent with being an outlier.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF values ≈ [0.98, 1.57, 1.0, 1.02, 1.0, 1.02, 3.63]; the isolated point has LOF ≫ 1.

**5.** The weighted KNN outlier score averages a point's distances to all its 1st…k-th nearest neighbours.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] Weighted-kNN aggregates (averages) the 1..k NN distances; plain kNN uses only the k-th.

---

## Question 374 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[1, 2], [2, 1], [0, 0], [0, 2], [10, 9], [11, 8], [8, 10], [10, 11]] with initial prototypes [[1, 2], [11, 8]]. Which statements are correct?

**1.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] The values are [0, 0, 0, 0, 1, 1, 1, 1].

**2.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**3.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.675.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.825, not 0.675.

**4.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**5.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

---

## Question 375 · Data Representation

Two objects are described by 10 binary (asymmetric/symmetric) variables: x1 = [1, 0, 1, 1, 0, 0, 1, 1, 1, 1] and x2 = [0, 0, 0, 1, 1, 1, 0, 0, 0, 1]. Which statements are correct?

**1.** The Jaccard coefficient Jc(x1,x2) is approximately 0.222.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.222.

**2.** The count of disagreements n10 + n01 is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 7, not 5.

**3.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**4.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**5.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.2.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.3, not 0.2.

---

## Question 376 · Data Representation

Consider two records described by 5 numerical variables: u = [1, -2, 0, -5, -5] and v = [-1, -5, -2, 2, 7]. Which statements are correct?

**1.** The Minkowski distance of order p=3 between u and v is approximately 12.53.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 12.83, not 12.53.

**2.** The Euclidean distance d(u,v) is approximately 14.39.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 14.49, not 14.39.

**3.** The inner product <u,v> is approximately -38.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ -36, not -38.

**4.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**5.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

---

## Question 377 · Hierarchical

Consider 5 objects with the symmetric distance matrix (0-based indices):

```
[0, 10, 11, 6, 3]
[10, 0, 10, 3, 8]
[11, 10, 0, 6, 11]
[6, 3, 6, 0, 4]
[3, 8, 11, 4, 0]
```

Which statements are correct?

**1.** Using Single-Linkage, the first merge joins objects 0 and 4 at height 3.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (0,)+(4,) at 3.

**2.** Using Complete-Linkage, the height of the final (root) merge is approximately 12.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 11, not 12.

**3.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**4.** Using Single-Linkage, the height of the final (root) merge is approximately 4.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 6, not 4.

**5.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

---

## Question 378 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-30, -27, 9, 22, 36, 67, 84, 88}. Which statements are correct?

**1.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 31.12, σ̂² = (1/n)Σ(x−μ̂)² ≈ 1878.61.

**2.** With ε = 25 and MinPts = 1, DBSCAN groups the data into the clusters [[-30, -27], [9, 22, 36], [67, 84, 88]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=25, MinPts=1) gives clusters [[-30, -27], [9, 22, 36], [67, 84, 88]]; no noise.

**3.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**4.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**5.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

---

## Question 379 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 4). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, BUTTER, CRACKERS, EGGS, JAM, MILK |
| 2 | BEER, BUTTER, CRACKERS, EGGS, MILK |
| 3 | CRACKERS, EGGS, JAM, MILK |
| 4 | BEER, CRACKERS, EGGS |
| 5 | BEER, EGGS |
| 6 | BEER, EGGS, JAM, MILK |
| 7 | BUTTER, CRACKERS, EGGS, MILK |
| 8 | BEER, BUTTER, MILK |
| 9 | CRACKERS, EGGS, JAM, MILK |
| 10 | BEER, BUTTER, EGGS, JAM, MILK |

**1.** With n distinct items the candidate search space contains 2^n possible itemsets.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Each item is in or out, giving 2^n itemsets — hence Apriori pruning is essential.

**2.** The confidence of the rule {MILK} ⇒ {JAM} is approximately 0.625.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 0.625.

**3.** The lift of the rule {MILK} ⇒ {JAM} is approximately 1.25.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 1.25.

**4.** The frequent itemset {EGGS} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

**5.** Confidence of X ⇒ Y is defined as support(X ∪ Y) / support(Y).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Confidence = support(X∪Y)/support(X) (divide by the antecedent's support).

---

## Question 380 · Data Representation

Two objects are described by 10 binary (asymmetric/symmetric) variables: x1 = [1, 1, 0, 1, 0, 1, 1, 0, 1, 0] and x2 = [0, 1, 0, 0, 1, 0, 1, 0, 0, 1]. Which statements are correct?

**1.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.4.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.4.

**2.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**3.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**4.** The count of 1–1 matches n11 is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 2, not 5.

**5.** The count of disagreements n10 + n01 is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 6, not 5.

---

## Question 381 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-29, -26, -10, 17, 23, 24, 85, 87}. Which statements are correct?

**1.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 21.38, σ̂² = (1/n)Σ(x−μ̂)² ≈ 1768.73.

**2.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**3.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [3, 3, 16, 2, 1, 1, 2, 6].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [3, 3, 16, 6, 1, 1, 2, 2], not [3, 3, 16, 2, 1, 1, 2, 6].

**4.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**5.** The MLE estimate of the mean μ is approximately 21.27.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 21.38, not 21.27.

---

## Question 382 · Hierarchical

Consider 4 objects with the symmetric distance matrix (0-based indices):

```
[0, 1, 12, 2]
[1, 0, 10, 10]
[12, 10, 0, 8]
[2, 10, 8, 0]
```

Which statements are correct?

**1.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**2.** Using Single-Linkage, the height of the final (root) merge is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 8, not 6.

**3.** Using Single-Linkage, the first merge joins objects 0 and 1 at height 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (0,)+(1,) at 1.

**4.** Using Complete-Linkage, the height of the final (root) merge is approximately 14.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 12, not 14.

**5.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

---

## Question 383 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 6). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BREAD, CRACKERS, EGGS |
| 2 | BREAD, CRACKERS, DIAPERS, EGGS, MILK |
| 3 | BREAD, CRACKERS, EGGS |
| 4 | CRACKERS, MILK |
| 5 | DIAPERS, EGGS |
| 6 | DIAPERS, MILK |
| 7 | BREAD, CRACKERS, DIAPERS, EGGS, MILK |
| 8 | BREAD, EGGS |
| 9 | BREAD, CRACKERS, DIAPERS, EGGS |
| 10 | BREAD, DIAPERS, MILK |
| 11 | BREAD, EGGS, MILK |
| 12 | BREAD, MILK |
| 13 | CRACKERS, DIAPERS, EGGS, MILK |
| 14 | BREAD, MILK |

**1.** The support count of {MILK} is approximately 12.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 9, not 12.

**2.** The frequent itemset {CRACKERS} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

**3.** The support count of the itemset {BREAD, CRACKERS} is approximately 3.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 5, not 3.

**4.** With n distinct items the candidate search space contains 2^n possible itemsets.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Each item is in or out, giving 2^n itemsets — hence Apriori pruning is essential.

**5.** The lift of the rule {BREAD} ⇒ {CRACKERS} is approximately 1.0.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 1.0.

---

## Question 384 · Probability & Density

A test has sensitivity P(+|D)=0.95 and specificity 0.99; disease prevalence is P(D)=0.02. Also consider the sample [4, 1, 2, 2, 3]. Which statements are correct?

**1.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**2.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**3.** The sample mean of the listed sample is approximately 2.4.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 2.4.

**4.** The posterior P(D | +) by Bayes' rule is approximately 0.66.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 0.66.

**5.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

---

## Question 385 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[3, 1], [2, 2], [0, 0], [0, 1], [8, 10], [10, 10], [11, 8], [8, 9]] with initial prototypes [[3, 1], [10, 10]]. Which statements are correct?

**1.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.698.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.798, not 0.698.

**2.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**3.** The final SSE (sum of squared errors) of the partition is approximately 18.25.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 18.25.

**4.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**5.** The final cluster labels (one per point, in order) are [0, 0, 0, 1, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 0, 0, 1, 1, 1, 1, 1].

---

## Question 386 · Probability & Density

A test has sensitivity P(+|D)=0.95 and specificity 0.95; disease prevalence is P(D)=0.05. Also consider the sample [1, 1, 2, 2, 5]. Which statements are correct?

**1.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**2.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**3.** The sample variance (÷ n−1) of the listed sample is approximately 2.7.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 2.7.

**4.** The posterior P(D | +) by Bayes' rule is approximately 0.7.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.5, not 0.7.

**5.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

---

## Question 387 · Data Representation

Consider two records described by 5 numerical variables: u = [-1, -4, 6, 9, 3] and v = [5, 8, -3, -1, -4]. Which statements are correct?

**1.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**2.** The Euclidean distance d(u,v) is approximately 20.75.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 20.25, not 20.75.

**3.** The Manhattan (city-block) distance d(u,v) is approximately 44.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 44.

**4.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

**5.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

---

## Question 388 · Hierarchical

Consider 5 objects with the symmetric distance matrix (0-based indices):

```
[0, 3, 11, 6, 3]
[3, 0, 5, 1, 5]
[11, 5, 0, 10, 4]
[6, 1, 10, 0, 10]
[3, 5, 4, 10, 0]
```

Which statements are correct?

**1.** Using Complete-Linkage, the height of the final (root) merge is approximately 10.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 11, not 10.

**2.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**3.** Using Single-Linkage, the height of the final (root) merge is approximately 3.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 4, not 3.

**4.** Using Single-Linkage, the first merge joins objects 1 and 3 at height 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (1,)+(3,) at 1.

**5.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

---

## Question 389 · Data Representation

Consider two records described by 4 numerical variables: u = [3, -1, -5, -5] and v = [3, -5, -5, -5]. Which statements are correct?

**1.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**2.** The cosine similarity cos(u,v) is approximately 0.901.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.901.

**3.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

**4.** The Minkowski distance of order p=3 between u and v is approximately 4.2.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 4.0, not 4.2.

**5.** The Suprema (Chebyshev) distance d(u,v) is approximately 4.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 4.

---

## Question 390 · Data Representation

Consider two records described by 5 numerical variables: u = [9, 3, 1, 4, 8] and v = [-5, 8, 1, 3, 8]. Which statements are correct?

**1.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

**2.** The Manhattan (city-block) distance d(u,v) is approximately 22.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 20, not 22.

**3.** The Suprema (Chebyshev) distance d(u,v) is approximately 16.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 14, not 16.

**4.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

**5.** The Minkowski distance of order p=3 between u and v is approximately 14.21.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 14.21.

---

## Question 391 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 6). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, BREAD, BUTTER, DIAPERS, EGGS |
| 2 | BEER, BREAD, MILK |
| 3 | BEER, BREAD, EGGS, MILK |
| 4 | BUTTER, MILK |
| 5 | BEER, BUTTER, DIAPERS, EGGS, MILK |
| 6 | BEER, BREAD, BUTTER, DIAPERS, EGGS, MILK |
| 7 | BUTTER, DIAPERS, EGGS, MILK |
| 8 | BREAD, BUTTER, EGGS |
| 9 | DIAPERS, MILK |
| 10 | BEER, BREAD, BUTTER, DIAPERS, EGGS, MILK |
| 11 | BEER, BREAD, DIAPERS, EGGS |
| 12 | BEER, EGGS, MILK |
| 13 | DIAPERS, MILK |
| 14 | BEER, BREAD, BUTTER, MILK |

**1.** By anti-monotonicity (downward closure), every subset of a frequent itemset is also frequent.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Apriori prunes any candidate having an infrequent subset before counting support.

**2.** The frequent itemset {BUTTER} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

**3.** Apriori must scan the database to count the support of a candidate even when one of its subsets is already known to be infrequent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The prune step removes such candidates first, so no database scan is needed for them.

**4.** With n distinct items the candidate search space contains 2^n possible itemsets.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Each item is in or out, giving 2^n itemsets — hence Apriori pruning is essential.

**5.** The confidence of the rule {BREAD} ⇒ {BUTTER} is approximately 0.525.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 0.625, not 0.525.

---

## Question 392 · Data Representation

Consider two records described by 3 numerical variables: u = [-5, 4, 7] and v = [6, 1, -1]. Which statements are correct?

**1.** The Minkowski distance of order p=3 between u and v is approximately 12.52.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 12.32, not 12.52.

**2.** The cosine similarity cos(u,v) is approximately -0.564.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ -0.564.

**3.** The Manhattan (city-block) distance d(u,v) is approximately 22.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 22.

**4.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

**5.** The Euclidean distance d(u,v) is approximately 13.93.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 13.93.

---

## Question 393 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0051 and 0.0071, with priors π_C1 = 0.3 and π_C2 = 0.7. Which statements are correct?

**1.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**2.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**3.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

**4.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**5.** The posterior probability (responsibility) of C2 at x is approximately 0.765.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.765.

---

## Question 394 · Data Representation

Consider two records described by 4 numerical variables: u = [6, -3, -4, -5] and v = [6, 0, -4, 3]. Which statements are correct?

**1.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

**2.** The Euclidean distance d(u,v) is approximately 8.54.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 8.54.

**3.** The Suprema (Chebyshev) distance d(u,v) is approximately 8.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 8.

**4.** The Minkowski distance of order p=3 between u and v is approximately 8.14.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 8.14.

**5.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

---

## Question 395 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0089 and 0.0195, with priors π_C1 = 0.7 and π_C2 = 0.3. Which statements are correct?

**1.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

**2.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**3.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

**4.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**5.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

---

## Question 396 · Data Representation

Two objects are described by 8 binary (asymmetric/symmetric) variables: x1 = [0, 0, 1, 1, 1, 1, 1, 0] and x2 = [0, 0, 0, 0, 1, 0, 1, 0]. Which statements are correct?

**1.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**2.** The Jaccard coefficient Jc(x1,x2) is approximately 0.4.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.4.

**3.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**4.** The count of disagreements n10 + n01 is approximately 3.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 3.

**5.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

---

## Question 397 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[1, 1], [3, 1], [0, 1], [0, 2], [11, 8], [9, 10], [8, 11], [11, 10]] with initial prototypes [[1, 1], [9, 10]]. Which statements are correct?

**1.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.515.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.815, not 0.515.

**2.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**3.** The final SSE (sum of squared errors) of the partition is approximately 18.25.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 18.25.

**4.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**5.** The final cluster labels (one per point, in order) are [1, 0, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [1, 0, 0, 0, 1, 1, 1, 1].

---

## Question 398 · Probability & Density

A test has sensitivity P(+|D)=0.99 and specificity 0.95; disease prevalence is P(D)=0.01. Also consider the sample [3, 5, 2, 1, 5]. Which statements are correct?

**1.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**2.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**3.** The sample mean of the listed sample is approximately 3.05.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 3.2, not 3.05.

**4.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**5.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

---

## Question 399 · Probability & Density

A test has sensitivity P(+|D)=0.9 and specificity 0.95; disease prevalence is P(D)=0.02. Also consider the sample [5, 2, 4, 4, 1]. Which statements are correct?

**1.** The posterior P(D | +) by Bayes' rule is approximately 0.269.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 0.269.

**2.** The sample mean of the listed sample is approximately 3.5.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 3.2, not 3.5.

**3.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**4.** The sample variance (÷ n−1) of the listed sample is approximately 2.7.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 2.7.

**5.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

---

## Question 400 · Probability & Density

A test has sensitivity P(+|D)=0.99 and specificity 0.95; disease prevalence is P(D)=0.01. Also consider the sample [5, 4, 5, 5, 6]. Which statements are correct?

**1.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**2.** The posterior P(D | +) by Bayes' rule is approximately 0.467.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.167, not 0.467.

**3.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**4.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**5.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

---

## Question 401 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {28, 52, 67, 85, 86, 96, 103}. Which statements are correct?

**1.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**2.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**3.** With ε = 15 and MinPts = 1, DBSCAN groups the data into the clusters [[28], [52, 67], [85, 86, 96, 103]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=15, MinPts=1) gives clusters [[28], [52, 67], [85, 86, 96, 103]]; no noise.

**4.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**5.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [1, 15, 15, 24, 1, 7, 7].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [24, 15, 15, 1, 1, 7, 7], not [1, 15, 15, 24, 1, 7, 7].

---

## Question 402 · Outlier Detection

Consider the 2-D points [[7, 4], [6, 5], [5, 4], [2, 0], [2, 6], [4, 1], [17, 14]]. Which statements are correct?

**1.** The unweighted KNN outlier scores with k=1 (per point, in order) are [1.41, 1.41, 1.41, 2.24, 3.61, 2.24, 14.14].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] The values are [1.41, 1.41, 1.41, 2.24, 3.61, 2.24, 14.14].

**2.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

**3.** Point 6 (the far point) receives the largest LOF, consistent with being an outlier.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF values ≈ [0.93, 1.17, 0.93, 1.7, 2.1, 1.7, 7.7]; the isolated point has LOF ≫ 1.

**4.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

**5.** LOF is a global density score that compares each point's density to the dataset-wide average density.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] LOF is a LOCAL/relative score: density vs the point's own neighbours.

---

## Question 403 · Data Representation

Consider two records described by 3 numerical variables: u = [-2, -4, 6] and v = [5, 0, 7]. Which statements are correct?

**1.** The cosine similarity cos(u,v) is approximately 0.497.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.497.

**2.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

**3.** The Suprema (Chebyshev) distance d(u,v) is approximately 8.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 7, not 8.

**4.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

**5.** The Manhattan (city-block) distance d(u,v) is approximately 12.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 12.

---

## Question 404 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-30, -11, 14, 31, 89, 94, 96}. Which statements are correct?

**1.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 40.43, σ̂² = (1/n)Σ(x−μ̂)² ≈ 2387.1.

**2.** The MLE estimate of the variance σ² (dividing by n) is approximately 2387.1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 2387.1.

**3.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**4.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**5.** The MLE estimate of the mean μ is approximately 40.43.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 40.43.

---

## Question 405 · Outlier Detection

Consider the 2-D points [[7, 1], [2, 7], [0, 0], [5, 1], [6, 3], [4, 1], [14, 17]]. Which statements are correct?

**1.** The unweighted KNN outlier scores with k=1 (per point, in order) are [2.0, 5.66, 4.12, 1.0, 2.24, 1.0, 15.62].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] The values are [2.0, 5.66, 4.12, 1.0, 2.24, 1.0, 15.62].

**2.** LOF is a global density score that compares each point's density to the dataset-wide average density.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] LOF is a LOCAL/relative score: density vs the point's own neighbours.

**3.** Hawkins defines an outlier as an observation that deviates so much it appears generated by a different mechanism.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] This is the classic Hawkins (1980) definition.

**4.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

**5.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

---

## Question 406 · Data Representation

Consider two records described by 3 numerical variables: u = [-5, -3, -3] and v = [-5, 5, 7]. Which statements are correct?

**1.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**2.** The Minkowski distance of order p=3 between u and v is approximately 11.48.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 11.48.

**3.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

**4.** The Euclidean distance d(u,v) is approximately 12.61.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 12.81, not 12.61.

**5.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

---

## Question 407 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[3, 1], [3, 2], [0, 3], [3, 1], [11, 8], [11, 11], [9, 11], [10, 8]] with initial prototypes [[3, 1], [11, 11]]. Which statements are correct?

**1.** The final SSE (sum of squared errors) of the partition is approximately 20.75.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 21.25, not 20.75.

**2.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**3.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.792, not 1.

**4.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] The values are [0, 0, 0, 0, 1, 1, 1, 1].

**5.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

---

## Question 408 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[2, 2], [1, 2], [1, 0], [0, 0], [8, 11], [9, 8], [9, 9], [11, 10]] with initial prototypes [[2, 2], [9, 8]]. Which statements are correct?

**1.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] The values are [0, 0, 0, 0, 1, 1, 1, 1].

**2.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**3.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.918.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.818, not 0.918.

**4.** The final SSE (sum of squared errors) of the partition is approximately 15.95.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 15.75, not 15.95.

**5.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

---

## Question 409 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0072 and 0.0147, with priors π_C1 = 0.5 and π_C2 = 0.5. Which statements are correct?

**1.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**2.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**3.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

**4.** The posterior probability (responsibility) of C2 at x is approximately 0.671.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.671.

**5.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

---

## Question 410 · Data Representation

Two objects are described by 10 binary (asymmetric/symmetric) variables: x1 = [0, 1, 0, 1, 0, 0, 0, 1, 1, 0] and x2 = [0, 0, 1, 0, 1, 0, 0, 1, 1, 0]. Which statements are correct?

**1.** The count of disagreements n10 + n01 is approximately 4.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 4.

**2.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**3.** The Jaccard coefficient Jc(x1,x2) is approximately 0.833.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.333, not 0.833.

**4.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**5.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

---

## Question 411 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[1, 2], [3, 2], [1, 3], [2, 1], [8, 10], [10, 11], [10, 8], [8, 9]] with initial prototypes [[1, 2], [10, 11]]. Which statements are correct?

**1.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**2.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**3.** The final SSE (sum of squared errors) of the partition is approximately 14.05.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 13.75, not 14.05.

**4.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**5.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.806.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 0.806.

---

## Question 412 · Probability & Density

A test has sensitivity P(+|D)=0.95 and specificity 0.99; disease prevalence is P(D)=0.01. Also consider the sample [1, 5, 2, 5, 5]. Which statements are correct?

**1.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**2.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**3.** The sample mean of the listed sample is approximately 3.6.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 3.6.

**4.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**5.** The sample variance (÷ n−1) of the listed sample is approximately 3.95.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 3.8, not 3.95.

---

## Question 413 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-26, -2, 60, 105, 106, 108}. Which statements are correct?

**1.** The MLE estimate of the mean μ is approximately 58.4.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 58.5, not 58.4.

**2.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**3.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**4.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 58.5, σ̂² = (1/n)Σ(x−μ̂)² ≈ 2945.25.

**5.** With ε = 15 and MinPts = 2, DBSCAN groups the data into the clusters [[105, 106, 108]] with [-26, -2, 60] as noise.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=15, MinPts=2) gives clusters [[105, 106, 108]]; noise = [-26, -2, 60].

---

## Question 414 · Data Representation

Two objects are described by 8 binary (asymmetric/symmetric) variables: x1 = [1, 0, 0, 0, 0, 0, 0, 1] and x2 = [1, 0, 1, 1, 1, 1, 1, 0]. Which statements are correct?

**1.** The Jaccard coefficient Jc(x1,x2) is approximately 0.443.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.143, not 0.443.

**2.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**3.** The count of 1–1 matches n11 is approximately 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 1.

**4.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**5.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.25, not 0.1.

---

## Question 415 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0093 and 0.0128, with priors π_C1 = 0.2 and π_C2 = 0.8. Which statements are correct?

**1.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**2.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

**3.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**4.** The posterior probability (responsibility) of C1 at x is approximately 0.304.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The correct value is ≈ 0.154, not 0.304.

**5.** The posterior probability (responsibility) of C2 at x is approximately 0.546.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The correct value is ≈ 0.846, not 0.546.

---

## Question 416 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 4). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BREAD, JAM, MILK |
| 2 | BEER, BREAD, BUTTER |
| 3 | BEER, CRACKERS, JAM, MILK |
| 4 | BREAD, BUTTER |
| 5 | BEER, BREAD, BUTTER, CRACKERS, JAM, MILK |
| 6 | BEER, CRACKERS |
| 7 | CRACKERS, MILK |
| 8 | BEER, BREAD, BUTTER, JAM, MILK |
| 9 | BEER, BUTTER, MILK |
| 10 | BEER, CRACKERS, JAM |
| 11 | BEER, BREAD, BUTTER, CRACKERS, JAM, MILK |
| 12 | BREAD, JAM |
| 13 | BEER, BUTTER, CRACKERS, JAM, MILK |
| 14 | BEER, BREAD, MILK |

**1.** The frequent itemset {BUTTER} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

**2.** Apriori must scan the database to count the support of a candidate even when one of its subsets is already known to be infrequent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The prune step removes such candidates first, so no database scan is needed for them.

**3.** The frequent itemset {BUTTER} is maximal (it has no frequent superset).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Maximal = no superset reaches support 4.

**4.** By anti-monotonicity (downward closure), every subset of a frequent itemset is also frequent.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Apriori prunes any candidate having an infrequent subset before counting support.

**5.** The support count of the itemset {MILK, BEER} is approximately 10.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 7, not 10.

---

## Question 417 · Data Representation

Consider two records described by 3 numerical variables: u = [9, 0, 8] and v = [-4, 6, 5]. Which statements are correct?

**1.** The Minkowski distance of order p=3 between u and v is approximately 13.46.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 13.46.

**2.** The Euclidean distance d(u,v) is approximately 14.63.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 14.63.

**3.** The Suprema (Chebyshev) distance d(u,v) is approximately 13.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 13.

**4.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**5.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

---

## Question 418 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0022 and 0.0097, with priors π_C1 = 0.3 and π_C2 = 0.7. Which statements are correct?

**1.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**2.** The posterior probability (responsibility) of C1 at x is approximately 0.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The correct value is ≈ 0.089, not 0.

**3.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

**4.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**5.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

---

## Question 419 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[3, 3], [1, 3], [0, 2], [3, 2], [10, 10], [8, 9], [10, 11], [11, 9]] with initial prototypes [[3, 3], [8, 9]]. Which statements are correct?

**1.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**2.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.651.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.801, not 0.651.

**3.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**4.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**5.** The final SSE (sum of squared errors) of the partition is approximately 15.25.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 15.25.

---

## Question 420 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0089 and 0.0149, with priors π_C1 = 0.4 and π_C2 = 0.6. Which statements are correct?

**1.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**2.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

**3.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**4.** The posterior probability (responsibility) of C2 at x is approximately 1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The correct value is ≈ 0.715, not 1.

**5.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

---

## Question 421 · Hierarchical

Consider 5 objects with the symmetric distance matrix (0-based indices):

```
[0, 9, 10, 7, 9]
[9, 0, 5, 2, 10]
[10, 5, 0, 2, 3]
[7, 2, 2, 0, 11]
[9, 10, 3, 11, 0]
```

Which statements are correct?

**1.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

**2.** Using Complete-Linkage, the height of the final (root) merge is approximately 9.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 11, not 9.

**3.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**4.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**5.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

---

## Question 422 · Hierarchical

Consider 4 objects with the symmetric distance matrix (0-based indices):

```
[0, 9, 10, 7]
[9, 0, 2, 11]
[10, 2, 0, 7]
[7, 11, 7, 0]
```

Which statements are correct?

**1.** Using Single-Linkage, the height of the final (root) merge is approximately 7.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 7.

**2.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**3.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**4.** Using Single-Linkage, the first merge joins objects 1 and 2 at height 2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (1,)+(2,) at 2.

**5.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

---

## Question 423 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 6). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, BUTTER, CRACKERS, EGGS, MILK |
| 2 | BEER, BUTTER |
| 3 | BEER, BUTTER |
| 4 | BUTTER, EGGS |
| 5 | BEER, BUTTER, CRACKERS, MILK |
| 6 | BUTTER, MILK |
| 7 | BEER, BUTTER, MILK |
| 8 | BEER, BUTTER, CRACKERS, EGGS, MILK |
| 9 | BEER, BUTTER, CRACKERS, MILK |
| 10 | BEER, BUTTER, CRACKERS, EGGS |
| 11 | BEER, BUTTER, EGGS |
| 12 | CRACKERS, EGGS, MILK |
| 13 | BEER, BUTTER, CRACKERS, EGGS, MILK |
| 14 | BEER, EGGS, MILK |

**1.** Apriori must scan the database to count the support of a candidate even when one of its subsets is already known to be infrequent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The prune step removes such candidates first, so no database scan is needed for them.

**2.** The frequent itemset {BEER} is maximal (it has no frequent superset).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Maximal = no superset reaches support 6.

**3.** The lift of the rule {CRACKERS} ⇒ {BUTTER} is approximately 0.9.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 1.0, not 0.9.

**4.** The frequent itemset {BEER} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

**5.** With n distinct items the candidate search space contains 2^n possible itemsets.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Each item is in or out, giving 2^n itemsets — hence Apriori pruning is essential.

---

## Question 424 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-20, 16, 30, 53, 60, 80, 85}. Which statements are correct?

**1.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 43.43, σ̂² = (1/n)Σ(x−μ̂)² ≈ 1198.24.

**2.** The MLE estimate of the mean μ is approximately 43.28.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 43.43, not 43.28.

**3.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [36, 14, 5, 7, 7, 14, 5].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [36, 14, 14, 7, 7, 5, 5], not [36, 14, 5, 7, 7, 14, 5].

**4.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**5.** The MLE estimate of the variance σ² (dividing by n) is approximately 1198.54.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 1198.24, not 1198.54.

---

## Question 425 · Hierarchical

Consider 5 objects with the symmetric distance matrix (0-based indices):

```
[0, 6, 8, 12, 12]
[6, 0, 7, 7, 5]
[8, 7, 0, 7, 6]
[12, 7, 7, 0, 7]
[12, 5, 6, 7, 0]
```

Which statements are correct?

**1.** Using Single-Linkage, the height of the final (root) merge is approximately 7.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 7.

**2.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**3.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**4.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

**5.** Using Single-Linkage, the first merge joins objects 1 and 4 at height 5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (1,)+(4,) at 5.

---

## Question 426 · Data Representation

Two objects are described by 8 binary (asymmetric/symmetric) variables: x1 = [0, 0, 1, 0, 1, 1, 1, 0] and x2 = [1, 1, 1, 0, 0, 1, 0, 0]. Which statements are correct?

**1.** The count of 1–1 matches n11 is approximately 2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 2.

**2.** The Jaccard coefficient Jc(x1,x2) is approximately 0.333.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.333.

**3.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**4.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**5.** The count of disagreements n10 + n01 is approximately 4.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 4.

---

## Question 427 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[3, 2], [0, 3], [1, 3], [3, 1], [8, 11], [8, 10], [9, 9], [8, 10]] with initial prototypes [[3, 2], [8, 10]]. Which statements are correct?

**1.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**2.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.83.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 0.83.

**3.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**4.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] The values are [0, 0, 0, 0, 1, 1, 1, 1].

**5.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

---

## Question 428 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-28, -12, 41, 53, 83, 101}. Which statements are correct?

**1.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**2.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [16, 12, 12, 16, 18, 18].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [16, 16, 12, 12, 18, 18], not [16, 12, 12, 16, 18, 18].

**3.** The MLE estimate of the variance σ² (dividing by n) is approximately 2177.99.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 2177.89, not 2177.99.

**4.** With ε = 25 and MinPts = 1, DBSCAN groups the data into the clusters [[-28, -12], [41, 53], [83, 101]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=25, MinPts=1) gives clusters [[-28, -12], [41, 53], [83, 101]]; no noise.

**5.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

---

## Question 429 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 5). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | CRACKERS, EGGS, JAM |
| 2 | BEER, BREAD, CRACKERS, EGGS, JAM |
| 3 | CRACKERS, EGGS, JAM |
| 4 | BEER, BREAD, CRACKERS, EGGS, JAM |
| 5 | BEER, BREAD, CRACKERS, EGGS, JAM |
| 6 | CRACKERS, EGGS |
| 7 | BREAD, CRACKERS, JAM |
| 8 | BEER, BREAD, JAM |
| 9 | BEER, BREAD, CRACKERS |
| 10 | BEER, BREAD, CRACKERS, EGGS, JAM |

**1.** The confidence of the rule {CRACKERS} ⇒ {EGGS} is approximately 0.628.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 0.778, not 0.628.

**2.** By anti-monotonicity (downward closure), every subset of a frequent itemset is also frequent.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Apriori prunes any candidate having an infrequent subset before counting support.

**3.** The frequent itemset {CRACKERS} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

**4.** The frequent itemset {CRACKERS} is maximal (it has no frequent superset).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Maximal = no superset reaches support 5.

**5.** The lift of the rule {CRACKERS} ⇒ {EGGS} is approximately 1.111.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 1.111.

---

## Question 430 · Data Representation

Two objects are described by 10 binary (asymmetric/symmetric) variables: x1 = [1, 0, 0, 1, 0, 0, 1, 0, 0, 0] and x2 = [1, 1, 1, 1, 1, 0, 1, 1, 1, 1]. Which statements are correct?

**1.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.4.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.4.

**2.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**3.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**4.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**5.** The count of 1–1 matches n11 is approximately 2.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 3, not 2.

---

## Question 431 · Data Representation

Two objects are described by 8 binary (asymmetric/symmetric) variables: x1 = [1, 1, 1, 0, 0, 0, 0, 1] and x2 = [0, 0, 0, 0, 1, 0, 0, 0]. Which statements are correct?

**1.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**2.** The count of 1–1 matches n11 is approximately 0.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.

**3.** The Jaccard coefficient Jc(x1,x2) is approximately 0.1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.0, not 0.1.

**4.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**5.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.375.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.375.

---

## Question 432 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0172 and 0.0107, with priors π_C1 = 0.2 and π_C2 = 0.8. Which statements are correct?

**1.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**2.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

**3.** The posterior probability (responsibility) of C1 at x is approximately 0.137.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The correct value is ≈ 0.287, not 0.137.

**4.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

**5.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

---

## Question 433 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {16, 17, 45, 79, 80, 98, 100, 103}. Which statements are correct?

**1.** The MLE estimate of the mean μ is approximately 67.1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 67.25, not 67.1.

**2.** With ε = 20 and MinPts = 1, DBSCAN groups the data into the clusters [[16, 17], [45], [79, 80, 98, 100, 103]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=20, MinPts=1) gives clusters [[16, 17], [45], [79, 80, 98, 100, 103]]; no noise.

**3.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**4.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**5.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 67.25, σ̂² = (1/n)Σ(x−μ̂)² ≈ 1155.44.

---

## Question 434 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {2, 25, 38, 55, 83, 86}. Which statements are correct?

**1.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 48.17, σ̂² = (1/n)Σ(x−μ̂)² ≈ 910.47.

**2.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**3.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**4.** The MLE estimate of the mean μ is approximately 48.07.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 48.17, not 48.07.

**5.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

---

## Question 435 · Data Representation

Consider two records described by 3 numerical variables: u = [4, 4, -2] and v = [-5, -5, -3]. Which statements are correct?

**1.** The cosine similarity cos(u,v) is approximately -0.538.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ -0.738, not -0.538.

**2.** The Euclidean distance d(u,v) is approximately 12.57.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 12.77, not 12.57.

**3.** The Suprema (Chebyshev) distance d(u,v) is approximately 11.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 9, not 11.

**4.** The inner product <u,v> is approximately -34.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ -34.

**5.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

---

## Question 436 · Hierarchical

Consider 4 objects with the symmetric distance matrix (0-based indices):

```
[0, 4, 4, 11]
[4, 0, 10, 10]
[4, 10, 0, 4]
[11, 10, 4, 0]
```

Which statements are correct?

**1.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**2.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

**3.** Using Complete-Linkage, the height of the final (root) merge is approximately 11.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 11.

**4.** Using Single-Linkage, the first merge joins objects 0 and 1 at height 4.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (0,)+(1,) at 4.

**5.** Using Single-Linkage, the height of the final (root) merge is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 4, not 6.

---

## Question 437 · Probability & Density

A test has sensitivity P(+|D)=0.95 and specificity 0.95; disease prevalence is P(D)=0.1. Also consider the sample [4, 3, 3, 1, 5]. Which statements are correct?

**1.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**2.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**3.** The posterior P(D | +) by Bayes' rule is approximately 0.979.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.679, not 0.979.

**4.** The sample variance (÷ n−1) of the listed sample is approximately 2.2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 2.2.

**5.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

---

## Question 438 · Data Representation

Two objects are described by 12 binary (asymmetric/symmetric) variables: x1 = [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0] and x2 = [1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0]. Which statements are correct?

**1.** The count of 1–1 matches n11 is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 6.

**2.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**3.** The count of disagreements n10 + n01 is approximately 4.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 4.

**4.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**5.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

---

## Question 439 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {5, 7, 18, 49, 61, 79, 96, 105}. Which statements are correct?

**1.** The MLE estimate of the mean μ is approximately 52.5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 52.5.

**2.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 52.5, σ̂² = (1/n)Σ(x−μ̂)² ≈ 1369.0.

**3.** The MLE estimate of the variance σ² (dividing by n) is approximately 1369.15.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 1369.0, not 1369.15.

**4.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**5.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

---

## Question 440 · Data Representation

Two objects are described by 8 binary (asymmetric/symmetric) variables: x1 = [1, 0, 0, 0, 1, 1, 1, 1] and x2 = [1, 1, 1, 0, 0, 0, 1, 0]. Which statements are correct?

**1.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**2.** The Jaccard coefficient Jc(x1,x2) is approximately 0.286.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.286.

**3.** The count of disagreements n10 + n01 is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 5.

**4.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.475.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.375, not 0.475.

**5.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

---

## Question 441 · Data Representation

Consider two records described by 5 numerical variables: u = [5, 4, 1, 3, 8] and v = [2, 2, -2, 4, -1]. Which statements are correct?

**1.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**2.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

**3.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

**4.** The Euclidean distance d(u,v) is approximately 10.35.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 10.2, not 10.35.

**5.** The Suprema (Chebyshev) distance d(u,v) is approximately 9.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 9.

---

## Question 442 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {48, 51, 72, 84, 85, 106, 107}. Which statements are correct?

**1.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [3, 1, 12, 3, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [3, 3, 12, 1, 1, 1, 1], not [3, 1, 12, 3, 1, 1, 1].

**2.** With ε = 25 and MinPts = 2, DBSCAN groups the data into the clusters [[48, 51, 72, 84, 85, 106, 107]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=25, MinPts=2) gives clusters [[48, 51, 72, 84, 85, 106, 107]]; no noise.

**3.** The MLE estimate of the variance σ² (dividing by n) is approximately 481.14.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 481.14.

**4.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**5.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

---

## Question 443 · Data Representation

Consider two records described by 5 numerical variables: u = [3, 5, 9, -5, 7] and v = [4, 2, 5, -2, -3]. Which statements are correct?

**1.** The Minkowski distance of order p=3 between u and v is approximately 10.18.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 10.38, not 10.18.

**2.** The Suprema (Chebyshev) distance d(u,v) is approximately 12.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 10, not 12.

**3.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

**4.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**5.** The Manhattan (city-block) distance d(u,v) is approximately 21.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 21.

---

## Question 444 · Probability & Density

A test has sensitivity P(+|D)=0.99 and specificity 0.9; disease prevalence is P(D)=0.1. Also consider the sample [1, 4, 6, 1, 2]. Which statements are correct?

**1.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**2.** The posterior P(D | +) by Bayes' rule is approximately 1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.524, not 1.

**3.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**4.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**5.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

---

## Question 445 · Probability & Density

A test has sensitivity P(+|D)=0.95 and specificity 0.95; disease prevalence is P(D)=0.02. Also consider the sample [6, 1, 5, 3, 3]. Which statements are correct?

**1.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**2.** The sample variance (÷ n−1) of the listed sample is approximately 3.7.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 3.8, not 3.7.

**3.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**4.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**5.** The sample mean of the listed sample is approximately 3.6.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 3.6.

---

## Question 446 · Hierarchical

Consider 4 objects with the symmetric distance matrix (0-based indices):

```
[0, 2, 4, 8]
[2, 0, 6, 11]
[4, 6, 0, 6]
[8, 11, 6, 0]
```

Which statements are correct?

**1.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

**2.** Using Single-Linkage, the first merge joins objects 0 and 1 at height 2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (0,)+(1,) at 2.

**3.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**4.** Using Single-Linkage, the height of the final (root) merge is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 6.

**5.** Using Complete-Linkage, the height of the final (root) merge is approximately 11.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 11.

---

## Question 447 · Outlier Detection

Consider the 2-D points [[4, 4], [0, 7], [5, 5], [2, 1], [7, 3], [6, 3], [15, 16]]. Which statements are correct?

**1.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

**2.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

**3.** LOF is a global density score that compares each point's density to the dataset-wide average density.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] LOF is a LOCAL/relative score: density vs the point's own neighbours.

**4.** The unweighted KNN outlier scores with k=2 (per point, in order) are [2.24, 5.39, 2.24, 4.47, 2.83, 2.24, 15.26].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] The values are [2.24, 5.39, 2.24, 4.47, 2.83, 2.24, 15.26].

**5.** Point 6 (the far point) receives the largest LOF, consistent with being an outlier.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF values ≈ [0.96, 2.32, 0.96, 1.73, 1.09, 1.05, 6.34]; the isolated point has LOF ≫ 1.

---

## Question 448 · Probability & Density

A test has sensitivity P(+|D)=0.9 and specificity 0.95; disease prevalence is P(D)=0.05. Also consider the sample [4, 4, 4, 1, 3]. Which statements are correct?

**1.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**2.** The sample variance (÷ n−1) of the listed sample is approximately 1.7.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 1.7.

**3.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**4.** The sample mean of the listed sample is approximately 3.2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 3.2.

**5.** The posterior P(D | +) by Bayes' rule is approximately 0.786.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.486, not 0.786.

---

## Question 449 · Hierarchical

Consider 5 objects with the symmetric distance matrix (0-based indices):

```
[0, 12, 9, 5, 11]
[12, 0, 3, 8, 3]
[9, 3, 0, 1, 2]
[5, 8, 1, 0, 8]
[11, 3, 2, 8, 0]
```

Which statements are correct?

**1.** Using Single-Linkage, the height of the final (root) merge is approximately 8.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 5, not 8.

**2.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**3.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

**4.** Using Complete-Linkage, the height of the final (root) merge is approximately 15.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 12, not 15.

**5.** Using Single-Linkage, the first merge joins objects 2 and 3 at height 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (2,)+(3,) at 1.

---

## Question 450 · Data Representation

Consider two records described by 3 numerical variables: u = [-1, 2, 1] and v = [5, 0, -4]. Which statements are correct?

**1.** The Manhattan (city-block) distance d(u,v) is approximately 13.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 13.

**2.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**3.** The Minkowski distance of order p=3 between u and v is approximately 6.94.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 7.04, not 6.94.

**4.** The inner product <u,v> is approximately -10.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ -9, not -10.

**5.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

---

## Question 451 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[2, 0], [3, 3], [0, 1], [0, 3], [9, 11], [10, 8], [9, 9], [9, 11]] with initial prototypes [[2, 0], [10, 8]]. Which statements are correct?

**1.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**2.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] The values are [0, 0, 0, 0, 1, 1, 1, 1].

**3.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.782.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 0.782.

**4.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**5.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

---

## Question 452 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[0, 0], [0, 3], [2, 3], [1, 3], [10, 8], [11, 8], [10, 10], [11, 8]] with initial prototypes [[0, 0], [11, 8]]. Which statements are correct?

**1.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**2.** The final SSE (sum of squared errors) of the partition is approximately 13.5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 13.5.

**3.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**4.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**5.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

---

## Question 453 · Data Representation

Consider two records described by 4 numerical variables: u = [8, 3, -3, -4] and v = [8, 1, -2, -1]. Which statements are correct?

**1.** The cosine similarity cos(u,v) is approximately 0.93.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.93.

**2.** The Minkowski distance of order p=3 between u and v is approximately 3.1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 3.3, not 3.1.

**3.** The Manhattan (city-block) distance d(u,v) is approximately 9.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 6, not 9.

**4.** The Euclidean distance d(u,v) is approximately 3.89.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 3.74, not 3.89.

**5.** The inner product <u,v> is approximately 77.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 77.

---

## Question 454 · Data Representation

Two objects are described by 8 binary (asymmetric/symmetric) variables: x1 = [0, 0, 1, 1, 0, 1, 1, 0] and x2 = [0, 1, 0, 1, 0, 1, 1, 0]. Which statements are correct?

**1.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**2.** The count of 1–1 matches n11 is approximately 3.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 3.

**3.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**4.** The count of disagreements n10 + n01 is approximately 2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 2.

**5.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

---

## Question 455 · Outlier Detection

Consider the 2-D points [[0, 0], [1, 1], [5, 7], [3, 6], [3, 2], [4, 7], [14, 12]]. Which statements are correct?

**1.** The unweighted KNN outlier scores with k=2 (per point, in order) are [3.61, 2.24, 2.24, 2.24, 4.609999999999999, 1.41, 11.18].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [3.61, 2.24, 2.24, 2.24, 3.61, 1.41, 11.18], not [3.61, 2.24, 2.24, 2.24, 4.609999999999999, 1.41, 11.18].

**2.** LOF is a global density score that compares each point's density to the dataset-wide average density.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] LOF is a LOCAL/relative score: density vs the point's own neighbours.

**3.** The weighted KNN outlier score averages a point's distances to all its 1st…k-th nearest neighbours.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] Weighted-kNN aggregates (averages) the 1..k NN distances; plain kNN uses only the k-th.

**4.** The reachability distance reach_dist_k(p,o) is defined as min{k-distance(o), d(p,o)}.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] It is the MAX of k-distance(o) and d(p,o), which smooths density fluctuations.

**5.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

---

## Question 456 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[1, 0], [2, 2], [2, 1], [2, 2], [10, 8], [10, 10], [10, 10], [8, 8]] with initial prototypes [[1, 0], [10, 10]]. Which statements are correct?

**1.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] The values are [0, 0, 0, 0, 1, 1, 1, 1].

**2.** The final SSE (sum of squared errors) of the partition is approximately 10.65.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 10.5, not 10.65.

**3.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**4.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**5.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

---

## Question 457 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0111 and 0.0037, with priors π_C1 = 0.6 and π_C2 = 0.4. Which statements are correct?

**1.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

**2.** The posterior probability (responsibility) of C2 at x is approximately 0.182.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.182.

**3.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

**4.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

**5.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

---

## Question 458 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[1, 2], [2, 2], [3, 0], [0, 1], [10, 10], [8, 11], [10, 8], [10, 11]] with initial prototypes [[1, 2], [8, 11]]. Which statements are correct?

**1.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**2.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**3.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] The values are [0, 0, 0, 0, 1, 1, 1, 1].

**4.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**5.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.963.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.813, not 0.963.

---

## Question 459 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[0, 0], [0, 3], [2, 2], [2, 2], [11, 10], [8, 10], [9, 9], [9, 10]] with initial prototypes [[0, 0], [8, 10]]. Which statements are correct?

**1.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**2.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**3.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 1, 1, 1, 1].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] The values are [0, 0, 0, 0, 1, 1, 1, 1].

**4.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**5.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.63.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.83, not 0.63.

---

## Question 460 · Hierarchical

Consider 4 objects with the symmetric distance matrix (0-based indices):

```
[0, 6, 6, 1]
[6, 0, 5, 1]
[6, 5, 0, 8]
[1, 1, 8, 0]
```

Which statements are correct?

**1.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**2.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**3.** Using Single-Linkage, the first merge joins objects 0 and 3 at height 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (0,)+(3,) at 1.

**4.** Using Single-Linkage, the height of the final (root) merge is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 5, not 6.

**5.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

---

## Question 461 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-19, 8, 22, 31, 35, 48, 92}. Which statements are correct?

**1.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**2.** The MLE estimate of the variance σ² (dividing by n) is approximately 1019.58.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 1019.43, not 1019.58.

**3.** With ε = 15 and MinPts = 1, DBSCAN groups the data into the clusters [[-19], [8, 22, 31, 35, 48], [92]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=15, MinPts=1) gives clusters [[-19], [8, 22, 31, 35, 48], [92]]; no noise.

**4.** The MLE estimate of the mean μ is approximately 31.0.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 31.0.

**5.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [27, 14, 9, 4, 4, 13, 44].  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] The values are [27, 14, 9, 4, 4, 13, 44].

---

## Question 462 · Data Representation

Consider two records described by 3 numerical variables: u = [9, 5, 1] and v = [-4, 1, -5]. Which statements are correct?

**1.** The cosine similarity cos(u,v) is approximately -1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ -0.537, not -1.

**2.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

**3.** The Suprema (Chebyshev) distance d(u,v) is approximately 10.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 13, not 10.

**4.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

**5.** The inner product <u,v> is approximately -36.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ -36.

---

## Question 463 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-17, -10, -4, -1, 54, 99, 107}. Which statements are correct?

**1.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [3, 6, 3, 7, 45, 8, 8].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [7, 6, 3, 3, 45, 8, 8], not [3, 6, 3, 7, 45, 8, 8].

**2.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**3.** The MLE estimate of the variance σ² (dividing by n) is approximately 2449.29.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 2449.39, not 2449.29.

**4.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

**5.** With ε = 15 and MinPts = 2, DBSCAN groups the data into the clusters [[-17, -10, -4, -1], [99, 107]] with [54] as noise.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=15, MinPts=2) gives clusters [[-17, -10, -4, -1], [99, 107]]; noise = [54].

---

## Question 464 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[0, 2], [3, 0], [3, 3], [3, 1], [10, 9], [11, 9], [8, 9], [8, 11]] with initial prototypes [[0, 2], [11, 9]]. Which statements are correct?

**1.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**2.** One iteration of k-means costs O(N·n·k), linear in the number of points.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Each iteration compares N points to k centroids over n dimensions.

**3.** The final SSE (sum of squared errors) of the partition is approximately 21.5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 21.5.

**4.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct value is ≈ 0.765, not 1.

**5.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

---

## Question 465 · Data Representation

Consider two records described by 5 numerical variables: u = [1, 6, 2, 0, -2] and v = [2, 6, 4, -5, 1]. Which statements are correct?

**1.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**2.** The Minkowski distance of order p=3 between u and v is approximately 5.24.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 5.44, not 5.24.

**3.** The Euclidean distance d(u,v) is approximately 6.24.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 6.24.

**4.** The inner product <u,v> is approximately 47.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 44, not 47.

**5.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

---

## Question 466 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 4). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BUTTER, CRACKERS, DIAPERS, EGGS, JAM |
| 2 | BUTTER, DIAPERS, JAM |
| 3 | CRACKERS, DIAPERS, EGGS, JAM |
| 4 | BUTTER, JAM |
| 5 | BUTTER, CRACKERS, DIAPERS, JAM |
| 6 | BUTTER, CRACKERS, DIAPERS, EGGS |
| 7 | BUTTER, CRACKERS, DIAPERS, JAM |
| 8 | CRACKERS, DIAPERS, EGGS, JAM |
| 9 | DIAPERS, EGGS, JAM |
| 10 | BUTTER, CRACKERS, DIAPERS, EGGS, JAM |
| 11 | BUTTER, EGGS |
| 12 | BUTTER, CRACKERS, DIAPERS, EGGS, JAM |

**1.** The support count of the itemset {JAM, EGGS} is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 6.

**2.** The confidence of the rule {JAM} ⇒ {EGGS} is approximately 0.1.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 0.6, not 0.1.

**3.** The frequent itemset {CRACKERS} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

**4.** The lift of the rule {JAM} ⇒ {EGGS} is approximately 0.9.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 0.9.

**5.** By anti-monotonicity (downward closure), every subset of a frequent itemset is also frequent.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Apriori prunes any candidate having an infrequent subset before counting support.

---

## Question 467 · Probability & Density

A test has sensitivity P(+|D)=0.95 and specificity 0.9; disease prevalence is P(D)=0.1. Also consider the sample [1, 1, 6, 2, 1]. Which statements are correct?

**1.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**2.** The sample mean of the listed sample is approximately 2.2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 2.2.

**3.** The posterior P(D | +) by Bayes' rule is approximately 0.514.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 0.514.

**4.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**5.** The sample variance (÷ n−1) of the listed sample is approximately 4.4.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 4.7, not 4.4.

---

## Question 468 · Data Representation

Consider two records described by 4 numerical variables: u = [-5, -4, -2, 2] and v = [-2, -1, 0, 7]. Which statements are correct?

**1.** The inner product <u,v> is approximately 31.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 28, not 31.

**2.** The Euclidean distance satisfies the triangle inequality, so it is a metric.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Euclidean is a metric: non-negativity, identity, symmetry and the triangle inequality hold.

**3.** The Minkowski distance of order p=3 between u and v is approximately 5.62.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 5.72, not 5.62.

**4.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**5.** The cosine similarity cos(u,v) is approximately 0.844.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.544, not 0.844.

---

## Question 469 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0052 and 0.0157, with priors π_C1 = 0.6 and π_C2 = 0.4. Which statements are correct?

**1.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**2.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

**3.** The posterior probability (responsibility) of C1 at x is approximately 0.482.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The correct value is ≈ 0.332, not 0.482.

**4.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

**5.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

---

## Question 470 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[2, 3], [3, 2], [0, 0], [0, 0], [9, 9], [8, 11], [11, 10], [10, 10]] with initial prototypes [[2, 3], [8, 11]]. Which statements are correct?

**1.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.802.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 0.802.

**2.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**3.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**4.** The final SSE (sum of squared errors) of the partition is approximately 20.5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 20.5.

**5.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

---

## Question 471 · Probability & Density

A test has sensitivity P(+|D)=0.99 and specificity 0.9; disease prevalence is P(D)=0.02. Also consider the sample [3, 3, 4, 5, 1]. Which statements are correct?

**1.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**2.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**3.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**4.** The sample mean of the listed sample is approximately 3.2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 3.2.

**5.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

---

## Question 472 · Data Representation

Two objects are described by 12 binary (asymmetric/symmetric) variables: x1 = [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0] and x2 = [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0]. Which statements are correct?

**1.** The Jaccard coefficient Jc(x1,x2) is approximately 0.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.25, not 0.

**2.** The count of disagreements n10 + n01 is approximately 4.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 6, not 4.

**3.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**4.** The count of 1–1 matches n11 is approximately 0.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 2, not 0.

**5.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.5.

---

## Question 473 · Data Representation

Consider two records described by 3 numerical variables: u = [5, 2, 1] and v = [9, 3, 1]. Which statements are correct?

**1.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**2.** The inner product <u,v> is approximately 52.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 52.

**3.** The Euclidean distance d(u,v) is approximately 4.27.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 4.12, not 4.27.

**4.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

**5.** The cosine similarity cos(u,v) is approximately 0.995.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.995.

---

## Question 474 · Data Representation

Consider two records described by 4 numerical variables: u = [1, 7, 8, -3] and v = [0, -2, -2, 7]. Which statements are correct?

**1.** The cosine similarity cos(u,v) is approximately -0.609.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ -0.609.

**2.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

**3.** The Suprema (Chebyshev) distance d(u,v) is approximately 7.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 10, not 7.

**4.** As p → ∞ the Minkowski distance tends to the Manhattan distance.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] As p→∞ it tends to the Suprema/Chebyshev distance; p=1 gives Manhattan.

**5.** The Manhattan (city-block) distance d(u,v) is approximately 32.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 30, not 32.

---

## Question 475 · Data Representation

Two objects are described by 12 binary (asymmetric/symmetric) variables: x1 = [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0] and x2 = [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0]. Which statements are correct?

**1.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**2.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.3.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.5, not 0.3.

**3.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**4.** The count of 1–1 matches n11 is approximately 3.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 2, not 3.

**5.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

---

## Question 476 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 5). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BUTTER, CRACKERS, DIAPERS |
| 2 | BREAD, MILK |
| 3 | BREAD, BUTTER, DIAPERS, EGGS, MILK |
| 4 | BUTTER, DIAPERS |
| 5 | BREAD, DIAPERS, MILK |
| 6 | BREAD, CRACKERS, MILK |
| 7 | BREAD, BUTTER, CRACKERS, DIAPERS, EGGS, MILK |
| 8 | CRACKERS, MILK |
| 9 | CRACKERS, DIAPERS, MILK |
| 10 | BREAD, CRACKERS, DIAPERS, MILK |
| 11 | BREAD, BUTTER, DIAPERS, EGGS, MILK |
| 12 | BREAD, BUTTER, CRACKERS, DIAPERS, EGGS, MILK |
| 13 | BUTTER, CRACKERS, DIAPERS, MILK |
| 14 | BREAD, BUTTER, CRACKERS, DIAPERS, EGGS, MILK |

**1.** Confidence of X ⇒ Y is defined as support(X ∪ Y) / support(Y).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Confidence = support(X∪Y)/support(X) (divide by the antecedent's support).

**2.** The frequent itemset {DIAPERS} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

**3.** With n distinct items the candidate search space contains 2^n possible itemsets.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Each item is in or out, giving 2^n itemsets — hence Apriori pruning is essential.

**4.** The confidence of the rule {BUTTER} ⇒ {BREAD} is approximately 0.325.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 0.625, not 0.325.

**5.** The lift of the rule {BUTTER} ⇒ {BREAD} is approximately 0.972.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 0.972.

---

## Question 477 · Data Representation

Two objects are described by 8 binary (asymmetric/symmetric) variables: x1 = [1, 1, 0, 1, 1, 0, 1, 0] and x2 = [1, 1, 0, 1, 0, 0, 1, 1]. Which statements are correct?

**1.** The count of disagreements n10 + n01 is approximately 2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 2.

**2.** The Jaccard coefficient Jc(x1,x2) is approximately 0.667.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.667.

**3.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**4.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**5.** The count of 1–1 matches n11 is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 4, not 5.

---

## Question 478 · Probability & Density

A test has sensitivity P(+|D)=0.99 and specificity 0.95; disease prevalence is P(D)=0.1. Also consider the sample [2, 4, 1, 6, 3]. Which statements are correct?

**1.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

**2.** The posterior P(D | +) by Bayes' rule is approximately 0.987.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 0.687, not 0.987.

**3.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**4.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**5.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

---

## Question 479 · Partitioning (k-Means)

Run k-means (squared Euclidean) on the 2-D points [[3, 0], [1, 3], [0, 3], [1, 3], [8, 10], [11, 8], [11, 9], [8, 8]] with initial prototypes [[3, 0], [11, 8]]. Which statements are correct?

**1.** Because it uses the mean as prototype, k-means is sensitive to outliers and tends to find globular clusters only.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Mean-based, real-valued, volumetric/globular clusters; outlier-sensitive.

**2.** The Silhouette Width Criterion ranges in [0, ∞).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] SWC ∈ [−1, +1]; higher is better, used to choose k.

**3.** The Silhouette Width Criterion (SWC) of the resulting partition is approximately 0.77.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] Computed value ≈ 0.77.

**4.** k-means is guaranteed to converge to the globally optimal partition regardless of the initial prototypes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] k-means only reaches a local optimum; the result depends on initialisation.

**5.** The final cluster labels (one per point, in order) are [0, 0, 0, 0, 1, 1, 2, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] The correct values are [0, 0, 0, 0, 1, 1, 1, 1], not [0, 0, 0, 0, 1, 1, 2, 1].

---

## Question 480 · Data Representation

Two objects are described by 12 binary (asymmetric/symmetric) variables: x1 = [0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0] and x2 = [1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1]. Which statements are correct?

**1.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

**2.** The count of 1–1 matches n11 is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 2, not 5.

**3.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**4.** The count of disagreements n10 + n01 is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 6.

**5.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

---

## Question 481 · Data Representation

Consider two records described by 4 numerical variables: u = [5, -4, -1, 1] and v = [1, -3, 5, 0]. Which statements are correct?

**1.** The Suprema (Chebyshev) distance d(u,v) is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 6.

**2.** The Manhattan (city-block) distance d(u,v) is approximately 13.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 12, not 13.

**3.** The Euclidean distance d(u,v) is approximately 7.65.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 7.35, not 7.65.

**4.** The Manhattan distance equals the Minkowski distance with p = 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Minkowski with p=1 is exactly the Manhattan distance.

**5.** Re-scaling variables to comparable ranges removes the implicit pre-weighting by which wide-range variables dominate the distance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Variables with wider ranges dominate distances; z-score/[0,1] rescaling removes this artefact.

---

## Question 482 · Data Representation

Consider two records described by 4 numerical variables: u = [2, 2, 5, -3] and v = [-3, -5, -3, -1]. Which statements are correct?

**1.** The inner product <u,v> is approximately -31.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ -28, not -31.

**2.** The Manhattan (city-block) distance d(u,v) is approximately 21.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 22, not 21.

**3.** The Suprema (Chebyshev) distance d(u,v) is approximately 8.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 8.

**4.** The Minkowski distance of order p=3 between u and v is approximately 9.86.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 9.96, not 9.86.

**5.** The cosine similarity cos(u,v) is approximately -0.851.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ -0.651, not -0.851.

---

## Question 483 · Probability & Density

A test has sensitivity P(+|D)=0.9 and specificity 0.95; disease prevalence is P(D)=0.05. Also consider the sample [5, 4, 1, 3, 2]. Which statements are correct?

**1.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**2.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**3.** The sample mean of the listed sample is approximately 3.15.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 3.0, not 3.15.

**4.** The sample variance (÷ n−1) of the listed sample is approximately 2.7.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 2.5, not 2.7.

**5.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

---

## Question 484 · Probability & Density

A test has sensitivity P(+|D)=0.9 and specificity 0.99; disease prevalence is P(D)=0.01. Also consider the sample [5, 4, 2, 3, 3]. Which statements are correct?

**1.** The sample mean of the listed sample is approximately 3.7.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 3.4, not 3.7.

**2.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**3.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**4.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

**5.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

---

## Question 485 · Probability & Density

A test has sensitivity P(+|D)=0.99 and specificity 0.99; disease prevalence is P(D)=0.02. Also consider the sample [2, 5, 6, 4, 6]. Which statements are correct?

**1.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**2.** The sample variance (÷ n−1) of the listed sample is approximately 2.9.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 2.8, not 2.9.

**3.** The sample mean of the listed sample is approximately 4.6.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 4.6.

**4.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**5.** A probability density function p(x) must satisfy ∫p(x)dx = 1, but p(x) itself may exceed 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] p(x) is a density (likelihood), not a probability; only the integral is bounded to 1.

---

## Question 486 · Data Representation

Two objects are described by 10 binary (asymmetric/symmetric) variables: x1 = [0, 0, 1, 1, 0, 0, 1, 0, 1, 0] and x2 = [0, 1, 0, 0, 1, 0, 0, 1, 1, 0]. Which statements are correct?

**1.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

**2.** SMC and Jaccard always give the same value for any pair of binary vectors.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] They coincide only when n00 = 0; in general SMC counts 0–0 matches and Jaccard does not.

**3.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.4.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.4.

**4.** The Jaccard coefficient Jc(x1,x2) is approximately 0.293.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.143, not 0.293.

**5.** If these variables are asymmetric (only 1's are informative), the Jaccard coefficient is the appropriate choice.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Jaccard drops the 0–0 matches, which is right for asymmetric variables.

---

## Question 487 · Hierarchical

Consider 4 objects with the symmetric distance matrix (0-based indices):

```
[0, 8, 10, 12]
[8, 0, 1, 9]
[10, 1, 0, 7]
[12, 9, 7, 0]
```

Which statements are correct?

**1.** Using Single-Linkage, the first merge joins objects 1 and 2 at height 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (1,)+(2,) at 1.

**2.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**3.** Using Complete-Linkage, the height of the final (root) merge is approximately 12.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 12.

**4.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**5.** Using Single-Linkage, the height of the final (root) merge is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 8, not 6.

---

## Question 488 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-29, -19, -13, -12, 7, 15, 38, 97}. Which statements are correct?

**1.** With ε = 25 and MinPts = 2, DBSCAN groups the data into the clusters [[-29, -19, -13, -12, 7, 15, 38]] with [97] as noise.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=25, MinPts=2) gives clusters [[-29, -19, -13, -12, 7, 15, 38]]; noise = [97].

**2.** The MLE estimate of the mean μ is approximately 10.3.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 10.5, not 10.3.

**3.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**4.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**5.** For variable k, the k-means SSE tends to decrease monotonically as k grows, so SSE alone cannot pick the best k across different k.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Clustering: Intro & Partitioning / k-Means] SSE → 0 as k → N; hence the elbow/silhouette heuristics are used instead.

---

## Question 489 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-28, 66, 70, 75, 96, 97}. Which statements are correct?

**1.** The MLE estimate of the mean μ is approximately 62.37.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 62.67, not 62.37.

**2.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

**3.** Fitting a single univariate Normal by Maximum Likelihood gives μ = sample mean and σ² = (1/n)·Σ(x−μ)², i.e. the sample mean and the (MLE) variance.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] MLE of a Normal: μ̂ = sample mean ≈ 62.67, σ̂² = (1/n)Σ(x−μ̂)² ≈ 1787.89.

**4.** With ε = 25 and MinPts = 2, DBSCAN groups the data into the clusters [[66, 70, 75, 96, 97]] with [-28] as noise.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=25, MinPts=2) gives clusters [[66, 70, 75, 96, 97]]; noise = [-28].

**5.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

---

## Question 490 · Hierarchical

Consider 4 objects with the symmetric distance matrix (0-based indices):

```
[0, 9, 12, 2]
[9, 0, 6, 7]
[12, 6, 0, 12]
[2, 7, 12, 0]
```

Which statements are correct?

**1.** Single-Linkage can detect elongated, arbitrarily shaped clusters but is sensitive to noise (chaining effect).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] MIN linkage chains points; good for arbitrary shapes, fragile to noise.

**2.** Using Single-Linkage, the first merge joins objects 0 and 3 at height 2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Smallest distance pair merges first: (0,)+(3,) at 2.

**3.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

**4.** Using Complete-Linkage, the height of the final (root) merge is approximately 12.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 12.

**5.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

---

## Question 491 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 5). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BREAD, BUTTER, DIAPERS, EGGS, JAM |
| 2 | BUTTER, DIAPERS, JAM |
| 3 | BREAD, BUTTER, DIAPERS, EGGS, JAM |
| 4 | BREAD, BUTTER, DIAPERS, EGGS |
| 5 | BUTTER, EGGS, JAM |
| 6 | BREAD, BUTTER, DIAPERS, EGGS, JAM |
| 7 | BREAD, BUTTER, EGGS, JAM |
| 8 | BREAD, BUTTER, EGGS, JAM |
| 9 | EGGS, JAM |
| 10 | BREAD, BUTTER, DIAPERS, EGGS, JAM |
| 11 | BREAD, EGGS, JAM |
| 12 | BREAD, DIAPERS, EGGS |
| 13 | BREAD, BUTTER, DIAPERS, EGGS |
| 14 | BREAD, BUTTER, DIAPERS, EGGS |

**1.** Confidence of X ⇒ Y is defined as support(X ∪ Y) / support(Y).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Confidence = support(X∪Y)/support(X) (divide by the antecedent's support).

**2.** With n distinct items the candidate search space contains 2^n possible itemsets.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Each item is in or out, giving 2^n itemsets — hence Apriori pruning is essential.

**3.** The support count of the itemset {EGGS, DIAPERS} is approximately 7.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 8, not 7.

**4.** The confidence of the rule {EGGS} ⇒ {DIAPERS} is approximately 0.615.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 0.615.

**5.** The lift of the rule {EGGS} ⇒ {DIAPERS} is approximately 1.057.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 0.957, not 1.057.

---

## Question 492 · Hierarchical

Consider 4 objects with the symmetric distance matrix (0-based indices):

```
[0, 5, 11, 4]
[5, 0, 3, 6]
[11, 3, 0, 1]
[4, 6, 1, 0]
```

Which statements are correct?

**1.** Hierarchical clustering can operate from a (dis)similarity matrix alone, without the original feature vectors (relational).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] AHC needs only pairwise distances, so it is a relational method.

**2.** Using Complete-Linkage, the height of the final (root) merge is approximately 11.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] Computed value ≈ 11.

**3.** Using Single-Linkage, the height of the final (root) merge is approximately 7.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] The correct value is ≈ 4, not 7.

**4.** Agglomerative hierarchical clustering typically needs O(N²) memory for the proximity matrix and about O(N³) time.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Hierarchical Clustering] It stores the N×N proximity matrix and does N merges each updating/searching it.

**5.** Agglomerative hierarchical clustering is greedy: an early merge can be undone later if it proves suboptimal.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Merges are irreversible; the greedy choice cannot be undone, so optimality is not guaranteed.

---

## Question 493 · Data Representation

Consider two records described by 5 numerical variables: u = [1, -2, 9, 7, -2] and v = [1, 3, 4, -2, 2]. Which statements are correct?

**1.** The Minkowski distance of order p=3 between u and v is approximately 10.24.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 10.14, not 10.24.

**2.** The cosine similarity cos(u,v) is approximately 0.289.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.189, not 0.289.

**3.** The Suprema (Chebyshev) distance d(u,v) is approximately 11.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 9, not 11.

**4.** The inner product <u,v> is approximately 13.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 13.

**5.** The Euclidean distance d(u,v) is approximately 11.82.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 12.12, not 11.82.

---

## Question 494 · Data Representation

Two objects are described by 10 binary (asymmetric/symmetric) variables: x1 = [0, 0, 0, 1, 1, 0, 1, 0, 0, 1] and x2 = [1, 1, 0, 0, 1, 1, 0, 1, 1, 0]. Which statements are correct?

**1.** The Jaccard coefficient Jc(x1,x2) is approximately 0.011.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 0.111, not 0.011.

**2.** The count of 1–1 matches n11 is approximately 1.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 1.

**3.** The Simple Matching Coefficient SMC(x1,x2) is approximately 0.2.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Data Representation] Computed value ≈ 0.2.

**4.** The count of disagreements n10 + n01 is approximately 6.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] The correct value is ≈ 8, not 6.

**5.** The Jaccard coefficient counts 0–0 matches in its numerator.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Data Representation] Jaccard removes n00 entirely; only SMC counts 0–0 agreements.

---

## Question 495 · 1-D Dataset (mixed)

Consider the one-dimensional dataset {-1, 0, 35, 45, 68, 72}. Which statements are correct?

**1.** Single-Linkage and Complete-Linkage must give the same hierarchy because the data is one-dimensional.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Hierarchical Clustering] Dimensionality is irrelevant; the two use min vs max inter-cluster distance and generally differ.

**2.** The MLE estimate of the mean μ is approximately 36.5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Computed value ≈ 36.5.

**3.** With ε = 10 and MinPts = 2, DBSCAN groups the data into the clusters [[-1, 0], [35, 45], [68, 72]] (no noise).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Density-Based Clustering] DBSCAN(ε=10, MinPts=2) gives clusters [[-1, 0], [35, 45], [68, 72]]; no noise.

**4.** The unweighted KNN outlier scores with k=1 (in dataset order, any Minkowski distance) are [4, 1, 10, 10, 4, 1].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [1, 1, 10, 10, 4, 4], not [4, 1, 10, 10, 4, 1].

**5.** The parallel/distributed version of k-means cannot run here because the number of points cannot be split evenly across nodes.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Clustering: Intro & Partitioning / k-Means] There is no such even-split requirement; this is not a constraint of k-means.

---

## Question 496 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0146 and 0.0069, with priors π_C1 = 0.2 and π_C2 = 0.8. Which statements are correct?

**1.** Computing these posteriors uses Bayes' rule (posterior ∝ prior × density).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] The E-step responsibility γ = πᵢ·N / Σ πₗ·N is exactly Bayes' theorem.

**2.** The posterior probability (responsibility) of C2 at x is approximately 0.654.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.654.

**3.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**4.** The posterior probability (responsibility) of C1 at x is approximately 0.346.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.346.

**5.** If both covariance matrices are diagonal, the clusters are necessarily spherical, never elliptical.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] Diagonal ⇒ axis-aligned ellipsoids; spherical only if all diagonal variances are equal.

---

## Question 497 · Probability & Density

A test has sensitivity P(+|D)=0.99 and specificity 0.9; disease prevalence is P(D)=0.05. Also consider the sample [1, 5, 2, 4, 3]. Which statements are correct?

**1.** The sample mean of the listed sample is approximately 2.85.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] The correct value is ≈ 3.0, not 2.85.

**2.** Kernel Density Estimation is a parametric density-estimation method.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] KDE (and kNN density) are NON-parametric; MLE / method of moments are parametric.

**3.** Zero covariance between two variables implies they are statistically independent.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Probability & Density Estimation] Zero covariance is necessary but NOT sufficient; a nonlinear dependence can remain.

**4.** Bayes' rule gives posterior = (likelihood × prior) / evidence.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] P(Y|X)=P(X|Y)P(Y)/P(X).

**5.** Two variables X, Y are independent iff p(X,Y) = p(X)·p(Y) for all values.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Probability & Density Estimation] Independence factorises the joint into the product of marginals.

---

## Question 498 · EM / GMM

In an EM-GMM with k=2 components C1, C2, the component densities at a point x are 0.0144 and 0.0159, with priors π_C1 = 0.3 and π_C2 = 0.7. Which statements are correct?

**1.** k-means can be viewed as a limiting/special case of EM-GMM.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] With hard assignments and equal spherical covariances, EM-GMM reduces to k-means.

**2.** EM fits the GMM by maximising the (log-)likelihood of the data.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] EM is a Maximum-Likelihood procedure; the log turns the product over points into a sum.

**3.** Unlike k-means, EM-GMM is insensitive to the initialisation of its parameters.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] EM converges only to a local optimum and is initialisation-sensitive (often seeded by k-means).

**4.** The posterior probability (responsibility) of C1 at x is approximately 0.28.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Overlapping Probabilistic Clustering / EM-GMM] Computed value ≈ 0.28.

**5.** EM-GMM assumes the variables are independent within a cluster, so within-cluster covariances are necessarily zero.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Overlapping Probabilistic Clustering / EM-GMM] The general GMM uses full covariance matrices; off-diagonals model correlation.

---

## Question 499 · Outlier Detection

Consider the 2-D points [[6, 5], [3, 7], [5, 4], [0, 3], [7, 0], [7, 6], [16, 16]]. Which statements are correct?

**1.** A LOF value close to 1 indicates a point lying in a region of homogeneous density (an inlier).  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF ≈ 1 ⇒ inlier; LOF ≫ 1 ⇒ outlier.

**2.** The weighted KNN outlier score averages a point's distances to all its 1st…k-th nearest neighbours.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] Weighted-kNN aggregates (averages) the 1..k NN distances; plain kNN uses only the k-th.

**3.** LOF is a global density score that compares each point's density to the dataset-wide average density.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] LOF is a LOCAL/relative score: density vs the point's own neighbours.

**4.** Point 6 (the far point) receives the largest LOF, consistent with being an outlier.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Unsupervised Outlier Detection] LOF values ≈ [1.33, 1.49, 0.88, 1.89, 1.97, 0.88, 5.84]; the isolated point has LOF ≫ 1.

**5.** The unweighted KNN outlier scores with k=2 (per point, in order) are [1.41, 3.61, 2.83, 5.1, 6.1, 2.83, 14.87].  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Unsupervised Outlier Detection] The correct values are [1.41, 3.61, 2.83, 5.1, 5.1, 2.83, 14.87], not [1.41, 3.61, 2.83, 5.1, 6.1, 2.83, 14.87].

---

## Question 500 · Frequent Itemsets

Consider this transaction database (Apriori, minimum support COUNT = 5). Which statements are correct?

| TID | Items |
| --- | --- |
| 1 | BEER, BREAD, CRACKERS, MILK |
| 2 | BEER, BREAD, CRACKERS, JAM, MILK |
| 3 | BEER, JAM |
| 4 | BEER, CRACKERS |
| 5 | JAM, MILK |
| 6 | BEER, BREAD, CRACKERS, JAM |
| 7 | BREAD, CRACKERS, JAM |
| 8 | BEER, BREAD, CRACKERS, JAM, MILK |
| 9 | BREAD, CRACKERS, JAM, MILK |
| 10 | BEER, BREAD, CRACKERS, MILK |

**1.** With n distinct items the candidate search space contains 2^n possible itemsets.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Each item is in or out, giving 2^n itemsets — hence Apriori pruning is essential.

**2.** The confidence of the rule {BEER} ⇒ {BREAD} is approximately 0.414.  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] The correct value is ≈ 0.714, not 0.414.

**3.** The frequent itemset {BREAD} is maximal (it has no frequent superset).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Maximal = no superset reaches support 5.

**4.** The frequent itemset {BREAD} is closed (no superset has the same support).  
&nbsp;&nbsp;&nbsp;**Answer: False.** [Frequent Itemsets & Association Rules] Closed = no superset shares its support; checked against all supersets.

**5.** The support count of the itemset {BEER, BREAD} is approximately 5.  
&nbsp;&nbsp;&nbsp;**Answer: True.** [Frequent Itemsets & Association Rules] Computed value ≈ 5.

---
