import sys; input=sys.stdin.readline

B = 100123456789
A = 27

MAX = 30
pows = [1]*MAX
for i in range(1, MAX):
    pows[i] = (pows[i-1] * A) % B

hashes = [{} for _ in range(MAX)]
result = {}

def add(string):
    hashed_str = 0
    res = 0
    for i in range(len(string)):
        x = hashes[i].get(hashed_str, 0) + 1
        hashes[i][hashed_str] = x
        res += x
        hashed_str += ord(string[i]) * pows[i]
        hashed_str %= B
    result[hashed_str] = res

def query(string):
    hashed_str = 0
    res = 0
    for i in range(len(string)):
        if not (x := hashes[i].get(hashed_str)):
            return res
        res += x
        hashed_str += ord(string[i]) * pows[i]
        hashed_str %= B
    return result.get(hashed_str, res)

n = int(input())
for _ in range(n):
    add(input())

q = int(input())
for _ in range(q):
    print(query(input()))
