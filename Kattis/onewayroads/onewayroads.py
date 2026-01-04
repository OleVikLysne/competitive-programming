from sys import stdin, stdout

N, M = map(int, stdin.readline().split())

g = [[] for _ in range(N)]
edges = set()
for _ in range(M):
    i, j = [int(x)-1 for x in stdin.readline().split()]
    if i > j:
        i, j = j, i
    g[i].append(j)
    g[j].append(i)
    edges.add((i, j))


stack = []
visited = [False]*N
component_nodes = set()
def dfs_cycle_search(v, w, stack, visited):
    stack.append(v)
    visited[v] = True
    for u in g[v]:
        if u == w or u in component_nodes and v in component_nodes:
            continue
        if visited[u]:
            stack.append(u)
            return False
        if not dfs_cycle_search(u, v, stack, visited):
            return False
    stack.pop()
    visited[v] = False
    return True

dfs_cycle_search(0, -1, stack, visited)
out_edges = set()

def add_to_comp(stack):
    if len(stack) <= 1: return
    component_nodes.add(stack[-1])
    for i in range(len(stack)-2, -1, -1):
        if stack[i] not in component_nodes:
            component_nodes.add(stack[i])
            out_edges.add((stack[i], stack[i+1]))
        else:
            out_edges.add((stack[i], stack[i+1]))
            break


add_to_comp(stack)


prev = 0
while prev < len(component_nodes) < N:
    prev = len(component_nodes)
    for v in component_nodes:
        visited = [True if i in component_nodes else False for i in range(N)]
        stack = []
        if not dfs_cycle_search(v, -1, stack, visited):
            add_to_comp(stack)
            break


if len(component_nodes) < N:
    stdout.write("NO")
else:
    stdout.write("YES\n")
    for i, j in out_edges:
        stdout.write(str(i+1) + " " + str(j+1) + "\n")
    for i, j in edges:
        if (i, j) not in out_edges and (j, i) not in out_edges:
            stdout.write(str(i+1) + " " + str(j+1) + "\n")
