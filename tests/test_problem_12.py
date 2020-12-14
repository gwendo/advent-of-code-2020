import unittest
from aoc.util.file_op import *
from aoc.day12.problem12 import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(25, navigate(read_file("problem12_test_input.txt")))

    def test_something3(self):
        self.assertEqual(286, navigate2(read_file("problem12_test_input.txt")))

    def test_something2(self):
        self.assertEqual(25, navigate(read_file("problem12_solution_input.txt")))

    def test_something4(self):
        self.assertEqual(286, navigate2(read_file("problem12_solution_input.txt")))
if __name__ == '__main__':
    unittest.main()
