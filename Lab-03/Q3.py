# III. a Python program to extract year, month, date and time using Lambda.
import time

current_time = time.ctime()

get_year = lambda date_obj:date_obj[-4:]
get_month = lambda date_obj: date_obj[4:7]
get_day = lambda date_obj: date_obj[8:10]
get_time = lambda date_obj: date_obj[11:-5]

print("year:",get_year(current_time))
print("month:",get_month(current_time))
print("day:",get_day(current_time))
print("time:",get_time(current_time))




