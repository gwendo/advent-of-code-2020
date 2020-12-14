import unittest
from aoc.day13.problem13 import *
from aoc.util.file_op import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(295, find_earliest_bus(read_file("problem13_test_input.txt")))

    def test_something2(self):
        self.assertEqual(295, find_earliest_bus(read_file("problem13_solution_input.txt")))

    def test_something3(self):
        self.assertEqual(1068781, find_earliest_offset(read_file("problem13_test_input.txt")))

    def test_something4(self):
        self.assertEqual(1, find_earliest_offset(read_file("problem13_solution_input.txt")))
if __name__ == '__main__':
    unittest.main()
