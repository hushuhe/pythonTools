# -*- coding: cp936 -*-
import time
import sys
ty=sys.getfilesystemencoding()
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
    
 #将时间戳转化为字符串
def ti2(a):
    x = time.localtime(a)
    return time.strftime('%Y-%m-%d %H:%M:%S',x)
#===========================function==========================
def changeNum(i):
    dict2 = {'0':'零','1':'一','2':'二','3':'三','4':'四','5':'五','6':'六','7':'七','8':'八','9':'九'}
    result = ''
    #print i
    for x in str(int(i)):
        if dict2.has_key(x):
            result += dict2[x]
        else:
            result += str(x)
    return result
def getLastZb(i):
    i= i.strip().split('\t')
    return i[0],i[1],i[2],i[-1]
 #==========================TIME END========================================       
cook_str='sessionid=dbe959086b7f2922e4c23416a020a818; csrftoken=ylOSHezRJzSIzoxcjil9oHIu9cNzCEX8'

i = 103104517052861508046282207214545477744

print changeNum(i)