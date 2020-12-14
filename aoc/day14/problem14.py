import re
from copy import copy, deepcopy
def init_program(input):
    mask = []
    memory = {}
    for line in input:
        parts = line.split("=")
        if parts[0].startswith('mask'):
            mask = list(parts[1].strip())
        else:
            m = re.search("\[(.*?)\]", parts[0]).group(1)
            num = int(parts[1])
            bi_num = list("{0:{fill}36b}".format(num, fill='0'))
            for i,b in enumerate(mask):
                if not b == 'X':
                    bi_num[i] = b
            memory[m] = int("".join(bi_num), 2)

    return sum(list(filter(lambda v: v != 0, memory.values())))


def init_program2(input):
    mask = []
    memory = {}
    for line in input:
        parts = line.split("=")
        if parts[0].startswith('mask'):
            mask = list(parts[1].strip())
        else:
            addr_point = re.search("\[(.*?)\]", parts[0]).group(1)
            num = int(parts[1])
            bi_addr = list("{0:{fill}36b}".format(int(addr_point), fill='0'))
            addr_points = [bi_addr]
            for i,b in enumerate(mask):
                if b == '1':
                    for ap in addr_points:
                        ap[i] = '1'
                elif b == 'X':
                    new_copies = []
                    for ap in addr_points:
                        copy = deepcopy(ap)
                        copy[i] = '0'
                        new_copies.append(copy)
                        ap[i] = '1'
                    addr_points.extend(new_copies)

            for p in addr_points:
                memory[str(int("".join(p), 2))] = num

    return sum(list(filter(lambda v: v != 0, memory.values())))
