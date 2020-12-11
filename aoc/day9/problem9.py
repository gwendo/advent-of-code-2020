from itertools import combinations


def find_number(input, preamble):
    curr_window = input[:preamble]
    remaining_input = input[preamble:]
    while len(remaining_input) > 0 and is_valid(remaining_input[0], curr_window):
        curr_window = curr_window[1:]
        curr_window.append(remaining_input[0])
        remaining_input = remaining_input[1:]
    return remaining_input[0]


def is_valid(l, curr_window):
    return {l}.issubset(set(list(map(lambda c: c[0] + c[1], combinations(curr_window, 2)))))


def find_weakness(input, preamble):
    weak = find_number(input, preamble)
    pairs = combinations(range(len(input)), 2)
    weakness = next(x for x in pairs if sum(input[x[0]:x[1]]) == weak)
    return min(input[weakness[0]:weakness[1]]) + max(input[weakness[0]:weakness[1]])
