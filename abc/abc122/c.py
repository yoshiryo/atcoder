n, q = map(int, input().split())
s = input()
cnt = [0]*n
now = 0
for i in range(n-1):
    if s[i] == "A" and s[i+1] == "C":
        now += 1
    cnt[i+1] += now 
for _ in range(q):
    l, r = map(int, input().split())
    print(cnt[r-1] - cnt[l-1])