l, r, d = map(int, input().split())
cnt = r//d - (l-1)//d
print(cnt)