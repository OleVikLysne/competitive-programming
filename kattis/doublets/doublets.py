import sys; input=sys.stdin.readline
from collections import defaultdict, deque

B = 2**31-1
A = 31 # cool prime number

def rolling_hash(string):
    hashed_str = 0
    n = len(string)
    for i in range(n):
        hashed_str += string[i] * pow(A, n-i, B)
        hashed_str %= B
    return hashed_str

def hash_substrings(string, hashed_str):
    n = len(string)
    for i in range(n):
        yield (hashed_str - string[i] * pow(A, n-i, B)) % B


def check(string1, string2):
    if len(string1) != len(string2):
        return False
    found = False
    for x, y in zip(string1, string2):
        if x != y:
            if found:
                return False
            found = True
    return found

words = []
for line in sys.stdin:
    if line == "\n": break
    words.append(tuple(ord(x) for x in line.rstrip()))

hashes = defaultdict(list)
word_to_idx = {}
g = [[] for _ in range(len(words))]
for word_idx in range(len(words)):
    word = words[word_idx]
    word_to_idx[word] = word_idx
    hash = rolling_hash(word)
    for sub_hash in hash_substrings(word, hash):
        for other_idx in hashes[sub_hash]:
            if check(words[word_idx], words[other_idx]):
                g[word_idx].append(other_idx)
                g[other_idx].append(word_idx)

        hashes[sub_hash].append(word_idx)

def shortest_path(source, target):
    q = deque([source])
    prev = [-1]*len(g)
    while q:
        v = q.popleft()
        for u in g[v]:
            if prev[u] != -1:
                continue
            prev[u] = v
            if u == target:
                return prev
            q.append(u)
    return False

def get_path(prev, start, target):
    v = target
    path = [v]
    while v != start:
        v = prev[v]
        path.append(v)
    path.reverse()
    return path


for line in sys.stdin:
    start, target = (tuple(ord(x) for x in y) for y in line.split())
    start_idx, target_idx = word_to_idx[start], word_to_idx[target]
    if (prev := shortest_path(start_idx, target_idx)) is False:
        print("No solution.")
    else:
        path = get_path(prev, start_idx, target_idx)
        for i in path:
            print("".join(chr(x) for x in words[i]))
    print()