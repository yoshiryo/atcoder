n, w = map(int, input().split())
l = [0]*(10**6)
for _ in range(n):
    s, t, p = map(int, input().split())
    l[s] += p
    l[t] -= p
now = 0
for i in range(len(l)):
    if now + l[i] > w:
        print("No")
        exit()
    now += l[i]
print("Yes")
