from collections import deque


h = 10**6


def ver1(h):
    q = deque([(1, 0)])
    best = [-1]*(h+1)
    best[0] = 0
    l = h
    while q and l > 0:
        c, n = q.popleft()
        if c > h:
            break
        for k in (n-c, n+c):
            if 0 <= k <= h:
                if best[k] == -1:
                    best[k] = c
                    l -= 1
            if k < -c:
                continue
            if k >= h-c:
                continue
            if c+1 > h:
                continue
            q.append((c+1, k))
    return best

def ver2(h):
    q = deque([(1, 0)])
    best2 = [-1]*(h+1)
    best2[0] = 0
    l = h
    while q and l > 0:
        c, n = q.popleft()
        y = n + c
        k = c
        while y <= h:
            if best2[y] == -1:
                l -= 1
                best2[y] = k
            k += 1
            y += k

        y = n - c
        k = c
        while y > 0:
            if best2[y] == -1:
                l -= 1
                best2[y] = k
            k += 1
            y -= k

        if c+1 > h:
            continue
        if n-c >= -c:
            q.append((c+1, n-c))
        if n+c < h+c:
            q.append((c+1,n+c))
    return best2


def min_moves_to_reach_N(N):
    N = abs(N)  # We'll work with positive N for simplicity
    if N == 0:
        return 0
    k = 0
    sum_k = 0
    
    while True:
        k += 1
        sum_k += k
        
        if sum_k >= N and (sum_k - N) % 2 == 0:
            return k
    


print(min_moves_to_reach_N(10**6))

# Example Usage
#arr = [min_moves_to_reach_N(x) for x in range(h+1)]
#arr = find_min_moves_up_to_K(h)
#print(arr)
#print(ver2(h))


