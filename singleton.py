#!/usr/bin/env python
# -*- coding: utf-8 -*-
DEBUG = True


class Singleton(type):
    def __init__(cls, name, bases, attr):
        """ 初始化class
        Keyword Arguments:
        cls   -- 
        name  -- 
        bases -- 
        attr  -- 
        """
        super(Singleton, cls).__init__(name, bases, attr)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        """ 单列的核心实现
        Keyword Arguments:
        cls      -- 
        *args    -- 
        **kwargs -- 
        """
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, ** kwargs)
        return cls.instance


def singleton(cls):
    """ 单例装饰器
    Keyword Arguments:
    cls -- 
    """
    instances = {}
    def get_instance(*args, **kwargs):
        """ 获取单例
        Keyword Arguments:
        *args    -- 
        **kwargs -- 
        """
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


class Setting(object):
    __metaclass__ = Singleton
    pass


@singleton
class Cache(object):
    pass


def main():
    s1 = Setting()
    s2 = Setting()
    assert id(s1) == id(s2), 'Singleton meta class has error'
    c1 = Cache()
    c2 = Cache()
    assert id(c1) == id(c2), 'singleton decorator has error'
    print 'all asserts passed'


if __name__ == '__main__' or DEBUG:
    main()
