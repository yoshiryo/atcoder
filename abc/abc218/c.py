def main():
    def count_sharp(s):
        ret = 0
        for s_row in s:
            ret += s_row.count('#')
        return ret

    def find_first_sharp(s):
        for row in range(N):
            for col in range(N):
                if s[row][col] == '#':
                    return row, col

    def is_same(s, t, dr, dc):
        for row in range(N):
            for col in range(N):
                row_s = row + dr
                col_s = col + dc
                if 0 <= row_s < N and 0 <= col_s < N:
                    if s[row_s][col_s] != t[row][col]:
                        return False
                else:
                    if t[row][col] == '#':
                        # グリッドから # がはみ出ているため
                        return False
        return True

    def rot(s):
        return list(zip(*s[::-1]))

    def judge(s, t):
        if count_sharp(s) != count_sharp(t):
            return False
        for _ in range(4):
            sr, sc = find_first_sharp(s)  # sの一番左上の#の位置
            tr, tc = find_first_sharp(t)  # tの一番左上の#の位置
            dr = sr - tr  # 平行移動する量を計算
            dc = sc - tc
            if is_same(s, t, dr, dc):
                return True
            t = rot(t)  # tを90度回転
        return False

    N = int(input())
    S = []
    for _ in range(N):
        _s = input()
        S.append(list(_s))
    T = []
    for _ in range(N):
        _t = input()
        T.append(list(_t))
    print("Yes" if judge(S, T) else "No")


if __name__ == '__main__':
    main()