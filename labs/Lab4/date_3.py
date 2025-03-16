from datetime import datetime
current_datetime = datetime.now()
clean_datetime = current_datetime.replace(microsecond=0)
print("Original:", current_datetime)
print("Without microseconds:", clean_datetime)
