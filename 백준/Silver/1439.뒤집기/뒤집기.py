data = input()

change0 = 0
change1 = 0
 
if data[0] == '0':
    #1로 바꾸는 경우
    change1 += 1
else:
    #0으로 바꾸는 경우
    change0 += 1
    
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            #0으로 바꾸는 경우
            change0 += 1
        else:
            #1로 바꾸는 경우
            change1 += 1
            
print(min(change0, change1))