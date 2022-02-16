import itertools
from re import search

S = input()
cs = set(S)
cs.add('.')
ans = 0
for i in range(1, 4):
  for p in itertools.product(cs, repeat = i):
      t = "".join(p)
      if search(t, S):
          ans += 1
print(ans)