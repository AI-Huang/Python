#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Feb-21-20 00:15
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)

import os

"""
可以用max(dict,key=dict.get)方法获得字典dict中value的最大值所对应的键的方法, max(dict, key)方法首先遍历迭代器, 并将返回值作为参数传递给key对应的函数, 然后将函数的执行结果传给key, 并以此时key值为标准进行大小判断, 返回最大值。
"""


def main():
    d = {0: 1, 1: 2, 2: 3, 3: 4}
    ret = max(d, key=d.get)
    print(ret)
    print(list(d.keys()))
    print(3 in d)


if __name__ == "__main__":
    main()
