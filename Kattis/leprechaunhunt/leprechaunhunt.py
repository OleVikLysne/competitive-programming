import sys; input=sys.stdin.readline
sys.setrecursionlimit(2**30)
import itertools
INF = 1 << 60


def lep(mask, i, mem, inf_visit):
    if mask & 1 << i:
        return 0
    best = 0
    for u in g[i]:
        if mask & 1 << u: continue
        best = max(best, villagers(mask, u, mem, inf_visit))
    best = max(best, villagers(mask, i, mem, inf_visit))
    return best

def villagers(mask, i, mem, inf_visit):
    if mem[mask][i] != -1:
        return mem[mask][i]
    mem[mask][i] = INF
    best = INF
    for v in range(N):
        if mask & 1 << v:
            for u in g[v]:
                if mask & 1 << u: continue
                best = min(best, 1 + lep((mask ^ (1 << v)) | (1 << u), i, mem, inf_visit))
    if best == INF:
        inf_visit.append((mask, i))
    mem[mask][i] = best
    return best


for c in range(1, INF):
    inp = input()
    if inp == "0\n": 
        break
    V, N, E = map(int, inp.split())
    g = [[] for _ in range(N)]
    while E:
        for e in input().split():
            E -= 1
            i, j = ord(e[0]) - ord("A"), ord(e[1]) - ord("A")
            g[i].append(j)
            g[j].append(i)

    best = INF
    mem = [[-1]*N for _ in range(1 << N)]
    for starting_spots in itertools.combinations(range(N), V):
        temp = 1
        mask = 0
        for s in starting_spots:
            mask |= 1 << s
        for i in range(N):
            if mask & 1 << i:
                continue
            inf_visit = []
            temp = max(temp, villagers(mask, i, mem, inf_visit))
            for m, j in inf_visit:
                mem[m][j] = -1

        best = min(best, temp)

    print(f"CASE {c}: {best if best != INF else 'NEVER'}")