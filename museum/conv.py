di = [-1,0,1,0]
dj = [0,-1,0,1]
n,m = map(int,raw_input().split())
ans = []
s = []
for i in xrange(n):
  s += [raw_input()]

def f(x,y): return (x+1)*(m+2)+(y+1)+1
# def check(x,y): return 0 <= x < n and 0 <= y < m

def cover(x,y):
  res = [f(x,y)]
  i = x-1; j = y
  while i >= 0:
    if s[i][j] != '.': break
    res += [f(i,j)]
    i -= 1
  i = x; j = y-1
  while j >= 0:
    if s[i][j] != '.': break
    res += [f(i,j)]
    j -= 1
  i = x+1; j = y
  while i < n:
    if s[i][j] != '.': break
    res += [f(i,j)]
    i += 1
  i = x; j = y+1
  while j < m:
    if s[i][j] != '.': break
    res += [f(i,j)]
    j += 1
  return res

def db(a):
  res = []
  for i in xrange(len(a)):
    for j in xrange(i):
      res += [[-a[i],-a[j]]]
  return res

def more2(a):
  res = []
  for i in xrange(len(a)):
    b = []
    for j in xrange(len(a)):
      if i != j: b += [a[j]]
    res += [b]
  return res


for i in xrange(n+2):
  for j in xrange(m+2):
    if i == 0 or i == n+1 or j == 0 or j == m+1:
      ans += [[-f(i-1,j-1)]]
for i in xrange(n):
  for j in xrange(m):
    if s[i][j] != '.':
      ans += [[-f(i,j)]]
    else:
      ans += [cover(i,j)]

for i in xrange(n):
  j = 0
  while j < m:
    if s[i][j] != '.':
      j += 1
      continue
    a = []
    while j < m:
      if s[i][j] != '.': break
      a += [f(i,j)]
      j += 1
    ans += db(a)
for j in xrange(m):
  i = 0
  while i < n:
    if s[i][j] != '.':
      i += 1
      continue
    a = []
    while i < n:
      if s[i][j] != '.': break
      a += [f(i,j)]
      i += 1
    ans += db(a)

for i in xrange(n):
  for j in xrange(m):
    a = []
    b = []
    for v in xrange(4):
      a += [f(i+di[v],j+dj[v])]
      b += [-f(i+di[v],j+dj[v])]
    if s[i][j] == '4':
      for k in xrange(4): ans += [[a[k]]]
    if s[i][j] == '0':
      for k in xrange(4): ans += [[b[k]]]
    if s[i][j] == '1':
      ans += [a]
      ans += db(a)
    if s[i][j] == '3':
      ans += [b]
      ans += db(b)
    if s[i][j] == '2':
      ans += more2(a)
      ans += more2(b)

print "p cnf",(n+2)*(m+2),len(ans)
for a in ans:
  for b in a:
    print b,
  print 0


