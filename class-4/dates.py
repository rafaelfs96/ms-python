from datetime import datetime, timedelta

today = datetime.now()
print(f'Today is: {today}')

# timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = today - one_day
print(f'Yesterday was: {yesterday}')

print(f'{today.day}/{today.month}/{today.year}')

birthday = input('When is your birthday? ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print(f'Birthday {birthday_date}')
