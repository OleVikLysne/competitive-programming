from sys import stdin
from collections import deque


def neighbours(i, j):
    for x, y in ( (i+1, j), (i-1, j), (i, j+1), (i, j-1) ):
        if 0 <= x < num_rows and 0 <= y < num_cols:
            yield x, y

def get_index(i, j):
    return i*num_cols+j


num_cols, num_rows, _ = map(int, stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(num_rows)]
char_weights = [int(x) for x in stdin.readline().split()]

node_count = (num_cols*num_rows*2)+1
weight_matrix = [[0 for _ in range(node_count)] for _ in range(node_count)]
sink = num_rows*num_cols

for i in range(num_rows):
    for j in range(num_cols):
        a = get_index(i, j)
        b = a + num_cols*num_rows
        char = grid[i][j]
        if char == "B":
            source = a
        
        if char != "." and char != "B":
            weight_matrix[a][b] = char_weights[ord(char)-97]
        else:
            weight_matrix[a][b] = float("inf")
        
        if not (0 < i < num_rows-1 and 0 < j < num_cols-1):
            weight_matrix[b][sink] = float("inf")

        for x, y in neighbours(i, j):
            weight_matrix[b][get_index(x, y)] = float("inf")
        



def bfs(source, sink):
    q = deque([source])
    level[source] = 0
    while q:
        v = q.popleft()
        for u in range(node_count):
              cap = weight_matrix[v][u]
              if cap > 0 and level[u] < 0:
                  level[u] = level[v] + 1
                  q.append(u)
                  
    return level[sink] != -1

def dfs(current, flow, sink):
    if current == sink or flow == 0:
        return flow
    
    for v in range(ptr[current], node_count):
        cap = weight_matrix[current][v]
        if level[v] == level[current]+1 and cap > 0:
            pushed_flow = dfs(v, min(flow, cap), sink)
            if pushed_flow > 0:
                weight_matrix[current][v] -= pushed_flow
                weight_matrix[v][current] += pushed_flow
                return pushed_flow
        ptr[current] += 1
    return 0

total_flow = 0
level = [-1 for _ in range(node_count)]
level[source] = 0

# Dinics Algorithm
while bfs(source, sink):
    ptr = [0 for _ in range(node_count)]
    while True:
        flow = dfs(source, float("inf"), sink)
        if flow == 0:
            break
        total_flow += flow
    level = [-1 for _ in range(node_count)]
    level[source] = 0


if total_flow == float("inf"):
    total_flow = -1
print(total_flow)