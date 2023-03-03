from datetime import datetime, timedelta
print("date and time: ", datetime.now().replace(hour=0, minute=0, second=0, microsecond=0))
new_date=datetime.now() - timedelta(days=5)
print(new_date.replace(hour=0, minute=0, second=0, microsecond=0))