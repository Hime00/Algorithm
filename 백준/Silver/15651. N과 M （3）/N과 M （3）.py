import sys
n,m = map(int,input().split())
a = [0]*m
def go(index, n, m):
    if index == m:
        for i in a:
          print(i,end=' ')
        print()
        return
    for i in range(1,n+1):
      a[index]=i
      go(index+1, n, m)

go(0,n,m)