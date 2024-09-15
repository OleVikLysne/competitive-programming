g: list[list[int]] = ...

def bipartite(g):
    def _bipartite(g, v, colours, c=0):
        if colours[v] != -1:
            if colours[v] != c:
                return False
            return True
        colours[v] = c
        c = (c+1) % 2
        for u in g[v]:
            if not _bipartite(g, u, colours, c):
                return False
        return True
    
    n = len(g)
    colours = [-1]*n
    for i in range(n):
        if colours[i] == -1:
            if not _bipartite(g, i, colours):
                return False
    return True