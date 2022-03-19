from collections import deque
import sys
input=sys.stdin.readline
case=int(input())
for i in range(case):
  n,m=map(int,input().split())
  q1=deque()
  q2=deque()
  orderlist=[]
  data=list(map(int,input().split()))
  
  for j in range(n):
    q1.append((data[j],j))
    q2.append(data[j])
    
  while q2:
    if q1[0][0]==max(q2):
      u,v=q1.popleft()
      x=q2.popleft()
      orderlist.append((u,v))   
    else:
      u,v=q1.popleft()
      x=q2.popleft()
      q1.append((u,v))
      q2.append(x)
  count=1    
  for k in orderlist:
    if k[1]==m:
      print(count)
    else:
      count+=1