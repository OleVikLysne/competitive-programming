from itertools import permutations

ADD = lambda x, y: x+y
SUB = lambda x, y: x-y
MUL = lambda x, y: x*y
DIV = lambda x, y: x/y
OPS = [
    MUL,
    DIV,
    ADD,
    SUB
]
M = {
    ADD: "+",
    SUB: "-",
    MUL: "*",
    DIV: "/"
}

c, t = map(int, input().split())
nums = [(float(x), 1) for x in input().split()]

def reconstruct(k, parent):
    if k < c:
        return int(nums[k][0])
    i, j, op = parent[k]
    return f"({reconstruct(i, parent)}{M[op]}{reconstruct(j, parent)})"

def solve(numbers: list, parent: list, visited: list, seen: set):
    state = [numbers[i][0] for i in range(len(numbers)) if not visited[i]]
    state.sort()
    state = tuple(state)
    if state in seen:
        return
    seen.add(state)

    for i in range(len(numbers)):
        if visited[i]:
            continue
        for j in range(len(numbers)):
            if i == j: continue
            if visited[j]:
                continue
            visited[i] = visited[j] = True
            (x, xc), (y, yc) = numbers[i], numbers[j]
            for op in OPS:
                if op == DIV and y == 0:
                    continue
                z = op(x, y)
                zc = xc+yc
                parent.append((i, j, op))

                if zc == c and (z+1e-4 < t) != (z-1e-4 < t):
                    print(reconstruct(len(numbers), parent))
                    exit()

                visited.append(False)
                numbers.append((z, zc))
                solve(numbers, parent, visited, seen)
                visited.pop()
                numbers.pop()
                parent.pop()

            visited[i] = visited[j] = False


parent = [(0, 0, ADD) for _ in range(c)]
visited = [False]*c
for numbers in permutations(nums):
    numbers = list(numbers)
    solve(numbers, parent, visited, set())