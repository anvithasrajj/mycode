#!/usr/bin/env python3

if __name__ == '__main__':
  a = ['cat', 'explain', 'mouse', 'lizard', 'horse', 'mongoose']

i = 0
while i < len(a) and 6 > len(a[i]):
  i += 1

if i < len(a):
  print(a[i])
