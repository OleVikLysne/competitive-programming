from math import cosh, sinh
d, s = [int(x) for x in input().split()]

def f(a):
    return a*cosh((d)/(2*a))-a

def l(a, d):
    return (2*a)*sinh(d/(2*a))

lower = 0
upper = 2**30
epsilon = 1e-5
while True:
    mid = (lower+upper)/2
    if abs(f(mid)-s) <= epsilon:
        break
        
    diff = f(mid)
    if diff < s:
        upper = mid
    else:
        lower = mid
        
print(l(mid, d))