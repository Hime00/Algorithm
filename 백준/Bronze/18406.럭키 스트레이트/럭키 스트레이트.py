a=list(map(int,input()))
# 리스트 슬라이싱 
b=a[:len(a)//2]
c=a[len(a)//2:]
if sum(b)==sum(c):
  print('LUCKY')
else:
  print('READY')
