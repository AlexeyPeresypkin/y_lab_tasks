"""
Задача №3. Секция статьи "Задача №3."
Написать метод zeros, который принимает на вход целое число (integer) и
возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) заданного числа:
"""


def zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count
