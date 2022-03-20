import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n=int(input())

sum=0
if n<=2:
  print(-1)
      
while n>=3:
  if n%5==0:
    sum=sum+n//5
    print(sum)
    break
  else:
    sum+=1
    n-=3
    if 1<=n<=2:
      print(-1)
      break
    elif n==0:
      print(sum)
      break