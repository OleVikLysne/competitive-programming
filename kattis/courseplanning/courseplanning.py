import sys; input = sys.stdin.readline
n, k = map(int, input().split())
m = {}
vals = []
pairs = []
for _ in range(n):
    x, w = input().split()
    w = int(w)
    q = x[-1]
    if q.isnumeric():
        x = x[:-1]
        i = m.setdefault(x, len(m))
        if i == len(pairs):
            pairs.append([-1, -1])
        pairs[i][int(q) - 1] = w
    else:
        vals.append((w, -1))

for i in range(len(pairs)):
    w1, w2 = pairs[i]
    if w2 < w1:
        vals.append(((w1 + w2) // 2, i))
    else:
        vals.append((w1, -1))
        vals.append((w2, -1))

vals.sort(key=lambda x: x[0])
selected_vals = []
selected_pairs = []
c = 0
for w, i in vals:
    if c == k or c == k+2:
        break
    if i == -1:
        selected_vals.append(w)
        c += 1
    elif c < k:
        selected_pairs.append(i)
        c += 2

if c == k:
    tot = sum(selected_vals) + sum(sum(pairs[i]) for i in selected_pairs)
elif c == k + 1:
    w1, w2 = pairs[selected_pairs.pop()]
    s1 = selected_vals.pop()
    tot = sum(selected_vals) + sum(sum(pairs[i]) for i in selected_pairs) + min(w1 + w2, s1 + w1)
else:  # c = k+2
    w1, w2 = pairs[selected_pairs.pop()]
    s2 = selected_vals.pop()
    s1 = selected_vals.pop() if selected_vals else 0
    tot = sum(selected_vals) + sum(sum(pairs[i]) for i in selected_pairs) + min(w1 + w2, s1 + w1, s1 + s2)
print(tot)
