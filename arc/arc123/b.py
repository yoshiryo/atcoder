n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
ans = 0
while a:
    a_num = a.pop()
    b_num = 0
    while b and a_num >= b_num:
        b_num = b.pop()
    if not b and a_num >= b_num:
        break
    c_num = 0
    while c and b_num >= c_num:
        c_num = c.pop()
    if not c == 0 and b_num >= c_num:
        break
    ans += 1
print(ans)