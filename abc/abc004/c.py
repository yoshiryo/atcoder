n = int(input())
ans = [1, 2, 3, 4, 5, 6]
if n%5 == 0:
    cnt = n//5
    start = cnt%6
    ans = ans[start:] + ans[:start]
else:
    cnt = n//5
    start = cnt%6
    ans = ans[start:] + ans[:start]
    n -= 5*cnt
    for i in range(n):
        ans[i], ans[i+1] = ans[i+1], ans[i]
print("".join(map(str, ans)))
