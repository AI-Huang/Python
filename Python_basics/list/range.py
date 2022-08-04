#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Mar-08-20 14:13
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)

import os
import random


def main():
    n = 10
    order = list(range(n))
    random.shuffle(order)
    print(order)


if __name__ == "__main__":
    main()
