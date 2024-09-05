import sys; input=sys.stdin.readline

u, k = map(int, input().split())
dishes = {}

dish_to_idx = {}
dishes = [[] for _ in range(u)]
ingredient_to_idx = {}
idx_to_ingredient = []

for j in range(u):
    dish = input().rstrip()
    dish_to_idx[dish] = len(dish_to_idx)
    h = int(input())
    for _ in range(h):
        ingredient, amount = input().split()
        if (i := ingredient_to_idx.get(ingredient)) is None:
            idx_to_ingredient.append(ingredient)
            i = len(ingredient_to_idx)
            ingredient_to_idx[ingredient] = i
        amount = int(amount)
        dishes[j].append((i, amount))


ingredient_count = [0]*len(ingredient_to_idx)

for _ in range(k):
    n = int(input())
    for _ in range(n):
        dish, amount = input().split()
        dish_idx = dish_to_idx[dish]
        amount = int(amount)
        for ingredient, c in dishes[dish_idx]:
            ingredient_count[ingredient] += amount*c

for x, y in sorted((idx_to_ingredient[x], y) for x, y in enumerate(ingredient_count) if y != 0):
    print(x, y)
