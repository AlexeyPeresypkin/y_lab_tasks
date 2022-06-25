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
    all_values = []
    total = math.prod(primes_l)
    all_values.append(total)
    if total > limit:
        return []

    for num in primes_l:
        for total in all_values:
            value = num * total
            if value <= limit and value not in all_values:
                all_values.append(value)
    return [len(all_values), max(all_values)]
