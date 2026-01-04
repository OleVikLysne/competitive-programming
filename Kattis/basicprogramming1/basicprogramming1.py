from sys import stdin

n, t = map(int, stdin.readline().split())
A = [int(x) for x in stdin.readline().split()]

if t == 1:
    print(7)

elif t == 2:
    if A[0] == A[1]:
        print("Equal")
    elif A[0] > A[1]:
        print("Bigger")
    else:
        print("Smaller")

elif t == 3:
    l = sorted(A[:3])
    print(l[1])

elif t == 4:
    print(sum(A))

elif t == 5:
    l = [x for x in A if x % 2 == 0]
    print(sum(l))

elif t == 6:
    l = [chr((x%26) + 97) for x in A]
    print("".join(str(x) for x in l))

elif t == 7:
    visited = set()
    i = 0
    while True:
        if i in visited:
            print("Cyclic")
            break
        if i >= len(A):
            print("Out")
            break
        if i == len(A)-1:
            print("Done")
            break

        visited.add(i)
        i = A[i]