import re

#--part 1--
with open ('input','r') as file:
    validPassports = []
    passports =[line.replace('\n',' ') for line in file.read().split('\n\n')]
    required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    for passport in passports:
        for word in required:
            if word not in passport:
                break
            if word == 'pid':
                validPassports.append(passport)
#--question 2--
hcl = '0123456789abcdef'
ecl = ['amb','blu','brn','gry','grn','hzl','oth']
valids = 0
for passport in validPassports:
    vals = [re.findall('(?<='+word+':)\S+',passport)[0] for word in required]
    byrCheck = 1920 <= int(vals[0]) <= 2002 
    iryCheck = 2010 <= int(vals[1]) <= 2020
    eyrCheck = 2020 <= int(vals[2]) <= 2030 
    hgtCheck = vals[3][-2:] == 'in' and 59 <= int(vals[3][:-2]) <= 76 or vals[3][-2:] == 'cm' and 150 <= int(vals[3][:-2]) <= 193
    hclCheck = vals[4][0]=='#' and len(vals[4])== 7 and all([letter in hcl for letter in vals[4][1:]]) 
    eclCheck = vals[5] in ecl
    pidCheck = len(vals[6]) == 9 and vals[6].isdigit()
    if all([byrCheck,iryCheck,eyrCheck,hgtCheck,hclCheck,eclCheck,pidCheck]):
        valids += 1


#print part 1 answer
print(len(validPassports))
#part 2 answer
print(valids)
