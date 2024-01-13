# from add import add

# output=add(7,8)
# print(output)

# from math import pow      math module
# output=pow(2,3)
# print(output)

# import math     #math package
# print(math.pow(2,3))

# import time     #time  module
# ticks=time.time()
# print("Number of ticks since 12:00 am, January1,1970:",ticks)

# import time
# localtime=time.localtime(time.time())
# print("Local current time:",localtime)
# local current time:time.struct_time(tm_year=2022,tm_mon=10,tm_mday=31,tm_hour=16,tm_min=10,tm_sec=53,tm_wday=0,tm_yday=304,tm_idst=0)
#isdst-daylight saving

# import calendar
# cal=calendar.month(2023,1)
# print(cal)

# from datetime import *
# m=str(input(""))
# #2022-11-15 11:00
# base=datetime.strptime(m,"%Y-%m-%d %H:%M")
# print(base)     #2022-11-15 11:00
# n=int(input())
#4
#Python timedelta() function is present under datetime library which is generally used
#for calculating difference in dates and also can be used for date manipulations in python
# for i in range(0,n):    #modify 1 to n
#     print(timedelta(days=i))
#output of this statement
#     0:00:00
# 1 day, 0:00:00
# 2 days, 0:00:00
# 3 days, 0:00:00
    # print(base+timedelta(days=i))
#output of this statement
#     0:00:00
# 2022-11-15 11:00:00
# 1 day, 0:00:00
# 2022-11-16 11:00:00
# 2 days, 0:00:00
# 2022-11-17 11:00:00
# 3 days, 0:00:00
# 2022-11-18 11:00:00

#tell method
text=["Hello\n","hi\n","Python\n"]
file=open("test.txt","w+")
file.writelines(text)
print("where the file cursor is:",file.tell())
#here we used tell()method which prints where the cursor position at
file.seek(0)
print("where the file cursor is:",file.tell())
print(file.readline())
print("where the file cursor is:",file.tell())
print(file.read())
print("where the file cursor is:",file.tell())
file.seek(1)
print("where the file cursor is:",file.tell())
file.seek(2)
print(file.read())

file.close()


file=open("test.txt","a+")
file.writelines(text)
print(file.seek(0))
