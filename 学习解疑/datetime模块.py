import datetime
# 获取当前时间
print(datetime.datetime.now())
# 获取当前日期
print(datetime.date.today())
# 获取前N天(days可正可负)
print(datetime.date.today()+datetime.timedelta(days=-2))
# 获取当天开始和结束时间(00:00:00 23:59:59.999999)
print(datetime.datetime.combine(datetime.date.today(),datetime.time.min))
print(datetime.datetime.combine(datetime.date.today(),datetime.time.max))
# 获取datetime时间差
print((datetime.datetime(2017,12,23,13,0,0) - datetime.datetime.now()).total_seconds())
print(datetime.datetime(2017,12,23,13,0,0) - datetime.datetime.now())
# 获取周几，从0开始，从周一开始，
print(datetime.date.today().weekday())
print(datetime.date(2017,11,26).weekday())#周日

# 月份信息
import calendar
today = datetime.date.today()
# monthrange() 返回一个数组，第一个值这个月的第一天是周几，第二个值这月有几天
last_day_num = calendar.monthrange(today.year, today.month)
# print(last_day_num[0],last_day_num[1])

# 类型转换
# datetime -> string
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# string -> datetime
print(datetime.datetime.strptime("2014-12-31 18:20:10", "%Y-%m-%d %H:%M:%S"))
# datetime -> timetuple
print(datetime.datetime.now().timetuple())
# timetuple -> datetime
# 步骤需要结合下面datetime -> timestamp
# timetuple => timestamp => datetime
# datetime -> date
print(datetime.datetime.now().date())
# date -> datetime
today = datetime.date.today()
print(datetime.datetime.combine(today, datetime.time()))
# datetime -> timestamp
import time
now = datetime.datetime.now()
print(time.mktime(now.timetuple()))
# timestamp -> datetime
print(datetime.datetime.fromtimestamp(1421077403.0))

