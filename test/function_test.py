# -*-coding:utf-8 -*-

from gameClub.club import GameClub
from gameClub.clubManager import ClubManager
from gameClub.config import db

manager = ClubManager()


def test_create_apply(club_id):
    """user申请创建加入俱乐部"""
    user = 18267  # uid
    # club_id = 'ec29cdeaa4647e4cf1b38ea06ec83b503b'
    manager.applying_for_club(club_id=club_id, user_id=user)


def test_get_appling_list(club_id):
    club_obj = manager._clubs[club_id]
    print club_obj.name
    appling_list = club_obj.appling_user_list()
    print 'appling_list: {}'.format(appling_list)
    return appling_list


def test_appling_handler(club_id, appling_id):
    """"""
    club_obj = manager._clubs[club_id]
    print appling_id
    result = club_obj.appling_handler(status=1, appling_id=appling_id)
    return result


def test_get_member(club_id):
    club_obj = manager._clubs[club_id]
    result = club_obj.get_member()
    print 'members: {}'.format(result)


def main(club_id):
    print manager.__dict__
    # 创建俱乐部申请
    test_create_apply(club_id)
    # 获取俱乐部未处理申请列表
    result = test_get_appling_list(club_id)
    assert result['status'] == 'ok'
    # 通过第一个未处理的申请
    appling_id = result['data'][0][0]
    print test_appling_handler(club_id, appling_id)
    #  获取俱乐部成员列表
    test_get_member(club_id)

if __name__ == '__main__':
    club_id = 'ec29eaa4647e4cf1b38ea06ec83b503b'
    main(club_id)



