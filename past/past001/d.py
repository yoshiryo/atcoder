n = int(input())
a = [int(input()) for _ in range(n)]
if len(set(a)) == n:
    print("Correct")
else:
    a.sort()
    ans = [0]*n
    for i in range(n):
        ans[a[i] - 1] += 1
    for i in range(n):
        if ans[i] == 0:
            ans2 = i+1
        elif ans[i] == 2:
            ans1 = i+1
        else:
            continue
    print(ans1, ans2)