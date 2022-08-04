#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Feb-19-20 23:36
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)
# @Link    : https://stackoverflow.com/questions/529424/traverse-a-list-in-reverse-order-in-python

import os


def main():
    """list倒序遍历，索引也倒序遍历
    """
    a = [1, 2, 3, 4]
    for i, e in reversed(list(enumerate(a))):
        print(i, e)


if __name__ == "__main__":
    main()
