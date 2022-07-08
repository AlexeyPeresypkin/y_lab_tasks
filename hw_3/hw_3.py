"""
Напишите функцию-декоратор, которая сохранит (закэширует) значение декорируемой функции multiplier (Чистая функция).
Если декорируемая функция будет вызвана повторно с теми же параметрами — декоратор должен вернуть сохранённый результат, не выполняя функцию.
"""

import redis

r = redis.Redis()


def cache(func):
    def wrapper(number: int):
        redis_data = r.get(number)
        if redis_data:
            return redis_data.decode()
        result = func(number)
        r.set(number, result)
        return result

    return wrapper


@cache
def multiplier(number: int):
    return number * 2


"""
Надо написать декоратор для повторного выполнения декорируемой функции через некоторое время. 
Использует наивный экспоненциальный рост времени повтора (factor) до граничного времени ожидания (border_sleep_time).

В качестве параметров декоратор будет получать:

call_count - число, описывающее кол-во раз запуска функций;
start_sleep_time - начальное время повтора;
factor - во сколько раз нужно увеличить время ожидания;
border_sleep_time - граничное время ожидания.
Формула:

t = start_sleep_time * 2^(n) if t < border_sleep_time
t = border_sleep_time if t >= border_sleep_time

Ожидаемый результат:

Кол-во запусков = call_count (допустим 3)
Начало работы
Запуск номер 1. Ожидание: t секунд. Результат декорируемой функций = func_result.
Запуск номер 2. Ожидание: t секунд. Результат декорируемой функций = func_result.
...
Конец работы
"""

import time


def try_repeat(call_count, start_sleep_time, factor, border_sleep_time):
    def inner(func):

        def wrapper(*args, **kwargs):
            nonlocal call_count, start_sleep_time
            for number in range(1, call_count + 1):
                time.sleep(start_sleep_time)
                result = func(*args, **kwargs)
                print(f'Запуск номер {number}. '
                      f'Ожидание: {start_sleep_time} сек. '
                      f'Результат декорируемой функций = {result}')
                start_sleep_time *= 2 * factor
                if border_sleep_time <= start_sleep_time:
                    start_sleep_time = border_sleep_time
            print('Конец работы')

        return wrapper

    return inner
