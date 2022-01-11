class UnionFind():
  def __init__(self, n):
      self.n = n
      self.parents = [-1] * n

  def find(self, x):
    if self.parents[x] < 0:
      return x
    else:
      self.parents[x] = self.find(self.parents[x])
      return self.parents[x]

  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)

    if x == y:
      return

    if self.parents[x] > self.parents[y]:
      x, y = y, x

    self.parents[x] += self.parents[y]
    self.parents[y] = x


  def same(self, x, y):
    return self.find(x) == self.find(y)

def flatten(h, w):
  return h+(H+1)*w
H, W = map(int, input().split())
mas = [[False]*W for _ in range(H)]
n = (H+1)*W
uf = UnionFind(n)
Q = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        r, c = q[1:]
        r -= 1
        c -= 1
        x = flatten(r, c)
        mas[r][c] = True
        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]
            y = flatten(nr, nc)
            if 0 <= nr < H and 0 <= nc < W:
                if mas[nr][nc]:
                    uf.union(x, y)
    else:
        ra, ca, rb, cb = q[1:]
        ra -= 1
        ca -= 1
        rb -= 1
        cb -= 1
        x = flatten(ra, ca)
        y = flatten(rb, cb)
        if mas[ra][ca] and mas[rb][cb] and uf.same(x, y):
            print("Yes")
        else:
            print("No")

