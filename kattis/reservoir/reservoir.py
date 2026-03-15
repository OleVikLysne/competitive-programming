import sys; input=sys.stdin.readline
import bisect

for _ in range(int(input())):
    n = int(input())
    pos = [-1] + [int(x) for x in input().split()]
    height = [10**6] + [int(x) for x in input().split()]
    SUB = height[:]

    res = [0]*(n+1)
    stack = [0]
    for i in range(1, n+1):
        h = height[i]
        sub = 0
        while height[stack[-1]] < h:
            j = stack.pop()
            sub += SUB[j]
            SUB[i] += SUB[j]

        tot = res[stack[-1]] + h * (pos[i]-pos[stack[-1]]-1) - sub
        res[i] = tot
        stack.append(i)

    res[0] = -1
    q = int(input())
    for _ in range(q):
        w = int(input())
        sys.stdout.write(f"{bisect.bisect_left(res, w)-1} ")
