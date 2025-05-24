#calculating exact time 1000 days from now
import datetime

now = datetime.datetime.now()
future = now + datetime.timedelta(days=1000)
print("current datetime:", now.strftime("%Y-%m-%d %H:%M:%S"))
print("future datetime:", future.strftime("%Y-%m-%d %H:%M:%S"))