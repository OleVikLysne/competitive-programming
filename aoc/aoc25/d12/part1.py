import sys

for _ in range(30):
    next(sys.stdin)
tot = 0
for line in sys.stdin:
    dim, *arr = line.split()
    r, c = map(int, dim.rstrip(":").split("x"))
    arr = list(map(int, arr))
    if sum(arr) <= r*c // 9:
        tot += 1
print(tot)



