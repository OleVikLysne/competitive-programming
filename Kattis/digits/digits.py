W, H = [int(x) for x in input().split()]
keys = [int(x) for x in input()]
grid = [[int(x) for x in input()] for _ in range(H)]


mem = {}
def foo(x, y, k):
    if (x,y,k) in mem:
        return mem[(x,y,k)]
    if x==W-1 and y==0:
        mem[(x,y,k)] = grid[y][x]
        return grid[y][x]
    val = grid[y][x]
    right, up, right_hop, up_hop = [2**30 for _ in range(4)]
    if x+1 < W:
        right = foo(x+1, y, k)
    if y-1 >= 0:
        up = foo(x, y-1, k)
    if k < len(keys):
        if x+keys[k]+1 < W:
            right_hop = foo(x+keys[k]+1, y, k+1)
        if y-(keys[k]+1) >= 0:
            up_hop = foo(x, y-(keys[k]+1), k+1)
    ret = val + min(right, up, right_hop, up_hop)
    mem[(x,y,k)] = ret
    return ret


print(foo(0, H-1, 0))