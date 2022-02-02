a, b = map(int, input().split())
d = b - a - 1
su = d*(d+1)//2
print(su - a)