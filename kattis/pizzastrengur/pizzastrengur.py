import random
n = int(input())
chars = ["P","I","Z","A"]
guess = []
for _ in range(n):
    random.shuffle(chars)
    for char in chars[:-1]:
        guess.append(char)
        print("".join(x for x in guess), flush=True)
        response = int(input())
        if response == 1:
            break
        elif response == 2:
            exit()
        guess.pop()
    else:
        guess.append(chars[-1])
        if len(guess) == n:
            print("".join(x for x in guess), flush=True)
            exit()
        
    