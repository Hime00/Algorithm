import sys
from collections import deque
n,m,k,x=map(int,input().split())
array = [[] for _ in range(n+1)]
# 인접 행렬로 간선 구현하기
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())		
    array[a].append(b)
  
distance=[-1]*(n+1)
queue=deque()

def bfs(start):
  queue.append(start)
  distance[start]=0
  while queue:
    first=queue.popleft()
    for i in array[first]:
      if distance[i]==-1:
        distance[i]=distance[first]+1
        queue.append(i)
bfs(x)
check=False
for i in range(len(distance)):
  if distance[i]==k:
    print(i)
    check=True
    
if check==False:
 print(-1)