n = int(input())
people = []
for _ in range(n):
    a, b = input().split()
    b = int(b)
    people.append((a, b))
people.sort(key=lambda x: x[1])


def binary_search(val):
    lower, upper = 0, n
    while lower + 1 < upper:
        mid = (lower + upper) // 2
        if people[mid][1] <= val:
            lower = mid
        else:
            upper = mid
    return lower


q = int(input())
for _ in range(q):
    i = int(input())
    idx = binary_search(i)
    if people[idx][1] > i:
        print(":(")
    else:
        print(people[idx][0])