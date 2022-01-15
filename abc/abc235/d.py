a, n = map(int, input().split())
ans = 0
while n != 1:
    if n%a == 0:
        n //= a
        ans += 1
    else:
        if n >= 10 and n%10 != 0:
            l = list(str(n))
            num = l[:len(l)-1]
            num.insert(0, l[len(l)-1])
            n = int(''.join(num))
            ans += 1
        else:
            print(-1)
            exit()
print(ans)