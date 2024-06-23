import sys

class Node:
    def __init__(self):
        self.count = 0
        self.children = {}


ROOT = Node()

def add(word):
    ROOT.count += 1
    s = ROOT.count
    current = ROOT
    for char in word:
        current = current.children.setdefault(char, Node())
        current.count += 1
        s += current.count
    return s


def find(word):
    s = ROOT.count
    current = ROOT
    for char in word:
        current = current.children.get(char)
        if current is None:
            return s
        s += current.count
    return s


n = int(sys.stdin.readline())
words = {}
for _ in range(n):
    i = sys.stdin.readline()
    word = tuple(ord(i[x]) for x in range(len(i)-1))
    s = add(word)
    words[word] = s


q = int(sys.stdin.readline())
for _ in range(q):
    i = sys.stdin.readline()
    query_word = tuple(ord(i[x]) for x in range(len(i)-1))
    s = words.get(query_word)
    if s is None:
        sys.stdout.write(str(find(query_word))+"\n")
    else:
        sys.stdout.write(str(s)+"\n")