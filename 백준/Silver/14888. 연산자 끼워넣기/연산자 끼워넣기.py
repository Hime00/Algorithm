import sys,time
input = sys.stdin.readline
from itertools import permutations

n = int(input())
array = list(map(int,list(input().split())))
a = list(map(int,list(input().split())))

idenlist=[]
result=[]
if a[0]>0:
  for i in range(a[0]):
    idenlist.append('+')
if a[1]>0:
  for i in range(a[1]):
    idenlist.append('-')
if a[2]>0:
  for i in range(a[2]):
    idenlist.append('*')
if a[3]>0:
  for i in range(a[3]):
    idenlist.append('/')    

data=list(set(permutations(idenlist,n-1)))


for iden in data:
  sum=array[0]
  for i in range(1,n):
    if iden[i-1]=='+':
      sum+=array[i]
    elif iden[i-1]=='-':
      sum-=array[i]
    elif iden[i-1]=='*':
      sum*=array[i]
    elif iden[i-1]=='/':
      if array[i]:
        if sum<0:
          sum=-(abs(sum)//array[i])
        else:
          sum//=array[i]
  result.append(sum)

print(max(result))
print(min(result))