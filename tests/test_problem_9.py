import unittest

from aoc.util.file_op import *
from aoc.day9.problem9 import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(find_number(list(map(lambda x: int(x), read_file("problem9_test_input.txt"))), 5), 127)

    def test_something2(self):
        self.assertEqual(find_number(list(map(lambda x: int(x), read_file("problem9_solution_input.txt"))), 25), 127)

    def test_something3(self):
        self.assertEqual(find_weakness(list(map(lambda x: int(x), read_file("problem9_test_input.txt"))), 5), 62)

    def test_something4(self):
        self.assertEqual(find_weakness(list(map(lambda x: int(x), read_file("problem9_solution_input.txt"))), 25), 62)
if __name__ == '__main__':
    unittest.main()
