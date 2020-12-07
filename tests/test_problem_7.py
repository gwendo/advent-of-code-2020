import unittest
from aoc.util.file_op import *
from aoc.day7.problem7 import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(4, find_bag_count(read_file("problem7_test_input.txt")))

    def test_something2(self):
        self.assertEqual(235, find_bag_count(read_file("problem7_solution_input.txt")))

    def test_something3(self):
        self.assertEqual(32, find_bag_contains(read_file("problem7_test_input.txt")))

    def test_something4(self):
        self.assertEqual(158493, find_bag_contains(read_file("problem7_solution_input.txt")))

if __name__ == '__main__':
    unittest.main()
