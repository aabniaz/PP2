import datetime as dt

a = dt.datetime(2023,2,17,23,59,59)
b = dt.datetime(2023,2,18,23,59,59)

c=(b-a).total_seconds()
print(c)