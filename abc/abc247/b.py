n = int(input())
st = [list(input().split()) for _ in range(n)]
for i in range(n):
    judge = False
    s = st[i][0]
    t = st[i][1]
    ok_s = True
    ok_t = True
    for j in range(n):
        if i != j:
            if s == st[j][0] or s == st[j][1]:
                ok_s = False
            if t == st[j][0] or t == st[j][1]:
                ok_t = False
    if ok_s == True or ok_t == True:
        judge = True
    if not judge:
        print("No")
        exit()
print("Yes")