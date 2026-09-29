y=int(input('Year = '))
m=int(input('Month = '))
d=int(input('Day = '))
print(f'{'Year =',y ,'Month= ',m,'Day= ',d}')
print(f'Year={y}, Month={m}, Day={d}')
import jdatetime
data_shamsi=jdatetime.date.fromgregorian(year=y, month=m, day=d)
print(data_shamsi.strftime('%y/%m/%d'))


