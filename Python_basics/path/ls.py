#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jan-16-20 21:19
# @Author  : Kelly Kan HUANG (kan.huang.hkust@gmail.com)

import os
from os import listdir
from os.path import isfile, join


def main():
    mypath = "C:\\Users\\kellyhwong\\GoogleDrive"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    print(onlyfiles)


if __name__ == "__main__":
    main()
