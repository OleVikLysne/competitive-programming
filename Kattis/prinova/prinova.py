n = int(input())
boys = sorted(int(x) for x in input().split())
a, b = map(int, input().split())
maxi = 0
best = None
if a % 2 == 0:
    a += 1
if b % 2 == 0:
    b -= 1
for i in range(n - 1):
    diff = boys[i + 1] - boys[i]
    add = diff // 2
    if add % 2 == 0:
        add += 1
    temp = boys[i] + add
    if temp < a:
        add -= a - temp
        temp += a - temp
    if temp > b:
        add -= temp - b
        temp -= temp - b
    if a <= temp <= b:
        if add > maxi:
            maxi = add
            best = boys[i] + add


if boys[0] - a > maxi:
    maxi = boys[0] - a
    best = a
if b - boys[-1] > maxi:
    maxi = b - boys[-1]
    best = b

print(best)
