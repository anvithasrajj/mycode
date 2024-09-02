#!/usr/bin/env python3

import sys

for s in sys.stdin:
    s = s.rstrip()
    middle = len(s) // 2
    if len(s) % 2 == 1:
      print(s[middle])
    else:
      print('No middle character')
