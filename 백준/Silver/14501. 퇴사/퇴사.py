n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
t=[]
p=[]
d=[0]*20
for i in data:
  t.append(i[0])
  p.append(i[1])

value=0
for i in range(n-1,-1,-1):
  time=t[i]+i
  if time<=n:
    d[i]=max(p[i]+d[time],value)
    value=d[i]
  else:
    d[i]=value
print(value)