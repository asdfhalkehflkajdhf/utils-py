import sqlite3
import os
import time
import sys

class downList():
    """
    database:数据库路径，库不存在时，新建
    """

    def __init__(self, database):
        """
        :param database:
        """
        #路径分割
        path = os.path.split(database)
        if len(path[0]) == 0:
            #是在当前目录下，不用新建目录
            pass
        else:
            #不在当前目标 或是其他目录,判断下路径是否存在
            if not os.path.exists(path[0]):
                os.makedirs(path[0], exist_ok=True)

        # 打开指定数据库
        # 库不存在时会新建一个
        # conn = sqlite3.connect('qqnews.db')
        # 使用:memory:标识打开的是内存数据库
        # con = sqlite3.connect(":memory:")
        self._conn = sqlite3.connect(database)
        # 这样我们就创建了一个游标对象：cu
        '''在sqlite3中，所有sql语句的执行都要在游标对象的参与下完成
            对于游标对象cu，具有以下具体操作：

                execute()           --执行一条sql语句
                executemany()       --执行多条sql语句
                close()             --游标关闭
                fetchone()          --从结果中取出一条记录
                fetchmany()         --从结果中取出多条记录
                fetchall()          --从结果中取出所有记录
                scroll()            --游标滚动
                光标（Cursor）可被用于迭代
                '''

        self._cur = self._conn.cursor()

    def __del__(self):
        self._cur.close()
        self._conn.close()

    def _get_tableName(self, tableName):
        """添加表名前缀"""
        return "table_"+tableName

    def createContextTable(self,tableName):
        """表名不能以数字开头，所以表名为 前缀+YYYYMMDD，  tableName为YYYYMMDD
        create table if not exists tableName,主要作用是url去重和更新数据   YYYYMMDD"""

        sql = 'create table if not exists '+self._get_tableName(tableName)+' (' \
                'newsId integer PRIMARY KEY autoincrement, ' \
                'url VARCHAR(256) not NULL,' \
                'createDate VARCHAR(30),' \
                'updateDate VARCHAR(30)' \
                ' )'

        try:
            self._conn.execute(sql)
        except sqlite3.Error as e:
            print(e.args[0], __file__,sys._getframe().f_lineno)
            return False
        print("createContextTable ok")
        return True

    def createQueueTable(self,tableName):
        #create table if not exists，主要作用是做为一个队列来缓存url,id字段为自增长，删除最小的
        sql = 'create table if not exists '+self._get_tableName(tableName)+'(' \
                'id integer PRIMARY KEY autoincrement, ' \
                'url VARCHAR(256) not NULL' \
                ' )'

        try:
            self._conn.execute(sql)
        except sqlite3.Error as e:
            print(e.args[0], __file__,sys._getframe().f_lineno)
            return False
        print("createQueueTable ok")
        return True

    def insertContextData(self, tableName, data):
        """
        tableName: 按日期建表
        data: 是一个list
             newsID: 每个站点新闻有唯一的ID号
             url: 完整URL
             createDate: 新闻文本创建日期
             updateDate: 当前系统日期
             [
             (newsID, url, createDate, updateDate),
             (newsID, url, createDate, updateDate)
             ]
        获取时间格式：time.strftime("%Y%m%d%H%M%S", time.localtime())

        这个是参数insert OR REPLACE
        https://stackoverflow.com/questions/418898/sqlite-upsert-not-insert-or-replace/4330694#4330694

        表示存在则更新，不存在则插入
         返回True false
        """

        '''import sqlite3
            connection = sqlite3.connect(':memory:')
            # Create a table
            connection.execute('CREATE TABLE events(ts, msg)')
            # Insert values,一次插入多条数据
            connection.executemany(
                'INSERT INTO events VALUES (?,?)',
                [
                    (1, 'foo'),
                    (2, 'bar'),
                    (3, 'baz')
                ]
            )
            # Print inserted rows
            for row in connection.execute('SELECT * FROM events'):
                print(row)
            for row in connection.execute('SELECT * FROM events'):
                print (row[0], row[1])
            
            (1, 'foo')
            (2, 'bar')
            (3, 'baz')
            1 foo
            2 bar
            3 baz
            '''
        '''
        表不存在
        try:
            connection.execute('SELECT * FROM eventssssss')
        except sqlite3.Error as e:
            print(e.args[0])
        no such table: eventssssss
        '''
        if data is None or data.__len__()==0 or tableName is None or tableName.__len__()==0:
            return True
        sql = 'INSERT OR REPLACE INTO '+self._get_tableName(tableName)+" VALUES (null,?,?,?)"
        try:
            # print(data)
            self._conn.executemany(sql,data)
        except sqlite3.Error as e:
            e_str =e.args[0]
            print(e.args[0],'|', __file__,'|',sys._getframe().f_lineno)

            if e_str.split(':')[0].__eq__("no such table"):
                self.createContextTable(tableName)
            return False
        #不提交，可能不会写入数据表中
        self._conn.commit()
        return True

    def findContextNewsId(self, tableName, newsIdList):
        """return resFindTrue, resFindFalse :返回是否存在数据list 和不存在list两个列表"""
        '''
        :param tableName:
        :param newsIdList:
        :return resFindTrue, resFindFalse :返回是否存在数据list 和不存在list两个列表
        '''
        a = "'"
        newsIdListStr = map(str,newsIdList)
        # executemany() can only execute DML statements,不能执行select 操作
        sql = "select newsid from " + self._get_tableName(tableName) + " where newsId in (" + ','.join(newsIdListStr) +")"
        print(sql)
        resFindTrue = []
        try:
            for row in self._conn.execute(sql):
                resFindTrue.append( row[0] )
        except sqlite3.Error as e:
            print(e.args[0], __file__,sys._getframe().f_lineno)
            e_str = e.args[0]
            if e_str.split(':')[0].__eq__("no such table"):
                self.createContextTable(tableName)
            # return False
        #集合减
        t = set(newsIdList)-set(resFindTrue)
        resFindFalse = list(t)
        return resFindTrue, resFindFalse
    def findContextURL(self, tableName, urlList):
        """return resFindTrue, resFindFalse :返回是否存在数据list 和不存在list两个列表"""
        '''
        :param tableName:
        :param newsIdList:
        :return resFindTrue, resFindFalse :返回是否存在数据list 和不存在list两个列表
        '''
        a = "'"

        # executemany() can only execute DML statements,不能执行select 操作
        sql = "select url from " + self._get_tableName(tableName) + " where url in (" + a+ "','".join(urlList) + a +")"
        # print(sql)
        resFindTrue = []
        try:
            for row in self._conn.execute(sql):
                resFindTrue.append( row[0] )
        except sqlite3.Error as e:
            print(e.args[0], __file__,sys._getframe().f_lineno)
            e_str = e.args[0]
            if e_str.split(':')[0].__eq__("no such table"):
                self.createContextTable(tableName)
            # return False
        #集合减
        t = set(urlList)-set(resFindTrue)
        resFindFalse = list(t)
        return resFindTrue, resFindFalse

    def queueList_Input(self, tableName,urlList):
        """
        :param urlList: 是一个list
            :param urlList: 完整urlList
              [
             (url, ),
             (url, )
             ]
        :return:如果失败,查看urlLIST中是否为元组，
        sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 1, and t
        len(img)，这不是一个元组
        74
        len((img,)) 这个是正确的，在单变量元组是，要在变量后边加一个逗号
        1


        """
        '''
        sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 1, and t

        你需要传递一个序列，但是你忘记了逗号使你的参数成为一个元组：

        cursor.execute('INSERT INTO images VALUES(?)', (img,))
        没有逗号，(img)只是一个分组表达式，而不是一个元组，因此img字符串被视为输入序列。如果该字符串长度为74个字符，那么Python会将其视为74个单独的绑定值，每个字符长度不等。

        >>> len(img)
        74
        >>> len((img,))
        1
        如果你发现它更容易阅读，你也可以使用列表文字：

        cursor.execute('INSERT INTO images VALUES(?)', [img])
        '''
        '''
        select * from EventTable order by EventDate ASC limit 1
        '''
        sql = "insert into " + self._get_tableName(tableName) + " values (null,?)"
        try:
            self._conn.executemany(sql, urlList)
        except sqlite3.Error as e:
            print(e.args[0], __file__,sys._getframe().f_lineno)
            return False
        #不提交，可能不会写入数据表中
        self._conn.commit()
        return True

    def queueList_Output(self,tableName, num=12):
        """
        :return:返回一个队列中的元组列表值，没有返回[]
        [（id, url）,
        （id, url）]
        """

        '''
        select * from EventTable order by EventDate ASC limit 1
        '''
        res = [] #返回结果，元组列表
        delList=[] #删除列表

        sql = "select * from " + self._get_tableName(tableName) + " order by id asc limit "+str(num)
        try:
            for row in self._conn.execute(sql):
                res.append( row )
                delList.append(str(row[0]))
        except sqlite3.Error as e:
            print(e.args[0], __file__,sys._getframe().f_lineno)
            return None

        # print(delList, ",".join(delList))
        if len(res)>0:
            sql = 'delete from '+self._get_tableName(tableName)+' where id in ('+ ",".join(delList) +")"
            try:
                self._conn.execute(sql)
            except sqlite3.Error as e:
                print(e.args[0], __file__,sys._getframe().f_lineno)
                return None
            # 不提交，可能不会写入数据表中
            self._conn.commit()
        return res

    def delAllTable(self):
        '''不能使用 多语句执行删除表操作'''
        # tableList=[]
        for row in self._conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"):
            sql = "DROP TABLE "+row[0]
            print(sql)
        for row in self._conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"):
            sql = "DROP TABLE "+row[0]
            # tableList.append(row)
            try:
                res = self._conn.execute(sql)
                print(res)
            except sqlite3.Error as e:
                print(e.args[0], __file__,sys._getframe().f_lineno)
                return False
        # sql = "DROP TABLE ?"

        return True

    def delTableData(self,tableName):
        sql = "DELETE FROM "+self._get_tableName(tableName)
        try:
            self._conn.execute(sql)
        except sqlite3.Error as e:
            print(e.args[0], __file__,sys._getframe().f_lineno)
            return False
        #不提交，可能不会写入数据表中
        self._conn.commit()

        return True

    def showTableInfo(self):
        """查看现在库中的所有表信息,sqlite_sequence表是在id自动增长时会存在，保存最后一个ID号"""
        for row in self._conn.execute("SELECT * FROM sqlite_master "):
            print(row)

    def showTableData(self,tableName, num=10):

        reCount = self.showTableDataCount(tableName)
        print("记录数：",reCount)
        if reCount <1:
            return

        if num is None:
            sql = "select * from "+self._get_tableName(tableName)
        else:
            sql = "select * from " + self._get_tableName(tableName)+" limit " + str(num)
        try:
            for row in self._conn.execute(sql):
                print(row)
        except sqlite3.Error as e:
            print(e.args[0], __file__,sys._getframe().f_lineno)

    def showTableDataCount(self,tableName):
        """获取表中有多少条记录"""
        res = 0
        sql = "select count(*) from " + self._get_tableName(tableName)
        try:
            for row in self._conn.execute(sql):
                res = row[0]
        except sqlite3.Error as e:
            print(e.args[0], __file__,sys._getframe().f_lineno)

        return res


def 测试1():
    '''新建库测试'''
    qqnewsDB = downList("qqnews.db")
    # qqnewsDB = downList("test/qqnews.db")
    # qqnewsDB.delAllTable()
    # qqnewsDB.showTableInfo()
    print("========================")
    '''新建表测试'''
    tableName =time.strftime("%Y%m%d", time.localtime())
    # tableName="20180129"
    qqnewsDB.createContextTable(tableName)
    qqnewsDB.showTableInfo()

def 测试2():
    '''新建库测试'''
    qqnewsDB = downList("qqnews.db")
    # qqnewsDB = downList("test/qqnews.db")
    # qqnewsDB.delAllTable()
    # qqnewsDB.showTableInfo()

    '''新建表测试'''
    tableName =time.strftime("%Y%m%d", time.localtime())
    # tableName="20180129"
    qqnewsDB.createContextTable(tableName)
    qqnewsDB.showTableInfo()

    '''插入数据测试，如果数据存在则更新，'''
    #执行两次，看3 4 列结果是否有变化
    for i in range(2):
        record = []
        for newsID in range(100):
            createDate = time.strftime("%Y%m%d%H%M%S", time.localtime())
            # a = (newsID, "http://test//"+str(newsID), createDate, createDate)
            a = ( "http://test//" + str(newsID), createDate, createDate)
            record.append(a)
        qqnewsDB.insertContextData(tableName, record)
        qqnewsDB.showTableData(tableName)
        reCount = qqnewsDB.showTableDataCount(tableName)
        print(reCount)

def 测试3():
    '''新建库测试'''
    qqnewsDB = downList("qqnews.db")
    # qqnewsDB = downList("test/qqnews.db")
    # qqnewsDB.delAllTable()
    # qqnewsDB.showTableInfo()

    '''新建表测试'''
    tableName =time.strftime("%Y%m%d", time.localtime())
    # tableName="20180129"
    qqnewsDB.createContextTable(tableName)
    qqnewsDB.showTableInfo()

    '''查找表中是否存在'''
    print()
    qqnewsDB.showTableData(tableName)
    recount = qqnewsDB.showTableDataCount(tableName)
    a = [2,20,200,25]
    res1, res2 = qqnewsDB.findContextNewsId(tableName, a) #存在返回TR

    print(tableName,res1,res2, recount)

def 测试4():
    '''新建库测试'''
    qqnewsDB = downList("qqnews.db")
    # qqnewsDB = downList("test/qqnews.db")
    # qqnewsDB.delAllTable()
    # qqnewsDB.showTableInfo()

    '''新建表测试'''
    tableName =time.strftime("%Y%m%d", time.localtime())
    # tableName="20180129"
    qqnewsDB.createContextTable(tableName)
    qqnewsDB.showTableInfo()

    '''队列测试'''
    record = []
    for newsID in range(100):
        a = ("http://test//"+str(newsID),)
        record.append(a)
    qqnewsDB.createQueueTable("queueList_T")
    qqnewsDB.queueList_Input("queueList_T",record)
    #查看取出的结果
    for i in range(50):
        res = qqnewsDB.queueList_Output("queueList_T")
        print(res)
        print("----------------------")
        qqnewsDB.showTableData("queueList_T")


if __name__ == '__main__':
    # 测试1()
    # 测试2()
    测试3()
    # 测试4()



    去重表名='table_sina_url'
    去重库名 = '../sinaNews.db'
    去重表page='table_page'

    qqnewsDB = downList(去重库名)
    qqnewsDB.showTableData(去重表page)
    recount = qqnewsDB.showTableDataCount(去重表page)
    print(recount)