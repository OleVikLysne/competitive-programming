import sys; input=sys.stdin.readline
n, m =map(int, input().split())
instruments = []
for _ in range(n):
    instruments.append(set(int(x) for x in input().split()[1:]))
notes = [int(x) for x in input().split()]
candidates = set(range(n))
s = 0
i = 0
while i < m:
    note = notes[i]
    for cand in candidates.copy():
        if note not in instruments[cand]:
            candidates.discard(cand)
    if not candidates:
        s += 1
        candidates = set(range(n))
        continue
    i += 1
print(s)