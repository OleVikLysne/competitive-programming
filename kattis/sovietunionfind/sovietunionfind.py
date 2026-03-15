import sys; input=sys.stdin.readline

def get_ruler(i):
    if parent[i] == -1:
        return i
    parent[i] = get_ruler(parent[i])
    return parent[i]

def _balkanize(i):
    for j in children[i]:
        _balkanize(j)
    parent[i] = -1
    children[i].clear()

def balkanize(i):
    _balkanize(get_ruler(i))

def annex(i, j):
    i = get_ruler(i)
    j = get_ruler(j)
    if i == j: return
    parent[j] = i
    children[i].append(j)


n, q = map(int, input().split())
parent = [-1]*(n+1)
children = [[] for _ in range(n+1)]

for _ in range(q):
    qt = sys.stdin.read(1)
    if qt == "a":
        i, j = map(int, input().split())
        annex(i, j)
    elif qt == "b":
        i = int(input())
        balkanize(i)
    else: # c
        i = int(input())
        ruler = get_ruler(i)
        print(ruler)
