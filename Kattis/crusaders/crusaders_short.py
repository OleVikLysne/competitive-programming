g=int;i=input;c=g(i().split()[0])+1;a=[0]*c;s=["A"]
for v in i().split():
 l,u=0,c
 while a[l]<g(v)>l+1<u:
  if a[m:=l+u>>1]<1:a[m]=g(i(f"Q {m} "))
  if a[m]>g(v):u=m
  else:l=m
 s+=[l]
print(*s)