while True:
    a, b = map(int, input().split())
    if a == 0 == b: break
    x = {int(input()) for _ in range(a)}
    s = 0
    for _ in range(b):
        if int(input()) in x:
            s+=1
    print(s)