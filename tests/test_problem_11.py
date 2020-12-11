import unittest
from aoc.util.file_op import *
from aoc.day11.problem11 import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(37, find_occupied(read_file("problem11_test_input.txt"), adjecent_count, 4))

    def test_something2(self):
        self.assertEqual(2126, find_occupied(read_file("problem11_solution_input.txt"), adjecent_count, 4))

    def test_something3(self):
        self.assertEqual(26, find_occupied(read_file("problem11_test_input.txt"), visible_count, 5))

    def test_something4(self):
        self.assertEqual(8, visible_count(4,3, [[seat for seat in row] for row in read_file("problem_11_seen_test.txt")]))

    def test_something5(self):
        self.assertEqual(0, visible_count(1,1, [[seat for seat in row] for row in read_file("problem_11_seen2.txt")]))

    def test_something6(self):
        self.assertEqual(5, visible_count(9,8, [[seat for seat in row] for row in read_file("problem11_seen3.txt")]))

    def test_something7(self):
        self.assertEqual(1914, find_occupied(read_file("problem11_solution_input.txt"), visible_count, 5))
if __name__ == '__main__':
    unittest.main()
