n=int(input())
array=[]
for i in range(n):
  x,y=map(int,input().split())
  array.append((x,y))
array.sort(key=lambda x:x[0])
# 우선순위가 y좌표이므로 마지막에 y좌표 우선정렬 한다
array.sort(key=lambda x:x[1])
for i in array:
  print(i[0],i[1])
