from collections import defaultdict

B = 2**61 - 1
A = 31

N, k = map(int, input().split())
string = [ord(x) for x in input()]

hashed_str = 0
n = len(string) + k - 1
for i in range(k):
    hashed_str += string[i] * pow(A, k - i - 1, B)
    hashed_str %= B

hashes = defaultdict(lambda: [0, (N, -1)])
hashes[hashed_str] = [1, (0, k - 1)]
for i in range(k, n):
    hashed_str -= string[(i - k) % N] * pow(A, k - 1, B)
    hashed_str *= A
    hashed_str += string[i % N]
    hashed_str %= B
    prev = hashes[hashed_str][1]
    if i-k+1 >= prev[1] and (i < N or i % N < prev[0]):
        hashes[hashed_str][0] += 1
        hashes[hashed_str][1] = (i - k + 1, i)


def build(j, k):
    n = k - j + 1
    lps = [0] * n
    length = 0
    i = 1
    while i < n:
        if string[(i + j) % N] == string[(length + j) % N]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
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


longest = max(hashes.values(), key=lambda x: x[0])[0]
candidates = []
for x in hashes.values():
    if x[0] == longest:
        candidates.append(x[1])

candidates.sort()
i, j = candidates[0]
pat = build(i, j)
for a, b in candidates[1:]:
    if a - i < len(pat):
        diff = pat[a - i]
    else:
        diff = 0
    if not min_lex(i + diff, j, a + diff, b):
        i, j = a, b
        pat = build(i, j)

print("".join(chr(string[k % N]) for k in range(i, j + 1)))
