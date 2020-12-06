import unittest
from aoc.util.file_op import *
from aoc.day6.problem6 import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(6911, group_answers(read_file("problem6_solution_input.txt")))

    def test_something_all(self):
        self.assertEqual(3473, group_answers_all(read_file("problem6_solution_input.txt")))

if __name__ == '__main__':
    unittest.main()
