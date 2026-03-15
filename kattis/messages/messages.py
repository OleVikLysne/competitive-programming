import sys; input=sys.stdin.readline

class Trie:
    def __init__(self):
        self.root = {}
    
    def add(self, word: str):
        current = self.root
        for char in word:
            current = current.setdefault(char, {})
        current["*"] = True
    
    def find_first(self, word: str, start):
        current = self.root
        for i in range(start, len(word)):
            char = word[i]
            if (current := current.get(char)) is None:
                return float("inf")
            if "*" in current:
                return i
        return float("inf")


trie = Trie()

while (inp:= input()) != "#\n":
    word = tuple(ord(inp[i]) for i in range(len(inp)-1))
    trie.add(word)


word = []
while (inp := input()) != "#\n":
    for i in range(len(inp)-1):
        word.append(ord(inp[i]))
    if word[-1] == ord("|"):
        word.pop()
        s = 0
        best = float("inf")
        for i in range(len(word)):
            if i > best:
                s += 1
                best = float("inf")
            j = trie.find_first(word, i)
            best = min(best, j)
        if best != float("inf"):
            s += 1
        print(s)
        word.clear()
