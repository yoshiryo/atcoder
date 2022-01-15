x = input()
password = ["0123", "1234","2345", "3456", "4567", "5678", "6789", "7890", "8901", "9012"]
num = len(set(list(x)))
if num == 1:
    print("Weak")
else:
    if x in password:
        print("Weak")
    else:
        print("Strong")