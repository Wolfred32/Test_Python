def factorial(n):
    """
    Вычисляет факториал числа n.

    Функция поддерживает только неотрицательные целые числа.

    Примеры:
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(3)
    6
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: Factorial is only defined for non-negative integers
    """
    if n < 0:
        raise ValueError("Factorial is only defined for non-negative integers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Основные случаи: n = 0, n = 1, небольшие положительные значения.
# Крайние случаи: отрицательные значения, при которых функция должна выдавать ошибку ValueError.
# Простая проверка: n = 1 и n = 0, где результат предсказуем — 1.