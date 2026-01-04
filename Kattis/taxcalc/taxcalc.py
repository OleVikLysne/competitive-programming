seq = input().split()
m = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y, 
    "/": lambda x, y: x // y
}

def solve(i):
    if seq[i] != "(":
        return int(seq[i]), i + 1
    op = m[seq[i + 1]]
    k = i + 2
    res, k = solve(k)
    while seq[k] != ")":
        x, k = solve(k)
        res = op(res, x)
    return res, k + 1

print(solve(0)[0])
