for i in range(6, 0, -1):
    for j in range(1,7):
        if j == i:
            print("#", end='')
        else:
            print(' ', end='')
    print()