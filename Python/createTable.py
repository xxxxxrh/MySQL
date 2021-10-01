import pymysql

#连接数据库
db = pymysql.connect(host = '47.114.110.135',port = 3306,user = 'root',passwd = 'Xrh981025',database = 'ShangHaiData',charset = 'utf8')

#获取游标
cursor  = db.cursor()


#创建 absdaaa 表
sql = """
    create table absdaaa(
    eid varchar(255) not null PRIMARY KEY,
    name varchar(255),
    age int,
    address varchar(255),
    create_time datetime
    )
"""

try:
    # 执行SQL语句
    cursor.execute(sql)
    print("创建数据库成功")
    # 查看创建了哪些表
    cursor.execute("SHOW TABLES")
    for x in cursor:
        print(x)
except Exception as e:
    print("创建数据库失败：case%s"%e)
finally:
    #关闭游标连接
    cursor.close()
    # 关闭数据库连接
    db.close()