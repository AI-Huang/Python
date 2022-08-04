#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Oct-25-18
# @Author  : Kelly Kan HUANG (kan.huang.hkust@gmail.com)

import os
import sys

print(__file__)  # __file__ 就是文件的完整路径
print(sys.argv[0])
print(os.path.dirname(__file__))

print(sys.path)


class Baby(object):

    def __init__(self, birthday, sex, name, weight):
        super(Baby, self).__init__()
        self.birthday = birthday  # 时间字符串
        self.sex = sex  # 性别，Boy or Girl
        self.name = name  # 名字，字符串
        self.weight = weight  # 公斤
        print("Hello! " + self.name + " Daddy/Mommy welcomes you to the World!")

    def newAttr(self):
        self.whatAttr = 123
        print(self.whatAttr)


myBaby = Baby("2018年10月25日14:10:52", "Boy", "Kiki", "3.5")
myBaby.newAttr()
