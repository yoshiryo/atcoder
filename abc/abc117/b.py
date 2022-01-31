n = int(input())
l = list(map(int, input().split()))
ma = max(l)
su = sum(l) - ma
if su > ma:
    print("Yes")
else:
    print("No")