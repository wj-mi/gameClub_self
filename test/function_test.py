# -*-coding:utf-8 -*-

from gameClub.club import GameClub
from gameClub.clubManager import ClubManager
from gameClub.config import db


manager = ClubManager()


class TestDemo(object):

    def test_create_club(self):
        club = GameClub(name='--test club231', chair_uuid=18263, game_types='1')
        print club.name

    # def test_get_reward(self):
    #     db.cur.callproc('get_reward', 3)
    #     result = db.cur.fetchall()
    #     print result


def test_create_apply(club_id):
    """user申请创建加入俱乐部"""
    user = 18263  # uid
    # club_id = 'ec29cdeaa4647e4cf1b38ea06ec83b503b'
    manager.applying_for_club(club_id=club_id, user_id=user)


def test_get_appling_list():
    club_obj = manager._clubs['club_id']
    print club_obj.name
    appling_list = club_obj.appling_user_list()
    print 'appling_list: {}'.format(appling_list)


def main(club_id):
    test_create_apply(club_id)
    test_get_appling_list()

if __name__ == '__main__':
    club_id = 'ec29eaa4647e4cf1b38ea06ec83b503b'
    main(club_id)



