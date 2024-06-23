def topological_sort(graph):
    topo_order = []
    visited = [False]*len(graph)
    recursion_stack = set()

    def dfs(node):
        if node in recursion_stack:
            raise ValueError("Graph is not a DAG")
        if not visited[node]:
            visited[node] = True
            recursion_stack.add(node)

            for neighbor in graph[node]:
                dfs(neighbor)
            recursion_stack.remove(node)

            topo_order.append(node)

    dfs(0)
    topo_order.reverse()
    return topo_order