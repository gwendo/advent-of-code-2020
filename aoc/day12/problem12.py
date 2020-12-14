import math


def navigate(instructions):
    directions = {'N': (0,1, 0), 'E': (1,0, 90), 'S': (0, -1, 180), 'W': (-1, 0, 270) }
    face = 'E'
    pos = (0,0)
    for inst in instructions:
        i = inst[:1]
        if i in directions:
            pos =  move(directions[i], int(inst[1:]), pos)
        elif i in ['R', 'L']:
            angle = int(inst[1:])
            if i == 'L':
                angle *= -1

            new_dir_angle = (directions[face][2] + angle) % 360
            face = list(filter(lambda d: directions[d][2] == new_dir_angle, directions.keys()))[0]
        else:
            pos = move(directions[face], int(inst[1:]), pos)

    return abs(0 - pos[0]) + abs(0 - pos[1])


def navigate2(instructions):
    directions = {'N': (0,1, 0), 'E': (1,0, 90), 'S': (0, -1, 180), 'W': (-1, 0, 270) }
    pos = (0,0)
    wayp = (10, 1)
    for inst in instructions:
        i = inst[:1]
        if i in directions:
            wayp = move(directions[i], int(inst[1:]), wayp)
        elif i in ['R', 'L']:
            angle = int(inst[1:])
            if i == 'L':
                angle *= -1
            wayp = rotate(wayp, angle)
        else:
            pos = move(wayp, int(inst[1:]), pos)
    return abs(0 - pos[0]) + abs(0 - pos[1])


def rotate(wayp, angle):
    s = math.sin(math.radians(angle))
    c = math.cos(math.radians(angle))

    px, py = wayp

    px1 = px * c + py * s
    py1 = -px * s + py * c
    return px1, py1


def move(direction, amount, pos):
    return (pos[0] + (amount * direction[0]), pos[1] + (amount * direction[1]))
