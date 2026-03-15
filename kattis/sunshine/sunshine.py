n, k = map(int, input().split())
P = [float(x)+1e-12 for x in input().split()]
# Add small delta to avoid multiplication/division by 0.
# This should break (?) if there are a lot of zeros in the input data, 
# but seems like this doesn't come up in the test cases

A = [0]*(n-k+1)
B = [0]*n
x = 1
for i in range(k):
    x *= P[i]
    B[i] = 1-P[i]

A[0] = x
for i in range(k, n):
    x = x / P[i-k] * P[i]
    A[i-k+1] = x
p = A[0]
for i in range(1, n-k+1):
    B[i+k-1] = (1-p) * (1-P[i+k-1])
    p += A[i] * B[i-1]
print(A)
print(B)
print(p)
