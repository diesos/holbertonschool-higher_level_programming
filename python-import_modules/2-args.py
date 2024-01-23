#!/usr/bin/env python3
import sys
argv = len(sys.argv) - 1
i = 1
if (argv < 1):
    print("0 arguments.")
else:
    print(f'{argv} arguments:')
    while (i <= argv):
        print(f'{i}: {sys.argv[i]}')
        i += 1