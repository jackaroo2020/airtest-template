#coding = utf-8

"""
数据库操作封装通用工具模块函数
"""

__author__ = "LT"

from airtest.core.api import *

import pymysql
from DBUtils.PooledDB import PooledDB, SharedDBConnection
from DBUtils.PersistentDB import PersistentDB, PersistentDBError, NotSupportedError

using("myconfig.air")
from myconfig import mysql_config

config = mysql_config

def get_db_pool(is_mult_thread):
    if is_mult_thread:
        poolDB = PooledDB(
            # 指定数据库连接驱动
            creator=pymysql,
            # 连接池允许的最大连接数,0和None表示没有限制
            maxconnections=3,
            # 初始化时,连接池至少创建的空闲连接,0表示不创建
            mincached=2,
            # 连接池中空闲的最多连接数,0和None表示没有限制
            maxcached=5,
            # 连接池中最多共享的连接数量,0和None表示全部共享(其实没什么卵用)
            maxshared=3,
            # 连接池中如果没有可用共享连接后,是否阻塞等待,True表示等等,
            # False表示不等待然后报错
            blocking=True,
            # 开始会话前执行的命令列表
            setsession=[],
            # ping Mysql服务器检查服务是否可用
            ping=0,
            **config
        )
    else:
        poolDB = PersistentDB(
            # 指定数据库连接驱动
            creator=pymysql,
            # 一个连接最大复用次数,0或者None表示没有限制,默认为0
            maxusage=1000,
            **config
        )
    return poolDB

# 创建连接
def create_conn():
    # 以单线程的方式初始化数据库连接池
    db_pool = get_db_pool(False)
    # 从数据库连接池中取出一条连接
    conn = db_pool.connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    return conn, cursor

# 关闭连接
def close_conn(conn, cursor):
    conn.close()
    cursor.close()

# 查询一条
def select_one(sql, args):
    conn, cur = create_conn()
    cur.execute(sql, args)
    result = cur.fetchone()
    close_conn(conn, cur)
    return result

# 根据条件查询所有
def select_all(sql, args):
    conn, cur = create_conn()
    cur.execute(sql, args)
    result = cur.fetchall()
    close_conn(conn, cur)
    return result

# 新增一条记录
def insert_one(sql, args):
    conn, cur = create_conn()
    result = cur.execute(sql, args)
    conn.commit()
    close_conn(conn, cur)
    return result

# 新增一条纪录 并返回主键id
def insert_one_pk(sql, args):
    conn, cur = create_conn()
    result = cur.execute(sql, args)
    conn.commit()
    close_conn(conn, cur)
    return cur.lastrowid

# 删除一条记录
def delete_one(sql,args):
    conn,cur = create_conn()
    result = cur.execute(sql,args)
    conn.commit()
    close_conn(conn,cur)
    return result
    
# 更新一条记录
def update_one(sql,args):
    conn,cur = create_conn()
    result = cur.execute(sql,args)
    conn.commit()
    close_conn(conn,cur)
    return result


# 私有方法内部启动测试
if __name__ == '__main__':
    # 增加
    # sql = "insert into uicase(id,type) VALUE (%s,%s)" 
    # res = insert_one(sql, [2,"test"])
    # print(res)
    
    # 删除
    # sql = "delete from uicase where id = %s"   
    # res = delete_one(sql, 2)
    # print(res)

    # 查询全部
    # sql = "select * from uicase" 
    # res = select_all(sql, [])
    # print(res)

    # 查询一条
    sql = "select * from uicase where id=%s"
    res = select_one(sql, "1")
    print(res)

    # 更新
    # sql = " UPDATE uicase set type=%s where id = %s"
    # res = update_one(sql,("myupdate","2"))
    # print(res)

