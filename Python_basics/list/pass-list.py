#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Feb-19-20 22:29
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)

import os


def do_something_to_a_list(l: list):
    l.remove(l[-1])


def test_list_pass_arg():
    """test function that shows list type is passed by reference
    """
    l = [1, 2, 3, 4]
    do_something_to_a_list(l)
    print(l)


def main():
    test_list_pass_arg()


if __name__ == "__main__":
    main()
