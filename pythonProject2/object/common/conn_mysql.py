#数据库
import pymysql
from pymysql.cursors import DictCursor
class MysqlHandler:
    def __init__(self,host=None,user=None,password=None,port=3306,database=None,charset='utf8',cursorclass=DictCursor):
        self.conn=pymysql.connect(host=host,user=user,password=password,port=port,
                                  database=database,charset='utf8',cursorclass=DictCursor)#连接数据库
        self.cursor = self.conn.cursor()  # 实例化游标
    def query(self,sql,one=True):
        self.cursor.execute(sql)#执行sql语句

        if one:
            return self.cursor.fetchone()#返回一条查询结果
        return self.cursor.fetchall()#返回全部查询结果
    def mysql_close(self):

        self.conn.close()#关闭
        self.cursor.close()
