#include <bits/stdc++.h>
#define fi first
#define se second
#define rep(i,n) for(int i = 0; i < (n); ++i)
#define rrep(i,n) for(int i = 1; i <= (n); ++i)
#define drep(i,n) for(int i = (n)-1; i >= 0; --i)
#define srep(i,s,t) for (int i = s; i < t; ++i)
#define each(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define rng(a) a.begin(),a.end()
#define maxs(x,y) x = max(x,y)
#define mins(x,y) x = min(x,y)
#define pb push_back
#define sz(x) (int)(x).size()
#define pcnt __builtin_popcountll
#define uni(x) x.erase(unique(rng(x)),x.end())
#define snuke srand((unsigned)clock()+(unsigned)time(NULL));
#define df(x) int x = in()
#define dame { puts("-1"); return 0;}
#define show(x) cout<<#x<<" = "<<x<<endl;
#define PQ(T) priority_queue<T,vector<T>,greater<T> >
#define bn(x) ((1<<x)-1)
#define newline puts("")
#define v(T) vector<T>
#define vv(T) vector<vector<T>>
using namespace std;
typedef long long int ll;
typedef unsigned uint;
typedef unsigned long long ull;
typedef pair<int,int> P;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<P> vp;
inline int in() { int x; scanf("%d",&x); return x;}
inline void priv(vi a) { rep(i,sz(a)) printf("%d%c",a[i],i==sz(a)-1?'\n':' ');}
template<typename T>istream& operator>>(istream&i,vector<T>&v)
{rep(j,sz(v))i>>v[j];return i;}
template<typename T>string join(const vector<T>&v)
{stringstream s;rep(i,sz(v))s<<' '<<v[i];return s.str().substr(1);}
template<typename T>ostream& operator<<(ostream&o,const vector<T>&v)
{if(sz(v))o<<join(v);return o;}
template<typename T1,typename T2>istream& operator>>(istream&i,pair<T1,T2>&v)
{return i>>v.fi>>v.se;}
template<typename T1,typename T2>ostream& operator<<(ostream&o,const pair<T1,T2>&v)
{return o<<v.fi<<","<<v.se;}
const int MX = 200005, INF = 1001001001;
const ll LINF = 1e18;
typedef v(string) vs;
#include <random>
random_device _rd;
mt19937 _mt(_rd()+time(0));
inline int rnd(int n) { return _mt()%n;}
inline int rnd(int l, int r) { return _mt()%(r-l+1)+l;}

const int di[] = {-1,-1,0,1,1,0,0}, dj[] = {0,-1,-1,0,1,1,0}; // <\^>\v.

const vi cell_num = {0,5,6,7,8,9,8,7,6,5,0};
const vi cell_begin = {0,1,1,1,1,1,2,3,4,5,0};
const int S = 6, N = 6;

int h, w;
vvi board;
vp pos;
int n;
ll full;
vl to;
int m;
vl sp, nb;

void init() {
  h = w = sz(cell_num);
  board = vvi(h,vi(w,-1));
  rep(i,h) {
    rep(j,cell_num[i]) {
      board[i][cell_begin[i]+j] = n++;
      pos.pb(P(i,cell_begin[i]+j));
    }
  }
  to = vl(n);
  rep(i,n) {
    rep(v,7) {
      int ni = pos[i].fi+di[v], nj = pos[i].se+dj[v];
      if (board[ni][nj] == -1) continue;
      to[i] |= 1ll<<board[ni][nj];
    }
  }
  full = (1ll<<n)-1;
}

void print(ll s) {
  ll nb = 0;
  rep(i,n) if (s>>i&1) nb |= to[i];
  vs t(h-2,string((w-2)*2-1,' '));
  rep(i,n) {
    char c = '.';
    if (nb>>i&1) c = 'x';
    if (s>>i&1) c = 'o';
    t[pos[i].fi-1][pos[i].se*2-2+(5-pos[i].fi)] = c;
  }
  for (string ns : t) cout<<ns<<endl;
  newline;
}


namespace Shapes {
  void dfs(ll s, ll b, ll used) {
    if (pcnt(s) == S) {
      sp.pb(s);
      nb.pb(b);
      return;
    }
    if (!s) {
      rep(i,n) {
        used |= 1ll<<i;
        dfs(s|1ll<<i, b|to[i], used);
      }
      return;
    }
    ll tmp = b^s;
    while (tmp) {
      ll x = tmp&-tmp;
      tmp ^= x;
      if (used&x) continue;
      used |= x;
      dfs(s|x, b|to[pcnt(x-1)], used);
    }
  }
  void init() {
    dfs(0,0,0);
  }
}

ll ans;
void dfs(int si, ll s, ll b) {
  if (pcnt(s) == S*N) {
    ++ans;
    print(s);
    return;
  }
  if (n-pcnt(b)+pcnt(s) < S*N) return;
  for (; si < m; ++si) {
    if (sp[si]&b) continue;
    dfs(si+1, s|sp[si], b|nb[si]);
  }
}

ll input() {
  vl ci(256,-1);
  ci['.'] = 0; ci['x'] = 1;
  ll res = 0;
  rep(i,n) {
    char c;
    scanf(" %c",&c);
    res |= ci[c]<<i;
  }
  return res;
}


int main() {
  init();
  Shapes::init();
  m = sz(sp);
  ll b = input();
  dfs(0,0,b);
  cout<<ans<<endl;
  return 0;
}




















