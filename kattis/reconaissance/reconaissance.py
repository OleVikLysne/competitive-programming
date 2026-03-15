n = int(input())
cars = []
for _ in range(n):
    a, b = [int(x) for x in input().split()]
    cars.append((a, b))


def get_pos(car, t):
    return car[0]+(car[1]*t)


def dist(t):
    min_pos = min(get_pos(car, t) for car in cars)
    max_pos = max(get_pos(car, t) for car in cars)
    return max_pos - min_pos


upper_bound = 200000
lower_bound = 0
epsilon = 1e-4
while True:
    mid = (upper_bound + lower_bound)/2
    if abs(dist(upper_bound)-dist(lower_bound)) < 1e-4:
        print(dist(mid))
        break
    if dist(mid) < dist(mid+epsilon):
        upper_bound = mid
    else:
        lower_bound = mid