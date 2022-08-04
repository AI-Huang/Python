#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jun-02-20 00:50
# @Author  : Kan HUANG (kan.huang@connect.ust.hk)

def main():
    l = [1, 1, 1, 2, 2, 4, 5, 2, 3, 9]
    d = {}
    for _ in l:
        d[_] = d.get(_, 0) + 1  # Count repeating values in a list
    print(d)
    ret = d.get(123, 321)
    print(ret)


if __name__ == "__main__":
    main()
