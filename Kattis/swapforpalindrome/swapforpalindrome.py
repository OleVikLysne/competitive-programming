seq = [ord(c)-97 for c in input()]
n = len(seq)
seq.append(0)

def eval(size):
    found = [0]*26
    for i in range(size, n):
        found[seq[i]] += 1
    h = size // 2
    if size % 2 == 1:
        found[seq[h]] += 1

    for k in range(n-size+1):
        i = k
        j = i + size - 1
        l, r = [], []
        while i < j:
            if seq[i] != seq[j]:
                l.append(seq[i])
                r.append(seq[j])
            if len(l) > 2:
                break
            i += 1
            j -= 1
        if not l:
            return True
        elif len(l) == 1:
            if found[l[0]] or found[r[0]]:
                return True
        elif len(l) == 2:
            if  (l[0] == r[1] and l[1] == r[0]) or \
                (l[0] == l[1] and r[0] == r[1]):
                return True
        found[seq[k+size]] -= 1
        found[seq[k]] += 1
        if size % 2 == 1:
            found[seq[k+h]] -= 1
            found[seq[k+h+1]] += 1
    return False


res = 1

# even numbers
lo, hi = 1, (n+2)//2
while lo < hi:
    mi = (lo+hi)//2
    if eval(mi*2):
        lo = mi + 1
    else:
        hi = mi
res = max(res, lo*2-2)

# odd numbers
lo, hi = 1, (n+1)//2
while lo < hi:
    mi = (lo+hi)//2
    if eval(mi*2+1):
        lo = mi + 1
    else:
        hi = mi
res = max(res, lo*2-1)

print(res)