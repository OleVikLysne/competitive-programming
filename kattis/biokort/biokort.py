import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
popularity = [int(input().split()[1]) for _ in range(n)]
popularity.sort()


prefix_sum = {0: 0}
counter = {0: 0}
s = 0
for i, x in enumerate(popularity, 1):
    s += x
    prefix_sum[x] = s
    counter[x] = i
maxi = prefix_sum[popularity[-1]]


def evaluate(pop):
    amount_single = maxi - (prefix_sum[pop] + (n - counter[pop]) * pop)
    return pop * k + amount_single * m


best = float("inf")
j = -1
for x in counter:
    res = evaluate(x)
    if res < best:
        best = res
        j = x

print(j, best)
