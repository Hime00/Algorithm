import copy
n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
d=copy.deepcopy(array)
for i in range(1,n):
  for j in range(i+1):
    if j==0:
      topleft=0
    else:
      topleft=d[i-1][j-1]
    if j==i:
      top=0
    else:
      top=d[i-1][j]
    d[i][j]+=max(topleft,top)
res=0
for k in range(n):
  res=max(res,d[n-1][k])
print(res)