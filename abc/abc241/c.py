n = int(input())
s = [input() for _ in range(n)]
dxs = [0, 1, 1, 1]
dys = [1, 1, 0, -1]
for i in range(n):
    for j in range(n):
        for d in range(4):
            dx = dxs[d]
            dy = dys[d]
            cnt = 0
            for k in range(6):
                nx = i + dx * k
                ny = j + dy * k
                if not (0 <= nx < n and 0 <= ny < n):
                    cnt = 100
                    break
                if s[nx][ny] == ".":
                    cnt += 1
            if cnt <= 2:
                print("Yes")
                exit()
print("No")
