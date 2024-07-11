from sys import stdin, stdout, setrecursionlimit
setrecursionlimit(2**30)

def topological_sort(g: list[list[int]], roots: list[int]):
    if not roots:
        return False

    topo_order = []
    visited = [False]*len(g)
    rec_stack = set()

    def dfs(v):
        if v in rec_stack:
            return False # not a DAG
        if not visited[v]:
            visited[v] = True
            rec_stack.add(v)

            for u in g[v]:
                if not dfs(u):
                    return False
            rec_stack.remove(v)

            topo_order.append(v)
        return True

    for root in roots:
        if not dfs(root):
            return False
    topo_order.reverse()
    return topo_order

n, m = map(int, stdin.readline().split())
g = [[] for _ in range(n)]
roots = set(range(n))
for _ in range(m):
    i, j = [int(x)-1 for x in stdin.readline().split()]
    g[i].append(j)
    if j in roots:
        roots.remove(j)

    
res = topological_sort(g, roots)
if res is False:
    stdout.write("IMPOSSIBLE")
else:
    for x in res:
        stdout.write(str(x+1)+"\n")