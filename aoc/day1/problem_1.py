import itertools
from functools import reduce


def calc_expense_report(report_lines, tuple_size):
    combos = next(filter(lambda x: sum(list(x)) == 2020, itertools.combinations(report_lines, tuple_size)), (0, 0))
    return reduce(lambda x, y: x * y, list(combos))

