N = int(input())
nodes = [int(x) for x in input().split()]
input()
luigi_pipes = [int(x) for x in input().split()]
pipes = list(set(range(N))-set(nodes))
pipes.sort()

pipe_data, coinroom_data = {}, {}

for pipe in pipes:
    next_warp = nodes[pipe]
    if next_warp == -1:
        pipe_data[pipe] = pipe
        num_warps = 0
        coin_room = pipe
    else:
        num_warps = 1
        while nodes[next_warp] != -1:
            num_warps += 1
            next_warp = nodes[next_warp]
        coin_room = next_warp
        pipe_data[pipe] = coin_room
    
    if coin_room not in coinroom_data:
        coinroom_data[coin_room] = (pipe, num_warps)
        continue
    
    if coinroom_data[coin_room][1] > num_warps:
        coinroom_data[coin_room] = (pipe, num_warps)
        
for luigi_pipe in luigi_pipes:
    coin_room = pipe_data[luigi_pipe]
    print(coinroom_data[coin_room][0])
