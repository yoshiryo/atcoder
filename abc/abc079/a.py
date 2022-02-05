n = input()
all = ["111", "222", "333", "444","555","666","777","888","999","000"]
for i in all:
    if i in n:
        print("Yes")
        exit()
print("No")