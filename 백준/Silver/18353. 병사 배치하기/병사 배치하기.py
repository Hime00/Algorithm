n = int(input())
array = list(map(int, input().split()))
d= [1] * n
part=[]
for i in range(1,n):
    part=[]
    for j in range(0,i):
        if array[j]>array[i]:
          d[i]=d[j]+1
          part.append(d[i])
    if len(part):
      d[i]=max(part)
print(n-max(d))