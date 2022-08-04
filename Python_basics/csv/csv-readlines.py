#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Nov-22-19 17:06
# @Author  : Kan HUANG (kan.huang@connect.ust.hk)

import os
inputs = open("inputs.csv", "r")
for line in inputs.readlines():
    line.strip(',')
    print(line)
