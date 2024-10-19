stone_1 = int(input("Введите число 3 to 20: "))
if 3 <= stone_1 <= 20:
    def password(k):
        password_win = ""
        for i in range(1, k):
            for j in range(i + 1, k):
                if k % (i + j) == 0:
                    password_win += str(i) + str(j)
        return password_win
    result = password(stone_1)
    print("Password: ", result)
else:
    print("Вы ввели неверное число!")