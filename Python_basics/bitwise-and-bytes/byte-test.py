#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Aug-09-20 18:50
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)

import os
import struct


def byte2int(b):
    b = struct.unpack('>B', b)
    b = b[0]
    return b


def main():
    str1 = b"AA"  # this is binary string
    print(str1)

    a = 0xAB
    print(a)  # print 171


if __name__ == "__main__":
    main()
