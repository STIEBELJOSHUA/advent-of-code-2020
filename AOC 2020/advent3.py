#--day 3 problem 1--
def findTrees(right,down):
    with open ('input','r') as file:
        i=0
        tree=0
        loop=0
        for line in file:
            if loop%down == 0:
                space = i%31
                if line[space] == '#':
                    tree+=1
                i+=right
            loop+=1
    return tree
print(findTrees(3,1))
#--problem 2--
trees = 1
for i in range(1,9,2):
    trees *= findTrees(i,1)
trees *= findTrees(1,2)
print(findTrees(3,2))
print(trees)
