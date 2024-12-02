import sys

s = 0
for line in sys.stdin:
    arr = [int(x) for x in line.split()]
    if len(arr) == 1:
        s += 1
        continue
    ord = arr[0] < arr[1]
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1] or (arr[i] < arr[i+1]) != ord or abs(arr[i]-arr[i+1]) > 3:
            break
    else:
        s += 1
print(s)