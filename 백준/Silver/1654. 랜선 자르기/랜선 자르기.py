import sys
input=sys.stdin.readline
k,n = map(int,input().split())
data=[int(input()) for _ in range(k)]

start=0
result=0
end=max(data)
while start<=end:
  mid=(start+end)//2
  sum=0
  for x in data:
    if mid==0:
      mid=1
    sum+=x//mid
  if n>sum:
    end=mid-1
  else:
    result=mid
    start=mid+1
print(result)