# -*- coding:utf-8 -*-
"""俱乐部管理
"""


class ClubManager(object):

    def __init__(self):
        """服务器启动时加载一次,读取所有的club到内存中"""
        # 通过club_uuid为键存取club
        self.clubs = {}



if __name__ == '__main__':
    manager = ClubManager()
