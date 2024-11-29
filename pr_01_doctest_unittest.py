 
"""Практическая работа №1."""

# Вводная часть
# -------------

"""
Существует несколько подходов к тестированию:
- непосредственное использование инструкции assert,
- doctest,
- unittest,
- pytest и др. внешние инструменты
"""

# Задание
# ----------

"""
В данной практической работе нужно использовать первые три подхода. Эти подходы доступны "из коробки" (не нужно устанавливать дополнительные пакеты).

Следует выбрать любой алгоритм: например, алгоритм сортировки, рассчёт значения функции (квадратичной, тригонометрической).

А потом протестировать тремя вариантами:
- непосредственно использовав инструкции assert,
- doctest,
- unittest,
"""

# Шаблон
# ----------

def algo_func(*args, **kwargs):
    """Функция, реализующая ваш алгоритм/математическую функцию.
    Вместо '...' напишите doctest
    ...
    """
    # здесь реализация алгоритма
    ...

if __name__ == '__name__':
    # здесь используйте инструкции assert
    assert algo_func(123) == 321, "функция работает не верно"
    ...

    # здесь вызовите код проверки через doctest
    ...

    # для unittest сделайте дополнительный файл в который поместите его тесты.


# Самопроверка
# ---------------

# 1. хорошо если выбранный/реализованный алгоритм/функция имеет ветвление if-else, цикл
# 2. придумайте "хорошие тесты", который позволят пройти все инструкция функции,
# 3. укажите крайние случаи для вашего алгоритма в комментарии или, лучше, в докстринге вашего модуля.
