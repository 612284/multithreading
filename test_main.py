import unittest
from main import count_primes_in_range

class TestPrimeCounting(unittest.TestCase):
    def test_small_range(self):
        self.assertEqual(count_primes_in_range(1, 10), 4)  # Прості: 2, 3, 5, 7

    def test_medium_range(self):
        self.assertEqual(count_primes_in_range(1, 100), 25)

    def test_large_range(self):
        self.assertEqual(count_primes_in_range(1, 1000), 168)

if __name__ == '__main__':
    unittest.main()
