#!/usr/bin/python
#-\*-coding: utf-8-\*-

'''
数据库授权
mysql -uroot -pqwert -hlocalhost
grant all on *.* to 'inception'@"%" identified by "123456";
flush privileges;

配置inc.cnf
inception_remote_backup_host=127.0.0.1
inception_remote_backup_port=3306
inception_remote_system_user=inception
inception_remote_system_password=123456
'''

''' 建表语句
CREATE DATABASE pro1;
CREATE TABLE IF NOT EXISTS pro1.mytable1 (
   `id` INT UNSIGNED AUTO_INCREMENT,
   `myname` VARCHAR(10) NOT NULL,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

'''

import pymysql

# 待审核/执行的sql语句（实际数据库的地址、端口 等参数）
sql='/*--user=root;--password=bbotte;--host=127.0.0.1;--port=3306;--enable-execute;*/\
inception_magic_start;\
use pro1;\
insert into mytable1 (myname) values ("bbotte");\
inception_magic_commit;'
try:
    conn=pymysql.connect(host='127.0.0.1',user='inception',passwd='123456',db='',port=6669,use_unicode=True,charset="utf8")    #inception配置文件inc.cnf中的用户名和密码
    cur=conn.cursor()
    ret=cur.execute(sql)
    result=cur.fetchall()
    num_fields = len(cur.description) 
    field_names = [i[0] for i in cur.description]
    print(result)
    cur.close()
    conn.close()
except pymysql.Error as e:
    print("Mysql Error %d: %s" % (e.args[0], e.args[1]) )
