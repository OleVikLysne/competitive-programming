n = int(input())
hunters = [int(x) for x in input().split()]
hunters.sort()

def check(mid):
    s = 0
    for x in hunters:
        s += min(abs(x), abs(mid-x))
    return s

def solve(lower, upper):
    while lower < upper:
        mid = (lower+upper)//2
        if check(hunters[mid]) < check(hunters[mid+1]):
            upper = mid
        else:
            lower = mid + 1
    return check(hunters[lower])


for i in range(len(hunters)):
    if hunters[i] >= 0:
        res = min(solve(0, i), solve(i, n-1))
        break
else:
    res = solve(0, n-1)
print(res)
