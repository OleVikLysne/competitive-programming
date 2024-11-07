from collections import defaultdict

B = 2**61-1
A = 31

N, k = map(int, input().split())
string = [ord(x) for x in input()]

hashed_str = 0
n = len(string) + k - 1
for i in range(k):
    hashed_str += string[i] * pow(A, k - i - 1, B)
    hashed_str %= B

hashes = defaultdict(list)
hashes[hashed_str].append((0, k - 1))
for i in range(k, n):
    j = i % N
    hashed_str -= string[(i - k) % N] * pow(A, k - 1, B)
    hashed_str *= A
    hashed_str += string[j]
    hashed_str %= B

    if len(hashes[hashed_str]) > 0:
        prev = hashes[hashed_str][-1][1]
        if i - k + 1 < prev or (i >= N and i % N >= hashes[hashed_str][0][0]):
            continue
    hashes[hashed_str].append((i - k + 1, i))


def build(pattern):
    n = len(pattern)
    lps = [0]*n
    length = 0
    i = 1
    while i < n:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length-1]
        else:
            i += 1

    temp = []
    res = []
    for x in lps:
        if x == 0:
            temp.reverse()
            res.extend(temp)
            temp.clear()
            res.append(0)
        else:
            temp.append(x)
    temp.reverse()
    res.extend(temp)
    return res

def min_lex(i, j, a, b):
    j %= N
    b %= N
    i %= N
    a %= N
    while i != j and a != b:
        if string[i] < string[a]:
            return True
        if string[i] > string[a]:
            return False
        i += 1
        a += 1
        i %= N
        a %= N
    return True


longest = len(max(hashes.values(), key=len))
candidates = []
for v in hashes.values():
    if len(v) == longest:
        candidates.append(v[0])

candidates.sort()
i, j = candidates[0]
pat = build(tuple(string[k % N] for k in range(i, j + 1)))
for a, b in candidates[1:]:
    if a-i < len(pat):
        diff = pat[a-i]
    else:
        diff = 0
    if not min_lex(i+diff, j, a+diff, b):
        i, j = a, b
        pat = build(tuple(string[k % N] for k in range(i, j + 1)))


print("".join(chr(string[k % N]) for k in range(i, j + 1)))
