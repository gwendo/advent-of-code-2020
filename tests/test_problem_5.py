import unittest
from aoc.day5.problem5 import *
from aoc.util.file_op import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(357, find_seat_id("FBFBBFFRLR"))

    def test_max(self):
        self.assertEqual(933, max(map(find_seat_id, read_file("problem5_solution_input.txt"))))

    def test_find_my_seat(self):
        self.assertEqual(711, find_available_seat(sorted(list(map(find_seat_id, read_file("problem5_solution_input.txt"))))))


if __name__ == '__main__':
    unittest.main()
