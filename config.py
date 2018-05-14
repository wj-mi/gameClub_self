# -*- coding:utf-8 -*-
"""mysql 配置，全局暂用一个连接"""
import MySQLdb


class BaseDB():
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user='root',
        passwd='123456',
        db='games',
    )

    def __init__(self):
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()


db = BaseDB()
