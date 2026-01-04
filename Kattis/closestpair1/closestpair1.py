from sys import stdin, stdout
from math import ceil

def squared_dist(vec1, vec2):
    (x1, y1), (x2, y2) = vec1, vec2
    return (x1-x2)**2 + (y1-y2)**2


def brute_force(i, j):
    d = float("inf")
    for k in range(i, j-1):
        for l in range(k+1, j):
            vec1, vec2 = arr[k], arr[l]
            distance = squared_dist(vec1, vec2)
            if distance < d:
                d = distance
                closest_pair = (vec1, vec2)
    return (d, closest_pair)

def closest_pair(i, j):
    if j-i <= 3:
        return brute_force(i, j)
    mid = ceil((i+j)/2)
    l = closest_pair(i, mid+1)
    r = closest_pair(mid, j)
    if l[0] < r[0]:
        d = l[0]
        closest = l[1]
    else:
        d = r[0]
        closest = r[1]
    mid_x = arr[mid][0]

    strip = []
    
    for i in range(mid-1, j):
        e = arr[i]
        if (e[0]-mid_x)**2 >= d:
            break
        strip.append(e)
    
    for i in range(mid-2, i-1, -1):
        e = arr[i]
        if (e[0]-mid_x)**2 >= d:
            break
        strip.append(e)


    strip.sort(key=lambda x: x[1])
    for i in range(len(strip)-1):
        for j in range(i+1, min((i+8), len(strip))):
            if (strip[j][1] - strip[i][1])**2 >= d:
                break
            distance = squared_dist(strip[i], strip[j])
            if distance < d:
                d = distance
                closest = (strip[i], strip[j])
    return (d, closest)



def parse_inp(x):
    res = 0
    decimal_idx = 0
    for (i, c) in enumerate(reversed(x)):
        if c == ".":
            decimal_idx = i
            continue
    
        if c == "-":
            res = -res
        elif decimal_idx == 0:
            res += (ord(c)-48) * 10**i
        else:
            res += (ord(c)-48) * 10**(i-1)
    
    res *= 10**(2-decimal_idx)
    return res


while True:
    n = int(stdin.readline())
    if n == 0:
        break

    arr = [tuple(map(parse_inp, stdin.readline().split())) for _ in range(n)]
    arr.sort(key=lambda x: x[0])
    p1, p2 = closest_pair(0, len(arr))[1]
    x1, y1 = p1
    x2, y2 = p2
    stdout.write(f"{x1/100} {y1/100} {x2/100} {y2/100}\n")