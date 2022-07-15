#this program will state the seconds, minutes, hours, days, months and years between two set dates

#imports
import time
from datetime import date
import datetime

#current time
current_time = time.strftime("%H:%M:%S")
current_date = date.today()
current_year = datetime.datetime.now().year

#welcome
print(current_year)
print(current_date)
print(current_time)
print("Welcome to Timezone Calculator Beta!")
target_year = int(input("Please input a year: "))

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

#leap years
leap_day_counter = int(year_difference) / 4
years2days_leap = int(years2days) + leap_day_counter
round(int(years2days_leap))
print(years2days_leap)

print(str(year_difference) + " Years,")
print(str(years2months) + " Months,")
print(str(years2weeks) + " Weeks,")
print(str(years2days_leap) + " Days,")
print(str(years2hours) + " Hours,")
print(str(years2minutes) + " Minutes,")
print(str(years2seconds) + " Seconds since that date. ")

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
