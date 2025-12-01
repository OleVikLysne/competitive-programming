import sys
from collections import Counter
a, b = [], []
for line in sys.stdin:
    x, y = map(int, line.split())
    a.append(x)
    b.append(y)

c = Counter(b)
s = 0
for x in a:
    s += c.get(x, 0)*x
print(s)