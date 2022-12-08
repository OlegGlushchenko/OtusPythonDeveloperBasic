"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*nums):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num ** 2 for num in nums]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    if num <= 1:
        return None
    is_simple = True
    checks = (num % i == 0 for i in range(2, (num // 2) + 1))
    for check in checks:
        if check:
            is_simple = False
            break
    return is_simple


def filter_numbers(nums, num_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if num_type == ODD:
        return list(filter(lambda num: (num % 2 != 0), nums ))
    if num_type == EVEN:
        return list(filter(lambda num: (num % 2 == 0), nums ))
    if num_type == PRIME:
        return list(filter(is_prime, nums ))