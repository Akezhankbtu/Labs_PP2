from datetime import datetime, timedelta

age = int(input("Введите возраст в years: "))
birth_date = datetime.now() - timedelta(days=age * 365.25)
time_difference = datetime.now() - birth_date
seconds = time_difference.total_seconds()

print(f"Age в секундах: {int(seconds)}")
