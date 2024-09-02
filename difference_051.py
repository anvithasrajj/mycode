#!/usr/bin/env python3

import sys

words = sys.stdin.readlines()

a = words[0].rstrip()
b = words[1].rstrip()

i = 0
sol = []
while i < len(a):
      if a[i] == b[i]:
        sol.append('-')
      else:
        sol.append('*')
      i += 1

print(a)
print(b)
print(''.join(sol))
