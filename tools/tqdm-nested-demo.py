#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Mar-04-21 17:17
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)
# @RefLink : https://stackoverflow.com/questions/23113494/double-progress-bar-in-python


from tqdm import tqdm
# from tqdm.auto import tqdm  # notebook compatible
import time
for i1 in tqdm(range(5)):
    for i2 in tqdm(range(300), leave=True):  # leave=False
        # do something, e.g. sleep
        time.sleep(0.01)
