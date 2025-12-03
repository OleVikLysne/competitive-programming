import sys

s = 0
for line in sys.stdin:
    seq = [int(x) for x in line.rstrip()]
    for j in range(11, -1, -1):
        a = max(seq[:-j] if j != 0 else seq)
        i = seq.index(a)
        seq = seq[i+1:]
        s += 10**j*a
print(s)