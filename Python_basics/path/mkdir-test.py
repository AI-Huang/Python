#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Mar-11-20 19:55
# @Author  : Kelly Kan HUANG (kan.huang.hkust@gmail.com)

import os


def main():
    # os.mkdir("./1/2/3/4") # 不能递归
    # os.mkdir("./1", exist_ok=True) # 没有 exist_ok 这个参数
    os.makedirs("./tmp/path/to/desired/directory", exist_ok=True)


if __name__ == "__main__":
    main()
