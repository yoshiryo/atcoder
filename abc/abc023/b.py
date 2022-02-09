n = int(input())
s = input()
now = "b"
if now == s:
    print(0)
else:
    for i in range(n):
        if i%3 == 0:
            now = "a" + now + "c"
        elif i%3 == 1:
            now = "c" + now + "a"
        else:
            now = "b" + now + "b"
        if now == s:
            print(i+1)
            exit()
    print(-1)