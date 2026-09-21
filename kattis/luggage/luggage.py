n, l = map(int, input().split())
arr = list(map(float, input().split()))
v = 10
b = True
while b:
    b = False
    for i in range(n):
        x = arr[i]
        for j in range(i):
            y = arr[j]
            d = abs(x-y)
            z = 2 - (d / v + 1) % l
            if z > 0:
                v = (d*v) / (d+z*v)
                if v < 0.1:
                    print("no fika")
                    exit()
                b = True
print(v)