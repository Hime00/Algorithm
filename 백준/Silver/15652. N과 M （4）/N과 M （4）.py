N,M=map(int,input().split())
result=[0]*M
def go(index,start):
  if index==M:
    for i in result:
      print(i,end=' ')
    print()
    return
  for i in range(start,N+1):
    result[index]=i
    start=i
    go(index+1,start)
go(0,1)