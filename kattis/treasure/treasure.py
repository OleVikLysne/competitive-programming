import sys

input = sys.stdin.readline
import heapq

INF = float("inf")
n, m, k = map(int, input().split())
num_nodes = n * m


def moves(i, j):
    for x, y in ((i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)):
        if 0 <= x < n and 0 <= y < m and get_weight(x, y) <= k:
            yield x, y


def get_node(i, j):
    return i * m + j


def get_weight(i, j):
    char = grid[i][j]
    if char == "S":
        return INF
    elif char == "G":
        return 1
    elif char == ".":
        return 1
    elif char == "F":
        return 2
    elif char == "M":
        return 3
    else:
        return INF


def dijkstra(source):
    dist = [(INF, INF)] * num_nodes
    dist[source] = 0
    prev = [-1] * num_nodes
    pq = [((0, -k), source)]
    while pq:
        (d, s), u = heapq.heappop(pq)
        for v, w in g[u]:
            days = d
            stamina = -s
            req_stamina = w
            if req_stamina > stamina:
                stamina = k - req_stamina
                days += 1
            else:
                stamina -= req_stamina

            if dist[v] > (days, -stamina):
                dist[v] = (days, -stamina)
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    return dist, prev


def get_path(dist):
    v = goal
    if dist[v] == (INF, INF):
        return False
    path = [v]
    while v != start:
        v = prev[v]
        path.append(v)
    path.reverse()
    return path


g = [[] for _ in range(num_nodes)]
grid = [input().rstrip() for _ in range(n)]
flat_rep = [0] * num_nodes
start = goal = None

for i in range(n):
    for j in range(m):
        v = get_node(i, j)
        if grid[i][j] == "S":
            start = v
        elif grid[i][j] == "G":
            goal = v

        for x, y in moves(i, j):
            u = get_node(x, y)
            weight = get_weight(x, y)
            g[v].append((u, weight))
            flat_rep[u] = weight


dist, prev = dijkstra(start)
if dist[goal] == (INF, INF):
    print(-1)
    exit()


path = get_path(prev)


stamina = k
days = 1
for v in path[1:]:
    if stamina == 0:
        stamina = k
        days += 1
    req_stamina = flat_rep[v]

    if req_stamina > stamina:
        stamina = k - req_stamina
        days += 1
    else:
        stamina -= req_stamina

print(days)
