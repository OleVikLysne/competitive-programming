from sys import stdin


class Trie:
    def __init__(self):
        self.root = {}

    def add(self, word: str):
        current = self.root
        for char in word:
            current = current.setdefault(char, {})
        if "*" not in current:
            current["*"] = 1
        else:
            current["*"] += 1

    def search(self, i, j):
        char = grid[i][j]
        if char not in self.root:
            return 0
        return self._search(i, j, self.root[char])

    def _search(self, i, j, current):
        s = current.get("*", 0)
        if s > 0:
            current["*"] = 0

        old_char = grid[i][j]
        grid[i][j] = 0
        for x, y in moves(i, j):
            if not grid[x][y]:
                continue
            char = grid[x][y]
            if char in current:
                s += self._search(x, y, current[char])
        grid[i][j] = old_char
        return s


def moves(i, j):
    for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
        if 0 <= x < h and 0 <= y < w:
            yield x, y


trie = Trie()
h, w = map(int, stdin.readline().split())
grid = [[ord(x) for x in stdin.readline().rstrip()] for _ in range(h)]

for _ in range(int(stdin.readline())):
    word = tuple(ord(x) for x in stdin.readline().rstrip())
    trie.add(word)

s = 0
for i in range(h):
    for j in range(w):
        s += trie.search(i, j)
print(s)
