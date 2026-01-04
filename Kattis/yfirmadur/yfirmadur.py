import sys; input=sys.stdin.readline
import heapq

n, q = map(int, input().split())
parent = [x for x in range(n+1)]
m = [x for x in range(n+1)]
rev_m = [x for x in range(n+1)]
heap = []

def add(x):
    i = len(rev_m)
    rev_m.append(0)
    parent.append(0)
    if not heap:
        j = len(m)
        m.append(0)
    else:
        j = heapq.heappop(heap)
    x = m[x]
    m[j] = i
    rev_m[i] = j
    parent[i] = x

def remove(x):
    heapq.heappush(heap, x)
    rev_m[m[x]] = -1

def query(x):
    x = m[x]
    y = parent[x]
    while rev_m[y] == -1:
        y = parent[y]
    while rev_m[parent[x]] == -1:
        parent[x], x = y, parent[x]
    return rev_m[y]


for i, x in enumerate(map(int, input().split()), 1):
    parent[i] = x
for _ in range(q):
    qt, x = input().split()
    x = int(x)
    match qt:
        case "+":
            add(x)
        case "-":
            remove(x)
        case "?":
            print(query(x))