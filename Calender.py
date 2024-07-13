"""python program to find the day of a particular date"""

import calendar
weekdays=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
Y,M,D=map(int,input().split())
a=calendar.weekday(Y,M,D)
print(weekdays[a])