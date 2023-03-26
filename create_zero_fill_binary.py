#!/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--byte_size", type=int)
parser.add_argument("-f", "--file_name", type=str)

args = parser.parse_args()
if args.byte_size is None:
    print("require byte size")
    exit(1)
    
if args.file_name is None:
    print("require file name")
    exit(1)
    
byte_size = args.byte_size
file_name = args.file_name

buf = []
for i in range(byte_size):
    buf.append(0)

byte_array = bytearray(buf)


with open(file_name, "wb") as f:
    f.write(byte_array)

