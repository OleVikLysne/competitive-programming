h, w = map(int, input().split())
arr = [int(x) for x in input().split()]

def eval(mid):
    air = 0
    water = 0
    for x in arr:
        water_level = max(0, mid-x)
        water += water_level
        air += h-water_level-x
    return air, water


lower, upper = 0, h
while lower+1 < upper:
    mid = (lower+upper)//2
    air, water = eval(mid)
    if water-air > 0:
        upper = mid
    else:
        lower = mid

air, water = eval(lower)
if lower+1 <= h:
    air1, water1 = eval(lower+1)
    lower0 = water-air
    lower1 = water1-air1
    if abs(lower1) < abs(lower0):
        lower += 1
        water = water1
        air = air1

if lower-1 >= 0:
    air1, water1 = eval(lower-1)
    lower0 = water-air
    lower1 = water1-air1
    if abs(lower1) <= abs(lower0):
        lower -= 1
        water = water1
        air = air1

print(lower, water)