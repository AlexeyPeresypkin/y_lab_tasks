"""
1. Задача на циклический итератор. Секция статьи "1. Задача на циклический итератор."
Надо написать класс CyclicIterator.
Итератор должен итерироваться по итерируемому объекту (list, tuple, set, range, Range2, и т. д.),
и когда достигнет последнего элемента, начинать сначала.
"""
import time


class CyclicIterator:
    def __init__(self, obj):
        self.obj = obj
        self.iter = iter(obj)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iter)
        except StopIteration:
            self.iter = iter(self.obj)
            return next(self.iter)


"""
2. Задача на разжатие массива. Секция статьи "2. Задача на разжатие массива."
У каждого фильма есть расписание, по каким дням он идёт в кинотеатрах. 
Для эффективности дни проката хранятся периодами дат. Например, прокат фильма проходит с 1 по 7 января, 
а потом показ возобновляется с 15 января по 7 февраля:
"""

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        for date_1, date_2 in self.dates:
            for day in range((date_2 - date_1).days + 1):
                yield date_1 + timedelta(day)


m = Movie('sw', [
    (datetime(2020, 1, 1), datetime(2020, 1, 7)),
    (datetime(2020, 1, 15), datetime(2020, 2, 7))
])

if __name__ == '__main__':
    for d in m.schedule():
        print(d)

    time.sleep(3)

    cyclic_iterator = CyclicIterator(range(3))
    for i in cyclic_iterator:
        print(i)
