from collections import deque
n = int(input())
s = input()
s = s[::-1]
d = deque([n])
now = s[0]
for i in range(1, n):
    if now == s[i]:
        if s[i] == "L":
            d.append(n-i)
        else:
            d.appendleft(n-i)
    else:
        if s[i] == "L":
            now = "L"
            d.appendleft(n-i)
        else:
            now = "R"
            d.append(n-i)
if s[-1] == "L":
    d.append(0)
else:
    d.appendleft(0)
d = list(d)    
print(*d)
    
