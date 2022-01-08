def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr
n = int(input())
l = factorization(n)
cnt = 0
for i in range(len(l)):
    cnt += l[i][1]
now = 1
ans = 0
while now < cnt:
    ans += 1
    now *= 2
print(ans)