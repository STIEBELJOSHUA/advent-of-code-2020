#answers to day 1 of advent of code 2020
with open ('input.txt','r') as file:
    data = [int(i) for i in file]
    
for num in data:
    target = 2020-num
    if target in data:
        answer = num*target
        print(answer)
        break
    
    
for num1 in data:
    for num2 in data:
        if num1 + num2 == 2020:
            print(num1*num2)
   
for num1 in data:
    for num2 in data:
        for num3 in data:
            if num1+num2+num3 == 2020:
                answer2 = num1*num2
print(answer2)
