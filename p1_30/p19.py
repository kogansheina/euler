#!/usr/bin/env python
import os
import sys
# counting Sundays which are the first of the month between 1/1/1901 and 31/12/2000
if __name__ == '__main__':
    Months = [31,28,31,30,31,30,31,31,30,31,30,31]
    year = 1900
    month = 1
    day = 1
    dayOfWeek = 1 # Monday
    counter = 0
    while year < 2001:
        # next first of month
        while day < Months[month-1]:
            day += 7
        while day > Months[month-1]:
            day -= 1
            if dayOfWeek == 0:
                dayOfWeek = 7
            dayOfWeek -= 1
        # day is the last in month, the next is the first of next month
        day = 1
        month += 1
        if month == len(Months)+1:
            month = 1
            year += 1
            if year == 1901:
                counter = 0
            elif year == 2001:
                break
            if year % 4 == 0:
                Months[1] = 29 # leap year
            else:
                Months[1] = 28 # regular year
        dayOfWeek += 1
        if dayOfWeek == 7:
            dayOfWeek = 0
        print "year=%d month=%d day=%d dayOfWeek=%d" % (year,month,day,dayOfWeek) 
        if day == 1 and dayOfWeek == 0:
            counter += 1
    print "counter = %d" % counter  
         
        
