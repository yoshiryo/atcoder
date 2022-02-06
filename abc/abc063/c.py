n = int(input())
s = [int(input()) for _ in range(n)]
score = sum(s)
if score%10 != 0:
    print(score)
else:
    s.sort()
    for i in range(n):
        if s[i]%10 != 0:
            print(score - s[i])
            exit()
    print(0)