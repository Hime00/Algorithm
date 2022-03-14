import sys
input = sys.stdin.readline
from collections import deque
n, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
s,x,y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
data=[]
for i in range(n):
      for j in range(n):
          if array[i][j]:
              data.append([array[i][j],0,i,j])
      data.sort(key=lambda x:x[0]) 
      q=deque(data)
def bfs():
    while q:
        target=q.popleft()
        if s==target[1]:
            break
        for dir in range(4):
            nx=target[2]+dx[dir]
            ny=target[3]+dy[dir]
            if nx<0 or ny<0 or nx>=n or ny>=n :
                continue
            if array[nx][ny]==0:
                array[nx][ny]=target[0]
                q.append([array[nx][ny],target[1]+1,nx,ny])
    return
  
bfs()
        
print(array[x-1][y-1])