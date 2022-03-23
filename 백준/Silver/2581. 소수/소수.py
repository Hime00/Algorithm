import sys,math
input=sys.stdin.readline
data=[]
m=int(input())
n=int(input())
num=m
def prime(num):
  if num<=1:
    return
  for x in range(2,int(math.sqrt(num))+1): 
    if num%x==0:
      return 
  data.append(num)  
while num<=n:
  prime(num)
  num+=1  
if not len(data):
  print(-1)
else:
  print(sum(data))
  print(min(data))