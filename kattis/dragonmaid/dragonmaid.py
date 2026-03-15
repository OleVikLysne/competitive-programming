import sys; input=sys.stdin.readline
import bisect

def comp(x, y):
    return P[x-1] > P[y-1] or (P[x-1] == P[y-1] and x < y)

def insort(arr, elem):
    res = []
    for i in range(len(arr)):
        if comp(arr[i], elem):
            res.append(arr[i])
        else:
            res.append(elem)
            res.extend(arr[i:9])
            break
    else:
        if len(res) < 10:
            res.append(elem)
    return res

n = int(input())
items = []
P = []
for i in range(n):
    p, v = map(int, input().split())
    P.append(p)
    items.append((i+1, v))
items.sort(key=lambda x: x[1])

table = [[-1], [items[0][0]]]
table.extend(insort(table[i], items[i][0]) for i in range(1, n))

for _ in range(int(input())):
    x, k = map(int, input().split())
    i = bisect.bisect_right(items, x, key = lambda x: x[1])
    print(*(table[i][:k]))