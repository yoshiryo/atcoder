a, b = input().split()
a = list(a)
b = list(b)
a_cnt = int(a[0]) + int(a[1]) + int(a[2])
b_cnt = int(b[0]) + int(b[1]) + int(b[2])

if a_cnt > b_cnt:
    print(a_cnt)
elif a_cnt < b_cnt:
    print(b_cnt)
else:
    print(a_cnt)
