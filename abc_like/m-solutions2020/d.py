n = int(input())
a = list(map(int, input().split()))
money = 1000
count = 0
 
for i in range(n-1):
  if a[i] < a[i+1]:
    count = money//a[i]
    money -= a[i]*count
    money += a[i+1]*count
print(money)