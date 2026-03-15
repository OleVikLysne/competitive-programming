input()
row_sums = []
col_sums = []
for x in map(int, input().split()):
    if x != 0: 
        row_sums.append(x)

for x in map(int, input().split()):
    if x != 0:
        col_sums.append(x)


def check():
    if sum(row_sums) != sum(col_sums):
        return False

    for n in row_sums:
        if n > len(col_sums):
            return False
        
        col_sums.sort(reverse=True)
        for i in range(n):
            col_sums[i] -= 1
            if col_sums[i] < 0:
                return False
    return True

if check():
    print("Yes")
else:
    print("No")