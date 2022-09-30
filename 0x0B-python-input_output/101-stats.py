#!/usr/bin/python3
"""
    Log parser
"""

import sys

s_code = {'200': 0, '301': 0, '400': 0, '401': 0,
          '403': 0, '404': 0, '405': 0, '500': 0}
f_size = 0
tens = 0
try:
    for line in sys.stdin:
        if len(line.split()) >= 2:
            f_size += int(line.split()[-1])
            if line.split()[-2] in s_code:
                s_code[line.split()[-2]] += 1
            tens += 1
        if tens % 10 == 0:
            print("File size: {}".format(f_size))
            for key in s_code:
                if s_code[key]:
                    print("{}: {}".format(key, s_code[key]))
    print("File size: {}".format(f_size))
    for key in s_code:
        if s_code[key]:
            print("{}: {}".format(key, s_code[key]))
except KeyboardInterrupt as e:
    print("File size: {}".format(f_size))
    for key in s_code:
        if s_code[key]:
            print("{}: {}".format(key, s_code[key]))
