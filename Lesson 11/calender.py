import calendar

# Method 1: Print the calendar for a specific month and year
year = 2025
month = 4
print(f"\nCalendar for {calendar.month_name[month]} {year}:")
print(calendar.month(year, month))

# Method 2: Print the full calendar for the whole year
print(f"\nFull Calendar for {year}:")
print(calendar.calendar(year))

# Method 3: Check if a given year is a leap year
year = 2024
is_leap = calendar.isleap(year)
print(f"\nIs {year} a leap year? {is_leap}")

# Method 4: Get the weekday of a specific date (e.g., 1st April 2025)
weekday = calendar.weekday(2025, 4, 1)  # 0 = Monday, 6 = Sunday
print(f"\nThe weekday for 1st April 2025 is: {calendar.day_name[weekday]}")

# Method 5: Get the number of days in a month
month_days = calendar.monthrange(2025, 4)[1]
print(f"\nNumber of days in April 2025: {month_days}")

print("""\nSummary:
calendar.month(): Prints a formatted calendar for a specific month.

calendar.calendar(): Prints a full year calendar.

calendar.isleap(): Checks if a year is a leap year.

calendar.weekday(): Finds the weekday of a specific date (returns an integer).

calendar.day_name[]: Converts the integer from weekday() into a human-readable weekday name.

calendar.monthrange(): Returns the number of days in a month.""")