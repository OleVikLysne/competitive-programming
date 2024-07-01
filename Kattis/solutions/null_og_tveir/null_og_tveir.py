mask = [int(x) for x in input()]

s = 2**(len(mask)-1)
if mask[0] >= 2:
    s += 1
elif mask[0] < 2:
    print(s)
    exit()

found = True if mask[0] > 2 else False
for i in range(1, len(mask)):
    j = len(mask) - i - 1
    if found:
        s += 2**j
        continue
    if mask[i] > 2:
        found = True
        s += 2**j
    elif mask[i] == 2:
        s += 2**j
print(s)