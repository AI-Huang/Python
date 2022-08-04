#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Oct-10-20 19:24
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)

import os


def list_comp_test1():
    """list comprehension test function 1
    """
    N = 3
    list1 = [0] * N
    print(f"list1: {list1}")
    # modify the first element
    list1[0] = 1
    print(f"list1: {list1}")


def list_comp_test2():
    """list comprehension test function 2
    """
    N = 3
    list2 = [[0, 1]] * N  # will copy by reference
    print(f"list2: {list2}")
    # modify the first element
    list2[0][0] = 1
    print(f"list2: {list2}")


def list_comp_test3():
    """list comprehension test function 2
    """
    N = 3
    list3 = [[0, 1] for _ in range(N)]  # will copy by truly copy
    print(f"list3: {list3}")
    # modify the first element
    list3[0][0] = 1
    print(f"list3: {list3}")


def main():
    print("Now testing list multiply operation...")
    list_comp_test2()
    print("Now testing list comprehension...")
    list_comp_test3()


if __name__ == "__main__":
    main()
