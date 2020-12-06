import re

with open ('input.txt','r') as file:
    passwds=[[i for i in re.split('\n|-| |:',line) if i] for line in file]

#part1
validpasses = 0
for pas in passwds:
    validchars = pas[3].count(pas[2])
    if validchars >= int(pas[0]) and validchars <= int(pas[1]):
        validpasses += 1
print(validpasses)

#part2
validpasses = 0
for pas in passwds:
    if (pas[3][int(pas[0])-1]==pas[2]) != (pas[3][int(pas[1])-1]==pas[2]):
        validpasses += 1
print(validpasses)


#oneliner solution 1
with open ('input.txt','r') as file: print(len([x for x in [[i for i in re.split('\n|-| |:',line) if i] for line in file] if x[3].count(x[2]) >= int(x[0]) and x[3].count(x[2]) <= int(x[1])]))
#oneliner solution 2
with open ('input.txt','r') as file: print(len([x for x in [[i for i in re.split('\n|-| |:',line) if i] for line in file] if (x[3][int(x[0])-1]==x[2]) != (x[3][int(x[1])-1]==x[2])]))
