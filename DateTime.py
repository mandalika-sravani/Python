import datetime

date = datetime.date(2026, 1, 2)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S: %m-%d-%Y")

target_date = datetime.datetime(2025, 1, 2, 12, 30, 1)
current_date = datetime.datetime.now()

if target_date < current_date:
    print("Target date has passed")
else:
    print("Target date has not passed")

