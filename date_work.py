# 1 задание. Печатные газеты использовали свой формат дат для каждого выпуска.
# Для каждой газеты из списка напишите формат указанной даты для перевода в объект datetime: 

from datetime import datetime

The_Moscow_Times = datetime.strptime('Wednesday, October 2, 2002', '%A, %B %d, %Y')
The_Guardian = datetime.strptime('Friday, 11.10.13', '%A, %d.%m.%y')
Daily_News = datetime.strptime('Thursday, 18 August 1977', '%A, %d %B %Y')

# 2 задание. Дан поток дат в формате YYYY-MM-DD, в которых встречаются некорректные значения:
# stream = ['2018-04-02', '2018-02-29', '2018-19-02']
# Напишите функцию, которая проверяет эти даты на корректность. Т. е. для каждой даты возвращает True (дата корректна) или False (некорректная дата).

stream = ['2018-04-02', '2018-02-29', '2018-19-02']

def correct_date(li):
    for i in li:
        if i == str(datetime.strptime(stream[0], '%Y-%m-%d'))[0:10]:
            print(True)
        else:
            print(False)

correct_date(stream)
