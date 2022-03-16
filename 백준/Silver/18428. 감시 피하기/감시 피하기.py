import sys,time,copy
input = sys.stdin.readline
from itertools import combinations

n = int(input())
array = [list(input().split()) for _ in range(n)]

visit=[[False]*n for _ in range(n)]
student=[]
teacher=[]
candidate=[]
for i in range(n):
  for j in range(n):
    if array[i][j]=='X':
      candidate.append([i,j])
    elif array[i][j]=='S':
      student.append([i,j])
    elif array[i][j]=='T':
      teacher.append([i,j]) 

dx=[-1,1,0,0]
dy=[0,0,-1,1]

object=list(combinations(candidate,3))
  
check=False    
for i in object:
  res=0
  array_=copy.deepcopy(array)
  visit_=copy.deepcopy(visit)
  for num in range(3):
    array_[i[num][0]][i[num][1]]='O'
  
  for j in teacher:
    for k in range(4):
      nx=j[0]+dx[k]
      ny=j[1]+dy[k]
      while 0<=nx<n and 0<=ny<n and array_[nx][ny]!='O':
          visit_[nx][ny]=True
          nx+=dx[k]
          ny+=dy[k]
  
  
  for s in student:
    if visit_[s[0]][s[1]]==False:
      res+=1
    else:
      break
  if res==len(student):
      print('YES')
      check = True
      break

if check==False:
  print('NO')