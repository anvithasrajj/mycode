#!/usr/bin/env python3

s = input()
s2 = input()
s3 = input()

if len(s) > len(s2) or len(s3):
  print(s)
elif len(s2) > len(s3) or len(s):
  print(s2)
elif len(s3) > len(s2) or len(s):
  print(s3)
