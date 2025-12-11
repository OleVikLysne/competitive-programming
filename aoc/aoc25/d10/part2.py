import sys
import z3

inp = []
for line in sys.stdin:
    a, *args, c = line.split()
    row = []
    z = list(map(int, c.strip("{}").split(",")))
    n = len(z)
    for x in args:
        e = [0]*n
        for i in map(int, x.strip("()").split(",")):
            e[i] = 1
        row.append(e) 
    row.append(z)
    inp.append(row)


def solve(row):
    arr, joltage = row[:-1], row[-1]
    n = len(joltage)
    k = len(arr)

    opt = z3.Optimize()

    scalars = [z3.Int(f"s{i}") for i in range(k)]
    vectors = [z3.IntVector(f"x{i}", n) for i in range(k)]
    ans_vector = z3.IntVector("y", n)

    for j in range(n):
        opt.add(z3.Sum(scalars[i] * vectors[i][j] for i in range(k)) == ans_vector[j])

    for i in range(k):
        for j in range(n):
            opt.add(vectors[i][j] == arr[i][j])

    for j in range(n):
        opt.add(ans_vector[j] == joltage[j])
    
    for i in range(k):
        opt.add(scalars[i] >= 0)

    obj = opt.minimize(z3.Sum(scalars))
    opt.check()
    return opt.lower(obj).as_long()


print(sum(solve(row) for row in inp))
            




