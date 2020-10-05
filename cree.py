# 

from datetime import date
from datetime import time
from datetime import datetime

#

today = date.today()
print("Today's date is",today)

# Is it October?

mo = "Yes!" if (today.month == 10) else "No..."
print("Is it October?", mo)

# Halloween countdown

if (today.month != 10):
  st = "It's not even October.."
else:
  print("Halloween is just ", 31 - today.day,"days away!")
