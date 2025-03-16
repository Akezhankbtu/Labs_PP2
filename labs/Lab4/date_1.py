from datetime import datetime,timedelta
current_date=datetime.now()
new_d=current_date-timedelta(days=5)

print("Current date:",current_date.strftime("%Y-%m-%d"))
print("5 days ago:", new_d.strftime("%Y-%m-%d"))
