import csv
import sys
from itertools import combinations

sys.stdout.reconfigure(encoding="utf-8")


def load_transactions(path: str) -> list[frozenset]:
    transactions = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            if len(row) < 2:
                continue
            items = frozenset(item.strip().upper() for item in row[1].split(",") if item.strip())
            if items:
                transactions.append(items)
    return transactions


def count_support(transactions: list, candidates: list[tuple]) -> dict[tuple, int]:
    counts = {c: 0 for c in candidates}
    for t in transactions:
        for c in candidates:
            if frozenset(c) <= t:
                counts[c] += 1
    return counts


def generate_join(frequent: list[tuple]) -> list[tuple]:
    """Apriori join: p and q join if they share first k-2 items and p[-1] < q[-1]."""
    candidates = []
    n = len(frequent)
    for i in range(n):
        for j in range(i + 1, n):
            p, q = frequent[i], frequent[j]
            if p[:-1] == q[:-1] and p[-1] < q[-1]:
                candidates.append(p + (q[-1],))
    return candidates


def prune_step(candidates: list[tuple], frequent_prev: set[tuple]) -> tuple[list, list]:
    """Remove candidates with an infrequent (k-1)-subset. Returns (kept, pruned_with_reason)."""
    kept, pruned = [], []
    for c in candidates:
        missing = next(
            (sub for sub in combinations(c, len(c) - 1) if sub not in frequent_prev),
            None,
        )
        (kept if missing is None else pruned).append((c, missing) if missing else c)
    return kept, pruned


def fmt(t: tuple) -> str:
    return "{" + ", ".join(t) + "}"


def apriori(transactions: list, min_sup: int) -> dict:
    # ── Level 1 ──────────────────────────────────────────────────
    item_counts: dict[str, int] = {}
    for t in transactions:
        for item in t:
            item_counts[item] = item_counts.get(item, 0) + 1

    frequent_1: dict[tuple, int] = {}
    parts = []
    for item in sorted(item_counts):
        sup = item_counts[item]
        tag = f"{item}({sup})" if sup >= min_sup else f"{item}({sup})*"
        parts.append(tag)
        if sup >= min_sup:
            frequent_1[(item,)] = sup

    print(f"\nL1  " + "  ".join(parts))
    print(f"    Frequent: " + ", ".join(f"{fmt(s)}({frequent_1[s]})" for s in sorted(frequent_1)))

    all_frequent: dict[int, dict[tuple, int]] = {1: frequent_1}
    k = 2

    while True:
        prev_frequent = all_frequent[k - 1]
        prev_sorted = sorted(prev_frequent)

        if len(prev_sorted) < 2:
            break

        candidates = generate_join(prev_sorted)
        if not candidates:
            break

        prev_freq_set = set(prev_sorted)

        # ── Prune (k ≥ 3) ────────────────────────────────────────
        if k >= 3:
            kept, pruned_list = prune_step(candidates, prev_freq_set)
        else:
            kept, pruned_list = candidates, []

        support_counts = count_support(transactions, kept)

        frequent_k: dict[tuple, int] = {}
        for c in kept:
            if support_counts[c] >= min_sup:
                frequent_k[c] = support_counts[c]

        # ── Print level ───────────────────────────────────────────
        cw = max(len(fmt(c)) for c in candidates)
        print(f"\nL{k}")

        if k >= 3:
            print(f"  Join:")
            for c in candidates:
                p, q = c[:-1], c[:-2] + (c[-1],)
                print(f"    {fmt(p)} + {fmt(q)} → {fmt(c)}")

            pruned_set = {c for c, _ in pruned_list}
            if pruned_list:
                print(f"  Prune:")
                for c, missing in pruned_list:
                    print(f"    {fmt(c)} — {fmt(missing)} not frequent → removed")

            print(f"  Support:")
            for c in kept:
                sup = support_counts[c]
                tag = "yes" if sup >= min_sup else f"NO (<{min_sup})"
                print(f"    {fmt(c)}({sup}) {tag}")
        else:
            # Level 2: compact table
            print(f"  {'Candidate':<{cw}}  Sup  Freq")
            for c in candidates:
                sup = support_counts[c]
                tag = "yes" if sup >= min_sup else f"NO (<{min_sup})"
                print(f"  {fmt(c):<{cw}}  {sup:>3}  {tag}")

        if not frequent_k:
            print(f"  No frequent {k}-itemsets.")
            all_frequent[k] = {}
            break

        print(f"  Frequent: " + ", ".join(f"{fmt(s)}({frequent_k[s]})" for s in sorted(frequent_k)))
        all_frequent[k] = frequent_k
        k += 1

    return all_frequent


def find_maximal(all_frequent: dict) -> list[tuple]:
    """Frequent itemsets with no frequent proper superset."""
    pool: dict[tuple, int] = {}
    for d in all_frequent.values():
        pool.update(d)
    pool_sets = {f: set(f) for f in pool}

    maximal = [
        (f, sup)
        for f, sup in pool.items()
        if all(not (pool_sets[f] < pool_sets[g]) for g in pool)
    ]
    return sorted(maximal, key=lambda x: (len(x[0]), x[0]))


def find_closed(all_frequent: dict) -> list[tuple]:
    """Frequent itemsets where no proper superset has the same support."""
    pool: dict[tuple, int] = {}
    for d in all_frequent.values():
        pool.update(d)
    pool_sets = {f: set(f) for f in pool}

    closed = []
    for f, sup in pool.items():
        is_closed = all(
            not (pool_sets[f] < pool_sets[g]) or pool[g] != sup
            for g in pool
        )
        if is_closed:
            closed.append((f, sup))
    return sorted(closed, key=lambda x: (len(x[0]), x[0]))


def generate_rules(
    transactions: list, all_frequent: dict, min_conf: float
) -> list[tuple]:
    """All association rules with confidence ≥ min_conf from frequent k-itemsets (k≥2)."""
    support_map: dict[tuple, int] = {}
    for d in all_frequent.values():
        support_map.update(d)

    rules = []
    for k, level_dict in all_frequent.items():
        if k < 2:
            continue
        for itemset, sup in level_dict.items():
            for r in range(1, len(itemset)):
                for antecedent in combinations(itemset, r):
                    consequent = tuple(sorted(set(itemset) - set(antecedent)))
                    ant_sup = support_map.get(antecedent)
                    if ant_sup is None:
                        ant_sup = count_support(transactions, [antecedent])[antecedent]
                        support_map[antecedent] = ant_sup
                    conf = sup / ant_sup
                    if conf >= min_conf:
                        rules.append((antecedent, consequent, sup, conf, ant_sup))

    return sorted(rules, key=lambda x: (-x[3], -x[2], x[0]))


def solve() -> None:
    path = input("Enter path to CSV file: ").strip().lstrip("﻿")
    min_sup = int(input("Enter minimum support count: ").strip())
    conf_raw = input("Enter minimum confidence for rules (0-1) [default=0.5]: ").strip()
    min_conf = float(conf_raw) if conf_raw else 0.5

    transactions = load_transactions(path)
    print(f"\n=== APRIORI  N={len(transactions)}  min_sup={min_sup}  min_conf={min_conf:.2f} ===")
    print("(* = not frequent)")

    all_frequent = apriori(transactions, min_sup)

    # ── Frequent itemsets summary ─────────────────────────────────
    print("\nFREQUENT ITEMSETS")
    for k in sorted(all_frequent):
        d = all_frequent[k]
        if d:
            print(f"  L{k}: " + ", ".join(f"{fmt(s)}({d[s]})" for s in sorted(d)))

    # ── Maximal ───────────────────────────────────────────────────
    maximal = find_maximal(all_frequent)
    print("\nMAXIMAL  (no frequent proper superset)")
    print("  " + "  ".join(f"{fmt(f)}({sup})" for f, sup in maximal))

    # ── Closed ────────────────────────────────────────────────────
    closed = find_closed(all_frequent)
    print("\nCLOSED  (no proper superset with equal support)")
    print("  " + "  ".join(f"{fmt(f)}({sup})" for f, sup in closed))

    # ── Association rules ─────────────────────────────────────────
    rules = generate_rules(transactions, all_frequent, min_conf)
    print(f"\nRULES  min_conf={min_conf:.2f}")
    if not rules:
        print("  (none)")
    else:
        rule_strs = [f"{fmt(a)} -> {fmt(c)}" for a, c, *_ in rules]
        rw = max(len(s) for s in rule_strs)
        print(f"  {'Rule':<{rw}}  Sup   Conf  Frac")
        for (a, c, sup, conf, ant_sup), rstr in zip(rules, rule_strs):
            print(f"  {rstr:<{rw}}  {sup:>3}  {conf:.4f}  {sup}/{ant_sup}")


if __name__ == "__main__":
    solve()
