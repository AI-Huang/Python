#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jan-01-19
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)

import struct


def byteToInt(b):
    b = struct.unpack('>B', b)
    b = b[0]
    return b


b = b'\xaa'
# bH = int(b) << 4
# bL = int(b) & b'\x0F'
bInt = byteToInt(b)
testResult = struct.unpack('>B', b)
testResult = testResult[0]

bH = bInt & 0xF0
bL = bInt & 0x0F
print(b)
print(testResult)
print(bH)
print(bL)
