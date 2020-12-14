import unittest
from aoc.util.file_op import *
from aoc.day14.problem14 import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(165, init_program(read_file("problem14_test_input.txt")))

    def test_something2(self):
        self.assertEqual(7440382076205, init_program(read_file("problem14_solution_input.txt")))

    def test_something3(self):
        self.assertEqual(208, init_program2(read_file("problem14_test_input2.txt")))

    def test_something4(self):
        self.assertEqual(4200656704538, init_program2(read_file("problem14_solution_input.txt")))

if __name__ == '__main__':
    unittest.main()
