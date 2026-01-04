n,p,d=map(int,input().split());x=input()*2;z=s=0
for i in range(n*2):
 if"X"<x[i]:z+=1
 if"X"<x[i-p]and-1<i-p:z-=1
 if i>=n and z<d:s+=1
print(s)