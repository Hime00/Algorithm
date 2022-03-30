import sys
input=sys.stdin.readline
d=[]
for i in range(41):
  for j in range(41):
    d.append([0,0])
d[0]=[1,0]
d[1]=[0,1]
for i in range(2,41):
  d[i][0]=d[i-1][0]+d[i-2][0]
  d[i][1]=d[i-1][1]+d[i-2][1]

case=int(input().rstrip())
for i in range(case):
  k=int(input().rstrip())
  print(d[k][0],d[k][1])