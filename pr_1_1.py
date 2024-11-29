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
    # Основные тесты для функции factorial
    assert factorial(5) == 120, "Ошибка: factorial(5) должен вернуть 120"
    assert factorial(0) == 1, "Ошибка: factorial(0) должен вернуть 1"
    assert factorial(1) == 2, "Ошибка: factorial(1) должен вернуть 1"
    assert factorial(3) == 6, "Ошибка: factorial(3) должен вернуть 6"
    
    # Проверка на ошибку при вводе отрицательного числа
    try:
        factorial(-1)
    except ValueError as e:
        assert str(e) == "Factorial is only defined for non-negative integers", \
            "Ошибка: неправильное сообщение об ошибке для factorial(-1)"

# Основные случаи: n = 0, n = 1, небольшие положительные значения.
# Крайние случаи: отрицательные значения, при которых функция должна выдавать ошибку ValueError.
# Простая проверка: n = 1 и n = 0, где результат предсказуем — 1.