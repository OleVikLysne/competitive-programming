from sys import stdin, stdout

def overlap(c1, c2):
    x1,y1,r1 = c1
    x2,y2,r2 = c2
    return (x1-x2)**2 + (y1-y2)**2 < (r1+r2)**2

def path_blocked(k):
    visited=set()
    for c in boundary_circles:
        if c>=k: break
        x,_,r = circles[c]
        if x+r > 200 or _path_blocked(c, k, visited):
            return True
    return False

def _path_blocked(src, k, visited):
    visited.add(src)
    for c in G[src]:
        if c >= k: break
        if c in visited: continue
        x,_,r = circles[c]
        if x+r>200 or _path_blocked(c, k, visited):
            return True
    return False


N = int(stdin.readline())
boundary_circles = []
circles = []
for i in range(N):
    x,y,r = tuple(int(x) for x in stdin.readline().split())
    if x-r<0:
        boundary_circles.append(i)
    circles.append((x,y,r))

G = [[] for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        if overlap(circles[i], circles[j]):
            G[i].append(j)
            G[j].append(i)


# binary search
lower, upper, mid = 0, N, N//2
while lower!=mid:
    if path_blocked(mid):
        upper=mid
    else:
        lower=mid
    mid = (lower+upper)//2
stdout.write(str(mid))