s = input().split("/")
year = int(s[0])
month = int(s[1])
day = int(s[2])
if year <= 2019 and month <= 4:
    print("Heisei")
else:
    print("TBD")
