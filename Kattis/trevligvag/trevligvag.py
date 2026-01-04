# 62 / 100

import sys

sys.setrecursionlimit(2**30)

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    g[u - 1].append((v - 1, w))

for arr in g:
    arr.sort()


base = (-1, 1, 1, 1)
mem = [base for _ in range(n)]


def search(v, collected, visit_count):
    if v == n - 1:
        return collected, visit_count

    if mem[v][0] != base[0]:
        pre_collect, pre_count, post_collect, post_count = mem[v]
        stored_score = (pre_collect + post_collect) / max(pre_count + post_count, 1)
        new_score = (collected + post_collect) / max(visit_count + post_count, 1)
        if new_score <= stored_score:
            return pre_collect + post_collect, pre_count + post_count

    best = mem[v]
    stored_score = -1
    for u, w in g[v]:
        coll, count = search(u, collected + w, visit_count + 1)
        score = coll / count
        if score > stored_score:
            best = (collected, visit_count, coll - collected, count - visit_count)
            stored_score = score

    mem[v] = best
    return (best[0] + best[2]), (best[1] + best[3])


a, b = search(0, 0, 0)
print(a / b)