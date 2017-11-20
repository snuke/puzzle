#! /usr/bin/python

def f(i, j, k): return i*81+j*9+k+1
def gf(i, j, k):
  x = i//3*3+j//3
  y = i%3*3+j%3
  return f(x,y,k)

def add(a):
  res = [[]]
  for i in xrange(9):
    res[0].append(a[i])
  for i in xrange(9):
    for j in xrange(i):
      res.append([-a[i],-a[j]])
  return res

ans = []
for i in xrange(9):
  for j in xrange(9):
    a = []
    b = []
    c = []
    d = []
    for k in xrange(9):
      a.append(f(i,j,k))
      b.append(f(j,k,i))
      c.append(f(k,j,i))
      d.append(gf(j,k,i))
    ans += add(a)
    ans += add(b)
    ans += add(c)
    ans += add(d)

s = raw_input()
t = []
for i in xrange(9):
  for j in xrange(9):
    x = int(s[i*9+j])
    if x == 0: continue
    ans += [[f(i,j,x-1)]]


print "p cnf",9**3,len(ans)
for a in ans:
  for b in a:
    print b,
  print 0