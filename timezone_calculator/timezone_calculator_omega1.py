#this program will state the seconds, minutes, hours, days, months and years between two set dates

#imports
import time
from datetime import date
import datetime

#current time
current_time = time.strftime("%H:%M:%S")
current_date = date.today()
current_year = datetime.datetime.now().year

#start of year
start_of_year_date = datetime.date(current_year, 1, 1)
date_since_start_of_year = current_date - start_of_year_date
start_of_year_time = datetime.time(0, 0, 0)
time_subtract1 = datetime.datetime.strptime(current_time, "%H:%M:%S")
time_subtract2 = datetime.datetime.strptime(str(start_of_year_time), "%H:%M:%S")
time_sum = time_subtract1 - time_subtract2
year = datetime.datetime.now().year
month = int(datetime.datetime.now().month)
day = datetime.datetime.now().day
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
second = datetime.datetime.now().second
week_div_month = int(month) * 4
hour_div_days = int(day) * 24
minute_div_hour = int(hour) * 60
second_div_minute = int(minute) * 60

#welcome
print(current_date)
print(current_time)
print("Welcome to Timezone Calculator Alpha!")
target_year = int(input("Please input a year: "))
target_month = int(input("Please input a month as a number: "))
target_day = int(input("Please input a day in the selected month: "))

#start of year continued
week = datetime.date(2000, 1, 1).strftime("%V")
days_div_week = int(week) * 7

#lists
leap_years = ("2000", "2004", "2008", "2012", "2016", "2020", "2024", "2028", "2032", "2036", "2040", "2044", "2048")

#calculator
year_difference = int(current_year) - int(target_year)
years2months = year_difference * 12
years2weeks = year_difference * 52
years2days = year_difference * 365
years2hours = year_difference * 8760
years2minutes = year_difference * 525600
years2seconds = year_difference * 31536000

#precise time
precise_year = current_year
month_since_start_year = month
day_since_start_month = day
day_precise = target_day
month_precise = target_month
years2months_precise = int(month_precise) + int(years2months) - 1
years2weeks_precise = int(day_precise) / 7
round(years2weeks_precise)
precise_months2weeks = years2months_precise * 4
precise_weeks2days = precise_months2weeks * 7
precise_days2hours = precise_weeks2days * 24
precise_hours2minutes = precise_days2hours * 60
precise_minutes2seconds = precise_hours2minutes * 60

#leap years
leap_day_counter = int(year_difference) / 4
years2days_leap = int(years2days) + leap_day_counter
years2days_leap_rounded = (round(years2days_leap))

#current time
years2weeks_current = int(years2weeks) + round(years2weeks_precise)
years2days_current = int(day) + int(years2days_leap_rounded) - int(day_precise)
years2hours_current = int(years2hours) - int(hour)
years2minutes_current = int(years2minutes) - int(minute)
years2seconds_current = int(years2seconds) - int(second) - 52000
round(int(years2seconds_current))

#future
year_difference_future = abs(year_difference)
years2months_future = abs(years2months)
years2weeks_future = abs(years2weeks_current)
years2days_future = abs(years2days_current)
years2hours_future = abs(years2hours_current)
years2minutes_future = abs(years2minutes_current)
years2seconds_future = abs(years2seconds_current)

#display
if current_year > target_year:
    print(str(year_difference) + " Years,")
    print(str(years2months_precise) + " Months,")
    print(str(years2weeks_current) + " Weeks,")
    print(str(years2days_current) + " Days,")
    print(str(years2hours_current) + " Hours,")
    print(str(years2minutes_current) + " Minutes,")
    print(str(years2seconds_current) + " Seconds since that date. ")
if current_year < target_year:
    print(str(year_difference_future) + " Years, ")
    print(str(years2months_future) + " Months, ")
    print(str(years2weeks_future) + " Weeks, ")
    print(str(years2days_future) + " Days, ")
    print(str(years2hours_future) + " Hours, ")
    print(str(years2minutes_future) + " Minutes, ")
    print(str(years2seconds_future) + " Seconds to that date. ")
if current_year == target_year:
    print("Have you got a screw loose? It's " + str(current_year) + " now, mate. Do you live under a rock? ")

#dump
#if current_year == leap_years:
    #years2days + 1
#if target_year <= 2020:
    #years2days + 1
#if target_year <= 2016:
    #years2days + 1
#if target_year <= 2012:
    #years2days + 1
#if target_year <= 2008:
    #years2days + 1

#time_since_start_of_year = (current_time) - (start_of_year_time)

#years2hours_current = ((time_sum.hour)("%H"))

#time extraction
#years2hours_current = time.strftime("%H")
#print(years2hours_current)
#years2hours_current = int(years2hours) +

#week = datetime.date(int(month), ).isocalendar().week
