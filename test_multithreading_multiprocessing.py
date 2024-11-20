import unittest
import threading
import multiprocessing
import time
from main import count_primes_in_range, simulate_heavy_computation

# Функція для виконання тесту у багатопоточному режимі
def run_threaded_tests():
    unittest.main(exit=False)

# Функція для виконання тесту у багатопроцесорному режимі
def run_multiprocessing_tests():
    unittest.main(exit=False)

# Клас тестів для обчислення простих чисел
class TestPrimeCounting(unittest.TestCase):
    def test_small_range(self):
        self.assertEqual(count_primes_in_range(1, 10), 4)  # Прості: 2, 3, 5, 7

    def test_large_range(self):
        self.assertEqual(count_primes_in_range(1, 10000), 1229)  # Прості до 10,000

    def test_very_large_range(self):
        self.assertEqual(count_primes_in_range(1, 50000), 5133)

# Клас тестів для важких обчислень
class TestHeavyComputation(unittest.TestCase):
    def test_factorial_small(self):
        self.assertEqual(simulate_heavy_computation(5), 120)

    def test_factorial_medium(self):
        self.assertEqual(simulate_heavy_computation(10), 3628800)

    def test_factorial_large(self):
        result = simulate_heavy_computation(15)  # Триваліший тест
        self.assertTrue(result > 0)

# Основна функція для запуску тестів
def run_tests(num_runs):
    threads = []
    processes = []

    # Запускаємо тести багатопоточним способом
    #for _ in range(num_runs):  # Виконуємо 100 разів
     #   thread = threading.Thread(target=run_threaded_tests)
     #   threads.append(thread)
      #  thread.start()

    # Запускаємо тести багатопроцесорним способом
    for _ in range(num_runs):  # Виконуємо 100 разів
        process = multiprocessing.Process(target=run_multiprocessing_tests)
        processes.append(process)
        process.start()

    # Очікуємо завершення всіх потоків
    #for thread in threads:
      #  thread.join()

    # Очікуємо завершення всіх процесів
    for process in processes:
        process.join()

if __name__ == '__main__':
    start_time = time.time()
    run_tests(100)  # Виконуємо 100 разів
    end_time = time.time()
    print(f"Total time taken for 100 runs: {end_time - start_time} seconds")
