import sys,time
input=sys.stdin.readline
data=[False]*10001
num=1
def d(num):
  sum=num
  for i in str(num):
    sum+=int(i)
  if sum<=10000:  
    data[sum]=True  
while num<=9999:
  d(num)
  num+=1
for i in range(1,10001):
  if not data[i]:
    print(i)
