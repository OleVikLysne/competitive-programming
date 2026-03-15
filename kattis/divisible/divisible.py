import sys; input = sys.stdin.readline


for _ in range(int(input())):
    d, n = map(int, input().split())
    sequence = [int(x) for x in input().split()]
    prefix_sum = [0]*n
    prefix_sum[0] = sequence[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + sequence[i]
    mask = [0]*d
    mask[0] = 1
    res = 0
    for i in range(n):
        res += mask[prefix_sum[i]%d]
        mask[prefix_sum[i]%d] += 1
    print(res)