#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-05-20 09:45
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)
# @Link    : https://docs.python.org/zh-cn/3/library/argparse.html#module-argparse

import argparse


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')

    """
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    # dest 可以是 python 函数
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
    """

    parser.add_argument(
        '--batch-size',  # 自动变成下划线
        type=int,
        default=100,
        help='input batch size for training (default: 100)')

    args = parser.parse_args()
    print(args.batch_size)
    # print(args.accumulate(args.integers))


if __name__ == "__main__":
    main()
