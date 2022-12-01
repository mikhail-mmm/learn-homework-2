"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

import datetime as dt

def print_days():
    today = dt.date.today().strftime("%d.%m.%Y")
    yesterday = (dt.date.today() - dt.timedelta(days=1)).strftime("%d.%m.%Y")
    past_date = (dt.date.today() - dt.timedelta(days=30)).strftime("%d.%m.%Y")
    print(f'Today: {today}.\nYesterday: {yesterday}.\n30 days ago: {past_date}')


def str_2_datetime(date_string):
    date_obj = dt.datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return date_obj

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
