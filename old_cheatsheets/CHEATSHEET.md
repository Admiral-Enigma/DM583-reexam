# DM583 exam toolkit — usage cheat-sheet

Files: `dist.py` (core), `cluster.py`, `outliers.py`, `gmm.py`, `freq.py`, `prob.py`
plus originals `misc.py` (`innerprod`, `posteriors`, `MLE_uni`) and `apriori.py`.
Pure stdlib only. 1-D points must be wrapped as 1-element lists, e.g. `[[-20],[-10],...]`.

## Data representation (dist.py)

    eucd(u,v) mand(u,v) mink(u,v,p) supd(u,v)        # distances
    cosine(u,v) pearson(u,v) spearman(u,v) innerprod(u,v)
    smc(u,v) jaccard(u,v) contingency(u,v)           # binary -> (n11,n10,n01,n00)
    mahalanobis(x, mean, covmat(data))               # square it for R's value
    zscore(col) rescale(col)                         # standardise a COLUMN
    ordinal(["Cool","Mild","Hot"], order=[...])      # -> [0,.5,1]
    onehot(cats, levels)  dis2sim(d[,dmax])  sim2dis(s)
    proxmat(data, eucd)                              # full distance matrix

## Partitioning / k-Means (cluster.py)

    labels, cents = kmeans(data, init=[[6,6],[4,6],[5,10]])
    sse(data, labels, cents)
    silhouette(data, labels)        # SWC in [-1,1]; try several k, pick max

## Hierarchical (cluster.py) -- D is a distance matrix

    ahc(D, "single")   # or "complete" / "average" / "ward"
    # -> [(clusterA, clusterB, height), ...]  (clusters = tuples of indices)
    cut(merges, n, k)               # slice hierarchy into k clusters

## Frequent itemsets / rules (apriori.py + freq.py)

    apriori(DB, 3, thresh=5)                          # prints frequent itemsets
    support(DB, {"DIAPERS"})                          # = 9
    confidence(DB, {"DIAPERS"}, {"BREAD","MILK"})     # = 5/9
    lift(...) conviction(...) rule_jaccard(...)
    is_closed(DB, {"BREAD","DIAPERS"})  is_maximal(DB, X, thresh=5)
    rules(DB, {"BREAD","DIAPERS","MILK"}, min_conf=.7)

## Density-based (cluster.py)

    labels, types = dbscan(data, eps=15, minpts=2)    # label 0 = noise
    # types[i] in {core, border, noise}; core counts the point itself

## Outlier detection (outliers.py)

    knn_outlier(data, k)            # score = distance to k-th NN
    wknn_outlier(data, k)           # avg distance to 1..k NN
    db_outlier(data, eps, pi)       # DB(eps,pi): True/False per point
    lof(data, k)                    # LOF ~1 inlier, >>1 outlier
    kdist / knn / reachdist / lrd   # LOF building blocks

## EM-GMM (gmm.py + misc.posteriors)

    gauss(x, mu, var)                       # 1-D normal pdf
    mvgauss(x, mean, cov)                   # multivariate normal pdf
    posteriors([d1,d2], [pi1,pi2])          # responsibilities from given densities
    responsibilities([d1,d2], [pi1,pi2])    # same, GMM-named
    estep(data, means, covs, priors)        # full responsibility matrix
    mstep(data, gamma)                      # -> (means, covs, priors)

## Probability & density (prob.py + misc.MLE_uni)

    bayes(likelihood, prior, evidence)
    mean(v)  var(v[,sample])  std(v)  cov(u,v)        # sample=False -> /n (MLE)
    expect(vals, probs)  marginal(joint, axis)  entropy(probs)
    MLE_uni(v)                              # (sample mean, MLE var)  [your misc.py]
    kde(x, data, h)                         # Gaussian kernel density at x
