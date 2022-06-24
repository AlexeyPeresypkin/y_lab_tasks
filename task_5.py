"""
Задача №5. Секция статьи "Задача №5."
Написать метод count_find_num, который принимает на вход список простых множителей (primesL) и целое число,
предел (limit), после чего попробуйте сгенерировать по порядку все числа.
Меньшие значения предела, которые имеют все и только простые множители простых чисел primesL.
"""
import math


def count_find_num(primes_l, limit):
    valid_factors = []
    all_factors = []

    for number in range(math.prod(primes_l), limit + 1):
        factors = []
        divisor = 2
        while divisor <= number:
            if number % divisor == 0:
                if divisor not in primes_l:
                    factors.clear()
                    break
                factors.append(divisor)
                number //= divisor
            else:
                divisor += 1
        all_factors.append(factors)

    for factor in all_factors:
        if set(primes_l) == set(factor):
            valid_factors.append(factor)

    if valid_factors:
        iterations = len(valid_factors)
        max_number = max([math.prod(factor) for factor in valid_factors])
        return [iterations, max_number]
    else:
        return []
