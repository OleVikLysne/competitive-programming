n = int(input())
print(n)
m = n % 3
if n > 3:
    if m > 0:
        n += 3 - m
    print(n // 3)
else:
    print(1)