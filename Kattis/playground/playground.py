while (n:=int(input()))!=0:
    x=sorted(float(x) for x in input().split())
    s=0
    for i in range(n-1):
        s+=x[i]
        if s>=x[i+1]:
            print("YES")
            break
    else:
        print("NO")