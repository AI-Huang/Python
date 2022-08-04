#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Nov-22-19 17:06
# @Author  : Kan HUANG (kan.huang@connect.ust.hk)

import os
import csv


def main():
    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']

    rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
            ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
            ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
            ]

    with open('stocks.csv', 'a') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)


if __name__ == "__main__":
    main()
