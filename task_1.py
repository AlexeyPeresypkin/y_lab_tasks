"""
Задача №1. Секция статьи "Задача №1."
Написать метод domain_name, который вернет домен из url адреса:
"""


def domain_name(url):
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

