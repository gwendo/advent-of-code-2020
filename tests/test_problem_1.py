import unittest
from aoc.day1.problem_1 import *
from aoc.util.file_op import *


class Problem1TestCase(unittest.TestCase):
    def test_calculate_expenses(self):
        self.assertEqual(514579, calc_expense_report(map(int, read_file('problem1_test_input.txt')), 2))

    def test_calculate_expenses_problem(self):
        self.assertEqual(355875, calc_expense_report(map(int, read_file('problem1_solution_input.txt')), 2))

    def test_calculate_expenses_three(self):
        self.assertEqual(140379120, calc_expense_report(map(int, read_file('problem1_solution_input.txt')), 3))

if __name__ == '__main__':
    unittest.main()
