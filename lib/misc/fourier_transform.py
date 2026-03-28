from math import pi, cos, sin

def fft(coef, inverse):
    n = len(coef)
    if n == 1:
        return coef
    a_coef = coef[::2]
    b_coef = coef[1::2]
    a_fft = fft(a_coef, inverse)
    b_fft = fft(b_coef, inverse)
    angle = 2*pi/n 
    if inverse:
        angle = -angle

    w = complex(cos(angle), sin(angle))
    wj = complex(1, 0)
    res = [complex(0, 0)]*n
    for j in range(n//2):
        res[j] = a_fft[j] + wj*b_fft[j]
        res[j+n//2] = a_fft[j] - wj*b_fft[j]
        wj *= w
    return res

def multiply(p1, p2):
    n = len(p1)
    transform = fft(p1, False)
    for i, x in enumerate(fft(p2, False)):
        transform[i] *= x
    return [round(x.real/n) for x in fft(transform, True)]