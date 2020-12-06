from functools import reduce


def traverse_slope(angle, slope):
    x, y = angle
    end = len(slope)
    curr_pos = list((0, 0))
    tree_count = 0
    while curr_pos[0]+1 < end:
        curr_pos[0] += x
        curr_pos[1] = ((curr_pos[1] + y) % (len(slope[0])))
        if slope[curr_pos[0]][curr_pos[1]] == '#':
            tree_count += 1
    return tree_count


def traverse_slope_list(angle_list, slope):
    return reduce(lambda x, y: x * y, list(map(lambda angle: traverse_slope(angle, slope), angle_list)))
