"""
数据库模块
"""
import mysql.connector
from mysql.connector import Error
from typing import Optional
from mysql.connector.connection import MySQLConnection

# 创建数据库连接
def db_connect() -> Optional[MySQLConnection]:
    """
    连接数据库
    参数：
        None
    返回值：
        db：数据库连接对象
    """
    try:
        db = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="your_username_here",
            password="your_password_here",
            database="your_database"
            )
    except Error as e:
            print("数据库连接失败:", e)
            db = None
    return db

if __name__ == '__main__':
    db_connect()
    cursor = db.cursor()
    db.close()
    db_connect()
    
    if db.is_connected():
        print("数据库连接成功!")
        db.close()
    else:
        print("数据库连接失败!")
