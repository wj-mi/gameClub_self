# -*- coding:utf-8 -*-


class GameException(Exception):

    def __init__(self, msg):
        Exception.__init__(self, msg)

