import sys; input=sys.stdin.readline
ops = ["*", "+", "-", "//"]
m = {}
bar = []
def foo():
    if len(bar) == 3:
        s = "4 " + " 4 ".join(ops[i] for i in bar) + " 4"
        res = eval(s)
        s = s.replace("//", "/")
        m[res] = s + f" = {res}"
        return
    for i in range(4):
        bar.append(i)
        foo()
        bar.pop()
foo()

for _ in range(int(input())):
    print(m.get(int(input()), "no solution"))
