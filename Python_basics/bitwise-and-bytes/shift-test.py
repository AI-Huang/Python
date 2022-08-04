#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-02-19
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)
# @RefLink : https://zhuanlan.zhihu.com/p/74645509
# @RefLink : https://stackoverflow.com/questions/37053379/times-two-faster-than-bit-shift-for-python-3-x-integers

import time


def main():
    start = time.process_time()
    N = 10000000  # 一千万次
    for _ in range(N):
        i = 1
        # i *= 32  # 0.588701s
        i <<= 5  # 0.890978s
        print(i)
        input()
    elapsed = (time.process_time() - start)
    print("Time used:", elapsed)


if __name__ == "__main__":
    main()
