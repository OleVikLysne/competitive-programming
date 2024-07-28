n, q = map(int, input().split())
l = []
for _ in range(n):
    a, b = input().split()
    a = a.rstrip(",")
    l.append((b, a))
l.sort()
m = {x[1]: i for i, x in enumerate(l, 1)}
for _ in range(q):
    print(m.get(input(), -1))
