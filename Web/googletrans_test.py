#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Feb-27-19 22:27
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)

from googletrans import Translator
translator = Translator()
detected = translator.detect('我愛你')
print(detected.lang)
print(detected.lang.find("zh") is not -1)

print(translator.translate('안녕하세요.', dest='zh-cn').text)
