import unittest
from main import count_primes_in_range, simulate_heavy_computation

class TestPrimeCounting(unittest.TestCase):
    def test_small_range(self):
        self.assertEqual(count_primes_in_range(1, 10), 4)  # Прості: 2, 3, 5, 7

    def test_large_range(self):
        self.assertEqual(count_primes_in_range(1, 10000), 1229)  # Прості до 10,000

    def test_very_large_range(self):
        self.assertEqual(count_primes_in_range(1, 50000), 5133)

class TestHeavyComputation(unittest.TestCase):
    def test_factorial_small(self):
        self.assertEqual(simulate_heavy_computation(5), 120)

    def test_factorial_medium(self):
        self.assertEqual(simulate_heavy_computation(10), 3628800)

    def test_factorial_large(self):
        result = simulate_heavy_computation(15)  # Триваліший тест
        self.assertTrue(result > 0)

if __name__ == '__main__':
    unittest.main()
