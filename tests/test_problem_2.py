import unittest
from aoc.day2.problem_2 import *
from aoc.util.file_op import *


class MyTestCase(unittest.TestCase):
    def test_is_password_valid(self):
        self.assertEqual(True, is_password_valid("1-3 a: abcde"))

    def test_count_valid_passwords(self):
        self.assertEqual(2, find_valid_passwords(read_file('problem2_test_input.txt'), is_password_valid))

    def test_count_valid_solution_passwords(self):
        self.assertEqual(445, find_valid_passwords(read_file('problem2_solution_input.txt'), is_password_valid))

    def test_count_valid_solution_passwords2(self):
        self.assertEqual(491, find_valid_passwords(read_file('problem2_solution_input.txt'), is_password_valid2))

if __name__ == '__main__':
    unittest.main()
