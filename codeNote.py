# -*- coding: cp936 -*-
import time
import sys
ty=sys.getfilesystemencoding()
#==========================TIME���========================================
#���ַ�����ʱ��ת��Ϊʱ���
def timestamp(a):
    timeArray = time.strptime(s, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp
    
#��ʽ����
#��a = "2013-10-10 23:40:00",���Ϊ a = "2013/10/10 23:40:00"
def ti(a):
    timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
    otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
    return otherStyleTime
    
 #��ʱ���ת��Ϊ�ַ���
def ti2(a):
    x = time.localtime(a)
    return time.strftime('%Y-%m-%d %H:%M:%S',x)
#===========================function==========================
def changeNum(i):
    dict2 = {'0':'��','1':'һ','2':'��','3':'��','4':'��','5':'��','6':'��','7':'��','8':'��','9':'��'}
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