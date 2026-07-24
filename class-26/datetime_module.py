import datetime as dt
print(dt.datetime.now())
print(dt.date(2027,12,15))
print(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

print(dt.datetime.now(dt.timezone.utc))
print(dt.datetime.now().timestamp())

