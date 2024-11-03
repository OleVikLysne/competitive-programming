seq = [char for char in input()]
m = {
    "[": "]",
    "<": ">",
    "{": "}",
    "(": ")",
}
rev_m = {v: k for k, v in m.items()}

def score(i, j):
    if (j-i) % 2 == 0:
        return 0
    c1, c2 = seq[i], seq[j]
    if c1 == c2 == "?":
        return 4
    if (c1 == "?" and c2 in rev_m) or (c1 in m and c2 == "?") or (m.get(c1) == c2):
        return 1
    return 0

mem = [[-1]*21 for _ in range(21)]
def search(i, n):
    if n-i <= 0:
        return 1
    if mem[i][n] != -1:
        return mem[i][n]
    res = 0
    for j in range(i+1, n, 2):
        s = score(i, j)
        if s:
            if (s2 := search(i+1, j)):
                res += s * s2 * search(j+1, n)
    mem[i][n] = res
    return res
print(search(0, len(seq)))