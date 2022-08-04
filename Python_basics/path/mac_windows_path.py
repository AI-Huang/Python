#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-08 10:15:29
# @Author  : Kelly Kan HUANG (kan.huang.hkust@gmail.com)

import os

model_dir = os.path.abspath("./model")
rel = "./model"
os.makedirs(rel, exist_ok=True)
with open(os.path.join(model_dir, "test.txt"), "w") as f:
    f.write("mac path test")
print(model_dir)
