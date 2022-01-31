a, b, c = input().split()
ans = max(int(a+b) + int(c), int(a+c) + int(b), int(b+a) + int(c),
          int(b+c) + int(a), int(c+a) + int(b), int(c+b) + int(a))
print(ans)
