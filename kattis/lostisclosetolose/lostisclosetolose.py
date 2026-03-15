B = 2**61-1 # 10**9+7 # 10**18+7 # 2987583780930787
A = 31

def sanitize(word: str):
    l = []
    for c in word:
        if c.isalpha():
            l.append(ord(c.lower()))
    return tuple(l)

import sys
from collections import defaultdict
hashes = defaultdict(list)
k = 82
words = set()
for line in sys.stdin:
    if line == "***\n":
        break
    for word in map(sanitize, line.split()):
        if word and word not in words:
            hashed_str = 0
            for i in range(len(word)):
                hashed_str += word[i] * pow(A, k - i - 1, B)
                hashed_str %= B
            words.add(word)
            hashes[hashed_str].append(word)


pairs = defaultdict(set)

for word in words:
    n = len(word)
    prefix = [0]*(n+1)
    for i in range(n):
        prefix[i+1] = (prefix[i] + word[i] * pow(A, k - i - 1, B)) % B
    for i in range(n):
        l = prefix[i]
        r = (prefix[n] - prefix[i+1]) % B
        hash = (l + r * A) % B
    
        for other in hashes[hash]:
            pairs[word].add(other)
            pairs[other].add(word)

    
    for i in range(n):
        for char in range(ord("a"), ord("z")+1):
            if char == word[i]: continue
            hash = prefix[n] - word[i] * pow(A, k - i - 1, B)
            hash += char * pow(A, k - i - 1, B)
            hash %= B
            for other in hashes[hash]:
                pairs[word].add(other)
    
    for i in range(n-1):
        hash = prefix[n]
        hash -= word[i] * pow(A, k - i - 1, B)
        hash += word[i+1] * pow(A, k - i - 1, B)
        hash -= word[i+1] * pow(A, k - i - 2, B)
        hash += word[i] * pow(A, k - i - 2, B)
        hash %= B
        
        for other in hashes[hash]:
            pairs[word].add(other)

found = False
for word in sorted(pairs.keys()):
    pairs[word].discard(word)
    if not pairs[word]:
        continue
    found = True
    x = sorted("".join(chr(y) for y in x) for x in pairs[word])
    print(f"{''.join(chr(y) for y in word)}:", *x)
if not found:
    print("***")