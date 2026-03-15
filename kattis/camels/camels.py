import sys; input = sys.stdin.readline


def merge_sort(arr, l, r):
    if l >= r:
        return 0
    count = 0
    mid = (l + r) // 2
    count += merge_sort(arr, l, mid)
    count += merge_sort(arr, mid + 1, r)

    i, j, k = l, mid + 1, l + n
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            arr[k] = arr[i]
            i += 1
        else:
            arr[k] = arr[j]
            count += mid - i + 1
            j += 1
        k += 1

    while i <= mid:
        arr[k] = arr[i]
        k += 1
        i += 1

    while j <= r:
        arr[k] = arr[j]
        k += 1
        j += 1

    for x in range(l, r + 1):
        arr[x] = arr[x + n]
    return count


n = int(input())
jaap = [int(x) - 1 for x in input().split()]
jan = [int(x) - 1 for x in input().split()]
thijs = [int(x) - 1 for x in input().split()]
jaap_map = [0] * n
jan_map = [0] * n
for i, e in enumerate(jaap):
    jaap_map[e] = i
for i, e in enumerate(jan):
    jan_map[e] = i

count = 0
for x, y in ((jaap_map, jan), (jaap_map, thijs), (jan_map, thijs)):
    l = [x[i] for i in y] + [0] * n
    count += merge_sort(l, 0, n - 1)
print((n * (n - 1) // 2 - count // 2))
