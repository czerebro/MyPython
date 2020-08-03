#using library datetime

from datetime import date, datetime, timedelta
import  locale

date
today = date.today()
print(today)
print(today.day)
print(today.month)
print(today.year)
print(today.weekday()) #monday=0, sunday=6

now = datetime.now()

print(now, sep='\n')
print(now.hour)
print(now.minute)
print(now.second)

days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
print(days[now.weekday()])

#format output
locale.setlocale(locale.LC_ALL, 'ru_ru.UTF-8')

print(now.strftime(('%a')))
print(now.strftime(('%A')))

print(f'Дата: {now.strftime("%A, %d %b %Y")}')
print(f'Время: {now.strftime("%H:%M:%S")}')

print(now.strftime('%c'))
print(now.strftime('%x'))  #only date
print(now.strftime('%X'))  #only time

now = datetime.today()
print(now.strftime('%c'))
d1 = now + timedelta(days=1, hours=2, minutes=10)
print(d1.strftime('%c'))