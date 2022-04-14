import sys
input=sys.stdin.readline
n=int(input())
white=0
blue=0

data=[list(map(int,input().rstrip().split())) for _ in range(n)]
def go(row_start,row_end,col_start,col_end):
  global white
  global blue
  row_mid=(row_start+row_end)//2
  col_mid=(col_start+col_end)//2
  
  if row_start-row_end==1:
    if data[row_start][col_start]==0:
        white+=1
    if data[row_start][col_start]==1:
        blue+=1
    return
  w=0
  b=0
  for i in range(row_start,row_end):
    for j in range(col_start,col_end):
      if data[i][j]==0:
        w+=1
      if data[i][j]==1:
        b+=1
  if w==0:
    blue+=1
    return
  if b==0:
    white+=1
    return
  go(row_start,row_mid,col_start,col_mid)
  go(row_mid,row_end,col_start,col_mid)
  go(row_start,row_mid,col_mid,col_end)
  go(row_mid,row_end,col_mid,col_end)

go(0,n,0,n)
print(white)
print(blue)