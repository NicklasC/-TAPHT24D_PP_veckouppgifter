from datetime import datetime,timedelta

#4.3A
print(f"Dagens datum: {datetime.now().strftime('%Y-%m-%d')}")

#4.3B
date_today = datetime.now()
date_in_7_days = date_today + timedelta(days=7)
print(f"Datum om 7 dagar: {date_in_7_days.strftime('%Y-%m-%d')}")
