import datetime
import math
from calendar import monthrange
from calendar import Calendar

dop_days = [0, 5, 1, 1, 0, 4, 1, 0, 0, 0, 0, 1, 0]
dop_arday = [0, 5, 11, 10, 11, 6, 10, 11, 11, 11, 11, 10, 11]
cl = Calendar()
oklad = 130000
q = datetime.date.today()
w = datetime.datetime.today().weekday()
days = monthrange(q.year, q.month)[1]
print(w)
for mdays in cl.itermonthdays(q.year, q.month):
    if mdays != 0:
        if datetime.date(q.year, q.month, mdays).isoweekday() >= 6:
            days = days-1
month = q.month
zp = oklad*0.87
print("ЗП:",zp)
zrday = days-dop_days[month]
arday = dop_arday[month]
avans = math.floor(oklad/zrday*arday*0.7/100*100)
zp = oklad*0.87-avans
print("Аванс:",avans,"ЗП:",zp, "Всего:" ,avans+zp)