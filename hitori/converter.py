#! /usr/bin/python
# -*- coding: utf-8 -*-
import itertools

h = w = 0
board = []
clauses = []
steps = 0

def main():
  inputs()
  cond_row()
  cond_column()
  cond_adj()
  cond_root()
  cond_bfs()
  cond_connected()
  outputs()

# pos -> var ID
def f_color(i, j): return i*w + j + 1
def f_bfs(i, j, k): return h*w*(k+1) + i*w + j + 1

def cond_at_most_one(vars):
  global clauses
  for var1, var2 in itertools.combinations(vars, 2):
    clauses += [[-var1, -var2]]

def cond_row():
  for i in xrange(h):
    for j in xrange(w):
      vars = []
      for k in xrange(w):
        if board[i][j] == board[i][k]:
          vars += [-f_color(i,k)]
      cond_at_most_one(vars)

def cond_column():
  for i in xrange(h):
    for j in xrange(w):
      vars = []
      for k in xrange(h):
        if board[i][j] == board[k][j]:
          vars += [-f_color(k,j)]
      cond_at_most_one(vars)

def adj_pair():
  adjs = []
  for i in xrange(h):
    for j in xrange(w):
      if i > 0: adjs += [((i-1,j),(i,j))]
      if j > 0: adjs += [((i,j-1),(i,j))]
  return adjs

def cond_adj():
  adjs = adj_pair()
  for p, q in adjs:
    cond_at_most_one([f_color(p[0],p[1]), f_color(q[0],q[1])])

def cond_root():
  vars = []
  for i in xrange(h):
    for j in xrange(w):
      vars += [f_bfs(i,j,0)]
  cond_at_most_one(vars)

def cond_bfs():
  global clauses, steps
  steps = h*w
  adjs = adj_pair()

  # bfs[i,j,k] => !color[i,j]
  for k in xrange(steps+1):
    for i in xrange(h):
      for j in xrange(w):
        clauses += [[-f_bfs(i,j,k), -f_color(i,j)]]

  # bfs[i,j,k+1] => or(bfs[i',j',k]) ((i,j) and (i',j') are adjacent)
  for k in xrange(steps):
    for i in xrange(h):
      for j in xrange(w):
        clause = [-f_bfs(i,j,k+1)]
        for ai, aj in [[i,j],[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
          if 0 <= ai < h and 0 <= aj < w:
            clause += [f_bfs(ai,aj,k)]
        clauses += [clause]

def cond_connected():
  global clauses
  for i in xrange(h):
    for j in xrange(w):
      clauses += [[f_bfs(i,j,steps), f_color(i,j)]]

def inputs():
  global h, w, board
  h, w = map(int, raw_input().split())
  for i in xrange(h):
    board += [map(int, raw_input().split())]

def outputs():
  n = 0
  for clause in clauses:
    n = max((n, max(clause), -min(clause)))
  print "p cnf", n, len(clauses)
  for clause in clauses:
    for literal in clause:
      print literal,
    print 0

if __name__ == "__main__":
  main()
