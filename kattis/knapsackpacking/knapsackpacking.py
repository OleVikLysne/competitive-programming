from sys import stdin, stdout


def impossible():
    stdout.write("impossible")
    exit()


def possible():
    stdout.write("\n".join(str(x) for x in foo))
    exit()


n = int(stdin.readline())
subset_sums = [int(stdin.readline()) for _ in range(2**n)]
subset_sums.sort()

if subset_sums[0] != 0:
    impossible()

TARGET_SUM = subset_sums[-1]
START = subset_sums[1]
foo = [START]
powerset_sums = [0, START]

occurences = {}
for x in subset_sums:
    if x in occurences:
        occurences[x] += 1
    else:
        occurences[x] = 1


for x in powerset_sums:
    occurences[x] -= 1


def try_add(value):
    foo.append(value)
    for i in range(len(powerset_sums)):
        x = powerset_sums[i] + value
        if occurences.get(x, 0) <= 0:
            revert_add(i)
            return False

        occurences[x] -= 1
        powerset_sums.append(x)
    return True


def revert_add(k=len(powerset_sums) // 2):
    for _ in range(k):
        occurences[powerset_sums.pop()] += 1
    foo.pop()


def search(s, prev):
    if s > TARGET_SUM:
        return
    if n == len(foo):
        if s == TARGET_SUM:
            possible()
        return

    lower = prev + 1
    upper = 2 ** len(foo) + 1

    for i in range(lower, upper):
        if i > lower and subset_sums[i] == subset_sums[i - 1]:
            continue

        if try_add(subset_sums[i]):
            search(s + subset_sums[i], i)
            revert_add()


search(START, len(foo))
impossible()
