import sys; input = sys.stdin.readline
sys.setrecursionlimit(2**30)


def increment_key(d, k):
    d[k] = d.get(k, 0) + 1

def decrement_key(d, k):
    val = d.get(k, 0) - 1
    if val <= 0:
        del d[k]
    else:
        d[k] = val


def build_graph(i):
    while g[i] == -1 and 0 <= (j := i + board[i]) < n:
        g[i] = j
        rev_g[j].append(i)
        i = j


def get_cycle_values(i):
    values = {board[i]: 1}
    j = g[i]
    while j != i:
        increment_key(values, board[j])
        j = g[j]
    return values


def dfs(i):
    if g[i] == -1:
        dfs_rev(i, {})
        return
    if visited[i]:
        dfs_rev(i, get_cycle_values(i))
        return
    visited[i] = True
    dfs(g[i])
    visited[i] = False


def dfs_rev(i, values, visit_set=None):
    if visit_set is None:
        visit_set = set()
    visit_set.add(i)
    increment_key(values, board[i])
    win_instances[i] = len(values)

    for j in rev_g[i]:
        if j not in visit_set:
            dfs_rev(j, values, visit_set)

    decrement_key(values, board[i])


n = int(input())
board = [int(x) for x in input().split()]

g = [-1 for _ in range(n)]
rev_g = [[] for _ in range(n)]
visited = [False]*n
win_instances = [0]*n

for i in range(n):
    build_graph(i)

for i in range(n):
    if win_instances[i] == 0:
        dfs(i)
print(sum(win_instances))