import itertools 
n = input()
l = []
for i in range(3, len(n)+1):
    l += list(itertools.product("753", repeat=i))

ans = 0
for i in l:
    num = "".join(list(i))
    if int(n) < int(num):
       continue
    else:
        if num.count("7") > 0 and num.count("5") > 0 and num.count("3"):
            ans += 1

print(ans)    