with open ('input.txt','r') as file:
    commands = file.read().strip().split('\n')

directions = {'N':0,'S':0,'E':0,'W':0}
compass = 'NESW'
facing = 'E'
for command in commands:
    direction = command[0]
    value = int(command[1:])
    if direction == 'R':
       turn = (compass.index(facing)+(value/90))%4
       facing = compass[int(turn)]
    elif direction == 'L':
        turn =(compass[::-1].index(facing) + (value/90))%4
        facing = compass[::-1][int(turn)]
    elif direction == 'F':
        directions[facing] += value
    else:
        directions[direction] += value

silver = abs(directions['N'] - directions['S']) + abs(directions['E'] - directions['W'])
print(silver)
