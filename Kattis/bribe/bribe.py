from sys import stdin, stdout


def search(c, m, visited, henchmen_left):
    if mem[visited*num_henchmen+c] != -1:
        res = mem[visited*num_henchmen+c]
    elif m < 0 or henchmen_left < c:
        res = 0
    elif c == 0:
        res = 1
    else:
        res = 0
        for j in range(num_henchmen):
            if visited & 1 << j:
                continue
            cost, prob = henchmen[j]
            new_visited = visited | 1 << j
            total = ((1-prob) * search(c, m-cost, new_visited, henchmen_left-1)
                    + prob    * search(c-1, m-cost, new_visited, henchmen_left-1))
            if total > res:
                res = total
    
    mem[visited*num_henchmen+c] = res
    return res


for _ in range(int(stdin.readline())):
    n, c, m = map(int, stdin.readline().split())
    henchmen = []
    for _ in range(n):
        cost, prob = map(int, stdin.readline().split())
        if cost <= m and prob > 9:
            henchmen.append((cost, prob/100))

    num_henchmen = len(henchmen)
    mem = [-1 for _ in range(2**num_henchmen*num_henchmen+c+1)]
    stdout.write(str(search(c, m, 0, num_henchmen))+"\n")