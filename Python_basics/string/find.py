#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Mar-09-20 23:48
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)

import os


def main():
    str1 = "demotest"
    ret = str1.find("ot")
    print(ret)
    if ret:
        print("hehe")
    ret = str1.find("de")
    print(ret)
    if ret:
        print("nohehe")
    ret = str1.find("zzz")
    print(ret)
    if ret:
        print("-1hehe")


if __name__ == "__main__":
    main()
