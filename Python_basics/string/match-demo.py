#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Feb-25-20 23:57
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)

import os


def main():
    str1 = "hahah123sas"
    print(str1.find("sb"))  # return -1 if not found
    # print(-1 is True)
    # print(1 is True)
    print(str1.find("123"))


if __name__ == "__main__":
    main()
