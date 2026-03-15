from sys import stdin, stdout
from collections import defaultdict


def sieve(n):
    n += 1
    prime = [True]*n
    prime[0] = prime[1] = False
    l = []
    for i in range(2, n):
        if not prime[i]:
            continue
        l.append(i)
        for j in range(i*2, n, i):
            prime[j] = False
    return l


def binary_search(l, val):
    lower, upper = 0, len(l)
    while lower < upper:
        mid = (lower+upper)//2
        if l[mid] == val:
            return mid
        if l[mid] < val:
            lower = mid
        else:
            upper = mid


def factorize(n):
    factors = []
    for p in primes:
        if p**2 > n:
            break

        if n % p == 0:
            factors.append(p)
            while n % p == 0:
                n //= p
    if n > 1:
        factors.append(n)
    return factors


def search():
    parent = [-1]*n
    stack = [(0, n-1, -1)]
    while stack:
        l, r, prev = stack.pop()
        if l >= r:
            if l == r:
                parent[l] = prev
            continue

        for i in range(r+1-l):
            if i % 2 == 0:
                i = l + (i//2)
            else:
                i = r - (i//2)
            
            lb, rb = bounds[i]
            if lb < l and rb > r:
                parent[i] = prev
                stack.append((l, i-1, i))
                stack.append((i+1, r, i))
                break
        else:
            return False
    return parent


def compute_bounds():
    bounds = []
    for i in range(n):
        lb, rb = -1, n
        factors = node_to_factors[i]
        for fact in factors:
            l = factor_to_nodes[fact]
            idx = binary_search(l, i)

            if idx > 0:
                lb = max(lb, l[idx-1])
            if idx < len(l)-1:
                rb = min(rb, l[idx+1])

        bounds.append((lb, rb))
    return bounds




primes = sieve(3163) # ceil(sqrt(10**7))
n = int(stdin.readline())
node_to_factors = [factorize(x) for x in map(int, stdin.readline().split())]
factor_to_nodes = defaultdict(list)
for i, factors in enumerate(node_to_factors):
    for fact in factors:
        factor_to_nodes[fact].append(i)



bounds = compute_bounds()
parent = search()
if parent:
    stdout.write(" ".join(str(x+1) for x in parent))
else:
    stdout.write("impossible")