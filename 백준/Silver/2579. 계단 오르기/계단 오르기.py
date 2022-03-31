import sys
input=sys.stdin.readline
n=int(input().rstrip())
data=[int(input().rstrip()) for _ in range(n)]
result=0
d=[0]*400
for i in range(1,n+1):
  if i==1:
    d[i]=data[0]
    continue
  if i==2:
    d[i]=data[0]+data[1]
    continue
  d[i]=max(d[i-2]+data[i-1],d[i-3]+data[i-2]+data[i-1])

print(d[n])