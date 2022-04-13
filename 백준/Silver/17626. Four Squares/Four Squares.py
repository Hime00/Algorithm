import math
n=int(input())
d=[0]*(n+1)
d[1]=1
if n==int(math.sqrt(n)) ** 2:
  print(1)
  exit(0)
for i in range(2,n+1):
  if i==int(math.sqrt(i))**2:
    d[i]=1
  l=1e9
  for j in range(1,int(math.sqrt(i))+1):
    l=min(l,d[i-(j**2)]+1)
  d[i]=l
print(d[n])