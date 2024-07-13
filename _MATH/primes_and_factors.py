
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