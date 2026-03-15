rows = cols = 8

def idxs():
    for i in range(rows):
        for j in range(cols):
            yield i, j

WHITE = ["P", "N", "B", "R", "Q", "K"]
BLACK = [x.lower() for x in WHITE]

ROOK_DELTAS = [(0, 1), (-1, 0), (0, -1), (1, 0)]
BISHOP_DELTAS = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
KNIGHT_DELTAS = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
QUEEN_DELTAS = BISHOP_DELTAS + ROOK_DELTAS

def valid_single_moves(i, j, deltas):
    for di, dj in deltas:
        x, y = i+di, j+dj
        if valid(i, j, x, y):
            yield x, y

def in_bounds(x, y):
    return 0 <= x < rows and 0 <= y < cols

def valid(i, j, x, y):
    return in_bounds(x, y) and (board[x][y] == "." or board[i][j].isupper() != board[x][y].isupper())

def pawn_moves(i, j):
    deltas = [(-1, -1), (-1, 1)] if board[i][j] == "P" else [(1, 1), (1, -1)]
    for x, y in valid_single_moves(i, j, deltas):
        if board[x][y] != ".":
            yield x, y

    deltas = (-1, 0) if board[i][j] == "P"else (1, 0)
    x, y = i+deltas[0], j+deltas[1]
    if (not valid(i, j, x, y)) or board[x][y] != ".":
        return
    yield x, y
    if (board[i][j] == "P" and i == 6) or (board[i][j] == "p" and i == 1):
        q, w = x+deltas[0], y+deltas[1]
        if (not valid(i, j, q, w)) or board[q][w] != ".":
            return
        yield q, w

def knight_moves(i, j):
    yield from valid_single_moves(i, j, KNIGHT_DELTAS)

def bishop_moves(i, j):
    yield from valid_multi_moves(i, j, BISHOP_DELTAS)

def rook_moves(i, j):
    yield from valid_multi_moves(i, j, ROOK_DELTAS)

def queen_moves(i, j):
    yield from valid_multi_moves(i, j, QUEEN_DELTAS)

def valid_multi_moves(i, j, deltas):
    for di, dj in deltas:
        x, y = i, j
        while True:
            q, w = x+di, y+dj
            if not valid(i, j, q, w):
                break
            yield q, w
            x, y = q, w
            if board[q][w] != ".":
                break

def king_moves(i, j):
    yield from valid_single_moves(i, j, QUEEN_DELTAS)
    
def get_pos(char):
    for i, j in idxs():
        if board[i][j] == char:
            return i, j
            
move_map = {
    "P": pawn_moves,
    "N": knight_moves,
    "B": bishop_moves,
    "R": rook_moves,
    "Q": queen_moves,
    "K": king_moves
}
for k, v in move_map.copy().items():
    move_map[k.lower()] = v


def get_opp(i, j):
    return BLACK if board[i][j].isupper() else WHITE

def is_in_check(i, j):
    opponent = get_opp(i, j)
    for k, l in idxs():
        if board[k][l] in opponent:
            func = move_map[board[k][l]]
            for x, y in func(k, l):
                if (x, y) == (i, j):
                    return True
    return False


def solve(step):
    pieces = WHITE if step == 0 else BLACK
    for i, j in idxs():
        char = board[i][j]
        if char not in pieces:
            continue
        func = move_map[char]
        for x, y in func(i, j):
            if char == "P" and x == 0:
                chars = ["Q", "N"]
            else:
                chars = [char]
            for c in chars:
                cur = board[x][y]
                board[i][j] = "."
                board[x][y] = c
                if step == 1:
                    if not is_in_check(*get_pos("k")):
                        board[x][y] = cur
                        board[i][j] = char
                        return False
                else:
                    if is_in_check(*get_pos("k")) and not is_in_check(*get_pos("K")):
                        if solve(1):
                            return i, j, x, y
                board[x][y] = cur
                board[i][j] = char
    return True


board = [[c for c in input()] for _ in range(rows)]
i, j, x, y = solve(0)
i = 8 - i
x = 8 - x
j = chr(j + ord("a"))
y = chr(y + ord("a"))
print(f"{j}{i}{y}{x}")