x = int(input(f" x = "))
y = int(input(f" y = "))

print(f"x = {x}, y = {y}")

if (((x**2)-3)+((y**2)-4))**0.5 <= 10:
    print(f"원의 내부에 있음")

else:
    print(f"원의 외부에 있음")