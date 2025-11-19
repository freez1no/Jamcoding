# 3개의 정수를 입력받아 리스트 a에 저장
a = list(map(int, input("정수 3개 입력: ").split()))

# if-else 만 사용하여 정렬
if a[0] <= a[1] and a[0] <= a[2]:
    if a[1] <= a[2]:
        print(a[0], a[1], a[2])
    else:
        print(a[0], a[2], a[1])
elif a[1] <= a[0] and a[1] <= a[2]:
    if a[0] <= a[2]:
        print(a[1], a[0], a[2])
    else:
        print(a[1], a[2], a[0])
else:  # a[2]가 가장 작은 경우
    if a[0] <= a[1]:
        print(a[2], a[0], a[1])
    else:
        print(a[2], a[1], a[0])
