#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-05-18 21:25 下午
# @Author  : HuangLi
# @Contact : lhuang9703@gmail.com
# @Site    : 
# @File    : add_ideal_answer.py
# @Software: PyCharm Community Edition
"""A script to add ideal answers into predict answers,from
a json format file to another json format file of BioASQ taskB
phase B"""

import os
import json
import argparse
import logging

log = logging.getLogger()
log.setLevel(logging.INFO)
fmt = logging.Formatter('%(asctime)s: [%(message)s]', '%m/%d/%Y %I:%M:%S %p')
console = logging.StreamHandler()
console.setFormatter(fmt)
log.addHandler(console)

parser = argparse.ArgumentParser()
parser.add_argument('--input_file1', type=str, default=None,
                    help='The file you want to add ideal answer')
parser.add_argument('--input_file2', type=str, default=None,
                    help='The file with ideal answer')
parser.add_argument('--out_file', type=str, default='a.json',
                    help='The result file')
parser.add_argument('--data_dir', type=str, default='../../data',
                    help='Path to input_file1 and input_file2')
args = parser.parse_args()


def data_from_json(filename):
    with open(filename, 'r', encoding='utf8') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    file_a = os.path.join(args.data_dir, args.input_file1)
    file_b = os.path.join(args.data_dir, args.input_file2)

    data_a = data_from_json(file_a)
    data_b = data_from_json(file_b)

    for i in range(len(data_a['questions'])):
        for j in range(len(data_b['questions'])):
            if data_b['questions'][j]['id'] == data_a['questions'][i]['id']:
                data_a['questions'][i]['ideal_answer'] = \
                    data_b['questions'][j]['ideal_answer'][0]
                break

    outfile = os.path.join(args.data_dir, args.out_file)
    with open(outfile, 'w') as f:
        json.dump(data_a, f, indent=2)