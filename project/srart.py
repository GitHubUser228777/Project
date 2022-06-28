import datetime
import math

zrday = 21
arday = 10
oklad = 130000
q = datetime.date.today()
print(q.month)
avans = math.floor(oklad/zrday*arday*0.7/100*100)
zp = oklad*0.87-avans
print(avans, zp, avans+zp)