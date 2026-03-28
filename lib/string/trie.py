class Trie:
    def __init__(self):
        self.root = {}
    
    def add(self, word: str):
        current = self.root
        for char in word:
            current = current.setdefault(char, {})
        current["*"] = True

    def query(self, word: str):
        current = self.root
        for char in word:
            if (current := current.get(char)) is None:
                return False
        return "*" in current
