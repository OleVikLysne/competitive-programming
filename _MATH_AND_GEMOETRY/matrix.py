def mat_mul(A, B, mod: int | None = None):
    if len(A[0]) != len(B):
        return None # invalid matrix multiplication
    rows, cols = len(A), len(B[0])
    C = [[0]*cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if mod is None:
                C[i][j] = sum(A[i][k]*B[k][j] for k in range(len(B)))
            else:
                C[i][j] = sum((A[i][k]*B[k][j]) % mod for k in range(len(B))) % mod
                
    return C

def mat_pow(A, power: int, mod: int | None = None):
    rows, cols = len(A), len(A[0])
    if rows != cols:
        return None # cant do fast matrix exponentiation
    res = [[0]*cols for _ in range(rows)]
    for i in range(rows):
        res[i][i] = 1
    
    while power:
        if power & 1:
            res = mat_mul(res, A, mod=mod)
        A = mat_mul(A, A, mod=mod)
        power >>= 1
    return res
            
def fib(n, mod: int | None = None):
    if n < 2:
        return n
    A = [[1, 1], [1, 0]]
    res = mat_pow(A, n-1, mod=mod)
    return res[0][0]