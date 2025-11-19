a,b,c = input("정수 3개 입력 : ").split()
print(a,b,c, type(a))

a = int(a)
b = int(b)
c = int(c)

print(type(a))

if a>b and a>c:
    if b>c:
        print(c,b,a)
    else:
        print(b,c,a)