import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
case=int(input())

for _ in range(case):
  k=int(input())
  n=int(input())
  data=[[0]*(n+1) for _ in range(k+1)]
  for i in range(1,n+1):
    data[0][i]=i
  for i in range(1,k+1):
    for j in range(1,n+1):
      sum=0
      for l in range(1,j+1):
        sum+=data[i-1][l]
      data[i][j]=sum
  print(data[k][n])