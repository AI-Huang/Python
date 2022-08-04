#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Apr-19-20 21:26
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)


def main():
    my_list = [1, 1, 1, 2, 3, 4, 1, 2]
    indices = [i for i, x in enumerate(my_list) if x == 1]
    print(indices)


if __name__ == "__main__":
    main()
