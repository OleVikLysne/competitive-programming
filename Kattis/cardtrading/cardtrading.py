N, T, K = [int(x) for x in input().split()]
A = [int(x)-1 for x in input().split()]
A_cards = {}
for card in A:
    A_cards[card] = 2 if card in A_cards else 1

sell = []
profit = 0
for t in range(T):
    a, b = [int(x) for x in input().split()]
    if t not in A_cards:
        profit -= 2*a
        sell.append(2*a)
    elif A_cards[t] == 1:
        profit -= a
        sell.append(a+b)
    elif A_cards[t] == 2:
        sell.append(2*b)
    
sell.sort(reverse=True)
profit += sum(sell[:T-K])
print(profit)