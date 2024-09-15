import sys; input=sys.stdin.readline
n, m = map(int, input().split())

W = sorted((int(x) for x in input().split()))
F = sorted((tuple(map(int, input().split())) for _ in range(m)), key=lambda x: x[1])
s = 0
while W and F:
    x, p = F.pop()
    for _ in range(min(x, len(W))):
        s += p*W.pop()
print(s)