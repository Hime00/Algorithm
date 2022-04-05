n=int(input())
m=int(input())
broken=[False]*10

if m>0:
  data=list(map(int,input().split()))
else:
  data=[]
  
for b in data:
  broken[b]=True
  
def check(c):
  if c==0:
    if broken[0]:
      return 0
    else:
      return 1
  else:
    result=0
    while c>0:
      if broken[c%10]:
        return 0
      c//=10
      result+=1
    return result
    
ans=abs(n-100)

for c in range(0,1000001):
  l=check(c)
  if l>0:
    press=abs(c-n) 
    ans=min(ans,press+l)

print(ans)