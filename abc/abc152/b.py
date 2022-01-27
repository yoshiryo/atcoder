a, b = map(int, input().split())
ab = str(a)*b
ba = str(b)*a
ans = [ab, ba]
ans.sort()
print(ans[0])