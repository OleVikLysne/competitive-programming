from collections import deque

f, s, g, u, d = map(int, input().split())
s -= 1
g -= 1
if s == g:
    print(0)
    exit()


def moves(pos):
    if pos - d >= 0:
        yield pos - d
    if pos + u < f:
        yield pos + u


q = deque([(s, 0)])
visited = [False] * f
visited[s] = True
while q:
    pos, presses = q.popleft()
    for next_pos in moves(pos):
        if next_pos == g:
            print(presses + 1)
            exit()
        if not visited[next_pos]:
            visited[next_pos] = True
            q.append((next_pos, presses + 1))
print("use the stairs")
