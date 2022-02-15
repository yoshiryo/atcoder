import os
import pathlib

name = input("追加したいディレクトリの名前を入力 : ")
dir_name = "C:\\Users\\ryota\\Desktop\\atcoder\\" + name + "\\" + name
first_num, end_num = map(int, input("追加するディレクトリの数字を入力 : ").split())
start_file_name, end_file_name = input("追加するファイル(a~oまで)の名前を入力 : ").split()
alp = "abcdefghijklmno"
satrt_index = alp.find(start_file_name)
end_index = alp.find(end_file_name)
for num in range(first_num, end_num + 1):
    num = str(num).zfill(3)
    new_dir = dir_name + num + "\\"
    os.mkdir(new_dir)
    for i in range(satrt_index, end_index+1):
        file = alp[i] + ".py"
        new_file = new_dir + file
        p = pathlib.Path(new_file)
        p.touch()

