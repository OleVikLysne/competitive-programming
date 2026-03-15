from math import sqrt

n = int(input())
cubes = []
cylinders = []
for _ in range(n):
    name, a = input().split()
    a = int(a)
    if name == "cube":
        cubes.append(a)
    else:
        cylinders.append(a)

cylinders.sort()
cubes.sort()

def max_cyl_in_cube(a):
    return a/2

def max_cube_in_cyl(a):
    return sqrt(2*a**2)

m = ["cube", "cylinder"]

def out(prev, a):
    if a != float("inf"):
        print(m[prev], a)



def solve(cube_idx, cyl_idx, prev, a):
    if cube_idx < 0 and cyl_idx < 0:
        out(prev, a)
        return True
    if prev == 0: # cube
        if cyl_idx != -1 and cylinders[cyl_idx] <= max_cyl_in_cube(a):
            if solve(cube_idx, cyl_idx-1, 1, cylinders[cyl_idx]):
                out(prev, a)
                return True
        
        if cube_idx != -1 and solve(cube_idx-1, cyl_idx, 0, cubes[cube_idx]):
            out(prev, a)
            return True
            
    else: # cylinder
        if cube_idx != -1 and cubes[cube_idx] <= max_cube_in_cyl(a):
            if solve(cube_idx-1, cyl_idx, 0, cubes[cube_idx]):
                out(prev, a)
                return True
        
        if cyl_idx != -1 and solve(cube_idx, cyl_idx-1, 1, cylinders[cyl_idx]):
            out(prev, a)
            return True
        
    return False
if not solve(len(cubes)-1, len(cylinders)-1, 0, float("inf")):
    print("impossible")