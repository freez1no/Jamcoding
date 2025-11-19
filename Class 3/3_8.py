x, y = input("점의 좌표 x, y를 입력하세요 : ").split()
x = int(x)
y = int(y)

if x > 0 and y > 0:
    print(f"1사분면에 있음")
elif x > 0 and y < 0:
    print(f"4사분면에 있음")
elif x < 0 and y > 0:
    print(f"2사분면에 있음")
elif x < 0 and y < 0:
    print(f"3사분면에 있음")
else:
    print(f"중앙(0,0)에 있음")