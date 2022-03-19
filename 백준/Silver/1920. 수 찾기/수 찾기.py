from bisect import bisect_left,bisect_right

n=int(input())
data=list(map(int,input().split()))
m=int(input())
array=list(map(int,input().split()))
data.sort()

def count_by_range(left,right):
  leftindex=bisect_left(data,left)
  rightindex=bisect_right(data,right)
  return rightindex-leftindex

for i in array:
  count=count_by_range(i,i)
  if count==0:
    print(0)
  else:
    print(1)