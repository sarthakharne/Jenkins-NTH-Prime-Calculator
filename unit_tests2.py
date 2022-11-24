#!/usr/bin/python3
import unittest
from nthprime import n_th_primes


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.nthprimecalculator = n_th_primes()

    def test_case1(self):
        self.assertEqual(self.nthprimecalculator.get_n_th_prime(-1), self.nthprimecalculator.ERROR_FLAG)

    def test_case2(self):
        self.assertEqual(self.nthprimecalculator.get_n_th_prime(5.2), self.nthprimecalculator.ERROR_FLAG)


if __name__ == '__main__':
    unittest.main()