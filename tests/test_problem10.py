import unittest
from aoc.util.file_op import *
from aoc.day10.problem10 import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(220, find_diff(list(map(int, read_file("problem10_test_input.txt")))))

    def test_something2(self):
        self.assertEqual(1848, find_diff(list(map(int, read_file("problem10_solution_input.txt")))))

    def test_something3(self):
        self.assertEqual(8, find_all_combos(list(map(int, read_file("problem10_simple_test_input.txt")))))

    def test_something4(self):
        self.assertEqual(19208, find_all_combos(list(map(int, read_file("problem10_test_input.txt")))))

    def test_something5(self):
        self.assertEqual(8099130339328, find_all_combos(list(map(int, read_file("problem10_solution_input.txt")))))
if __name__ == '__main__':
    unittest.main()
