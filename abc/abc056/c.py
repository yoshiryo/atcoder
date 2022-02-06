x = int(input())
cnt = 0
for i in range(1, 10**5+1):
    if 0.5*i*(i+1) >= x:
        print(i)
        break