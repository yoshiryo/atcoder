N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
if 0 in T and 0 not in S or 1 in T and 1 not in S:
    print(-1)
    exit()
 
first = None
for i in range(len(S)):
    if not S[i] == S[0]:
        first = i
        break
if first is None:
    print(len(T))
    exit()

last = None
for i in range(len(S))[::-1]:
    if not S[i] == S[0]:
        last = i
        break
d = min(first, len(S) - last)

ans = 0
now = S[0]
judge = True
for i in range(M):
    if now == T[i]:
        ans += 1
    else:
        if judge:
            ans += d
            judge = False
        else:
            ans += 1
        ans += 1
        now = T[i]
print(ans)