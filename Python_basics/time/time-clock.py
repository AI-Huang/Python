#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-23 13:52:57
# @Author  : Kelly Kan HUANG (kan.huang.hkust@gmail.com)
# @Link    : http://www.runoob.com/numpy/numpy-array-from-existing-data.html

import os
import numpy as np
import time
"""
numpy.asarray(a, dtype = None, order = None)
a   任意形式的输入参数，可以是，列表, 列表的元组, 元组, 元组的元组, 元组的列表，多维数组
"""
"""
numpy.zeros(shape, dtype = float, order = 'C')
"""


def main():
    _ = np.zeros([2, 3, 4], dtype=float, order='C')
    print(_)
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    t = (4, 2)
    l_np = np.asarray(l)
    start = time.perf_counter()
    for _ in range(10000000):  # 1.9972499999999997 s
        l_ = l.copy()
    elapsed = (time.perf_counter() - start)
    print(elapsed, "s")


if __name__ == "__main__":
    main()
