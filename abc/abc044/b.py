w = list(input())
alp = "abcdefghijklmnopqrstuvwxyz"
cnt = [0]*26
for s in w:
    index = alp.find(s)
    cnt[index] += 1
for i in cnt:
    if i%2 != 0:
        print("No")
        exit()
print("Yes")