while(n := int(input())) != 0:
    c = 100000
    reverse = 0
    for _ in range(n):
        x=float(input())
        y = 1 / x
        c, reverse = int(max(c, reverse*x*0.97)), int(max(reverse, y*0.97*c))
    print("{:.2f}".format(c/100))