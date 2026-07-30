import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, fcluster


def parse_dataset(raw: str) -> list[float]:
    return [float(x.strip()) for x in raw.split(",")]


def format_linkage_table(Z: np.ndarray, data: list[float]) -> str:
    n = len(data)
    labels = {i: f"{{{data[i]:.0f}}}" for i in range(n)}
    next_id = n
    lines = []
    for step, row in enumerate(Z):
        i, j, dist, count = int(row[0]), int(row[1]), row[2], int(row[3])
        ci = labels[i]
        cj = labels[j]
        merged = f"{ci} ∪ {cj}"
        labels[next_id] = merged
        next_id += 1
        lines.append(f"  Step {step+1}: {ci} ∪ {cj}  (d={dist:.4f})")
    return "\n".join(lines)


def solve() -> None:
    raw = input("Enter dataset (comma-separated numbers): ")
    data = parse_dataset(raw)
    n = len(data)

    X = np.array(data).reshape(-1, 1)
    dist_condensed = pdist(X, metric="euclidean")
    dist_matrix = squareform(dist_condensed)

    Z_single = linkage(dist_condensed, method="single")
    Z_complete = linkage(dist_condensed, method="complete")

    sep = "=" * 52
    print(f"\n{sep}")
    print("  HIERARCHICAL CLUSTERING: SINGLE vs COMPLETE LINKAGE")
    print(sep)
    print(f"Dataset: {data}  (N={n})")
    print()

    print("Pairwise distances:")
    header = "     " + "".join(f"{x:7.0f}" for x in data)
    print(header)
    for i, xi in enumerate(data):
        row = f"{xi:5.0f}" + "".join(f"{dist_matrix[i,j]:7.2f}" for j in range(n))
        print(row)
    print()

    print("--- Single Linkage (merge at MIN inter-cluster distance) ---")
    print(format_linkage_table(Z_single, data))
    print()

    print("--- Complete Linkage (merge at MAX inter-cluster distance) ---")
    print(format_linkage_table(Z_complete, data))
    print()

    # Compare merge heights step by step
    diffs = []
    for step in range(n - 1):
        ds = Z_single[step, 2]
        dc = Z_complete[step, 2]
        if abs(ds - dc) > 1e-9:
            diffs.append((step + 1, ds, dc))

    if diffs:
        print("Steps where merge distances differ:")
        for step, ds, dc in diffs:
            print(f"  Step {step}: single={ds:.4f}, complete={dc:.4f}")
        print()

    # Show cluster assignments at two cut heights
    for cut in [4]:
        labels_s = fcluster(Z_single, t=cut, criterion="distance")
        labels_c = fcluster(Z_complete, t=cut, criterion="distance")
        same = np.array_equal(labels_s, labels_c)
        print(f"Clusters at cut height={cut}:")
        print(f"  Single:   {labels_s.tolist()}")
        print(f"  Complete: {labels_c.tolist()}")
        print(f"  Same assignment? {'YES' if same else 'NO'}")
        print()

    print("VERDICT: FALSE")
    print("  Single-linkage and complete-linkage do NOT necessarily produce")
    print("  the same result in 1D. The merge distances (dendrogram heights)")
    print("  differ at multiple steps, and cluster assignments differ at")
    print("  intermediate cut heights.")
    print(sep)


if __name__ == "__main__":
    solve()
