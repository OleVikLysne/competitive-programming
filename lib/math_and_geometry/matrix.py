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


def mat_add(A, B, mod: int | None = None):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return None # cant add matrices with dimension mismatch
    rows, cols = len(A), len(A[0])
    C = [[0]*cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            C[i][j] = A[i][j] + B[i][j]
            if mod is not None:
                C[i][j] %= mod
    return C

    
def fib(n, mod: int | None = None):
    A = [[1, 1], [1, 0]]
    res = mat_pow(A, n, mod=mod)
    return res[0][1]


def gaussian_elim(A, b):
    """
    Solve for the vector x that satisfies Ax = b
    """
    n = len(A)
    for i in range(n):
        A[i].append(b[i])

    for j in range(n):
        max_row = max(range(j, n), key = lambda i: abs(A[i][j]))
        A[j], A[max_row] = A[max_row], A[j]
        for i in range(j + 1, n):
            if A[j][j] != 0:
                c = -A[i][j] / A[j][j]
                A[i][j] = 0
                for k in range(j+1, n+1):
                    A[i][k] += c * A[j][k]

    multiple = False
    for i in range(n):
        if all(A[i][j] == 0 for j in range(n)):
            multiple = True
            if A[i][-1] != 0:
                return "inconsistent system"
    if multiple:
        return "multiple solutions"

    b = [A[i].pop() for i in range(n)]
    x = [0]*n
    for i in range(n - 1, -1, -1):
        x[i] = b[i] / A[i][i]
        for k in range(i - 1, -1, -1):
            b[k] -= A[k][i] * x[i]
    return x