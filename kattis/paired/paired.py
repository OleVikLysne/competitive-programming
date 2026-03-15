n = int(input())
arr = [int(x) for x in input().split()]

occ = [0]*(10**5+1)
stack = []
j = 0
for i in range(n):
    x = arr[i]
    occ[x] += 1
    if occ[x] == 3:
        stack.append((j, i))
        while arr[j] != x:
            occ[arr[j]] -= 1
            j += 1
        j += 1
        occ[x] -= 1
stack.append((j, n))

longest = 0
while stack:
    j, n = stack.pop()
    if (n-j) - ((n-j) % 2) <= longest:
        continue
    occ = {}
    once = 0
    for i in range(j, n):
        x = arr[i]
        count = occ.get(x, 0) + 1
        occ[x] = count
        if count == 1:
            once += 1
        elif count == 2:
            once -= 1

    if once == 0:
        longest = max(longest, n-j)
        continue

    k = j
    for i in range(j, n):
        if occ[arr[i]] == 1:
            stack.append((k, i))
            k = i + 1
    stack.append((k, n))

print(longest)