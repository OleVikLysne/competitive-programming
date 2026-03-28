rows: int = ...
cols: int = ...


def valid_moves(i, j):
    l = []
    for x, y in (
        (i + 1, j),
        (i - 1, j),
        (i, j + 1),
        (i, j - 1),
        (i + 1, j + 1),
        (i - 1, j + 1),
        (i + 1, j - 1),
        (i - 1, j - 1),
    ):
        if 0 <= x < rows and 0 <= y < cols:
            l.append((x, y))
    return l


def valid_moves(i, j):
    l = []
    for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
        if 0 <= x < rows and 0 <= y < cols:
            l.append((x, y))
    return l


def valid_chess_knight_moves(i, j):
    l = []
    for x, y in (
        (i + 2, j + 1),
        (i - 2, j + 1),
        (i + 2, j - 1),
        (i - 2, j - 1),
        (i + 1, j + 2),
        (i - 1, j + 2),
        (i + 1, j - 2),
        (i - 1, j - 2),
    ):
        if 0 <= x < rows and 0 <= y < cols:
            l.append((x, y))
    return l
