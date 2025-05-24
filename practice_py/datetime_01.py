import datetime

now = datetime.datetime.now()

s = now.strftime("""
                 year  is %Y
                 month is %m
                 day   is %d
                 hour  is %H
                 min   is %M
                 sec   is %S""")
s1 = now.strftime("%Y-%m-%d %H:%M:%S")
print(s)
print(s1)
#this is really cool
print(now.strftime("%Y %m %d - %I %H %M %S %p"))

