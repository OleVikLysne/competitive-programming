n = int(input())
l = [int(x) for x in input().split()]
lstr = [str(x) for x in l]

def max_mod(s):
    return int("9"+s[1:])
def min_mod(s):
    if len(s) == 1:
        return 0
    return int("1"+s[1:])

def out(i, s):
    l[i] = s
    print(*l)
    exit()

for i in range(n):
    if i > 0 and (m:=min_mod(lstr[i])) < l[i-1]:
        out(i, m)
    
    if i < n-1 and (m:=max_mod(lstr[i])) > l[i+1]:
        out(i, m)

print("impossible")