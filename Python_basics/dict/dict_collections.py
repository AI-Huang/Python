#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Aug-04-22 14:28
# @Author  : Kan HUANG (kan.huang@connect.ust.hk)


class Computer:

    def __init__(self, maxprice=900):
        self.__maxprice = maxprice

    def sell(self):
        print('Selling Price: {}'.format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price


def main():
    # Use dictionary as the container for a collection
    # Initialize the object first, then initialize whole dictionary
    computers = {
        "computer1": Computer(maxprice=900),
        "computer2": Computer(maxprice=1800),
    }

    for k, computer in computers.items():
        computer.sell()


if __name__ == "__main__":
    main()
