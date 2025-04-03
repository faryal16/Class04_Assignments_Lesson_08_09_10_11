import time

# 1. Get the current time in seconds since the epoch (Unix time)
epoch_time = time.time()
print(f"\nCurrent time in seconds since the epoch: {epoch_time}")


ticks = time.time()
print("\nNumber of ticks since 12:00am, January 1, 1970:", ticks)

# 2. Get the current local time (as a tuple)
local_time = time.localtime()
print("\nLocal time as a tuple:")
print(local_time)

# 3. Convert the tuple to a human-readable string
local_time_string = time.asctime(local_time)
print("\nLocal time as a string:", local_time_string)

# 4. Sleep for 3 seconds
print("\nWaiting for 3 seconds...")
time.sleep(3)
print("3 seconds have passed.")

# 5. Measure how long a task takes
start_time = time.time()
# Example task: sleeping for 2 seconds
time.sleep(2)
end_time = time.time()
task_duration = end_time - start_time
print(f"\nTask took {task_duration:.2f} seconds to complete.")

# 6. Get the current time as a formatted string
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print("\nCurrent formatted local time:", formatted_time)

# 7. Get the current UTC time as a formatted string
utc_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
print("\nCurrent UTC time:", utc_time)

print("""\nSummary:
time.time() is useful for getting the current time in seconds since the epoch.

time.localtime() and time.gmtime() give the current local time and UTC time, respectively, as a tuple.

time.asctime() converts the struct_time to a human-readable string.

time.sleep() pauses execution for a specified duration.

time.strftime() formats time into a readable string based on a given format.""")