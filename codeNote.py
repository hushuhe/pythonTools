import time
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

#===========================decode==========================
import sys
ty=sys.getfilesystemencoding()


#==========================TIME END========================================
cook_str='sessionid=dbe959086b7f2922e4c23416a020a818; csrftoken=ylOSHezRJzSIzoxcjil9oHIu9cNzCEX8'