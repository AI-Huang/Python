#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Mar-10-20 13:32
# @Author  : Your Name (you@example.org)
# @Link    : https://blog.csdn.net/B_H_L/article/details/9406675
# @Link    : https://zhuanlan.zhihu.com/p/28676503

import os
import zipfile

DIR = "D:\\mac_Code_workspaces"  # 要整个打包的目录
ZIP_FILENAME = os.path.basename(DIR) + ".zip"
ZIP_FILEPATH = os.path.abspath(os.path.join(DIR, os.pardir))
ZIP_FILEPATH = os.path.join(ZIP_FILEPATH, ZIP_FILENAME)


def main():
    # 把整个文件夹内的文件打包
    f = zipfile.ZipFile(ZIP_FILEPATH, 'w', zipfile.ZIP_DEFLATED)
    startdir = DIR
    for dirpath, dirnames, filenames in os.walk(startdir):
        for filename in filenames:
            src_file = os.path.join(dirpath, filename)
            f.write(src_file, src_file)
    f.close()


if __name__ == "__main__":
    main()
