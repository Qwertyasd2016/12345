import os
import argparse
import sys
parser = argparse.ArgumentParser(
    description='tree'
)
parser.add_argument(
    'path',
    type=str,
    #nargs='-',
    help='path'
)
parser.add_argument(
    '-fo',
    '--folders',
    action='store_true',
)
parser.add_argument(
    '-i',
    '--include SOME_TEXT',
    action='store_true',
)
parser.add_argument(
    '-e',
    '--exclude SOME_TEXT',
    action='store_true',
)
parser.add_argument(
    '-a',
    '--all',
    action='store_true',
)
parser.add_argument(
    '-f',
    '--full-name',
    action='store_true',
)
dir = os.listdir(sys.argv[1])
print(sys.argv[1])
for i in range(len(dir)):
    if os.path.isfile(sys.argv[1] + '/' + dir[i]):
        print('  ',dir[i])
    if os.path.isdir(sys.argv[1] + '/' + dir[i]):
        print('  ',dir[i])
        dirdir = os.listdir(sys.argv[1] + '/' + dir[i])
        for j in range(len(dirdir)):
            print('     ', dirdir[j])