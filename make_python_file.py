import os
import pathlib

name = input("ファイルを作成したいディレクトリの名前を入力 : ")
dir_name = "C:\\Users\\ryota\\Desktop\\atcoder\\" + name + "\\" + name
first_num, end_num = map(int, input("ディレクトリの数字を入力 : ").split())

for num in range(first_num, end_num + 1):
    num = str(num).zfill(3)
    new_dir = dir_name + num + "\\"
    #os.mkdir(new_dir)
    for file in ["a.py", "b.py", "c.py"]:
        new_file = new_dir + file
        p = pathlib.Path(new_file)
        p.touch()
