n = int(input())
arr = [int(x) for x in input().split()]
sorted_arr = sorted(arr)
q = int(input())
mapping = {x : i for i, x in enumerate(sorted_arr)}
q_target = mapping[q]
i = 0
while arr[q_target] != q:
    x = arr[i]
    j = mapping[x]
    if i == j:
        i += 1
        continue
    arr[i], arr[j] = arr[j], arr[i]
print(*arr)