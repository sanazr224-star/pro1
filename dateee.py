import jdatetime

y = int(input('Year  = '))
m = int(input('Month  = '))
d = int(input('Day  = '))

print(f'Year={y}, Month={m}, Day={d}')

data_shamsi = jdatetime.date.fromgregorian(year=y, month=m, day=d)

print("Solar_calendar_date")
print(data_shamsi.strftime('%Y/%m/%d'))
