import sys

input = sys.stdin.readline

B = 2**31 - 1  # 2**61-1 # 10**9+7 # 2987583780930787 # 100123456789
A = 31
MAX = 250_000

pows = [1] * MAX
for i in range(1, MAX):
    pows[i] = (pows[i - 1] * A) % B


def rolling_hash(string):
    hashed_str = 0
    k = len(string)
    for i in range(k):
        hashed_str += string[i] * pows[k - i - 1]
        hashed_str %= B
    return hashed_str


def roll_hash(string, k):
    n = len(string)
    hashed_str = 0
    l = []
    for i in range(k):
        hashed_str += string[i] * pows[k - i - 1]
        hashed_str %= B
    l.append(hashed_str)
    for i in range(k, n):
        hashed_str -= string[i - k] * pows[k - 1]
        hashed_str *= A
        hashed_str += string[i]
        hashed_str %= B
        l.append(hashed_str)
    return l


for _ in range(int(input())):
    string, pattern = [tuple(map(ord, x)) for x in input().split()]
    hash = rolling_hash(pattern)
    n = len(string)
    k = len(pattern)

    left = [-1] * n
    right = [-1] * n
    for i, h2 in enumerate(roll_hash(string, k)):
        if h2 == hash:
            left[i] = 0
            right[i + k - 1] = 0

    d = 2**60
    for i in range(n - 1, -1, -1):
        if left[i] == 0:
            d = 0
        left[i] = d
        d += 1

    d = 2**60
    for i in range(n):
        if right[i] == 0:
            d = 0
        right[i] = d
        d += 1

    turns = n - k
    i = 0
    j = n - 1
    t = 0
    for turns_left in range(turns, 0, -1):
        moves_left = (turns_left + 1) // 2
        if t == 0:
            if left[i] < moves_left:
                i += 1
            else:
                j -= 1
        else:
            if left[i] >= moves_left:
                i += 1
            else:
                j -= 1
        t = (t + 1) % 2
    print("Alice" if left[i] == right[j] == 0 else "Bob")
