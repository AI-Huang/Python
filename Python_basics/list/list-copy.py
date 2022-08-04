#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-28 17:20:00
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)

import os

a = [1, 2, 3, 4, 5]
b = list(a)
# print(id(a))
# print(id(b))

data = [
    [1, 0, 0, 1, 0, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]
data1 = data.copy()  # нет
# data1 = data[:] # нет
# data1 = list(data) # нет
# data1 = list(data) # нет
# data1 = copy.copy(data) # нет
# for all of above five, data1 will change with data, even they differ from ID

data[0][0] = 0
print(id(data))
print(id(data1))
print(data)
print(data1)
# Out:
# 4450009608
# 4450115528
# [[0, 0, 0, 1, 0, 0, 1, 1, 1], [1, 0, 1, 0, 0, 0, 0, 1, 0], [1, 1, 0, 0, 0, 0, 0, 1, 0], [1, 0, 1, 0, 0, 0, 0, 1, 0], [1, 0, 0, 1, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
# [[0, 0, 0, 1, 0, 0, 1, 1, 1], [1, 0, 1, 0, 0, 0, 0, 1, 0], [1, 1, 0, 0, 0, 0, 0, 1, 0], [1, 0, 1, 0, 0, 0, 0, 1, 0], [1, 0, 0, 1, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
# data1 = list(data)
# data2 = data
# print(data1)
# print(id(data))
# print(id(data1))
# print(id(data2)) # id 一样

# data3 = data.copy()
# print(id(data3))

# class DataSpace(object):
#     """docstring for DataSpace"""
#     def __init__(self, data):
#         super(DataSpace, self).__init__()
#         # self.data = data # 跟data2 = data 是一样的
#         self.data = data.copy() # 不一样了。。。

# dataSpace = DataSpace(data)
# print(id(dataSpace.data))
