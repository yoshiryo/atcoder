a, b, c, d = map(int, input().split())
now = "takahashi"
while True:
    if now == "takahashi":
        c -= b
        now = "aoki"
    else:
        a -= d
        now = "takahashi"
    if a <= 0 or c <= 0:
        break
if now == "takahashi":
    print("No")
else:
    print("Yes")