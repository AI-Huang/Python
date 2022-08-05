#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jun-25-21 17:31
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)

import os


class C(object):
    pass


def main():
    c = C()
    c.a1 = 1
    print(vars(c))
    c.__dict__.update({"a1": 2})
    print(vars(c))


if __name__ == "__main__":
    main()
