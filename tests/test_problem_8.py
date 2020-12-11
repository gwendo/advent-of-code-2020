import unittest
from aoc.util.file_op import *
from aoc.day8.problem8 import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(5, find_loop(read_file("problem8_test_input.txt")))

    def test_something2(self):
        self.assertEqual(2025, find_loop(read_file("problem8_solution_input.txt")))

    def test_something3(self):
        self.assertEqual(2025, fix_loop(read_file("problem8_test_input.txt")))

    def test_something4(self):
        self.assertEqual(2001, fix_loop(read_file("problem8_solution_input.txt")))
if __name__ == '__main__':
    unittest.main()
