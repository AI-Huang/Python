#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-27-21 14:05
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)


import yaml


def main():
    config_file = "basics/yaml_test.yaml"
    with open(config_file, 'r', encoding="utf-8") as file:
        try:
            config = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)
        print(type(config))
        print(config)


if __name__ == "__main__":
    main()
