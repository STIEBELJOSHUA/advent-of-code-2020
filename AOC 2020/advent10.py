with open ('input.txt','r') as file:
	adapters = [int(x) for x in file.read().strip().split()]
	adapters.sort()
	
joltages = []
for i in range(0,len(adapters)):
	if i == 0:
		joltages.append(adapters[i])
	else:
		joltages.append(adapters[i]-adapters[i-1])

silver = joltages.count(1) * (joltages.count(3)+1)
print(silver)



	
