import sys

s = 0

def unsafe(arr, i, j, ord):
    if j >= len(arr):
        return False
    return arr[i] == arr[j] or (arr[i] < arr[j]) != ord or abs(arr[i]-arr[j]) > 3


s = 0
for line in sys.stdin:
    arr = [int(x) for x in line.split()]
    if len(arr) == 1:
        s += 1
        continue
    ord = arr[0] < arr[1]
    dummy = False
    i = 0
    while i < len(arr)-1:
        if unsafe(arr, i, i+1, ord):
            if dummy:
                break
            dummy = True
            a, b = unsafe(arr, i, i+2, ord),  unsafe(arr, i+1, i+2, ord)
            if a and b:
                break
            if not a:
                i += 1
        i += 1
    else:
        s += 1
                
print(s)