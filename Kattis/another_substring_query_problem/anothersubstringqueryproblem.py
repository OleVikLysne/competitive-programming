import sys; input=sys.stdin.readline
from collections import defaultdict

B = 2**31-1
A = 31



string = [ord(x) for x in input().rstrip()]
n = len(string)
pows = [1]*n
for i in range(1, n):
    pows[i] = (pows[i-1] * A) % B
hash_df = [defaultdict(list) for _ in range(n+1)]

def get_hash(seq):
    hashed_str = 0
    for i in range(len(seq)):
        hashed_str += seq[i] * pows[len(seq)-i-1]
        hashed_str %= B
    return hashed_str
    

def get_df(s: int):
    if hash_df[s]:
        return hash_df[s]
    hashed_str = 0
    for i in range(s):
        hashed_str += string[i] * pows[s-i-1]
        hashed_str %= B
    
    hash_df[s][hashed_str].append(0)
    for i in range(s, n):
        hashed_str -= string[i-s] * pows[s-1]
        hashed_str *= A
        hashed_str += string[i]
        hashed_str %= B
        hash_df[s][hashed_str].append(i-s+1)
    return hash_df[s]

for _ in range(int(input())):
    seq, k = input().split()
    k = int(k)-1
    max_idx = n - len(seq)
    if k > max_idx:
        print(-1)
        continue
    seq = [ord(x) for x in seq]
    df = get_df(len(seq))
    hash = get_hash(seq)
    idxs = df[hash]
    print(idxs[k]+1 if k < len(idxs) else -1)
