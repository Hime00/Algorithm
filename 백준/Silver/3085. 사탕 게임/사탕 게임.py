n=int(input())
data=[list(input()) for _ in range(n)]
res=0
def check(data,start_row,end_row,start_col,end_col):
  n = len(data)
  ans = 1
  for i in range(start_row, end_row+1):
    cnt = 1
    for j in range(1, n):
      if data[i][j] == data[i][j-1]:
        cnt += 1
      else:
        cnt = 1
      ans=max(ans,cnt)
      
  for i in range(start_col, end_col+1):
    cnt = 1
    for j in range(1, n):
      if data[j][i] == data[j-1][i]:
        cnt += 1
      else:
        cnt = 1
      ans=max(ans,cnt)
      
  return ans
    
for i in range(n):
  for j in range(n):
      
    if j+1<n:
      
      data[i][j],data[i][j+1] = data[i][j+1],data[i][j]
      temp=check(data,i,i,j,j+1)
      res=max(res,temp)
      
      data[i][j+1],data[i][j] = data[i][j],data[i][j+1]
      
    if i+1<n:
      
      data[i][j],data[i+1][j] = data[i+1][j],data[i][j]
      temp=check(data,i,i+1,j,j)
      res=max(res,temp)
      data[i+1][j],data[i][j] = data[i][j],data[i+1][j]
      
print(res)