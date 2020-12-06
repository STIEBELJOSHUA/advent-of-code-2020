import re

with open ('input.txt','r') as file:
    passwds=[[i for i in re.split('\n|-| |:',line) if i] for line in file]


validpasses = 0
for pas in passwds:
    validchars = pas[3].count(pas[2])
    if validchars >= int(pas[0]) and validchars <= int(pas[1]):
        validpasses += 1
print(validpasses)

validpasses = 0
for pas in passwds:
    if (pas[3][int(pas[0])-1]==pas[2]) != (pas[3][int(pas[0])-1]==pas[2]):
        validpasses += 1
print(validpasses)


#oneliner solution
with open ('input.txt','r') as file: print(len([x for x in [[i for i in re.split('\n|-| |:',line) if i] for line in file] if x[3].count(x[2]) >= int(x[0]) and x[3].count(x[2]) <= int(x[1])]))
