import sys

input = sys.stdin.readline

n = int(input())
b, s = map(int, input().split())
if b < s:
    b, s = s, b
total = 0
min_balls, extra_balls = divmod(b + s, n)
if s < min_balls:
    total += min_balls - s
    s = min_balls
if b > min_balls:
    extra_balls -= 1
if s > min_balls:
    extra_balls -= 1
extra_balls = max(0, extra_balls)
total += min_balls * (n - 2) + extra_balls
print(total)