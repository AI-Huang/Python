#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jan-07-20 18:17
# @Author  : Kelly Kan HUANG (kan.huang.hkust@gmail.com)
# @Link    : https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/index.html

import os


def fab3(max):
    """改写后的 fab 函数通过返回 List 能满足复用性的要求，但是更有经验的开发者会指出，该函数在运行中占用的内存会随着参数 max 的增大而增大，如果要控制内存占用，最好不要用 List
    """
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L


class Fab(object):
    """关键！Fab 类通过 next() 不断返回数列的下一个数，内存占用始终为常数
    """

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()


def fab(max):
    """yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator
    """
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1


def main():
    # fab(5) 相当于 return 一个 generator
    for n in fab(5):
        print(n)


if __name__ == "__main__":
    main()
