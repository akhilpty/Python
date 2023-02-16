import datetime as dt

# cu means Current
cu_datetime=dt.datetime.now()
cu_year=cu_datetime.year
cu_month=cu_datetime.month
cu_weekofyear=cu_datetime.isocalendar().week
cu_weekday=cu_datetime.strftime('%A')
cu_dayofyear=cu_datetime.strftime('%j')
cu_dayofmonth=cu_datetime.strftime('%d')
cu_dayofweek=cu_datetime.strftime('%w')

print('Current date & time is :',cu_datetime)
print('Current Year is:',cu_year)
print('Current Month is:.' ,cu_month)
print('Week number of the year is:',cu_weekofyear)
print('Weekday of the week is:',cu_weekday)
print('Day of year is:',cu_dayofyear)
print('Day of the month is:',cu_dayofmonth)
print('Day of the week is:',cu_dayofweek)