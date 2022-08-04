#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jan-02-19
# @Author  : Kelly Kan HUANG (kan.huang.hkust@gmail.com)

import os
from datetime import datetime


def main():
    now = datetime.now()
    print(type(now.hour))
    return
    # f = open("dateData.csv", "w+")
    for i in range(20):
        print(now.strftime('%Y-%m-%d %H:%M:%S %p'))
        # f.write(dt.strftime('%Y-%m-%d %H:%M:%S %p') + "," + str(i) + '\n')
    # f.close()


if __name__ == "__main__":
    main()
