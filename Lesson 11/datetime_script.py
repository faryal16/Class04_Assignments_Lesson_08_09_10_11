import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()

# Method 1: Get the current date only
current_date = current_datetime.date()
print("\nCurrent Date:", current_date)

# Method 2: Get the current time only
current_time = current_datetime.time()
print("\nCurrent Time:", current_time)

# Method 3: Get the weekday (0 = Monday, 6 = Sunday)
weekday = current_datetime.weekday()
print("\nWeekday:", weekday)

# Method 4: Get the year, month, day, hour, minute, second separately
year = current_datetime.year
month = current_datetime.month
day = current_datetime.day
hour = current_datetime.hour
minute = current_datetime.minute
second = current_datetime.second

print(f"\nYear: {year}, Month: {month}, Day: {day}")
print(f"\nHour: {hour}, Minute: {minute}, Second: {second}")

# Method 5: Add 7 days to the current date
new_date = current_datetime + datetime.timedelta(days=7)
print("\nNew Date after 7 days:", new_date.strftime("%Y-%m-%d %H:%M:%S"))

# Method 6: Subtract 3 hours from the current time
new_time = current_datetime - datetime.timedelta(hours=3)
print("\nTime after subtracting 3 hours:", new_time.strftime("%Y-%m-%d %H:%M:%S"))
