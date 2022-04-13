import sys
input=sys.stdin.readline
data=dict()
n,m=map(int,input().rstrip().split())
for _ in range(n):
  site,pw=input().rstrip().split()
  data[site]=pw
for _ in range(m):
  can=input().rstrip()
  print(data[can])
