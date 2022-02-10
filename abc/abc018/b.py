s = input()
n = int(input())
for _ in range(n):
    l, r = map(int, input().split())
    t = s[l-1:r]
    s = s[:l-1] + t[::-1] + s[r:]
print(s)