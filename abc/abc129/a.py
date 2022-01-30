p, q, r = map(int, input().split())
all = [p+q, q+r, r+p]
print(min(all))