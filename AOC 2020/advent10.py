import sys
import functools


sys.setrecursionlimit(1000000000)


with open ('input.txt','r') as file:
	adapters = [int(x) for x in file.read().strip().split()]
	adapters.append(0)
	adapters.append(max(adapters)+3)
	adapters.sort()
	
joltages = []
for i in range(1,len(adapters)):
		joltages.append(adapters[i]-adapters[i-1])

silver = joltages.count(1) * (joltages.count(3))


@functools.lru_cache(maxsize=None)
def find_permutations(i,list):
	permutations=0
	if i >= len(list)-2:
		permutations += 1
	elif i == len(list)-3:
		for x in [j for j in range(1,3) if adapters[i+j] <= adapters[i]+3]:
			permutations += find_permutations(x+i,list)
	else:
		for x in [j for j in range(1,4) if adapters[i+j] <= adapters[i]+3]: 
			permutations += find_permutations(x+i,list)
	return permutations

print(silver)
gold = find_permutations(0,tuple(adapters))
print(gold)