with open ('input.txt','r') as file:
    numbers = [int(x) for x in file.read().split()]


for i in range(25,len(numbers)):
    has_sum = False
    previous = numbers[i-25:i]
    for num in previous:
        target = numbers[i]-num
        if target in previous:
            has_sum = True

    if has_sum == False:
        silver = numbers[i]

print(silver)
            
def gold_star():
    for i in range(0,len(numbers)):
        count = i
        possible_sum = []
        while sum(possible_sum) <= silver:
            count += 1
            if sum(possible_sum) == silver:
                return min(possible_sum) + max(possible_sum)
            possible_sum = numbers[i:count]

print(gold_star())
