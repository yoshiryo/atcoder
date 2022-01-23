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
N = int(input())
l = factorization(N)
cnt = 0
if N == 1:
    print(0)
else:
    for i in range(len(l)):
        k = 1
        while True:
            if l[i][1] - k >= 0:
                cnt += 1
                l[i][1] -= k
                k += 1
            else:
                break
    print(cnt)
