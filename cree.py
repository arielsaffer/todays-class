# 

from datetime import date
from datetime import time
from datetime import datetime

#

today = date.today()
print("Today's date is",today)

# Is it October?

mo = "Yes!" if (today.month == 10) else "No..."
print(mo)

# Halloween countdown

if (today.month != 10):
  st = "It's not even October.."
else:
  print(31 - today.day,"days to go!")
