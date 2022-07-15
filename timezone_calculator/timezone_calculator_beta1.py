#this program will state the seconds, minutes, hours, days, months and years between two set dates
import time
from datetime import date
import datetime
current_time = time.strftime("%H:%M:%S")
current_date = date.today()
current_year = datetime.datetime.now().year
leap_years = ("2000", "2004", "2008", "2012", "2016", "2020", "2024", "2028", "2032", "2036", "2040", "2044", "2048")
if current_year == leap_years:
    years2days + 1
print(current_year)
print(current_date)
print(current_time)
print("Welcome to Timezone Calculator Beta!")
target_year = int(input("Please input a year: "))
year_difference = int(current_year) - int(target_year)
years2months = year_difference * 12
years2weeks = year_difference * 52
years2days = year_difference * 365
years2hours = year_difference * 8760
years2minutes = year_difference * 525600
years2seconds = year_difference * 31536000
print(str(year_difference) + " Years,")
print(str(years2months) + " Months,")
print(str(years2weeks) + " Weeks,")
print(str(years2days) + " Days,")
print(str(years2hours) + " Hours,")
print(str(years2minutes) + " Minutes,")
print(str(years2seconds) + " Seconds since that date. ")
