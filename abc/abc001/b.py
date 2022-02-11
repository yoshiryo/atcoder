n = int(input())
if n < 100:
    print("00")
elif(n<=5000):
    print(str(n//100).zfill(2))
elif(n<=30000):
    print(n//1000+50)
elif(n<=70000):
    print((n//1000-30)//5+80)
else:
    print(89)