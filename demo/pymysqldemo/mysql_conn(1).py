# Edit by zhengnan 2020/1/17#

import pymysql

'''
# 打开数据库连接
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='test',charset='utf8')

# 使用cursor()方法创建一个游标对象
cursor = conn.cursor()

#  使用execute()方法执行SQL查询
cursor.execute('Select version()')

# 使用fetchone()方法获取单条数据
data = cursor.fetchone()

# 打印
print('database version: %s' % data)

# 关闭数据库连接
cursor.close()
conn.close()'''


'''*****************数据库创建表操作*******************'''
# 打开数据库连接
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='test')

# 使用cursor()方法创建一个游标对象cursor
cursor = conn.cursor()  # 游标对象用于执行查询和获取结果

# 使用execute()方法执行SQL，如果表存在则将其删除
cursor.execute('DROP TABLE IF EXISTS test_employee')

# 使用预处理语句创建表
sql = """CREATE TABLE `test_employee` (
  `first_name` varchar(255) DEFAULT NULL COMMENT '姓',
  `last_name` varchar(255) DEFAULT NULL COMMENT '名',
  `age` int(11) DEFAULT NULL COMMENT '年龄',
  `sex` varchar(255) DEFAULT NULL COMMENT '性别',
  `income` varchar(255) DEFAULT NULL COMMENT '收入'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""

# 执行SQL语句
cursor.execute(sql)

# 关闭数据库连接
conn.close()


'''*****************数据库插入操作*******************'''
# 打开数据库连接
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='test')

# 使用cursor()方法获取操作游标
cursor = conn.cursor()

# SQL语句：向数据表中插入数据
sql = """INSERT INTO test_employee(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

# 异常处理
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交事务到数据库执行
    conn.commit()  # 事务是访问和更新数据库的一个程序执行单元
except:
    # 如果发生错误则执行回滚操作
    conn.rollback()

# 关闭数据库连接
conn.close()


'''*****************数据库查询操作*******************'''
# 打开数据库连接
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='test')

# 使用cursor()方法获取操作游标
cursor = conn.cursor()

# SQL语句：查询
sql = "SELECT * FROM test_employee WHERE income > 1000 "

# 异常处理
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有的记录列表
    results = cursor.fetchall()
    # 遍历列表
    for row in results:
        # 打印列表元素
        print(row)
        # 姓
        first_name = row[0]
        # 名
        last_name = row[1]
        # 年龄
        age = row[2]
        # 性别
        sex = row[3]
        # 收入
        income = row[4]
        # 打印列表元素
        print(first_name, last_name, age, sex, income)
except:
    print('Uable to fetch data!')

# 关闭数据库连接
conn.close()


'''*****************数据库更新操作*******************'''
# 打开数据库连接
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='test')

# 使用cursor()方法获取操作游标
cursor = conn.cursor()

# SQL语句，执行更新操作
sql = 'UPDATE test_employee SET age = age + 5 WHERE sex = "M"'

# 异常处理
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交到数据库执行
    conn.commit()
except:
    # 发生错误时回滚
    conn.rollback()

# 关闭数据库连接
conn.close()


'''*****************数据库表删除操作*******************'''
# 打开数据库连接
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='test')

# 使用cursor()方法获取操作游标
cursor = conn.cursor()

# SQL语句，执行删除操作
sql = 'DELETE FROM test_employee WHERE age >20'

# 异常处理
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交到数据库执行
    conn.commit()
except:
    # 发生错误时回滚
    conn.rollback()

# 关闭数据库连接
conn.close()