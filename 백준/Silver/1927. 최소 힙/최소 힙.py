import sys,heapq
input=sys.stdin.readline
n=int(input())
data=[]
for _ in range(n):
  op=int(input())
  if op==0:
    if len(data)==0:
      print(0)
    else:
      k=heapq.heappop(data)
      print(k)
  else:
    heapq.heappush(data,op)