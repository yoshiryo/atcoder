import math 

a, b = map(int, input().split())
yakusu = math.gcd(a, b)

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

if yakusu == 1:
    print(1)
else:
    print(len(factorization(yakusu))+1)