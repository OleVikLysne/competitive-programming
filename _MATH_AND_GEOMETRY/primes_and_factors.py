import math


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


def factorize(number, primes):
    factors = []
    for p in primes:
        if p**2 > number:
            break

        if number % p == 0:
            factors.append(p)
            while number % p == 0:
                number //= p
    if number > 1:
        factors.append(number)
    return factors


import random
def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    for _ in range(100):
        a = random.randint(2, n-2)
        if pow(a, n-1, n) != 1:
            return False
    return True


def chinese_remainder(mod_pairs: tuple[int, int]):
    total = 0
    prod = math.prod(x[1] for x in mod_pairs)
    for a, m in mod_pairs:
        p = prod // m
        total += a * mul_inv(p, m) * p
    return total % prod

def mul_inv(a, b):
    if b == 1: 
        return 1
    b0 = b
    x0, x1 = 0, 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1