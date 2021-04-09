# 1 задание. Печатные газеты использовали свой формат дат для каждого выпуска.
# Для каждой газеты из списка напишите формат указанной даты для перевода в объект datetime: 

from datetime import datetime

The_Moscow_Times = datetime.strptime('Wednesday, October 2, 2002', '%A, %B %d, %Y')
The_Guardian = datetime.strptime('Friday, 11.10.13', '%A, %d.%m.%y')
Daily_News = datetime.strptime('Thursday, 18 August 1977', '%A, %d %B %Y')
