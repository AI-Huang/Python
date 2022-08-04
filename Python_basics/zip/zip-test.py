#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Apr-19-20 21:21
# @Author  : Kelly Kan HUANG (kan.huang.hkust@gmail.com)

import os


def main():
    l1 = [1, 2, 3]
    l2 = [4, 5, 6, 7]
    z = zip(l1, l2)
    d = dict(z)
    print(z)
    print(d)
    for e in z:
        print(e)


if __name__ == "__main__":
    main()
