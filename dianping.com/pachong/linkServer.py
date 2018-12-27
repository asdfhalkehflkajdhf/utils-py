import  pymysql
import time


class linkServer():
    def __init__(self, host, user, pw, dbname):
        self.host=host
        self.user = user
        self.pw = pw
        self.dbname = dbname



    def getLinkState(self, key):
        # 打开数据库连接
        # db = pymysql.connect("localhost", "root", "123456", "dianpingstatusvalidation", charset='utf8')
        try:
            db = pymysql.connect(self.host, self.user, self.pw, self.dbname, charset='utf8')
            if db is None:
                #     链接db失败,
                '''检查是网络问题还是服务器问题'''
                return

            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

            sql = 'CALL link_check("%s", %d)'%(key, int(round(time.time() * 1000)))

            # 使用 execute()  方法执行 SQL 查询
            cursor.execute(sql)

            # 使用 fetchone() 方法获取单条数据.
            # print(cursor.fetchall())
            data = cursor.fetchone()

            # print("data : %s " % data)
            # 关闭数据库连接
            cursor.close()
            '''更新数据操作必须执行　commit'''
            db.commit()
            db.close()
        except Exception as e:
            print(e)
        return data

    def setHeartBeat(self, key):
        """
        返回　none 为失败
        :param key:
        :return:
        """
        # 打开数据库连接
        try:
            # db = pymysql.connect("localhost", "root", "123456", "dianpingstatusvalidation", charset='utf8')
            db = pymysql.connect(self.host, self.user, self.pw, self.dbname, charset='utf8')
            if db is None:
                #     链接db失败,
                '''检查是网络问题还是服务器问题'''
                return

            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
            sql = 'CALL up_user_state("%s")'%(key)
            # 使用 execute()  方法执行 SQL 查询
            cursor.execute(sql)

            # 使用 fetchone() 方法获取单条数据.
            # print( cursor.fetchone() )
            data = cursor.fetchone()
            # 关闭数据库连接
            cursor.close()
            db.commit()
            db.close()
        except Exception as e:
            '''写入日志'''
            print(e)
        return data
if __name__=="__main__":
    db = linkServer("localhost", "root", "123456", "dianpingstatusvalidation")
    print( db.getLinkState('ffffffs') )
    print( db.setHeartBeat('ffffffs') )
    # db.getLinkState()
