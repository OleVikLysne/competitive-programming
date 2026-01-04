t = int(input())
for _ in range(t):
    n = int(input())-1
    print((8*pow(9, n, 1_000_000_007)) % 1_000_000_007)