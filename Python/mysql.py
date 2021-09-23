import pymysql
#连接数据库
db = pymysql.connect(host = 'xxxxx',port = 3306,user = 'root',passwd = '****',database = 'xrhTest',charset = 'utf8')

#获取游标
cursor  = db.cursor()

#数据操作

sql = 'select * from tb_stu1;'
cursor.execute(sql)
ret1 = cursor.fetchone()  # 取一条
print(ret1)
# cur.execute('INSERT INTO tb_stu1(id,name,sex,birthday) VALUES ( 1,"小明", "男", "2015-11-02");')
##将修改的内容提交到数据库
# db.commit()

#关闭游标和数据库连接
cursor.close()
db.close()
