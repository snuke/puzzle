#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys

h = w = 0
board = []

def main():
  if len(sys.argv) < 3:
    print "usage: python visualizer.py in.txt out.txt"
    exit(0)
  inputs()
  outputs()

def inputs():
  global h, w, board, mode
  h, w = map(int, open(sys.argv[1]).readline().split())
  f = open(sys.argv[2])
  if f.readline() != "SAT\n":
    print "There is no solution."
    exit(0)
  results = map(int, f.readline().split())
  for i in xrange(h):
    board += [['.']*w]
    for j in xrange(w):
      if results[i*w+j] > 0: board[i][j] = '#'
  if len(sys.argv) >= 4:
    if sys.argv[3] == "digit":
      f = open(sys.argv[1])
      f.readline()
      for i in xrange(h):
        row = f.readline().split()
        for j in xrange(w):
          if board[i][j] == '.': board[i][j] = row[j]
          else: board[i][j] = '.'

def outputs():
  for i in xrange(h):
    print "".join(board[i])

if __name__ == "__main__":
  main()
