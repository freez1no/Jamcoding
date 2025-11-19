age = int(input("나이를 입력하시오 : "))
height = int(input("키를 입력하시오(단위 cm)"))

if height >= 150 and age >= 19:
    print(f"입장할 수 있습니다")
else:
    print(f"입장할 수 없습니다")