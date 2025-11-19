#이름, 키입력받기
name = input("이름을 입력하세요 :")
height = int(input("키(cm)를 입력하세요 :"))

#키 비교하기
if height < 140:
    print(f"{name}님은, 놀이기구를 탈 수 없습니다.")
else:
    print(f"{name}님은, 놀이기구 타세용..")