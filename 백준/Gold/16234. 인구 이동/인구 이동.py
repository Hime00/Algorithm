import sys,time,copy
input = sys.stdin.readline
from collections import deque

n,l,r=map(int,input().split())
array = [list(map(int,input().split())) for _ in range(n)]

begin=time.time()

dx=[-1,1,0,0]
dy=[0,0,-1,1]
result=0

def bfs(x,y):
  q=deque()
  q.append([x,y])
  visit[x][y]=True
  visit_.append([x,y])
  while q:
    u,v=q.popleft()
    for i in range(4):
      nx=u+dx[i]
      ny=v+dy[i]
      if 0<=nx<n and 0<=ny<n and l<=abs(array[nx][ny]-array[u][v])<=r :
        if not visit[nx][ny]:
          q.append([nx,ny])
          visit[nx][ny]=True
          visit_.append([nx,ny])
  return
  
def common(visit_):
  sum=0
  div=0
  for vi in visit_:
    sum+=array[vi[0]][vi[1]]  
    div+=1
  if div>1:
    global check
    check=True
  for vi in visit_:
    array[vi[0]][vi[1]]=sum//div 

while True:
  a=0
  visit=[[False]*n for _ in range(n)]
  check=False
  for i in range(n):
    for j in range(n):
      visit_=[]
      if not visit[i][j]:
        bfs(i,j)
      common(visit_)   
  if check==False:
    break
  result+=1
end=time.time()

print(result)  