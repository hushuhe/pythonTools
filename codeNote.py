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
#==========================TIME END========================================