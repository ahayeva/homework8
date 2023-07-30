if __name__ == "__main__":
    #EXERCISE 1
#     print(" виберіть операцію")
#     print("1 - сума трьох чисел")
#     print("2 - добуток трьох чисел")
#     choice = int(input("введіть номер операції (1 або 2): "))
#     if choice == 1:
#     num1 = float(input("введіть перше число: "))
#     num2 = float(input("введіть друге число: "))
#     num3 = float(input("введіть третє число: "))
#     result = num1 + num2 + num3
#     print("ума трьох чисел", result)
# elif choice == 2:
#     num1 = float(input("введіть перше число: "))
#     num2 = float(input("введіть друге число: "))
#     num3 = float(input("введіть третє число: "))
#     result = num1 * num2 * num3
#     print("добуток трьох чисел:", result)
# else:
#     print("Не вірна операція. введіть 1 або 2.")
# # Exercise 2
#     print("1 -максимум з трьох чисел")
#     print("2 -мінімум з трьох чисел")
#     print("3 -середньоарифметичне трьох чисел")
#
#     choice = int(input("введіть номер операції (1, 2 або 3): "))
#     if choice == 1:
#         num1 = float(input("введіть перше число: "))
#         num2 = float(input("введіть друге число: "))
#         num3 = float(input("введіть третє число: "))
#         result = max(num1, num2, num3)
#         print("максимум з трьох чисел", result)
#     elif choice == 2:
#         num1 = float(input("введіть перше число"))
#         num2 = float(input("введіть друге число"))
#         num3 = float(input("введіть третє число"))
#         result = min(num1, num2, num3)
#         print("мінімум з трьох чисел", result)
#     elif choice == 3:
#         num1 = float(input("введіть перше число"))
#         num2 = float(input("введіть друге число"))
#         num3 = float(input("введіть третє число"))
#         result = (num1 + num2 + num3) / 3
#         print("середньоарифметичне всіхчисел", result)
#     else:
#         print("не вірнифй вибір .введіть 1, 2 або 3.")
#
# EXERCISE 3
    print("1 - конвертація метрів в милі")
    print("2 - конвертація метрів в дюйми")
    print("3 - конвертація метрів в ярди")

    choice = int(input("введіть номер операції (1, 2 або 3): "))
    meters = float(input("введіть кількість метрів: "))

    if choice == 1:
        miles = meters * 0.000621371
        print(meters, "метрів дорівнює", miles, "миль")
    elif choice == 2:
        inches = meters * 39.3701
        print(meters, "метрів дорівнює", inches, "дюймів")
    elif choice == 3:
        yards = meters * 1.09361
        print(meters, "метрів дорівнює", yards, "ярдів")
    else:
        print("Не вірний вибір операції. Введіть 1, 2 або 3.")