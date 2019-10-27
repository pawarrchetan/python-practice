#!/usr/bin/env python3.7

import argparse
import sys

# build the parser

parser = argparse.ArgumentParser(description='Read a file and reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int,
                    help='The number of lines to read')
parser.add_argument('--version', '-v', action='version',
                    version='%(prog)s 1.0')

args = parser.parse_args()

try:
    f = open(args.filename)
    limit = args.limit
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(2)
else:
    with open(args.filename) as f:
        lines = f.readlines()
        lines.reverse()

        if args.limit:
            lines = lines[:args.limit]

        for line in lines:
            print(line.strip()[::-1])
finally:
    print("Finally")
