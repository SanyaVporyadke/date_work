# 1 задание. Печатные газеты использовали свой формат дат для каждого выпуска.
# Для каждой газеты из списка напишите формат указанной даты для перевода в объект datetime: 

from datetime import datetime
from datetime import timedelta

The_Moscow_Times = datetime.strptime('Wednesday, October 2, 2002', '%A, %B %d, %Y')
The_Guardian = datetime.strptime('Friday, 11.10.13', '%A, %d.%m.%y')
Daily_News = datetime.strptime('Thursday, 18 August 1977', '%A, %d %B %Y')

# 2 задание. Дан поток дат в формате YYYY-MM-DD, в которых встречаются некорректные значения:
# stream = ['2018-04-02', '2018-02-29', '2018-19-02']
# Напишите функцию, которая проверяет эти даты на корректность. Т. е. для каждой даты возвращает True (дата корректна) или False (некорректная дата).

#создать отдельную функцию на корректность даты
stream = ['2018-04-02', '2018-02-29', '2018-19-02']

def correct_date(str_d):
        try:
            if str_d == datetime.strptime(str_d, '%Y-%m-%d').strftime('%Y-%m-%d'):
                return True
        except ValueError:
            return False


def correct_li_date(li):
    for i in li:
        print(correct_date(i))


#3 задание. Напишите функцию date_range, которая возвращает список дат за период от start_date до end_date. Даты должны вводиться в формате YYYY-MM-DD.
#  В случае неверного формата или при start_date > end_date должен возвращаться пустой список.

def date_range(start_date, end_date):
    res = []
    if correct_date(start_date) == False and correct_date(end_date) == False or start_date > end_date:
        return res
    else:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        i = 0
        current_date = start_date
        while current_date <= end_date:
            res.append(current_date.strftime('%Y-%m-%d'))
            current_date += timedelta(days=1)
    return res

# 4 задание.
DEFAULT_USER_COUNT = 3

def delete_and_return_last_user(region, default_list=['A100', 'A101', 'A102']):
#Удаляет из списка default_list последнего пользователя и возвращает ID нового последнего пользователя.
    element_to_delete = default_list[-1]
    default_list.remove(element_to_delete)
    return default_list[-2]

# print(delete_and_return_last_user(1))
# print(delete_and_return_last_user(1))
# ответ: в списке 3 элемента, при удалении последнего остаюся элементы с индексами -2(А101) и -3(А100),
# но при повторном вызове функции A101 становится -1, а А100 -2, сначала происходит удаление и затем попытка вернуть значение с индексом -2,
# но тогда А100 остается с индексом -1, а элемента с индексом -2 уже просто не существует.
# ошибка list out of range возникает при попытке обращения к индексу элемента, которого не существует.
