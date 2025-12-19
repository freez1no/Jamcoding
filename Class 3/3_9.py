x = int(input("정수를 입력하세요 : "))
if x%2 == 0:
    print(f"{x}는 2로 나누어집니다")
else:
    print(f"{x}는 2로 나누어지지 않습니다")
    
if x%3 !=0:
    print(f"{x}는 3으로 나누어지지 않습니다.")
else:
    print(f"{x}는 3으로 나누어집니다")

if x%2 == 0 and x%3 == 0:
    print(f"{x}는 2와 3모두에 대해서 동시에 나누어집니다")
else:
    print(f"{x}는 2와 3모두에 대해서 동시에 나누어지지는 않습니다")