#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century
#unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century
#(1 Jan 1901 to 31 Dec 2000)?

import time
def is_leapyear(year):
    if year % 4 == 0:
        if (year % 100) == 0 and (year % 400) == 0:
            return True
        elif (year % 100) == 0 and (year % 400) != 0:
            return False
        else:
            return True
    return False

def calc_first_day_of_year(year):
    if is_leapyear(year):
        #difference between year and 1900 will give us the number of days
        #we move ahead a day. We then need to calculate leap years as
        #they will add one additional day. To calculate the first day
        #of the year we would need to take one day away if it's a leapyear
        #becuase the extra day doesn't happen yet during that year.
        #We can then get the remainder of dividing by 7 to see what day
        #of the week it is. If it's 6 (which we have matched to Sunday)
        #then the first day of the year is a Sunday and we need to return that
        first_day = ((((year - 1900) + ((year - 1900))-1) // 4)) % 7
        return first_day
    else:
        first_day = ((year - 1900) + ((year - 1900) // 4)) % 7
        return first_day

def calc_first_suns_in_year(year, days):
    months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31,\
    11:30, 12:31}
    total_days = 0
    first_day_of_year = calc_first_day_of_year(year)

    if is_leapyear(year):
        months[2] = 29
    else:
        months[2] = 28

    if first_day_of_year == 6:
        first_sun_in_year = 1
    else:
        first_sun_in_year = 0


    for i in range(2,13):
        if ((months[i-1] + total_days) % 7) + first_day_of_year == 6:
            first_sun_in_year += 1
            total_days += months[i-1]
        else:
            total_days += months[i-1]
    return first_sun_in_year

def calc_total_first_suns(days):
    total_first_sundays = 0
    for i in range(1901,2001):
        total_first_sundays += calc_first_suns_in_year(i, days)
    return total_first_sundays


days = {0:'mon', 1:'tues', 2:'wed', 3:'thurs', 4:'fri', 5:'sat', 6:'sun'}

start = time.time()
total_sundays = calc_total_first_suns(days)
elapsed = (time.time() - start)
print("result %s returned in %s seconds." % (total_sundays,elapsed))
