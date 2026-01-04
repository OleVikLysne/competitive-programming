from collections import defaultdict
B = 2**31 - 1 # 2**61-1 # 10**9+7 # 10**18+7
A = 31


def roll_hash(string, k, b=False):
    n = len(string)
    hashed_str = 0
    for i in range(k):
        hashed_str += string[i] * pow(A, k - i - 1, B)
        hashed_str %= B
    hashes = defaultdict(list)
    hashes[hashed_str].append(0)
    for i in range(k, n):
        hashed_str -= string[i - k] * pow(A, k - 1, B)
        hashed_str *= A
        hashed_str += string[i]
        hashed_str %= B
        hashes[hashed_str].append(i-k+1)

        if not b and len(hashes[hashed_str]) > 1:
            if check(string, hashes[hashed_str][-2], hashes[hashed_str][-1], k):
                return True
    if not b:
        return False
    return hashes

def check(string, i, j, lower):
    a = i
    while i < a+lower:
        if string[i] != string[j]:
            return False
        i += 1
        j += 1
    return True

string = tuple(ord(x) for x in input())
lower, upper = 1, len(string)
while lower < upper:
    mid = (lower+upper)//2
    if roll_hash(string, mid):
        if lower == mid:
            break
        lower = mid
    else:
        upper = mid



cur = None
hashes = roll_hash(string, lower, True)
for l in hashes.values():
    if len(l) == 1:
        continue
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if check(string, l[i], l[j], lower):
                s = string[l[i]:l[i]+lower]
                if cur is None or s < cur:
                    cur = s
print("".join(chr(x) for x in cur))
