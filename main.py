import math
import time

def is_prime(n):
    """Перевіряє, чи є число простим."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def count_primes_in_range(start, end):
    """Рахує кількість простих чисел у заданому діапазоні."""
    return sum(1 for i in range(start, end + 1) if is_prime(i))

def simulate_heavy_computation(n):
    """Імітує важкий розрахунок, наприклад, обчислення факторіалу."""
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total
