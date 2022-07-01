"""
Задача №2. Секция статьи "Задача №2."
Написать метод int32_to_ip, который принимает на вход 32-битное целое число
(integer) и возвращает строковое представление его в виде IPv4-адреса:
"""

import ipaddress


def int32_to_ip(int32):
    return str(ipaddress.ip_address(int32))

