n, k, q = map(int, input().split())
ans = [0]*n
for _ in range(q):
    a = int(input())
    ans[a-1] += 1
for a in ans:
    if (q - a) < k:
        print("Yes")
    else:
        print("No")
