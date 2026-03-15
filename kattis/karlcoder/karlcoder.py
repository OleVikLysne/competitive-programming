def query(i):
    print(f"buf[{i}]", flush=True)

i = 2
while True:
    query(i)
    if int(input()) == 0:
        break
    i *= 2

lower, upper = 2, i+1
tried = set()
while lower<upper:
    mid = (lower+upper)//2
    if mid in tried:
        lower += 1
        continue
    tried.add(mid)
    query(mid)
    if int(input()) == 0:
        upper = mid
    else:
        lower = mid
print(f"strlen(buf) = {lower}")