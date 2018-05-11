# -*- coding:utf-8 -*-

import time

from config import db
from utils.generate_uuid import compress_uuid

from utils.gameError import GameException


class GameClub(object):

    def __init__(self, *args, **kwargs):
        """俱乐部初始化 传入uuid 若存在俱乐部则读取俱乐部数据,否则创建新的俱乐部"""
        db.cur.close()
        db.cur = db.conn.cursor()
        self.uuid = kwargs.get('uuid')
        db.cur.callproc('get_club_by_uuid', (self.uuid, ))
        result = db.cur.fetchall()
        assert len(result) == 1
        self.name, self.pay_type, self.max_person, self.game_card, self.chairman, \
            self.game_type, self.status, self.create_time = result[0]

        # 其余俱乐部初始化工作

    # def __repr__(self):
    #     print '<class: GameClub>: {}'.format(self.name)


    # TODO 仅正主席可设置
    def set_pay_type(self, **kwargs):
        """设置俱乐部付费方式 int 0:平摊付费 1:代理付费"""
        self.pay_type = kwargs.get('pay_type')
        # 暂未考虑权限

        # update club info

    def delete_club(self, **kwargs):
        """删除俱乐部：改变俱乐部状态status=0 """
        # TODO权限控制
        result = {}
        try:
            status = kwargs.get('status')
            if self.status != status:
                self.status = status
                db.cur.callproc('delete_club', (self.status, self.uuid))
                # update db
            result['status'] = 'ok'
            result['msg'] = 'delete club success'
        except Exception as e:
            result['status'] = 'failed'
            result['msg'] = 'delete club failed; {}'.format(e.message)
        finally:
            return result

    def update_club_info(self, **kwargs):
        """更新俱乐部基本信息,name, pay_type, """
        result = {}
        try:
            self.name = kwargs.get("name")
            self.pay_type = kwargs.get("pay_type")
            #
            result['status'] = 'ok'
            result['msg'] = 'setting success'
        except Exception as e:
            result['status'] = 'failed'
            result['msg'] = e.message
        finally:
            return result

    def setting_club(self, **kwargs):
        """后台修改俱乐部信息接口,可修改status和max_person"""
        result = {}
        try:
            self.status = kwargs.get("status")
            self.max_person = kwargs.get("max_person")
            #
            db.cur.callproc('update_club_info', (self.uuid, self.status, self.max_person))
            result['status'] = 'ok'
            result['msg'] = 'set success'
        except Exception as e:
            result['status'] = 'failed'
            result['msg'] = e.message
        finally:
            return result

    def turn_cards_to_user(self, **kwargs):
        """给用户转卡 转让俱乐部库存给用户
        user: user id , num:充值数量
        """
        result = {}
        try:
            user_id = kwargs.get('user')
            num = kwargs.get("num")
            #
        except Exception as e:
            result['status'] = 'failed'
            result['msg'] = e.message
        finally:
            return result




def applying_for_club(user_id, club_id=None, club_name=None):
    """申请加入俱乐部, 通过club_id, 或club_name申请加入俱乐部"""
    result = {}
    try:
        if not club_id and not club_name:
            raise GameException("club_id or club_name is need!")

    except GameException as game_err:
      result['result'] = 'failed'
      result['msg'] = game_err.message


if __name__ == '__main__':
    data = {"name": '--我的俱乐部231', "chair_uuid": 18263, "game_types": '1'}
    club = GameClub(**data)
    print club.__dict__
    db.close()
