s = 0
for x in next(open(0)).split(","):
    a, b = x.split("-")
    for n in range(int(a), int(b)+1):
        n = str(n)
        if n[:len(n)//2] == n[len(n)//2:]:
            s += int(n)
print(s)