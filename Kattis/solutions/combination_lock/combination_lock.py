while True:
    inp = input()
    if inp == "0 0 0 0":
        break
    d, x, y, z = map(int, inp.split())    
    deg = 80
    deg += (d-x) % 40
    d = x
    deg += 40
    deg += (y-d) % 40
    d = y
    deg += (d-z) % 40
    print(int((deg*360)/40))