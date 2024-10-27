
B = 2**31-1 # 2**61-1 # 10**9+7
A = 31

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