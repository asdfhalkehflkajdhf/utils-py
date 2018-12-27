from pymongo import MongoClient
import log
import re
import json
import os

global __isWriteToDB
__isWriteToDB = True

global __g_tableName
__g_tableName='table_'
global __g_dbName


'''==================================================='''
def __get去文件名中不支持符号(str):
    # /  \: *" < > | ？
    # _是一个文件名的链接符号，也去掉，\需要用三个\来表示\\\
    ruler = "[\s+]+|[+:\"_\\\/<*>|?]+"
    # string = re.sub(ruler.decode("utf8"), "".decode("utf8"), temp)  #python 2.7
    string = re.sub(ruler, "", str) #python 3.6
    return string
def __link测试(ip, port):
    logger = log.get_logger("dataToDB")
    import socket
    res = False
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(1)
    try:
        sk.connect((ip, port))
        res = True
        logger.info("%s, %d connect OK"%(ip, port))
    except Exception:
        res = False
        logger.info("%s, %d connect False" % (ip, port))
        # print( 'Server port 80 not connect!')
    sk.close()
    return res
def __check表名路径(路径):
    if not os.path.exists(路径):
        os.makedirs(路径,exist_ok=True)
'''==================================================='''
'''==================================================='''

# 链接数据库
def openDB(dbName,ip=None, port=None ):
    global __g_dbName
    __g_dbName =dbName
    global __isWriteToDB
    if ip is None or port in None:
        __isWriteToDB = False
    else:
        if __link测试(ip, port):
            __isWriteToDB = True
        else:
            __isWriteToDB = False

    if __isWriteToDB:
        '''写入mongoDB，链接数据库'''
        pass
    else:
        '''写入文件'''
        if not os.path.exists(dbName):
            '''新建本地文件数据库名'''
            logger = log.get_logger('')
            logger.info("新建库文件：%s"%(dbName))
            os.makedirs(dbName, exist_ok=True)

def __writeDataToFile(item,日期,来源,标题):
    """

        :param item:
        :param 日期:‘YYYY-MM-DD HH:MM:SS’
        :param 标题:
        :return:
        """
    # logger = log.get_logger('')
    global __g_dbName
    global __g_tableName
    日期=日期.split()
    tableName = __g_tableName+日期[0]
    tableNamePath = os.path.join(__g_dbName,tableName)
    '''在文件名中会把 符号_过虑，是一个分割符'''

    记录名=__get去文件名中不支持符号(日期[1])+'_'+__get去文件名中不支持符号(来源)+'_'+__get去文件名中不支持符号(标题)
    __check表名路径(tableNamePath)
    记录文件路径=os.path.join(tableNamePath,记录名)

    f = open(记录文件路径,'w',encoding='utf8')
    # 写入文件时，不使用ascii格式
    print(json.dumps(item, ensure_ascii=False),file=f)
    f.close()
    # json数据写入文件，生成日志
    try:
        print(记录文件路径)
    except Exception:
        print()

    pass
def __writeDataToDB(item):
    """

    :param item:
    :param 日期:‘YYYY-MM-DD HH:MM:SS’
    :param 标题:
    :return:
    """

    pass

'''对外接口，写入数据'''
def writeDataToSave(item,日期,来源,标题):
    global __isWriteToDB
    if __isWriteToDB:
        __writeDataToDB(item)
    else:
        __writeDataToFile(item,日期,来源,标题)
        pass

if __name__ == "__main__":
    # openDB('localhost', 27016, 'asdf')
    # import os
    # # os.makedirs('testttt')
    #
    # a = '1/--_2\\3:45*6" 7<8- >9 |10 ？'
    # a= _get去文件名中不支持符号(a)
    # print(a)
    info = {'newID': 3232,
             'newTitle': 'asdfasdf',
             'newContext': 'asdfasdfasdf',
             'newKey': ['asdf', '234']
             }
    openDB('ttt',None, None)
    writeDataToSave(info,'2018-02-07 09:51:20', '测试','asd夺要:/?')