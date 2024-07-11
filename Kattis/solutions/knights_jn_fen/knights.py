from collections import deque
from sys import stdin, stdout


def valid_moves(pos):
    i, j = divmod(pos, 5)
    if i >= 2:
        if j >= 1:
            yield pos-11
        if j <= 3:
            yield pos-9
    if i <= 2:
        if j >= 1:
            yield pos+9
        if j <= 3:
            yield pos+11

    if j >= 2:
        if i >= 1:
            yield pos-7
        if i <= 3:
            yield pos+3

    if j <= 2:
        if i >= 1:
            yield pos-3
        if i <= 3:
            yield pos+7



def next_boards(board):
    pos = board >> 25
    tile = (board >> pos) & 1
    for next_pos in valid_moves(pos):
        next_tile = (board >> next_pos) & 1
        tile_diff = next_tile ^ tile
        pos_diff = next_pos ^ pos
        mask = (tile_diff << next_pos) | (tile_diff << pos) | (pos_diff << 25)

        yield board ^ mask


target_board = 0b011001111101111001110000100000

q = deque([(target_board, 0)])
target = {}
while q:
    board, k = q.popleft()
    target[board] = k
    if k+1 > 5:
        continue
    
    for next_board in next_boards(board):
        if next_board not in target:
            q.append((next_board, k+1))


visited = set()
N = int(stdin.readline())
for _ in range(N):
    board = 0
    for i in range(5):
        inp = stdin.readline()
        for j in range(5):
            if inp[j] == "0":
                continue
            pos = (4 - i)*5 + (4 - j)
            board |= 1 << pos
            if inp[j] == " ":
                board |= pos << 25

    q.append((board, 0))
    while q:
        board, k = q.popleft()
        if board in target:
            stdout.write(f"Solvable in {target[board] + k} move(s).\n")
            break
        if k+1 > 5:
            continue

        visited.add(board)
        for next_board in next_boards(board):
            if next_board not in visited:
                q.append((next_board, k+1))
    else:
        stdout.write("Unsolvable in less than 11 move(s).\n")

    q.clear()
    visited.clear()
