from itertools import combinations
n,m=map(int,input().split())
array=[list(map(int,input().split())) for i in range(n)]
house=[]
target=[]

for r in range(n):
  for c in range(n):
    if array[r][c]==2:
      target.append((r,c))
    
for r in range(n):
  for c in range(n):
    if array[r][c]==1:
      house.append((r,c))
     
abc=list(combinations(target,m))      

finalDistance=[]
for i in abc:
  sumOfPart=0
  for k in house:
    len=[]
    for j in range(m):
      len.append(abs(k[0]-i[j][0])+abs(k[1]-i[j][1]))
    sumOfPart+=min(len)  
  finalDistance.append(sumOfPart)  

print(min(finalDistance))