n = int(input())
a = list(map(int, input().split()))
stu = []
for i in range(n):
    stu.append([a[i], i+1])
stu = sorted(stu, key=lambda x:x[0], reverse=True)
for _, num in stu:
    print(num)
