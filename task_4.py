"""
Задача №4. Секция статьи "Задача №4."
Написать метод bananas, который принимает на вход строку и
возвращает количество слов «banana» в строке.
"""

from itertools import combinations


def bananas(s) -> set:
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
