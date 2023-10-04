import datetime as dt
# 获取datetime module 的datetime class 的 now method 的 year/month/week 等attributes
# now.weekday() : 0 表示星期一
# 创建 datetime object: dt.datetime()
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

date_of_birth = dt.datetime(year=1999, month=12, day=15)
print(day_of_week)
print(date_of_birth)