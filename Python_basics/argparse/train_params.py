#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-05-20 09:53
# @Author  : Kan HUANG (kan.huang.hkust@gmail.com)
# @Link    : https://docs.python.org/zh-cn/3/library/argparse.html#module-argparse

import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Process some training parameters we care.')
    parser.add_argument('--start_epoch', type=int, dest='start_epoch',
                        action='store', default=0, help='start_epoch, i.e., epoches that have been trained, e.g. 80.')  # 已经完成的训练数
    parser.add_argument('--batch_size', type=int, dest='batch_size',
                        action='store', default=16, help='batch_size, e.g. 16.')  # 16 for Mac, 64, 128 for server
    parser.add_argument('--train_epochs', type=int, dest='train_epochs',
                        action='store', default=150, help='train_epochs, e.g. 150.')  # training 150 epochs to fit enough
    parser.add_argument('--if_fast_run', type=bool, dest='if_fast_run',
                        action='store', default=False, help='If set a fast run, the prog will train for 3 epochs.')
    parser.add_argument('--loss', type=str, dest='loss',
                        action='store', default="bce", help='loss name, e.g., bce or cce.')
    parser.add_argument('--exper_name', type=str, dest='exper_name',
                        action='store', default="ResNet56v2", help='exper_name, user named experiment name, e.g., ResNet56v2_BCE.')
    parser.add_argument('--config_file', type=str, dest='config_file',
                        action='store', default="./config/config.json", help='config_file path, e.g., ./config/config.json.')
    parser.add_argument('--ckpt', type=str, dest='ckpt',
                        action='store', default="", help='ckpt, model ckpt file.')
    parser.add_argument('--positive_class', type=str, dest='positive_class',
                        action='store', default="bad_1", help='ckpt, model ckpt file, e.g. bad_1 or good_0.')
    parser.add_argument('--alpha', type=float, dest='alpha',
                        action='store', default=0.99, help='alpha for focal loss if this loss is used.')
    parser.add_argument('--n', type=int, dest='n',
                        action='store', default=6, help='n, order of ResNet, 2 or 6.')
    parser.add_argument('--version', type=int, dest='version',
                        action='store', default=2, help='version, version of ResNet, 1 or 2.')
    args = parser.parse_args()
    print(type(args))
    print(args)


if __name__ == "__main__":
    main()
