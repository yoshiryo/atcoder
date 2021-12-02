from collections import deque
s = input()
k = int(input())
que = deque()
rem = k
ans, score = 0, 0
for char in s:
    score += 1
    if char == ".":
        que.append(1)
        rem -= 1
    else:
        que.append(0)

    while rem < 0:
        rem += que.popleft()
        score -= 1

    ans = max(ans, score)
print(ans)