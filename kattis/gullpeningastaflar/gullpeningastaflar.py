n = int(input())
k = n + 1
print("? " + " ".join(str(x) for x in range(1, k)))
weight = int(input())
base_sum = n * k * (k - 1) // 2
print(f"! {weight-base_sum}")
