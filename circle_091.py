#!/usr/bin/env python3

class Point(object):

  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def midpoint(self, other):
    x = (self.x + other.x) / 2
    y = (self.y + other.y) / 2
    return Point(x, y)

  def __str__(self):
    return f'({self.x:.1f}, {self.y:.1f})'

class Circle(object):

  def __init__(self, radius=1, centre=None):
    self.radius = radius
    self.centre = Point(0,0) if centre is None else centre

  def __str__(self):
    out = []
    out.append(f'(Centre: {self.x:.1f}, {self.y:.1f})')
    out.append(f'Radius: {self.radius}')
    return '\n'.join(out)
