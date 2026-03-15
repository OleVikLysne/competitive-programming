from sys import stdin, stdout


class Node:
    def __init__(self):
        self.count = 0
        self.children = {}

    def add(self, word):
        self.count += 1
        s = self.count
        current = self
        for char in word:
            current = current.children.setdefault(char, Node())
            current.count += 1
            s += current.count
        current.children["*"] = s
        return s

    def find(self, word):
        s = self.count
        current = self
        for char in word:
            current = current.children.get(char)
            if current is None:
                return s
            s += current.count
        return current.children.get("*", s)


n = int(stdin.readline())
trie = Node()
for _ in range(n):
    inp = stdin.readline()
    word = tuple(ord(inp[x]) for x in range(len(inp) - 1))
    s = trie.add(word)


q = int(stdin.readline())
for _ in range(q):
    inp = stdin.readline()
    query_word = tuple(ord(inp[x]) for x in range(len(inp) - 1))
    stdout.write(str(trie.find(query_word)) + " ")
