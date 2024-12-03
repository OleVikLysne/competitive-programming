import re
import sys
s = 0
bool = True
for line in sys.stdin: 
    for x in re.finditer(r"(mul\([0-9]{1,3},[0-9]{1,3}\))|do\(\)|don't\(\)", line):
        x = x.group()
        if x == "don't()":
            bool = False
            continue
        elif x == "do()":
            bool = True
            continue
        if not bool:
            continue
        x = x.strip("mul()")
        a, b = (int(y) for y in x.split(","))
        s += a*b
print(s)