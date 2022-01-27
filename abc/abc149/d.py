n, k = map(int, input().split())
R, S, P =map(int, input().split())
t = input()
ans = 0
l = []
for i in range(n):
    if t[i] == "r":
        now = "p"
        point = P
    elif t[i] == "s":
        now = "r"
        point = R
    else:
        now = "s"
        point = S
    
    if (i - k  >= 0) and l[i - k] == now:
        now = " "
        point = 0
        
    ans += point
    l.append(now)

print(ans)