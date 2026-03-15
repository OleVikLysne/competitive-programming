import sys; input=sys.stdin.readline

n, s = map(int, input().split())

m = {
    "2": "2",
    "5": "5",
    "8": "8",
    "1": "1",
    "0": "0",
    "9": "6",
    "6": "9"
}

l = []
def try_rev(string):
    z = []
    for num in reversed(string):
        x = m.get(num)
        if x is None:
            return
        z.append(x)
    return int("".join(x for x in z))

for i, c in enumerate(input().split()):
    y = int(c)
    l.append((y, i))
    if (x := try_rev(c)) is not None and x != y:
        l.append((x, i))

l.sort(key=lambda x: x[0])
i = 0
j = 1
while i < len(l)-1:
    sum = l[i][0] + l[j][0]
    if sum < s or l[i][1] == l[j][1]:
        if j == len(l)-1:
            i += 1
        else:
            j += 1
        continue
    if sum == s:
        print("YES")
        exit()
    i += 1
    while l[i][0]+l[j][0] > s and i != j:
        j -= 1
    if i == j:
        break
print("NO")
