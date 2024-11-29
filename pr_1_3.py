import unittest
from pr_1_1 import factorial


class TestFactorial(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(1), 1)

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            factorial(-1)


if __name__ == '__main__':
    unittest.main()

# Основные случаи: n = 0, n = 1, небольшие положительные значения.
# Крайние случаи: отрицательные значения, при которых функция должна выдавать ошибку ValueError.
# Простая проверка: n = 1 и n = 0, где результат предсказуем — 1.