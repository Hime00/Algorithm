n=int(input())
a=0
b=0
def go(num,div):
  count=0
  while not num%div:
    count+=1
    num/=div
  return count
for i in range(1,n+1):
  if i%2==0:
    a+=go(i,2)
  if i%5==0:
    b+=go(i,5)
print(min(a,b))