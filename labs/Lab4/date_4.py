from datetime import datetime

date1 = datetime(2025, 2, 15, 12, 0, 0)
date2 = datetime(2025, 2, 10, 12, 0, 0)

time_difference = abs(date1 - date2)
seconds = time_difference.total_seconds()

print("In seconds:", seconds)
