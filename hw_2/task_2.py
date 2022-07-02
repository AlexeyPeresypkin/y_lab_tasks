from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    @staticmethod
    def period_delta(date1, date2, result):
        start = datetime.date(date1)
        periods = (date2 - date1 + timedelta(days=1)).days
        for day in range(periods):
            date = (start + timedelta(days=day)).strftime('%Y-%m-%d %H:%M:%S')
            result.append(date)
        return result

    def schedule(self) -> Generator[datetime, None, None]:
        result = []
        for date in self.dates:
            self.period_delta(date[0], date[1], result)
        for item in result:
            yield item


m = Movie('sw', [
    (datetime(2020, 1, 1), datetime(2020, 1, 7)),
    (datetime(2020, 1, 15), datetime(2020, 2, 7))
])
for d in m.schedule():
    print(d)
