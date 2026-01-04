import sys; input=sys.stdin.readline

B =  2**31-1
A = 31

def get_pfs(string):
    n = len(string)
    pfs = [0]*(n+1)
    for i in range(n):
        pfs[i+1] = (pfs[i] + string[i] * pow(A, n - i - 1, B)) % B
    return pfs

def find_idx(pfs, n, k, m):
    occ = {}
    idx = -1
    a = 1
    for i in range(n-k+1):
        hash = ((pfs[i+k] - pfs[i]) * a) % B
        v = occ.get(hash, 0) + 1
        if v >= m:
            idx = i
        occ[hash] = v
        a = (a * A) % B
    return idx


def solve(string, m):
    n = len(string)
    pfs = get_pfs(string)
    l, r = 1, n+1
    while l + 1 < r:
        mid = (l+r)//2
        idx = find_idx(pfs, n, mid, m)
        if idx != -1:
            l = mid
        else:
            r = mid
    idx = find_idx(pfs, n, l, m)
    if idx != -1:
        return f"{l} {idx}"
    return "none"


while (m := int(input())) != 0:
    string = [ord(x) for x in input().rstrip()]
    print(solve(string, m))
