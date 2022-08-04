#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Feb-22-20 00:31
# @Author  : Kelly Kan HUANG (kan.huang.hkust@gmail.com)

import os
import time


def main():
    """ 每隔 period 检查一下目录的可写性"""
    path_start_time = "D:/check-disk-time.txt"

    t = time.localtime()
    t = time.strftime("%Y-%m-%d,%H-%M-%S", t)
    with open(path_start_time, "w") as f:
        f.write(t)

    path = "D:/check-disk.txt"
    while True:
        time.sleep(5)
        t = time.localtime()
        t = time.strftime("%Y-%m-%d,%H-%M-%S", t)
        print("Dist check: %s" % t)
        with open(path, "w") as f:
            f.write(t)


if __name__ == "__main__":
    main()
