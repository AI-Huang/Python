#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : Apr-28-19 16:20
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)

import os

data = [
    [1, 0, 0, 1, 0, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

data1 = [
    [1, 0, 0, 1, 0, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

print(data is data1)  # False
print(data == data1)  # True

score = [1, 2, 3]
del score[-1]
print(score)
print(tuple(score))
