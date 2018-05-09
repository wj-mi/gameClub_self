# -*-coding:utf-8 -*-

import unittest
from gameClub.club import GameClub
from gameClub.config import db

class TestDemo(unittest.TestCase):

    def test_create_club(self):
        club = GameClub(name='--test club231', chair_uuid=18263, game_types='1')
        print club.name

    # def test_get_reward(self):
    #     db.cur.callproc('get_reward', 3)
    #     result = db.cur.fetchall()
    #     print result


if __name__ == '__main__':
    unittest.main()
