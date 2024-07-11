board = [[int(x) for x in input().split()] for _ in range(4)]
n = int(input())


def left():
    b = []
    for j in reversed(range(4)):
        row = []
        for i in range(4):
            row.append(board[i][j])
        b.append(row)
    return b

if n == 0:
    board = left()
    board = left()
elif n == 1:
    board = left()
    board = left()
    board = left()
elif n == 3:
    board = left()


for i in range(4):
    for j in reversed(range(4)):
        for k in reversed(range(j)):
            if board[i][k] == 0:
                continue
            if board[i][k] == board[i][j]:
                board[i][j] *= 2
                board[i][k] = 0
            break



for i in range(4):
    for j in range(4):
        if board[i][j] == 0:
            board[i].pop(j)
            board[i].insert(0, 0)

if n == 0:
    board = left()
    board = left()
elif n == 1:
    board = left()
elif n == 3:
    board = left()
    board = left()
    board = left()

for row in board:
    print(" ".join(str(x) for x in row))