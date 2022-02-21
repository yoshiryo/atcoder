n = int(input())
ans = [['.' for _ in range(n)] for _ in range(n)]

for i in range(n-1):
  if i%2 == 0:
    for j in range(i+1):
      ans[j][i+1] = '#'
  else:
    for j in range(i+1):
      ans[i+1][j] = '#'
for i in range(n):
  print(''.join(ans[i]))
