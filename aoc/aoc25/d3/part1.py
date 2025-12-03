import sys

s = 0
for line in sys.stdin:
    seq = [int(x) for x in line.rstrip()]
    a = max(seq[:-1])
    i = seq.index(a)
    b = max(seq[i+1:])
    s += 10*a+b
print(s)