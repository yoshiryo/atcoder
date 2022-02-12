n = int(input())
R = list(map(int, input().split()))
C = list(map(int, input().split()))
q = int(input())
ans = ""
for _ in range(q):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    cnt = R[r] + C[c]
    if cnt >= n+1:
        ans += "#"
    else:
        ans += "."
print(ans)