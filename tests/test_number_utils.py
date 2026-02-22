from coe_number.number_utils import is_prime_list
import unittest


class PrimeListTest(unittest.TestCase):

    # ✅ กรณีปกติ (True)
    def test_all_prime(self):
        self.assertTrue(is_prime_list([2, 3, 5, 7]))

    # ✅ มีเลขไม่ prime
    def test_contains_non_prime(self):
        self.assertFalse(is_prime_list([2, 4, 5]))

    # ✅ มีเลข 1 (ไม่ใช่ prime)
    def test_contains_one(self):
        self.assertFalse(is_prime_list([1, 2, 3]))

    # ✅ มีเลข 0
    def test_contains_zero(self):
        self.assertFalse(is_prime_list([0, 2, 3]))

    # ✅ มีเลขติดลบ
    def test_contains_negative(self):
        self.assertFalse(is_prime_list([-3, 2, 5]))

    # ✅ list ว่าง (loop ไม่ทำงานเลย)
    def test_empty_list(self):
        self.assertTrue(is_prime_list([]))

    # ✅ เลขเดียวและเป็น prime
    def test_single_prime(self):
        self.assertTrue(is_prime_list([]))
    def test_single_not_prime(self):
        self.assertFalse(is_prime_list([9]))