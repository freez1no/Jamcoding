Q = 2
W = 3
E = 9

a,b,c = input("정수 3개 입력 : ").split()

a = int(a)
b = int(b)
c = int(c)

if a == Q:
    if b == W:
        if c == E:
            print(f"상금 1천만원")
    elif b == E:
        if c == W:
            print(f"상금 1천만원")
    else:
        print("상금 1만원")
elif b == Q:
    if c == W:
        if a == E:
            print(f"상금 1천만원")
    elif c == E:
        if a == W:
            print(f"상금 1천만원")
    else:
        print("상금 1만원")

elif c == Q:
    if b == W:
        if a == E:
            print(f"상금 1천만원")
    elif a == E:
        if b == W:
            print(f"상금 1천만원")
    else:
        print("상금 1만원")

else:
    print(f"다음기회에...")