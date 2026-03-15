N, k = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(N)]
input() 

mem = {}
def foo(i, blocks, last_block=(-2,-2)):
    x, y = last_block
    state = y if i-x == 1 else 2
    if (i, blocks, state) in mem: 
        return mem[(i, blocks, state)]
    if blocks == k:
        mem[(i, blocks, state)] = sum((grid[a][b] for a in range(i, N) for b in range(2)))
        return mem[(i, blocks, state)]
    if N-i < k-blocks:
        return -2**30
    
    if x + 1 == i:
        val = max(
            grid[i][(y+1)%2]        + foo(i+1, blocks+1, last_block=(i, y)),
            grid[i][0] + grid[i][1] + foo(i+1, blocks, last_block)
        )
    else:
        val = max(
            grid[i][1]              + foo(i+1, blocks+1, last_block=(i, 0)),
            grid[i][0]              + foo(i+1, blocks+1, last_block=(i, 1)),
            grid[i][0] + grid[i][1] + foo(i+1, blocks, last_block)
        )
    mem[(i, blocks, state)] = val
    return val
    
    
print(foo(0,0))