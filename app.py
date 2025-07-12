from datetime import datetime, timedelta
now = datetime.now()

# Print the current date and time
print(now)

today = now.date()
print(today)


fromatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date:", )
