N=input()
sum=0
for i in range(1,len(N)+1):
  if len(N)==i:
    sum+=i*(int(N)-10**(i-1)+1)
    break
  sum+=((10**i-1)-10**(i-1)+1)*i
print(sum)