n = int(input())
l = [int(input()) for _ in range(n)]
if n % 2 == 0:
    if any(x % 2 == 1 for x in l):
        print("Ja")
    else:
        print("Nej")
else:
    if any(x % 2 == 0 for x in l):
        print("Ja")
    else:
        print("Nej")