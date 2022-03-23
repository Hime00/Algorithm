import sys,time
input=sys.stdin.readline
data=[]
num=1
def d(num):
  sum=num
  for i in str(num):
    sum+=int(i)
  data.append(sum)  
while num<=9999:
  d(num)
  num+=1
for i in range(1,10001):
  if i not in data:
    print(i)
