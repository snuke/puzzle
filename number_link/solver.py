from graphillion import GraphSet

def readInts():
  return list(map(int, filter(lambda s: s != '', input().split())))

h,w = readInts()
a = [readInts() for i in range(h)]

cellId = [[i*w+j for j in range(w)] for i in range(h)]
cells = []
for i in range(h):
  for j in range(w):
    cells.append((i,j))

edges = []
for i in range(h):
  for j in range(w):
    for di,dj in [(1,0),(0,1)]: # (-1,0),(0,-1)
      ni, nj = i+di, j+dj
      if 0 <= ni < h and 0 <= nj < w:
        v, u = cellId[i][j], cellId[ni][nj]
        edges.append((v,u))

degs = {}
clue = {}
for i in range(h):
  for j in range(w):
    if a[i][j] != 0:
      degs[cellId[i][j]] = 1
      if a[i][j] in clue:
        clue[a[i][j]].append(cellId[i][j])
      else:
        clue[a[i][j]] = [cellId[i][j]]
    else:
      degs[cellId[i][j]] = 2

grps = []
for _,p in clue.items():
  grps.append(p)

GraphSet.set_universe(edges)
sols = GraphSet.graphs(vertex_groups=grps,
                         degree_constraints=degs,
                         no_loop=True)

print('# of Solutions: %d' % sols.len())

def choose(gs):
  for g in gs.rand_iter():
    return g
sol = choose(sols)

def output(sol):
  sh,sw = h*2+1,w*4+1
  s = [[' ' for j in range(sw)] for i in range(sh)]

  for i in range(sh):
    s[i][0] = s[i][-1] = '|'
  for j in range(sw):
    s[0][j] = s[-1][j] = '-'
  for i in range(h+1):
    for j in range(w+1):
      s[i*2][j*4] = '+'
  for e in sol:
    si,sj = cells[e[0]]
    ti,tj = cells[e[1]]
    if si == ti:
      for j in range(sj*4+2,tj*4+3):
        s[si*2+1][j] = '#'
    else:
      for i in range(si*2+1,ti*2+2):
        s[i][sj*4+2] = '#'
  for i in range(h):
    for j in range(w):
      if a[i][j] == 0:
        continue
      ns = '%03d' % a[i][j]
      for k in range(3):
        s[i*2+1][j*4+1+k] = ns[k]

  for i in range(sh):
    print(''.join(s[i]))

output(sol)




