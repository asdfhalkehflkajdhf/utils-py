import datetime as DT
import time

'''
时间格式　'2016-12-21 10:22:56'
'''

def get时间字符串():
    """获取　时间的字符串 主要是用于存入数据库"""
    return DT.datetime.now().__str__()

def get字符串转时间戳(timestring):
    ''''''
    '''<class 'str'> 2018-02-09 18:17:53.761988,会报错'''
    timestring=timestring.split('.')[0]
    return DT.datetime.strptime(timestring, '%Y-%m-%d %H:%M:%S')

def get当前时间戳(days=0):
    """
    取正则是当前日期几天后，取－是当前日期的前几天
    :param days:
    :return:
    """
    return DT.datetime.now()+DT.timedelta(days=days)

def get相差天数(data):
    """主要是在过滤网页时用"""
    cur =DT.datetime.now()
    return (cur-data).days

def get时间戳前n天时间戳(data,ndays):
    """返回的是一个时间数据，"""
    return data + DT.timedelta(days=-ndays)


def ISOString2Time( dataStr ):
    """输入为是一个2006-04-12 16:46:40格式字符串，返回的是一个秒数值，"""
    '''
    convert a ISO format time to second
    from:2006-04-12 16:46:40 to:23123123
    把一个时间转化为秒
    '''
    dataStr=dataStr.split('.')[0]
    d=DT.datetime.strptime(dataStr,"%Y-%m-%d %H:%M:%S")
    return time.mktime(d.timetuple())

def Time2ISOString( seconde ):
    """输入为秒数，返回的是一个2006-04-12 16:46:40格式字符串，"""
    '''
    convert second to a ISO format time
    from: 23123123 to: 2006-04-12 16:46:40
    把给定的秒转化为定义的格式
    '''
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime( float(seconde) ) )

if __name__ == "__main__":
    a = get时间字符串()
    print(type(a),a)

    # a = get字符串转时间戳(a)
    # print(type(a),a)
    #
    # a = get字符串转时间戳('2018-02-03 18:40:42')
    # print(a)

    # a = get相差天数(a)
    # print(a)

    # a = get当前时间戳(days=-10)
    # print(type(str(a)),str(a))
    '''==============================='''
    # a = ISOString2Time(a)
    # print(type(a),a)
    # a = Time2ISOString("1518171142.755")
    # print(a)
    # a = Time2ISOString(1518160974)
    # print(a)
    curData = get当前时间戳()
    rollData_2 = get时间戳前n天时间戳(curData,5)
    a = str(rollData_2)
    print(type(a),a.split())
    print(type(rollData_2), rollData_2)
