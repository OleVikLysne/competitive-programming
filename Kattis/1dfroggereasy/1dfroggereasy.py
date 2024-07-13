import sys; input = sys.stdin.readline

n, s, m = map(int, input().split())
i = s-1
board = [int(x) for x in input().split()]
if board[i] == m:
    print("magic\n0")
    exit()
visited = [False]*n
h = 0
while visited[i] is False:
    visited[i] = True
    i += board[i]
    h += 1
    if i < 0:
        print(f"left\n{h}")
        exit()
    elif i >= n:
        print(f"right\n{h}")
        exit()
    elif board[i] == m:
        print(f"magic\n{h}")
        exit()

print(f"cycle\n{h}")