#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Feb-16-20 19:02
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)
# @Link    : https://docs.python.org/zh-cn/3/library/json.html
# @Link    : https://www.geeksforgeeks.org/json-dumps-in-python/
# @Link    : https://python3-cookbook.readthedocs.io/zh_CN/latest/c06/p02_read-write_json_data.html

import os
import json


def main():
    # json.dumps
    DATA = {
        "name": "ACME",
        "price": 542.23,
        "shares": 100
    }
    # json.dumps() function converts a Python object into a json string.
    json_str = json.dumps(DATA)
    print(type(json_str))  # <class 'str'>
    print(json_str)

    # json.loads load data into dict from json string
    d = json.loads(json_str)
    print(type(d))  # <class 'dict'>
    price = d["price"]
    print(price)

    # json.load
    # Writing JSON DATA
    with open('Web/json/data_write.json', 'w') as f:
        json.dump(DATA, f, sort_keys=True, indent=2)

    # Reading DATA back
    with open('Web/json/data_write.json', 'r') as f:
        data = json.load(f)
        print(data)


if __name__ == "__main__":
    main()
