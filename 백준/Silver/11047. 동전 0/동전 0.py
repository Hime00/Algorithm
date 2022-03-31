import sys
input=sys.stdin.readline
n,k=map(int,input().rstrip().split())
data=[int(input()) for _ in range(n)]
result=0
index=n-1
while k:
  if k>=data[index]:
    result+=k//data[index]
    k%=data[index]
  index-=1
print(result)