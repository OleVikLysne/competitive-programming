def search(board, count, best, mem=None):
    if mem is None:
        mem = {}
    board_tuple = tuple(x for x in board)
    if board_tuple in mem:
        return mem[board_tuple]
    for i in range(len(board)):
        if board[i] != 1:
            continue
        if i >= 2:
            if board[i-1] == 1 and board[i-2] == 0:
                board[i-1] = 0
                board[i-2] = 1
                board[i] = 0
                best = min(search(board, count-1, best, mem), best)
                board[i-1] = 1
                board[i-2] = 0
                board[i] = 1
        if i <= len(board)-3:
            if board[i+1] == 1 and board[i+2] == 0:
                board[i+1] = 0
                board[i+2] = 1
                board[i] = 0
                best = min(search(board, count-1, best, mem), best)
                board[i+1] = 1
                board[i+2] = 0
                board[i] = 1
    mem[board_tuple] = min(count, best)
    return mem[board_tuple]


for _ in range(int(input())):
    board = [0 if char == "-" else 1 for char in input()]
    count = board.count(1)
    print(search(board, count, count))