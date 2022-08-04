#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Oct-23-20 16:51
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)

import os


def join_test1():
    # @RefLink : https://github.com/tensorflow/models/blob/r1.13.0/tutorials/rnn/ptb/reader_test.py#L32
    string_data = "\n".join(
        [" hello there i am",
         " rain as day",
         " want some cheesy puffs ?"])
    print(string_data)


def main():
    join_test1()


if __name__ == "__main__":
    main()
