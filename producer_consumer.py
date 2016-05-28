#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time


"""利用python的协程实现生产者、消费者模型"""
def consumer(producer_):
    """消费者
    Keyword Arguments:
    producer_ -- 生产者
    """
    p = producer_.next()
    while True:
        if p < 100:
            print '[CONSUMER] Consuming %d' % (p,)
            p = producer_.send(1)
        else:
            print '[CONSUMER] Produce %d >= 100, stopped' % (p,)
            producer_.close()
            break


def producer():
    """生产者
    """
    a, b = 1, 0
    while True:
        a, b = a+b, a
        print '[PRODUCER] Producing %d...' % (a,)
        time.sleep(1)
        res = yield a
        print '[PRODUCER] Consumer returned %d' % (res,)


def main():
    producer_ = producer()
    consumer(producer_)

if __name__ == '__main__':
    main()
