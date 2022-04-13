import sys
input=sys.stdin.readline
n=int(input())
data=list(map(int,input().rstrip().split()))
d=[0]*(n)
data.sort()
a=0
for i in range(len(data)):
  a+=data[i]
  d[i]=a
print(sum(d))