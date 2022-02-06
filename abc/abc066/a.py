price = list(map(int, input().split()))
price.sort()
print(sum(price[:2]))