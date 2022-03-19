from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
data=[list(map(int,input().split())) for _ in range(n)]
ranklist=[]
for person in data:
  rank=1
  for j in range(len(data)):
    if person[0]<data[j][0] and person[1]<data[j][1]:
      rank+=1

  ranklist.append(rank)
  print(rank,end=' ')