n = int(input())
if n % 2 == 1:
    print("impossible")
    exit()
employees = []
for _ in range(n):
    employees.append([int(x) for x in input().split()])
    
    
def team(i, j):
    pool = employees[i][0] + employees[j][0]
    biljard = employees[i][1] + employees[j][1]
    return (pool, biljard)

employees.sort(key=lambda x: x[0])
dummy = False
target = team(0, n-1)
for i in range(1, len(employees)-1):
    j = n-i-1
    if team(i, j) != target:
        dummy = True
        break

if dummy:
    employees.sort(key=lambda x: x[1])
    target = team(0, n-1)
    for i in range(1, len(employees)-1):
        j = n-i-1
        if team(i, j) != target:
            print("impossible")
            break
    else:
        print("possible")
else:
    print("possible")