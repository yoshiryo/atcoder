from collections import Counter
n = int(input())
a = list(map(int, input().split()))
q = int(input())
su = sum(a)
C = Counter(a)
ans = []
for _ in range(q):
    b, c = map(int, input().split())
    cnt1 = C[b]
    su -= b*cnt1
    su += c*cnt1
    C[c] += cnt1
    C[b] = 0
    ans.append(su)
for a in ans:
    print(a)