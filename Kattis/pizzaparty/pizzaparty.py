import sys; input=sys.stdin.readline

def get_mask(splitter, cond):
    mask = 0
    cond = cond.split(splitter)
    for x in cond:
        i = m.setdefault(x, len(m))
        mask |= 1 << i
    return mask

m = {}
c = int(input())
ors = []
ands = []
inc_mask = 0
for _ in range(c):
    inp = input().rstrip()
    if inp[:3] == "if ":
        cond, res = inp[3:].split(" then ")
        res = m.setdefault(res, len(m))
        if " or " in cond:
            mask = get_mask(" or ", cond)
            ors.append((mask, res))
        else:
            mask = get_mask(" and ", cond)
            ands.append((mask, res))
    else:
        i = m.setdefault(inp, len(m))
        inc_mask |= 1 << i

dummy = True
while dummy:
    dummy = False
    for i in range(len(ors)-1, -1, -1):
        mask, res = ors[i]
        if inc_mask & mask:
            inc_mask |= 1 << res
            dummy = True
            ors[i], ors[-1] = ors[-1], ors[i]
            ors.pop()
    for i in range(len(ands)-1, -1, -1):
        mask, res = ands[i]
        if inc_mask & mask == mask:
            inc_mask |= 1 << res
            dummy = True
            ands[i], ands[-1] = ands[-1], ands[i]
            ands.pop()
print(inc_mask.bit_count())