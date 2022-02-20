a=list(map(int,input()))
b=a[:len(a)//2]
c=a[len(a)//2:]
if sum(b)==sum(c):
  print('LUCKY')
else:
  print('READY')