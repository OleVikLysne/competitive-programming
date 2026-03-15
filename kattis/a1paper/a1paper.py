n = int(input())
arr = [0] + [int(x) for x in input().split()]

res = 0
while arr[0] != 1:
    s = 2**(-3/4)
    p = 0
    for i in range(1, n):
        if arr[i] >= 2**(i-p):
            for j in range(i-p-1, -1, -1):
                res += 2**j * s
                s *= 2**(0.5)
            arr[p] += 1
            arr[i] -= 2**(i-p)
            break
        s /= 2**(0.5)
        if arr[i] != 0:
            p = i
    else:
        print("impossible")
        break
else:
    print(res)
