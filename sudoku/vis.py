raw_input()
a = map(int,raw_input().split())

d = []
for i in xrange(9):
  d += [[0]*9]

for v in a:
    if v <= 0: continue
    v -= 1
    x = v//81
    y = v//9%9
    d[x][y] = v%9+1

for i in xrange(9):
  s = ""
  for j in xrange(9):
    s += str(d[i][j])
  #print s[::-1]
  print s