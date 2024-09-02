#!/usr/bin/env python3

class MP3Track(object):

  def __init__(self, title, duration):
    self.title = title
    self.duration = duration

  def __str__(self):
    out = []
    out.append(f'Title: {self.title}')
    out.append(f'Duration: {self.duration}')
    return '\n'. join(out)

class MP3Collection(object):

  def __init__(self):
    self.d = {}

  def add(self, MP3Track):
    self.d[MP3Track.title] = MP3Track

  def remove(self, tite):
    if title in self.d:
      del self.d[title]



  
