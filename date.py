#-*- coding:utf-8 -*-
import datetime
today =datetime.date.today()
print(today)

#获取昨天和明天的时间
yesterday = today - datetime.timedelta(days=1)
print(yesterday)
tomorrow = today + datetime.timedelta(days=1)
print(tomorrow)

#获取上周五的日期。获取具体时间，需要引入两个模块 datetime,calendar
import datetime,calendar

last_friday = datetime.date.today()
oneday = datetime.timedelta(days = 1)

while last_friday.weekday()!=calendar.FRIDAY:
	last_friday -= oneday
print(last_friday.strftime('%A,%d-%b-%Y'))

#计算机循环运行时间
import time
start = time.clock()
sum = 0
for i in range(1,100):
	sum = sum + i
print(sum)
end = time.clock()
print('代码运行时间:%s 秒'%(end-start))

#定时任务：每三秒打印一次时间,引申功能，定时爬虫
import time,os

def exe(cmd,inc = 60):
	while True:
		os.system(cmd);
		time.sleep(inc)
exe("echo %time%",3)

