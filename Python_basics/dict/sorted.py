#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Mar-04-20 21:00
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)

import os


def main():
    l = [1, 1, 1, 2, 2, 4, 5, 2, 3, 9]
    d = {}
    for _ in l:
        d[_] = d.get(_, 0) + 1
    print(d)
    # print(d.items()) # list of tuples
    ret = sorted(d.items(), key=lambda d: d[1], reverse=True)
    # sortedClass = sorted(classCount.items(), key=lambda d: d[1], reverse=True)
    print(ret[0][0])


if __name__ == "__main__":
    main()
