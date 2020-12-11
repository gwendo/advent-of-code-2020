from copy import copy, deepcopy


def find_occupied(seating_chart, rule, limit):
    matr = [[seat for seat in row] for row in seating_chart]
    prev_matr = deepcopy(matr)
    curr_matr = apply_rule(matr, prev_matr, rule, limit)
    while True:
        if prev_matr != curr_matr:
            # for r in prev_matr:
            #     print(r)
            # print('---------------------------------')
            prev_matr = deepcopy(curr_matr)
            curr_matr = apply_rule(curr_matr, prev_matr, rule, limit)
        else:
            break
    return [c for row in curr_matr for c in row].count('#')


def apply_rule(my_matr, p_matr, rule, limit):
    for r in range(len(my_matr)):
        for c in range(len(my_matr[0])):
            if my_matr[r][c] != '.':
                if my_matr[r][c] == 'L' and rule(r, c, p_matr) == 0:
                    my_matr[r][c] = '#'
                elif my_matr[r][c] == '#' and rule(r, c, p_matr) >= limit:
                    my_matr[r][c] = 'L'
    return my_matr

def visible_count(r, c, m_matr):
    n = (-1, 0)
    ne = (-1, 1)
    e = (0, 1)
    se = (1,1)
    s = (1, 0)
    sw = (1, -1)
    w = (0, -1)
    nw = (-1, -1)
    directions = [n, ne, e ,se, s ,sw, w, nw]
    res = list(map(lambda dir: seen(r,c, dir, m_matr), directions))
    return res.count(True)


def seen(r, c, dir, m_matr):
    if r + dir[0] < 0 or r + dir[0] >= len(m_matr):
        return False
    if c + dir[1] < 0 or c + dir[1] >= len(m_matr[0]):
        return False
    if m_matr[r + dir[0]][c + dir[1]] == '#':
        return True
    if m_matr[r + dir[0]][c + dir[1]] == 'L':
        return False
    return seen(r + dir[0], c + dir[1], dir,  m_matr)



def adjecent_count(r, c, m_matr):
    adj = []
    for y in range(max(0, r - 1), min(r + 2, len(m_matr))):
        for x in range(max(0, c-1), min(c+2, len(m_matr[0]))):
            if not (x == c and y == r):
                adj.append(m_matr[y][x])
    return adj.count('#')