n = int(input())
arr = [int(x) for x in input().split()]
dir = True
i = 0
j = 0
for k in range(n-1):
    if dir:
        if arr[k+1] < arr[k]:
            if j != 0:
                print("No")
                exit()
            dir = not dir
            i = k
    else:
        if arr[k+1] > arr[k]:
            dir = not dir
            j = k + 1
if arr[i] <= arr[j]:
    print("Yes")
else:
    print("No")
