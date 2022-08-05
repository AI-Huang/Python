#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : Jun-14-19 17:09
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)

import string

l1 = [1, 2, 3]
l2 = [4, 5, 6]
z = zip(l1, l2)
print([_ for _ in z])
print(string.ascii_lowercase)
