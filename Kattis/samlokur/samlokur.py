from sys import stdin

def no():
    print("Neibb")
    exit()
    
def yes():
    print("Jebb")
    exit()
    
def due(i):
    if i >= n:
        no()
    return qd[i][1]

def quality(i):
    if i >= n:
        no()
    return qd[i][0]
    
def visited(i):
    if i >= n:
        no()
    return v[i]

def next_possible(i):
    j = i + 1
    while visited(j):
        j += 1
    return j

n, k = map(int, stdin.readline().split())
q = map(int, stdin.readline().split())
d = map(int, stdin.readline().split())
qd = [(a, b) for a, b in zip(q, d) if a >= 4]
qd.sort(key = lambda x: x[1])

n = len(qd)

v = [False]*n
j = -1
for i in range(k):
    j = next_possible(j)
    while due(j) - i <= 0:
        j = next_possible(j)
    v[j] = True
    x = next_possible(j)
    while quality(x) + quality(j) < 9:
        x = next_possible(x)
    v[x] = True
yes()