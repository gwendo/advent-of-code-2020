import unittest
from aoc.day3.problem3 import *
from aoc.util.file_op import *


class MyTestCase(unittest.TestCase):
    def test_test_input(self):
        self.assertEqual(7, traverse_slope((1,3), read_file('problem3_test_input.txt')))
    def test_test_input_list(self):
        self.assertEqual(336, traverse_slope_list([(1,3),(1,1), (1,5), (1,7), (2,1)], read_file('problem3_test_input.txt')))
    def test_solution_input(self):
        self.assertEqual(145, traverse_slope((1,3), read_file('problem3_solution_input.txt')))

    def test_test_solution_list(self):
        self.assertEqual(3424528800, traverse_slope_list([(1, 3), (1, 1), (1, 5), (1, 7), (2, 1)],
                                                      read_file('problem3_solution_input.txt')))
if __name__ == '__main__':
    unittest.main()
