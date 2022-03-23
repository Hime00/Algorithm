import sys
input=sys.stdin.readline
n,m = map(int,input().split())
data=list(map(int,input().split()))
start=0
result=0
end=max(data)
while start<=end:
  mid=(start+end)//2
  sum=0
  for x in data:
    if x>mid:
      sum+=x-mid
  if m>sum:
    end=mid-1
  else:
    result=mid
    start=mid+1
print(result)