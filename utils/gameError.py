# -*- coding:utf-8 -*-


class GameException(Exception):

    def __init__(self, msg):
        Exception.__init__(self, msg)


def new_cur(db):
    db.cur.close()
    db.cur = db.conn.cursor()