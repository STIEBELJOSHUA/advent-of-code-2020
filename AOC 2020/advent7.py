import re

with open ('input.txt','r') as file:
    rules = file.read().strip().split('\n')


def get_children(bag,checked):
    global goldbags
    checked = []
    if bag == 'shiny gold':
        goldbags+=1
        return
    else:
        children = return_children(bag)
        print(children)
        for child in children:
            if child not in checked:
                checked.append(child)
                get_children(child,checked)


def return_children(bag):
    for rule in rules:
        bags = re.findall('(?=\w+\s\w+\sbag)\w+\s\w+',rule)
        if bags[0] == bag:
            return bags[1:]

answer1 = 0
checked=[]
for rule in rules:
    goldbags = 0
    get_children(re.findall('(?=\w+\s\w+\sbag)\w+\s\w+',rule)[0],checked)
    print(re.findall('(?=\w+\s\w+\sbag)\w+\s\w+',rule)[0])
    print(goldbags)
    if goldbags>0:
        answer1+=1
        print(answer1)

#solution to question 1
print(answer1-1)
