from sys import stdin

n = int(stdin.readline())
clock1 = [int(x) for x in stdin.readline().split()]
clock2 = [int(x) for x in stdin.readline().split()]
clock1.sort()
clock2.sort()

new_clock1 = [0 for _ in range(n*2)]
new_clock2 = [0 for _ in range(n)]
for i in range(n-1):
    new_clock1[i] = (clock1[i+1]-clock1[i])
    new_clock2[i] = (clock2[i+1]-clock2[i])

new_clock1[n-1] = (360_000+clock1[0]-clock1[n-1])
new_clock2[n-1] = (360_000+clock2[0]-clock2[n-1])
for i in range(n):
    new_clock1[i+n] = new_clock1[i]

clock1 = new_clock1
clock2 = new_clock2

def kmp(text, pattern):
    lps = build_lps(pattern)
    i, j = 0, 0

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            return True

        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return False


def build_lps(pattern):
    length = 0
    lps = [0 for _ in range(len(pattern))]
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1

    return lps

if kmp(clock1, clock2):
    print("possible")
else:
    print("impossible")