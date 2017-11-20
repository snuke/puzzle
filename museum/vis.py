def seto(s,i):
  t = list(s)
  t[i] = 'o'
  return "".join(t)

n,m = map(int,raw_input().split())
s = []
for i in xrange(n):
  s += [raw_input()]
raw_input()
a = map(int,raw_input().split())
for v in a:
  if v <= 0: continue
  x = (v-1)//(m+2)-1
  y = (v-1)%(m+2)-1
  s[x] = seto(s[x],y)

for i in xrange(n): print s[i]