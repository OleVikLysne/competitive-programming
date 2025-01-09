import sys; input=sys.stdin.readline
import bisect

def comp(x, y):
    return P[x] > P[y] or (P[x] == P[y] and x < y)

def merge(arr1, arr2, k):
    res = []
    i = 0
    j = 0
    for _ in range(k):
        if i >= len(arr1) and j >= len(arr2):
            break
        if i < len(arr1) and (j >= len(arr2) or comp(arr1[i], arr2[j])):
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    return res

n = int(input())
items = []
P = []
for i in range(n):
    p, v = map(int, input().split())
    P.append(p)
    items.append((i, v))
items.sort(key=lambda x: x[1])


table = [[] for _ in range(n)]
table[0] = [items[0][0]]
for i in range(1, n):
    table[i] = merge(table[i-1], [items[i][0]], 10)


q = int(input())
for _ in range(q):
    x, k = map(int, input().split())
    i = bisect.bisect_right(items, x, key = lambda x: x[1])
    if i == 0:
        print("-1")
    else:
        print(*(table[i-1][j]+1 for j in range(min(k, i))))