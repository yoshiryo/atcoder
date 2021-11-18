n = int(input())
S = list(map(int, input().split()))
men_list = []
for a in range(1, 400):
    for b in range(1, 400):
        men = 4*a*b + 3*a + 3*b
        if men <= 1000:
            men_list.append(men)
cnt = 0
for s in S:
    if s not in men_list:
        cnt += 1
print(cnt)
