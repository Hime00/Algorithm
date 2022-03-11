n=int(input())
a=list(map(int,input().split()))
if n==1:
  print(a[0]**2)
else:
  print(max(a)*min(a))