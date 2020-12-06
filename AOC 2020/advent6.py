with open ('input','r') as file:
    groups = [line.split('\n') for line in file.read().strip().split("\n\n")]

part1 = 0
for group in groups:
    yes=len(set(''.join(group)))
    part1+=yes


part2 = 0
for group in groups:
    for letter in min(group,key=len):
        x = [list for list in group if letter in list]
        if len(x) == len(group):
            part2+=1

print(part1)
print(part2)
        
