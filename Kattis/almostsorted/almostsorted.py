n = int(input())
arr = [int(x) for x in input().split()]
q = int(input())
m = {x : i for i, x in enumerate(sorted(arr))}
k = m[q]
i = 0
while arr[k] != q:
    j = m[arr[i]]
    if i == j:
        i += 1
        continue
    arr[i], arr[j] = arr[j], arr[i]
print(*arr)