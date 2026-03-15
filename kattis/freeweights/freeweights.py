n = int(input())
main_row = [int(x) for x in input().split()]
if n == 1:
    print(main_row[0])
    exit()

solo = set()
for x in [int(x) for x in input().split()]:
    if x not in solo:
        solo.add(x)
    else:
        solo.remove(x)
    main_row.append(x)

cost = max(solo) if len(solo)>0 else 0

k = 0
while k+1<len(main_row):
    i = main_row[k]
    j = main_row[k+1]
    
    if i == j:
        k+=2
        continue
    elif i < j:
        k+=1
        cost = max(i, cost)
    else:
        cost = max(j, cost)
        main_row[k+1] = i
        k+=1
print(cost)