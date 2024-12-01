import sys
a, b = [], []
for line in sys.stdin:
    x, y = map(int, line.split())
    a.append(x)
    b.append(y)
a.sort()
b.sort()
s = 0
for i in range(len(a)):
    s += abs(a[i]-b[i])
print(s)