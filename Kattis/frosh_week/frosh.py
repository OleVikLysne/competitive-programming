from sys import stdin, stdout
n = int(stdin.readline())
s = [int(stdin.readline()) for _ in range(n)] + [0]*n
def merge_sort(arr, l, r):
    if l>=r: return 0
    count = 0
    mid = (l+r)//2
    count += merge_sort(arr, l, mid)
    count += merge_sort(arr, mid+1, r)

    i, j, k = l, mid+1, l+n
    while i<=mid and j<=r:
        if arr[i] <= arr[j]:
            arr[k] = arr[i]
            i+=1
        else:
            arr[k] = arr[j]
            count += mid-i+1
            j+=1
        k+=1

    while i<=mid:
        arr[k] = arr[i]
        k+=1
        i+=1

    while j<=r:
        arr[k] = arr[j]
        k+=1
        j+=1

    for x in range(l, r+1):
        arr[x] = arr[x+n]
    return count

stdout.write(str(merge_sort(s, 0, n-1)))