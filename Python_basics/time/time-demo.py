#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Sep-18-19 20:55
# @Author  : Kelly Kan HUANG (kan.huang.hkust@gmail.com)

import time
import datetime
import os


def test1():
    current_time = time.time()
    current_time = time.localtime(current_time)
    time_str = time.strftime("%Y%m%d%H%M%S", current_time)
    print(time_str)

    t1 = "2019-11-25 20:28:24 PM"
    t2 = "2019-11-25 20:48:24 PM"
    t1 = time.strptime(t1, "%Y-%m-%d %H:%M:%S %p")
    t2 = time.strptime(t2, "%Y-%m-%d %H:%M:%S %p")
    # print(t1 < t2)
    # print(t1 > t2)
    # print(t2 - t1) # invalid
    print(t1)
    print(t2)
    # t1_str = time.strftime("%Y%m%d%H%M%S", t1)
    # print(t1_str)
    tt1 = time.mktime(t1)
    print(tt1)


def main():
    # print(time.gmtime(0))
    test1()


if __name__ == "__main__":
    main()
