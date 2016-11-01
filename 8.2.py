import sys
import argparse
parser = argparse.ArgumentParser(
    description='Калькулятор'
)
parser.add_argument(
    'values',
    type=float,
    nargs='+',
    help='исходные числа'
)
parser.add_argument(
    '-a',
    '--action',
    type = str,
    action='store',
)
parser.add_argument(
    '-v',
    '--verbose',
    action='store_true',
)
args = parser.parse_args()

values = args.values
if args.action == '*':
    result = values[0]*values[1]
if args.action == '/':
    result = values[0]/values[1]
if args.action == '+':
    result = values[0]+values[1]
if args.action == '-':
    result = values[0]-values[1]

if args.verbose:
    print(values[0], args.action, values[1], '=', result)
else:
    print(result)