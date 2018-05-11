# -*- coding:utf-8 -*-
"""俱乐部管理
"""
import json
import time
from config import db

from club import GameClub
from utils.generate_uuid import compress_uuid
from utils.gameError import GameException


class ClubManager(object):

    def __init__(self):
        """服务器启动时加载一次,读取所有的club到内存中"""
        # 通过club_uuid为键存取club
        self._clubs = self.prepare_clubs()

    def prepare_clubs(self):
        """将所有club读入内存 status=1"""
        active_clubs = []
        db.cur.callproc('find_active_clubs')
        results = db.cur.fetchall()
        active_clubs = {item[0]: GameClub(uuid=item[0]) for item in results}
        for k, v in active_clubs.items():
            print k, v
        return active_clubs

    def create_new_club(self, *args, **kwargs):
        """创建俱乐部 name, chair_uuid, game_types
        name:俱乐部名称　char_uuid:主席用户id"""
        result = {}
        try:
            name = kwargs.get('name', '')
            chairman = kwargs.get('chair_uuid')
            game_type = kwargs.get('game_types')
            uuid = compress_uuid()
            create_time = time.time()

            # 调用存储过程，创建一条俱乐部信息
            db.cur.callproc('create_game_club', (chairman, create_time, uuid,
                                                 name, game_type))

            # result = db.cur.fetchall()[0]
            # print 'result-----: {}'.format(result)
            # self.pay_type, self.max_person, self.game_card, self.game_types, self.status = result
            # print self.pay_type, self.max_person, self.game_card, self.game_types, self.status

            # 生成club对象加载到内存中
            self._clubs['uuid'] = GameClub(uuid=uuid)
            result['status'] = 'ok'
            result['msg'] = 'create new club success'
        except GameException as game_error:
            result['status'] = 'failed'
            result['msg'] = game_error.message
            print "club init error: {}".format(game_error.message)
        except Exception as e:
            result['status'] = 'failed'
            result['msg'] = e.message
            print "club init error: {}".format(e.message)
        finally:
            return result


if __name__ == '__main__':
    manager = ClubManager()
    print manager.__dict__
