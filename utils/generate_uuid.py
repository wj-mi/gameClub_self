# -*-coding:utf-8 -*-

from uuid import uuid4


def compress_uuid():
    """生成３２位的uuid"""
    return uuid4().hex
