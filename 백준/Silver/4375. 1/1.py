while True:
  try:
    n=int(input())
  except:
    exit(0)
  cnt=1
  num=1
  while True:
    num = num % n
    if num==0:
      print(cnt)
      break
    num = (num * 10)%n + 1%n
    cnt+=1