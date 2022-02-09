n, a, b = map(int, input().split())
now = 0
for _ in range(n):
    s, d = input().split()
    d = int(d)
    if s == "East":
        if d < a:
            now += a
        elif a <= d <= b:
            now += d
        else:
            now += b
    else:
        if d < a:
            now -= a
        elif a <= d <= b:
            now -= d
        else:
            now -= b
if now < 0:
    print("West", abs(now))
elif now == 0:
    print(0)
else:
    print("East", now)