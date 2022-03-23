import sys,time
input=sys.stdin.readline
n,m,b = map(int,input().split())
data=[list(map(int,input().split())) for _ in range(n)]
array=[]
maxdata=[]
sum_data=0

for x in data:
  sum_data+=sum(x)
for x in data:
  maxdata.append(max(x))
max_num=max(maxdata)
num=max_num

while num>=0:
  result=0
  if b+sum_data<num*(n*m):
    num-=1
    continue
    
  for i in range(n):
    for j in range(m):
      if data[i][j]>num:
        result+=(data[i][j]-num)*2
      elif data[i][j]<num:
        result+=(num-data[i][j])
  array.append((result,num))
  num-=1

array.sort(key=lambda x:x[0])
print(array[0][0],array[0][1])