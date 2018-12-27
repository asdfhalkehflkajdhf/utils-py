import sqlite3
import os
import time
import sys

class commentsList():
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

    # comments
    # table_文章ID
    # 时间，内容，层级，用户id, 昵称，评论id, 父评论id
    def createContextTable(self,tableName):
        """表名不能以数字开头，所以表名为 前缀+YYYYMMDD，  tableName为YYYYMMDD
        create table if not exists tableName,主要作用是url去重和更新数据   YYYYMMDD"""

        sql = 'create table if not exists '+self._get_tableName(tableName)+' (' \
                'cmtId VARCHAR(64) PRIMARY KEY, ' \
                'rootId VARCHAR(64),'\
                'pId VARCHAR(64),'\
                'userId  VARCHAR(64),' \
                'userpId  VARCHAR(64),' \
                'userNick VARCHAR(64),' \
                'userRegion VARCHAR(64),' \
                'date VARCHAR(11) not NULL,' \
                'time VARCHAR(9) not NULL,' \
                'dateTime VARCHAR(20) not NULL,' \
                'up integer,' \
                'content VARCHAR(1024)' \
                ' )'

        try:
            self._conn.execute(sql)
        except sqlite3.Error as e:
            print(e.args[0], __file__,sys._getframe().f_lineno)
            return False
        print("createContextTable ok")
        return True

    def insertContextData(self, tableName, data):
        """
        tableName: 按日期建表
        data: 是一个list

            'cmtId VARC
            'rootId VAR
            'pId VARCHA
            'userId  VA
            'userpId  V
            'userNick V
            'userRegion
            'date VARCH
            'time VARCH
            'dateTime V
            'up integer
            'content VA
             [
             (cmtId, rootId, pId, userId userpId, userNick, userRegion, date, time, dateTime, up, content),
             (cmtId, rootId, pId, userId userpId, userNick, userRegion, date, time, dateTime, up, content),
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
        sql = 'INSERT OR REPLACE INTO '+self._get_tableName(tableName)+" VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
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

    def findContext(self, tableName, startDate, endDate):
        """return list :返回列表, date 参数格式 为yyyy-mm-dd"""
        # executemany() can only execute DML statements,不能执行select 操作
        sql = "select * from " + self._get_tableName(tableName) + " where date >= '%s' and date <= '%s'"%(startDate, endDate)
        print(sql)
        resFindTrue = []
        try:
            for row in self._conn.execute(sql):
                resFindTrue.append( row )
        except sqlite3.Error as e:
            print(e.args[0], __file__,sys._getframe().f_lineno)
            e_str = e.args[0]
            if e_str.split(':')[0].__eq__("no such table"):
                self.createContextTable(tableName)
            # return False
        return resFindTrue

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

        reCount = self.getTableDataCount(tableName)
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

    def getTableDataCount(self,tableName):
        """获取表中有多少条记录"""
        res = 0
        sql = "select count(*) from " + self._get_tableName(tableName)
        try:
            for row in self._conn.execute(sql):
                res = row[0]
        except sqlite3.Error as e:
            print(e.args[0], __file__,sys._getframe().f_lineno)

        return res

    def checkTableNameIsExists(self,tableName):
        """返回0不存在，返回1存在"""
        sql = "SELECT COUNT(*) FROM sqlite_master where type='table' and name='%s'"%(self._get_tableName(tableName))
        for row in self._conn.execute(sql):
            return row[0]
            # print(row[0], type(row))
    def getTableList(self):
        tableList=[]
        sql = "SELECT name FROM sqlite_master where type='table' "
        for row in self._conn.execute(sql):
            tableList.append( row[0])
        return tableList


def 测试1():
    '''新建库测试'''
    qqnewsDB = commentsList("comment.db")
    # qqnewsDB = downList("test/qqnews.db")
    # qqnewsDB.delAllTable()
    qqnewsDB.showTableInfo()
    qqnewsDB.getTableList()
    print("========================")
    '''新建表测试'''
    tableName =time.strftime("%Y%m%d", time.localtime())
    # tableName="20180129"
    reCount = qqnewsDB.getTableDataCount(tableName)
    print(reCount)
    qqnewsDB.createContextTable(tableName)
    qqnewsDB.showTableInfo()

def 测试2():
    '''新建库测试'''
    qqnewsDB = commentsList("comment.db")
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
    # [
    #     (cmtId, rootId, pId, userId userpId, userNick, userRegion, date, time, dateTime, up, content),
    # (cmtId, rootId, pId, userId , userpId, userNick, userRegion, date, time, dateTime, up, content),
    # ]

    for i in range(2):
        record = []
        for newsID in range(100):
            createDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # a = (newsID, "http://test//"+str(newsID), createDate, createDate)
            a = ( "123123132123"+str(newsID), '0','0','fasdf','0','中国','北主', createDate.split()[0], createDate.split()[1], createDate, 2, 'asd士大夫')
            record.append(a)
        a = (
        "1231231321232222", '0', '0', 'fasdf', '0', '中国', '北主', '2018-02-05', createDate.split()[1], createDate, 2,
        'asd士大夫')

        record.append(a)
        qqnewsDB.insertContextData(tableName, record)
        qqnewsDB.showTableData(tableName)
        reCount = qqnewsDB.getTableDataCount(tableName)
        print(reCount)

def 测试3():
    '''新建库测试'''
    qqnewsDB = commentsList("comment.db")
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
    recount = qqnewsDB.getTableDataCount(tableName)
    print('total:',recount)
    res = qqnewsDB.findContext(tableName, '2018-02-01', '2018-02-10')
    print(tableName,res.__len__(),res)

    res = qqnewsDB.findContext(tableName, '2018-02-15', '2018-02-15')
    print(tableName,res.__len__(),res)

def 测试4():
    qqnewsDB = commentsList("comment.db")
    '''新建表测试'''
    tableName =time.strftime("%Y%m%d", time.localtime())

    qqnewsDB.checkTableNameIsExists(tableName)
    qqnewsDB.checkTableNameIsExists(tableName+'sss')

if __name__ == '__main__':
    测试1()
    # 测试2()
    # 测试3()
    # 测试4()

