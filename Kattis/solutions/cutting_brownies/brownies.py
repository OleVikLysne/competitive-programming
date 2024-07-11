# for c in"V"*int(input()):
#  B,D,p=input().split()
#  if c>p:B,D=D,B
#  while B:B,D,x=int(B)/2,int(D)/2,B<=D
#  print(p,"can"+x*"not","win")


for c in"V"*int(input()):
 B,D,p=input().split()
 l=(p<c)
 if l:B,D=D,B
 u = (bin(int(B)))<=(bin(int(D)))
 #u = len(bin(int(B)*(l-0.5)))<=len(bin(int(D)*(l-0.5)))
 print(p,"can"+u*"not","win")

