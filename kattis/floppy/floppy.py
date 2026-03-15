import sys; input=sys.stdin.readline

for _ in range(int(input())):
    t, n = map(int, input().split())
    p = [1]*(t+1)
    for _ in range(n):
        s, e = map(int, input().split())
        x = e-s
        c = [0]*(t+1)
        for j in range(x, t+1):
            c[j-x] |= p[j]
        for j in range(t+1-x):
            c[j+x] |= p[j]
        p = c
    if 1 not in p:
        print("impossible")
        break
else:
    print("possible")