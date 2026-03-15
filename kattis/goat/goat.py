import math
x, y, x1, y1, x2, y2 = [int(x) for x in input().split()]

def dist(x,y,x1,y1):
    return math.sqrt( (x-x1)**2 + (y-y1)**2 )

if x <= x1:
    if y <= y1: # bottom left of house
        print(dist(x,y,x1,y1))
    elif y1 <= y <= y2: # left of house
        print(x1-x)
    else: # top left of house
        print(dist(x,y,x1,y2))
elif x1 <= x <= x2:
    if y <= y1: # bottom of house
        print(y1-y)
    else: # top of house
        print(y-y2)

else:
    if y <= y1: # bottom right of house
        print(dist(x,y,x2,y1))
    elif y1 <= y <= y2: # right of house
        print(x-x2)
    else: #top right of house
        print(dist(x,y,x2,y2))