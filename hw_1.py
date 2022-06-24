import ipaddress
from itertools import combinations
import math


def domain_name(url):
    """
    Задача №1. Секция статьи "Задача №1."
    Написать метод domain_name, который вернет домен из url адреса:
    """
    x = url.split("/")
    if x[0] == "https:" or x[0] == "http:":
        x = x[2].split(".")
    else:
        x = x[0].split(".")
    if x[0] == 'www':
        domain = x[1]
    else:
        domain = x[0]
    return domain


def int32_to_ip(int32):
    """
    Задача №2. Секция статьи "Задача №2."
    Написать метод int32_to_ip, который принимает на вход 32-битное целое число
    (integer) и возвращает строковое представление его в виде IPv4-адреса:
    """
    return str(ipaddress.ip_address(int32))


def zeros(n):
    """
    Задача №3. Секция статьи "Задача №3."
    Написать метод zeros, который принимает на вход целое число (integer) и
    возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) заданного числа:
    """
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count


def bananas(s) -> set:
    """
    Задача №4. Секция статьи "Задача №4."
    Написать метод bananas, который принимает на вход строку и
    возвращает количество слов «banana» в строке.
    """
    find_word = 'banana'
    result = set()
    for combination in combinations(range(len(s)), len(s) - len(find_word)):
        list_s = list(s)
        for index in combination:
            list_s[index] = '-'
        variant = ''.join(list_s)
        if variant.replace('-', '') == find_word:
            result.add(variant)
    return result


def count_find_num(primes_l, limit):
    """
    Задача №5. Секция статьи "Задача №5."
    Написать метод count_find_num, который принимает на вход список простых множителей (primesL) и целое число,
    предел (limit), после чего попробуйте сгенерировать по порядку все числа.
    Меньшие значения предела, которые имеют все и только простые множители простых чисел primesL.
    """
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
