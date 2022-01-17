n = int(input())
s = list(input())
q = int(input())
judge = True
for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        if judge:
            s[a-1], s[b-1] = s[b-1], s[a-1]
        else:
            if a > n and b > n:
                s[a-1-n], s[b-1-n] = s[b-1-n], s[a-1-n]
            elif a > n and b <= n:
                s[a-1-n], s[b-1+n] = s[b-1+n], s[a-1-n]
            elif a <= n and b > n:
                s[a-1+n], s[b-1-n] = s[b-1-n], s[a-1+n]
            else:
                s[a-1+n], s[b-1+n] = s[b-1+n], s[a-1+n]
    else:
        if judge:
            judge = False
        else:
            judge = True
if judge:
    print(''.join(s))
else:
    print(''.join(s[n:]) + ''.join(s[:n]))