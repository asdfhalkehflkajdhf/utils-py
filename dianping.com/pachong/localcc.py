''''''

'''实现本地数据和配置存储'''
'''
-- 表：table_businessInfo
DROP TABLE IF EXISTS table_businessInfo;
CREATE TABLE table_businessInfo (business_id BIGINT (20) PRIMARY KEY, review_all BIGINT (20), review_tg BIGINT (20));

-- 表：table_commentInfo
DROP TABLE IF EXISTS table_commentInfo;
CREATE TABLE table_commentInfo (comment_id INTEGER PRIMARY KEY AUTOINCREMENT, ctime DATETIME, context TEXT, type_id BIGINT, level INTEGER, business_id INT, font_id INTEGER, layout_id INTEGER);

-- 表：table_commentType　固定的
DROP TABLE IF EXISTS table_commentType;
CREATE TABLE table_commentType (type_id INTEGER PRIMARY KEY AUTOINCREMENT, "desc" TEXT);

-- 表：table_config  php读取和配置
DROP TABLE IF EXISTS table_config;
CREATE TABLE table_config (crawlingInterval INTEGER);
INSERT INTO table_config (crawlingInterval) VALUES (60);

-- 表：table_coreStat 固定一条记录，core程序进行更新
DROP TABLE IF EXISTS table_coreStat;
CREATE TABLE table_coreStat (state BOOLEAN, uptime DATETIME);

-- 表：table_fontLibrary　添加
DROP TABLE IF EXISTS table_fontLibrary;
CREATE TABLE table_fontLibrary (font_id INT PRIMARY KEY, url CHAR (256));

-- 表：table_layout   添加
DROP TABLE IF EXISTS table_layout;
CREATE TABLE table_layout (layout_id INT PRIMARY KEY, url CHAR (256));

'''
import sqlite3

class localcc():
    def __init__(self, dbPath):
        self.db_conn = sqlite3.connect(dbPath)
        '''https://blog.csdn.net/zhaihaifei/article/details/53898260
        转化为字典格式的工厂方法
        '''
        self.db_conn.row_factory=self.__dict_factory
        self.db_cursor = self.db_conn.cursor()
        pass

    def __del__(self):
        self.db_cursor.close()
        self.db_conn.close()

    def __dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def __BKDRHash(self, str):
        seed = 131
        hash = 0
        for ch in str:
            hash = hash * seed + ord(ch)
        return hash & 0x7FFFFFFF

    def getTableBusinessInfo(self):
        """

        :return:
        """
        sql = "select business_id, review_all, review_tg, desc, uptime from table_businessInfo;"
        self.db_cursor.execute(sql)
        return self.db_cursor.fetchall()
        pass

    def upTableBusinessInfo(self, business_id, review_all, review_tg, desc, uptime):
        """
        :param business_id:
        :param review_all:
        :param review_tg:
        :param desc:
        :param uptime:
        :return:
        """
        sql = "updata table_businessInfo set review_all=%d, review_tg=%d, desc='%s', uptime='%s' where business_id=%d;"%(review_all, review_tg, desc, uptime, business_id)
        self.db_cursor.execute(sql)
        self.db_conn.commit()

    def addTableCommentInfo(self,stime, context, type_id, level, business_id, font_id, layout_id_list):
        """

        :return:
        """
        sql = "insert into table_commentInfo(ctime, context, type_id, level, business_id, font_id, layout_id) values('%s', '%s', %d, %d, %d, %d, '%s')"%(
            stime, context, type_id, level, business_id, font_id, layout_id_list
        )
        self.db_cursor.execute(sql)
        self.db_conn.commit()
        pass

    def upTableCoreStat(self, state):
        """
        :param state: 0表示正常，非０表示出错，可以到出错表查找相应信息
        :return:
        """
        sql = "update table_coreStat set state=%d, uptime=datetime();"%(state)
        self.db_cursor.execute(sql)
        self.db_conn.commit()
        pass

    def addTableFontLibrary(self, url):
        hashKey = self.__BKDRHash(url)
        sql = """insert or IGNORE into table_fontLibrary(url, font_id, hash_key)values('%s', %d, %d);"""%(url, hashKey, hashKey)
        self.db_cursor.execute(sql)
        self.db_conn.commit()
        return hashKey
        pass

    def addTableLayout(self, url):
        hashKey = self.__BKDRHash(url)
        sql = """insert or IGNORE into table_layout(url, layout_id, hash_key)values('%s', %d, %d);"""%(url, hashKey, hashKey)
        self.db_cursor.execute(sql)
        self.db_conn.commit()
        return hashKey
        pass

    def addCommentType(self, desc):
        """

        :param desc:
        :return:
        """
        hashKey = self.__BKDRHash(desc)
        sql = "insert into [table_commentType]([type_id], [desc]) select %d, '%s' where not exists (select type_id, desc from [table_commentType] where [type_id]=%d)"%(hashKey, desc, hashKey)
        self.db_cursor.execute(sql)
        self.db_conn.commit()
        return hashKey

    def addErrorInfo(self, desc):
        """

        :param desc:
        :return:
        """
        sql = """insert into table_errorInfo(desc, ctime)values('%s', datetime());"""%(desc)
        # sql = """insert into table_errorInfo(desc, ctime)values('%s', '2018-12-11 13:06');""" % (desc)
        self.db_cursor.execute(sql)
        self.db_conn.commit()

if __name__=="__main__":
    t = localcc('cc')
    t.addErrorInfo("asdf")
