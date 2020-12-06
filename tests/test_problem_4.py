import unittest
from aoc.util.file_op import *
from aoc.day4.problem4 import *

class MyTestCase(unittest.TestCase):
    def test_test_input(self):
        self.assertEqual(2, count_valid_passwords(read_file("problem4_test_input.txt")))

    def test_solution_input(self):
        self.assertEqual(145, count_valid_passwords(read_file("problem4_solution_input.txt")))

    def test_valid_passports(self):
        self.assertTrue(all(map(validate_password, extract_passwords(read_file("problem4_valid_passport.txt")))))

    def test_invalid_passports(self):
        self.assertTrue(all(map(lambda res: not res, map(validate_password, extract_passwords(read_file("problem4_invalid_passports.txt"))))))

    def test_validations(self):
        self.assertTrue(byr("2002"))
        self.assertFalse(byr("2003"))

        self.assertTrue(hgt("60in"))
        self.assertTrue(hgt("190cm"))
        self.assertFalse(hgt("190in"))
        self.assertFalse(hgt("190"))

        #hcl
        self.assertTrue(hcl("#123abc"))
        self.assertFalse(hcl("#123abz"))
        self.assertFalse(hcl("123abc"))

        #ecl
        self.assertTrue(ecl("brn"))
        self.assertFalse(ecl("wat"))

        #pid
        self.assertTrue(pid("000000001"))
        self.assertFalse(pid("0123456789"))


if __name__ == '__main__':
    unittest.main()
