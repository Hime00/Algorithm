import sys
input=sys.stdin.readline
n=int(input())
data=[]
for i in range(10):
  for j in range(10):
    for k in range(10):
      for l in range(10):
        value=i*(10**6)+j*(10**5)+k*(10**4)+l*(10**3)+666
        data.append(value)

for i in range(10):
  for j in range(10):
    for k in range(10):
      for l in range(10):
        value=i*(10**6)+j*(10**5)+k*(10**4)+6660+l
        data.append(value)

for i in range(10):
  for j in range(10):
    for k in range(10):
      for l in range(10):
        value=i*(10**6)+j*(10**5)+66600+k*(10**1)+l
        data.append(value)        

for i in range(10):
  for j in range(10):
    for k in range(10):
      for l in range(10):
        value=i*(10**6)+666000+j*(10**2)+k*(10**1)+l
        data.append(value)
        
data=list(set(data))
data.sort()
print(data[n-1])