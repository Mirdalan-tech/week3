#Задание
#Напечатайте в консоль даты: вчера, сегодня, месяц назад
#Превратите строку "01/01/17 12:10:03.234567" в объект datetime

from datetime import datetime, date, timedelta
dt_now=datetime.now()
date_str = "01/01/17 12:10:03.234567"
date_dt = datetime.strptime(date_str, '%m/%d/%y %H:%M:%S.%f')
delta = timedelta(days= 1)
delta2 = timedelta()
print(dt_now - delta)
print(dt_now - delta*30)
print(dt_now)
print(date_dt)
