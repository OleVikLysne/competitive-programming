B = 2**31 - 1 # 2**61-1 # 10**9+7 # 2987583780930787
A = 31

def roll_hash(string, k):
    n = len(string)
    hashed_str = 0
    l = []
    for i in range(k):
        hashed_str += string[i] * pow(A, k - i - 1, B)
        hashed_str %= B
    l.append(hashed_str)
    for i in range(k, n):
        hashed_str -= string[i - k] * pow(A, k - 1, B)
        hashed_str *= A
        hashed_str += string[i]
        hashed_str %= B
        l.append(hashed_str)
    return l


def rolling_hash(string):
    hashed_str = 0
    k = len(string)
    for i in range(k):
        hashed_str += string[i] * pow(A, k - i - 1, B)
        hashed_str %= B
    return hashed_str


def hash_substrings(string, hashed_str):
    k = len(string)
    for i in range(k):
        yield (hashed_str - string[i] * pow(A, k - i - 1, B)) % B
