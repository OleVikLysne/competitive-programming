n, T = map(int, input().split())
A, B, C, t0 = map(int, input().split())

counts = [0]*(C+1)
visit_time = [-1]*(C+1)
visit_time[t0] = 0
counts[t0] = 1
prev = t0
break_point = -1
for i in range(1, n):
    ti = (A * prev + B) % C + 1
    if visit_time[ti] != -1:
        if break_point == -1:
            break_point = ti
        elif break_point == ti:
            break
        counts[ti] += (n-visit_time[ti]-1) // (i-visit_time[ti])
    else:
        counts[ti] += 1
        visit_time[ti] = i
    prev = ti

t = 0
pen = 0
c = 0
for i in range(1, C+1):
    max_amount = (T-t) // i
    if max_amount <= 0 or c == n:
        break
    amount = min(max_amount, counts[i], n-c)
    c += amount
    pen += amount * t + i * (amount*(amount+1))//2
    pen %= 10**9+7
    t += amount * i

print(c, pen)