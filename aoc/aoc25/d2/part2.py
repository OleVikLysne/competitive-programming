s = 0
for x in next(open(0)).split(","):
    a, b = x.split("-")
    for n in range(int(a), int(b)+1):
        n = str(n)
        for step in range(1, len(n)//2+1):
            x = set(n[i:i+step] for i in range(0, len(n), step))
            if len(x) == 1:
                s += int(n)
                break
print(s)