sx, sy, tx, ty = map(int, input().split())
ans = ""
dx = tx - sx
dy = ty - sy
ans += "U"*dy
ans += "R"*dx
ans += "D"*dy
ans += "L"*dx
ans += "L"
ans += "U"*(dy+1)
ans += "R"*(dx+1)
ans += "D"
ans += "R"
ans += "D"*(dy+1)
ans += "L"*(dx+1)
ans += "U"
print(ans)