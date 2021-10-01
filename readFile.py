import pymysql
import pandas as pd
# 读取数据 我这里是把 xlsx 文件放在了 python 文件的同一级目录下
df = pd.read_excel('test.xlsx')
datas=df.values
# print(datas)

#连接数据库
db = pymysql.connect(host = '47.114.110.135',port = 3306,user = 'root',passwd = 'Xrh981025',database = 'ShangHaiData',charset = 'utf8')

#获取游标
cursor  = db.cursor()

rowSum = 0
#数据操作
for data in datas:
    sqlHead = 'INSERT INTO clearAccount(eid,seq_no,leader,employees,clear_type,row_update_time) VALUES ('
    eid = data[1]
    seq_no = str(data[2])
    leader = data[3]
    employees = data[4]
    clear_type = str(data[5])
    row_update_time = data[6]
    # 拼接字符串
    sql = f'INSERT INTO absdaaa(eid, \
name, age, address, create_time) \
VALUES ("{eid}", "{leader}", "{seq_no}", "{employees}", "{row_update_time}");'
    print(sql)
    # 执行 sql 语句
    cursor.execute(sql)
    rowSum = rowSum + 1
    #将修改的内容提交到数据库
    db.commit()

print(f'共插入{rowSum}条数据')

#关闭游标和数据库连接
cursor.close()
db.close()
