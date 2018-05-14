# -*- coding:utf-8 -*-

import time

from config import db
from utils.generate_uuid import compress_uuid

from utils.gameError import GameException, new_cur


class GameClub(object):

    def __init__(self, *args, **kwargs):
        """俱乐部初始化 传入uuid 若存在俱乐部则读取俱乐部数据,否则创建新的俱乐部"""
        new_cur(db)
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

    def appling_user_list(self):
        """查看俱乐部未处理申请消息"""
        result = {}
        new_cur(db)
        db.cur.callproc('find_appling', (self.uuid,))
        data = db.cur.fetchall()
        print data
        result['status'] = 'ok'
        result['data'] = list(data)
        return result

    # TODO权限
    def appling_handler(self, **kwargs):
        """处理用户加入俱乐部请求
        apply_id: 用户申请表id
        status: 审核结果 1: 通过 -1: 拒绝 0:暂未处理
        """
        new_cur(db)
        result = {}
        try:
            # 改变申请状态,若status=1 通过, user加入club关联表
            status = kwargs.get('status')
            appling_id = kwargs.get('appling_id')

            # call proc
            db.cur.callproc("club_appling_handler", (appling_id, status, time.time()))
            result['status'] = 'ok'
            result['msg'] = 'success'
        except Exception as e:
            result['status'] = 'failed'
            result['msg'] = e.message
        finally:
            return result

    def get_member(self, **kwargs):
        """获取俱乐部所有会员"""
        new_cur(db)
        result = {}
        db.cur.callproc('get_club_member', (self.uuid,))
        data = db.cur.fetchall()
        result['status'] = 'ok'
        result['data'] = list(data)
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





if __name__ == '__main__':
    data = {"name": '--我的俱乐部231', "chair_uuid": 18263, "game_types": '1'}
    club = GameClub(**data)
    print club.__dict__
    db.close()
