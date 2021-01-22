import pymysql

#连接数据库
db=pymysql.connect(host='49.233.125.29',port=8066,
                     user='zmkb',password='3r4edvfc%TGB',
                   cursorclass=pymysql.cursors.DictCursor)
#初始化游标
cursor=db.cursor()

#执行sql语句
cursor.execute("select mobile from zjx_pad.users  limit 5")
cursor.execute("update zjx_pad.users set mobile='13472293379' where userid=123")

#提交事务
db.commit()
#获取首行数据
print(cursor.fetchone())

#获取所有行数据
print(cursor.fetchall())

#游标对象关闭
cursor.close()
#关闭连接
db.close()
