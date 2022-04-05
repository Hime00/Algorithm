import sys
N,M=map(int,input().split())
data=[list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
blocks = (
 ((0,1), (0,2), (0,3)),
 ((1,0), (2,0), (3,0)),
 ((1,0), (1,1), (1,2)),
 ((0,1), (1,0), (2,0)),
 ((0,1), (0,2), (1,2)),
 ((1,0), (2,0), (2,-1)),
 ((0,1), (0,2), (-1,2)),
 ((1,0), (2,0), (2,1)),
 ((0,1), (0,2), (1,0)),
 ((0,1), (1,1), (2,1)),
 ((0,1), (1,0), (1,1)),
 ((0,1), (-1,1), (-1,2)),
 ((1,0), (1,1), (2,1)),
 ((0,1), (1,1), (1,2)),
 ((1,0), (1,-1), (2,-1)),
 ((0,1), (0,2), (-1,1)),
 ((0,1), (0,2), (1,1)),
 ((1,0), (2,0), (1,1)),
 ((1,0), (2,0), (1,-1)),
)
ans=0
for i in range(N):
  for j in range(M): 
    for block in blocks:
      check=True
      res=data[i][j]
      for x,y in block:
        nx=x+i
        ny=y+j
        if 0<=nx<N and 0<=ny<M:
          res+=data[nx][ny]
        else:
          check=False  
          break
      if check:
        ans=max(ans,res)
print(ans)