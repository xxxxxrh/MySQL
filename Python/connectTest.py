import pymysql


#连接数据库
db = pymysql.connect(host = 'xxxxx',port = 3306,user = 'root',passwd = '****',database = 'xrhTest',charset = 'utf8')


#获取游标
cursor  = db.cursor()


# 拼接字符串
sql = 'select * from clearAccount'
# 执行 sql 语句
cursor.execute(sql)
results = cursor.fetchall()
print(results)
#关闭游标和数据库连接
cursor.close()
db.close()
