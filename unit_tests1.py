#!/usr/bin/python3
import unittest
from nthprime import n_th_primes


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_case1(self):
        nthprimecalculator = n_th_primes()
        self.assertEqual(nthprimecalculator.get_n_th_prime(2), 3)

    def test_case2(self):
        nthprimecalculator = n_th_primes()
        self.assertEqual(nthprimecalculator.get_n_th_prime(5), 11)

    def test_case3(self):
        nthprimecalculator = n_th_primes()
        self.assertEqual(nthprimecalculator.get_n_th_prime(10), 29)


if __name__ == '__main__':
    unittest.main()