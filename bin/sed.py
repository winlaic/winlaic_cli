#!/usr/bin/env python3

import argparse
from sys import stdin, stdout, stderr
from pathlib import Path
import re


def main(args: argparse.Namespace):
    script = args.script
    script = ['    ' + item for item in script.split('\n')]
    script.insert(0, 'def parse_line(line):')
    script = '\n'.join(script) + '\n'
    print(script, file=stderr, flush=True)
    exec(script, globals())
    for line in args.input:
        line = line.rstrip()
        line = parse_line(line)
        args.output.write(line + '\n')



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('script')
    parser.add_argument('input')
    parser.add_argument('-i', '--inplace', action='store_true')
    args = parser.parse_args()

    if args.input == '-':
        input_path = None
        args.input = stdin
    else:
        input_path = Path(args.input)
        args.input = input_path.open('r', encoding='utf8')

    if args.inplace:
        assert input_path is not None, 'Inplace operation require input to be path.'
        temp_output_path = input_path.with_name(input_path.name + '.tmp')
        args.output = temp_output_path.open('w', encoding='utf8')

    else:
        args.output = stdout

    main(args)

    args.input.close()
    args.output.close()

    if args.inplace:
        input_path.rename(input_path.with_name(input_path.name + '.bak'))
        temp_output_path.rename(input_path)
