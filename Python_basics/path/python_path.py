#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-16-20 19:17
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)
# @Link    : http://example.org

import os


def main():
    # 本源码文件的绝对路径
    print(os.path.abspath(__file__))
    # 本源码文件所在文件夹的路径
    print(os.path.dirname(os.path.abspath(__file__)))


if __name__ == "__main__":
    main()
