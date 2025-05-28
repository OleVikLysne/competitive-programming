B = 2**31 - 1 # 2**61-1 # 10**9+7 # 2987583780930787 # 100123456789
A = 31

MAX = 1_000_000
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


