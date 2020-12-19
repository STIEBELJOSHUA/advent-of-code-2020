import re

with open ('input.txt','r') as file:
    rules = file.read().strip().split('\n')
    bags = {}
    for rule in rules:
        parsed = re.findall('(?=\w+\s\w+\sbag)\w+\s\w+',rule)
        ints = re.findall('\d(?=\s\w+\s\w+\sbag)',rule)
        bags[parsed[0]] = {}
        for i in range(0,len(parsed[1:])):
            if ints:
                bags[parsed[0]][parsed[i+1]]=ints[i]
            else:
                bags[parsed[0]][parsed[i+1]]=0
    print(bags)

    

def contains_gold(bag):
    if 'shiny gold' in bags[bag]:
        return True
    else:
        for child in bags[bag]:
            if child != 'no other' and contains_gold(child):
                    return True
        

answer1 = 0
for bag in bags:
    print(bag)
    if contains_gold(bag):
        answer1+=1
        print(answer1)

#solution to question 1
print(answer1)

def sum_bags(node):
    sum = 0
    if 'no other' in bags[node]:
        return 0
    else:
        for child in bags[node]:
            sum += int(bags[node][child]) * (1 + sum_bags(child))
    return sum


print(sum_bags('shiny gold'))
