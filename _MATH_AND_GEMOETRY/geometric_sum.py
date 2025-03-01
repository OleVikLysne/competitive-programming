def geometric_sum_mod_m(a, n, m):
    """
    Computes the sum (1 + a + a^2 + ... + a^n) % m
    """
    n += 1
    t = 1
    res = 0
    while n:
        if n & 1:
            res = (res * a + t) % m
        t *= (a+1)
        t %= m
        a *= a
        a %= m
        n >>= 1
    return res