#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Feb-21-20 21:45
# @Author  : Kelly Kan HUANG (kan.huang.hkust@gmail.com)

import os


def main():
    l = os.listdir(".")
    print(l)
    print(sorted(l))


if __name__ == "__main__":
    main()
