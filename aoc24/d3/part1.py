import re
import sys
s = 0
for line in sys.stdin: 
    for x in re.finditer(r"mul\([0-9]{1,3},[0-9]{1,3}\)", line):
        x = x.group().strip("mul()")
        a, b = (int(y) for y in x.split(","))
        s += a*b
print(s)