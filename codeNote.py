import time
#==========================TIME相关========================================
#将字符串的时间转换为时间戳
def timestamp(a):
    timeArray = time.strptime(s, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp
    
#格式更改
#如a = "2013-10-10 23:40:00",想改为 a = "2013/10/10 23:40:00"
def ti(a):
    timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
    otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
    return otherStyleTime
#==========================TIME END========================================