la = [int(x) for x in input().split()]
targets = {la[-2], la[-1]}
l = la[:-2]
l.sort(reverse=True)

for j in range(1, 6):
    for k in range(j + 1, 6):
        x = l[j]
        y = l[k]
        group = [l[0], x, y]
        res = sum(group)
        if res in targets:
            group2 = []
            for i in range(6):
                if i != 0 and i != j and i != k:
                    group2.append(l[i])
            res2 = sum(group2)
            if res2 in targets:
                if len(targets) == 1 or res2 != res:
                    if res2 == la[-2]:
                        group, group2 = group2, group
                    print(
                        " ".join(str(x) for x in group),
                        " ".join(str(x) for x in group2),
                    )
                    exit()
