import sys; input=sys.stdin.readline

def is_white(x, y, s):
    if x==0 and y == 0:
        return False
    if x == 0:
        if y % s == 0:
            return False
        y //= s
        if y % 2 == 1:
            return True
        return False
    elif y == 0:
        if x % s == 0:
            return False
        x //= s
        if x % 2 == 1:
            return True
        return False
    
    if x % s == 0 or y % s == 0:
        return False
    x //= s
    y //= s
    return (x+y) % 2 == 1


def get_point(x, y, s):
    return (x%s, y%s)



def solve(s, x, y, dx, dy):
    count = 0
    visited = {}
    while True:
        if (a := visited.get(p := get_point(x, y, s), 0)) == 2: 
            return -1
        visited[p] = a + 1
        if is_white(x, y, s):
            return count, x, y
        x += dx
        y += dy
        count += 1
        
while (inp := tuple(map(int, input().split()))) != (0,0,0,0,0):
    res = solve(*inp)
    if res == -1:
        print("The flea cannot escape from black squares.")
    else:
        count, x, y = res
        print(f"After {count} jumps the flea lands at ({x}, {y}).")
