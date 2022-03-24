x, y = map(int, input().split())
day = 0
for i in range(1, x):
  if i in [1, 3, 5, 7, 8, 10, 12]:
    day += 31
  elif i in [4, 6, 9, 11]:
    day += 30
  elif i in [2]:
    day += 28
day += y

if day % 7 == 1:
    print("MON")
elif day % 7 == 2:
    print("TUE")
elif day % 7 == 3:
    print("WED")
elif day % 7 == 4:
    print("THU")
elif day % 7 == 5:
    print("FRI")
elif day % 7 == 6:
    print("SAT")
elif day % 7 == 0:
    print("SUN")