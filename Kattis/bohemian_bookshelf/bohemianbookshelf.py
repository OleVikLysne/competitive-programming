import sys; input=sys.stdin.readline

N, HEIGHT, WIDTH = map(int, input().split())

H = []
W = []
for _ in range(N):
    h, w = map(int, input().split())
    H.append(h)
    W.append(w)


def out(upright, stacked):
    u = [i+1 for i in range(N) if upright & 1 << i]
    s = [i for i in range(N) if stacked & 1 << i]
    s.sort(key=H.__getitem__, reverse=True)
    s = [i+1 for i in s]
    print("upright", *u)
    print("stacked", *s)
    exit()

def impos():
    print("impossible")
    exit()


def knapsack(maxH):
    maxi = HEIGHT
    knap = [0]*(maxi+1)
    if must_stack:
        knap[stack_height] = must_stack
    else:
        for j in range(N):
            if H[j] <= maxH and W[j] <= maxi:
                knap[W[j]] = 1 << j

    for j in range(N):
        if H[j] > maxH:
            continue
        for k in range(maxi-W[j], -1, -1):
            if knap[k] and not knap[k] & (1 << j):
                knap[k+W[j]] = knap[k] | (1 << j)

    for k in range(maxi, -1, -1):
        if knap[k]:
            return knap[k]
    return 0


must_stack = 0
stack_height = 0
min_stack_width = 0
for i in range(N):
    if H[i] > HEIGHT or W[i] > WIDTH:
        must_stack |= 1 << i
        stack_height += W[i]
        min_stack_width = max(min_stack_width, H[i])

if stack_height > HEIGHT:
    impos()

def solve(maxH):
    stacked = knapsack(maxH)
    if not stacked:
        return
    
    upright = ((1 << N) - 1) ^ stacked
    if not upright:
        j = -1
        for i in range(N):
            if W[i] > WIDTH or H[i] > HEIGHT:
                continue
            if j == -1 or W[i] < W[j]:
                j = i
        stacked ^= 1 << j
        upright |= 1 << j

    w = 0
    for i in range(N):
        if upright & 1 << i:
            w += W[i]
    if w + maxH > WIDTH:
        return
    out(upright, stacked)


for maxH in H:
    if maxH < min_stack_width: continue
    solve(maxH)
impos()