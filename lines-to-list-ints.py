#!/usr/bin/env python3

ls = []

n = input()
while n != 'end':
  ls += n
  n = input()

z = []
i = 0
while i < len(ls):
  ls[i] = int(ls[i])
  z.append(ls[i])
  i += 1

print(z)
