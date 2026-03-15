c, t = [int(x) for x in input().split()]
adj_list = [[] for _ in range(c+1)]
for _ in range(t):
    a, b = [int(x) for x in input().split()]
    adj_list[a].append(b)
    adj_list[b].append(a)

mole_1 = set(range(1, c+1))
mole_2 = set()
visited = set()
path = []

def dfs(node):
    visited.add(node)
    #path.append(node)
    for adj_node in adj_list[node]:
        if adj_node not in visited:
            path.append(adj_node)
            dfs(adj_node)
            path.pop()

    path.append(node)

        



        

        

def output():
    print(f"{len(path)} {len(mole_1)}")
    print(*path)
    if len(mole_1) > 0:
        print(*mole_1)
        print(*mole_2)
    exit()

                
dfs(1)
print(path)
# print(mole_1)
# print(mole_2)

