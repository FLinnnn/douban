#-*- coding = utf-8 -*-
#@Author : FLin
#@Time : 2020/9/24 22:21
#@SoftWare : PyCharm
import sqlite3
# 打开或创建
conn=sqlite3.connect("test.db")
'''
# 获取游标
c=conn.cursor()
# sql语句
sql='''
# CREATE TABLE company
# (id int primary key not null,
# name text not null,
# age int not null,
# address char(50),
# salary real);
'''
#执行语句
c.execute(sql)
# 提交数据库操作
conn.commit()
# 关闭数据库连接
conn.close()

# print("open database success")


'''
# 插入
'''
c=conn.cursor()
sql='''
# INSERT INTO company(id,name,age,address,salary)
# VALUES (1,"fl",18,"xian",9999);
'''
c.execute(sql)
conn.commit()
conn.close()
'''
# 查询
c=conn.cursor()
sql='''
SELECT id,name,age,address,salary from company
'''
i=c.execute(sql)
for key in i:
    print(key)
    print("id={}".format(key[0]))
    print("name={}".format(key[1]))
    print("age={}".format(key[2]))
    print("address={}".format(key[3]))
    print("salary={}".format(key[4]))

conn.close()


