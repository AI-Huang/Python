#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : May-30-19 19:31
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)

import requests

r = requests.get('http://www.weather.com.cn/data/sk/101020100.html')
r.encoding = 'utf-8'
print(r.status_code)
print("")
print(r.content)
print("")
print(r.text)

city = r.json()
# .decode('utf-8')
print(city)
