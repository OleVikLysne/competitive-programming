n, m = map(int, input().split())
l = [{x for x in range(1, n+1)}]
for _ in range(m):
    x = input().split()
    a = {int(x[i]) for i in range(n//2)}
    b = {int(x[i]) for i in range(n//2, n)}
    new_l = []
    for m in (a, b):
        for z in l:
            y = z.intersection(m)
            if len(y) > 1:
                new_l.append(y)
    l = new_l
    if not l:
        print("YES")
        exit()
print("NO")
