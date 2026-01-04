n,d=map(int,input().split());p=sorted(int(input())for _ in"."*n);s=1;b=p[0]
for x in p:
 if d<x-b:b=x;s+=1
print(s)