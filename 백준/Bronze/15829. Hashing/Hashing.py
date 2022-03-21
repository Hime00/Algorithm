l = int(input())
a = list(input())
result = 0
for i in range(l):
    result += ((ord(a[i])-96)*31**i)
print(result%1234567891)