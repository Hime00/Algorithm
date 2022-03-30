import sys
input=sys.stdin.readline
n,m=map(int,input().rstrip().split())
data=dict()
for i in range(n):
  data[input().rstrip()]=i
count=0
result=[]
for i in range(m):
  k=input().rstrip()
  if k in data:
    count+=1
    result.append(k)
result.sort()
print(count)    
for i in result:
  print(i)