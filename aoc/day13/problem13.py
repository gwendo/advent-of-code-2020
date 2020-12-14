import operator
from functools import reduce
def find_earliest_bus(schedule):
    time = int(schedule[0])
    buses = list(map(lambda b: (b, find_larger_than(time, b) - time),
                     (map(int, filter(lambda s: not s == 'x', schedule[1].split(','))))))
    my_bus = reduce(lambda a,b: a if a[1] < b[1] else b, buses)
    return my_bus[0] * my_bus[1]


def find_larger_than(t, b):
    sum = 0
    while sum <= t:
        sum += b
    print(b, sum)
    return sum


def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1


def find_earliest_offset(schedule):
    buses = list(schedule[1].split(','))
    ix = range(len(buses))
    ix_buses = zip(ix, buses)
    ix_buses = list(map(lambda bx: (bx[0], int(bx[1])), filter(lambda ib: not ib[1] == 'x', ix_buses)))
    sorted_buses = sorted(ix_buses, key=lambda b: b[1], reverse=True)
    step = 1
    solved = False
    ans = 0
    for curr_bus in sorted_buses:
        solved = False
        print(curr_bus)
        while not solved:
            if not ans % curr_bus[1] == (curr_bus[1] - curr_bus[0]) % curr_bus[1]:
                ans += step
            else:
                step *= curr_bus[1]
                solved = True
    return ans


