s = list(input().split())
t = list(input().split())
cnt = 0
for i in range(3):
    if s[i] != t[i]:
        cnt += 1
if cnt == 0 or cnt == 3:
    print("Yes")
else:
    print("No")