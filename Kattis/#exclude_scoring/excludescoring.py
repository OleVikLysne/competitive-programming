import sys; input = sys.stdin.readline
SCORE_MAP = (100, 75, 60, 50, 45, 40, 36, 32, 29, 26, 24, 22, 20, 18, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

def get_score(i):
    if i >= 30:
        return 1
    return SCORE_MAP[i] + 1


n, m = map(int, input().split())
k = min(4, n - 1)
contestants = [sorted((map(int, input().split())), reverse=True)[:k] for _ in range(m)]
our_score = sum(contestants[0])
cur_scores = []
worst_rank = 1

for i in range(1, m):
    best_agg = contestants[i]
    score = sum(best_agg)
    if score > our_score:
        worst_rank += 1
        continue
    score -= min(best_agg) if k >= 4 else 0
    if score + 101 <= our_score:
        continue
    cur_scores.append(score)

cur_scores.sort(reverse=True)

def binary_search():
    lower, upper = 0, len(cur_scores) + 1
    while lower + 1 < upper:
        mid = (lower + upper) // 2
        total = 0
        c = 0
        for i in range(mid):
            diff = our_score - cur_scores[i]
            total += get_score(mid - i - 1)
            c += 1
            avg_score = -(-total // c)
            if avg_score > diff:
                total = 0
                c = 0
        if c == 0:
            lower = mid
        else:
            upper = mid
    return lower

print(worst_rank + binary_search())
