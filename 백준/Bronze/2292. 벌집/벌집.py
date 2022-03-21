n = int(input())
line = 1
num = 1
if n == 1:
  print(1)
else:
  while True:
    if n <= num:
      print(line)
      break
    num += (6 * line)
    line += 1