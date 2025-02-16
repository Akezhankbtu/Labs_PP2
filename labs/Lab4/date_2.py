from datetime import datetime,timedelta
current_date=datetime.now()
yesterday=current_date-timedelta(days=1)
tomorraw=current_date+timedelta(days=1)

print("Today:",current_date.strftime("%Y-%m-%d"))
print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorraw.strftime("%Y-%m-%d"))
