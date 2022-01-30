n = int(input())
AB = []
for _ in range(n):
    a, b = map(int, input().split())
    l = [a, b]
    AB.append(l)

AB = sorted(AB, key=lambda x:(x[1], x[0]))
cnt = 0
for i in range(n):
    cnt += AB[i][0]
    if cnt > AB[i][1]:
        print("No")
        exit()
print("Yes")