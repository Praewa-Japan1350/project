import unittest
from coe_number.number_utils import is_prime_list


class PrimeListTest(unittest.TestCase):

    def test_all_prime(self):
        self.assertTrue(is_prime_list([2, 3, 5, 7]))

    def test_contains_non_prime(self):
        self.assertFalse(is_prime_list([2, 4, 5]))

    def test_contains_one(self):
        self.assertFalse(is_prime_list([1, 2, 3]))

    def test_contains_zero(self):
        self.assertFalse(is_prime_list([0, 2, 3]))

    def test_contains_negative(self):
        self.assertFalse(is_prime_list([-3, 2, 5]))

    def test_empty_list(self):
        self.assertTrue(is_prime_list([]))

    def test_single_prime(self):
        self.assertTrue(is_prime_list([7]))

    def test_single_not_prime(self):
        self.assertFalse(is_prime_list([9]))


if __name__ == "__main__":
    unittest.main()
