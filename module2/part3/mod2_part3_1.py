# Пользователь вводит с клавиатуры число в диапазоне от 1 до 100. Если число кратно 3 (делится на 3
# без остатка) нужно вывести слово Fizz. Если число
# кратно 5 нужно вывести слово Buzz. Если число
# кратно 3 и 5 нужно вывести Fizz Buzz. Если число
# не кратно не 3 и 5 нужно вывести само число.
print("Введите число от одного до ста:")
the_number = int(input()) in range(1, 101)
if the_number > 100 or the_number < 1:
    print("Ошибка.")
elif the_number % 3 == 0:
    print("Fizz, bro")
elif the_number % 5 == 0:
    print("Buzz")
elif the_number % 3 == 0 and the_number % 5 == 0:
    print("Fizz Buzz")
else:
    print(the_number)