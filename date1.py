from datetime import datetime, timedelta

today = datetime.now()

one_day = timedelta(days=1)

yesterday = today - one_day
print('Today is: '+str(today))
print('Yesterday was: '+str(yesterday))

one_week = timedelta(weeks=1)

last_weekday = today - one_week

print('Last week: '+str(last_weekday))

print('Day: '+str(today.day))
print('Month: '+str(today.month))
print('Year: '+str(today.year))

print('Hour: '+str(today.hour))
print('Minutes: '+str(today.minute))
print('Seconds: '+str(today.second))