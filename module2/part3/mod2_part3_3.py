# Написать программу подсчета стоимости разговора для разных мобильных операторов.
# Пользователь вводит стоимость разговора и выбирает с какого на какой оператор он звонит. Вывести стоимость на экран.
print("Введите стоимость разговора:")
price = int(input())
print("Окей, введите с какого оператора вы собираетесь звонить: (MTS, Beeline, Yota)")
the_mazafaka_operator = input()
print("Отлично. На какой оператор вы собираетесь звонить? (выбор, если что, тот же)")
the_shit_operator = input()
if the_mazafaka_operator == "MTS" and the_shit_operator == "MTS":
    print("Цена телефонного разговора составляет:")
    print(price * 1)
elif the_mazafaka_operator == "MTS" and the_shit_operator == "Beeline":
    print(f"Цена телефонного разговора составляет:")
    print(price * 2)
elif the_mazafaka_operator == "MTS" and the_shit_operator == "Yota":
    print(f"Цена телефонного разговора составляет:")
    print(price * 3)
elif the_mazafaka_operator == "Beeline" and the_shit_operator == "Yota" or "Beeline" or "MTS":
    print(f"Цена телефонного разговора составляет:")
    print(price * 2)
else:
    print("Ошибка. Возможно, вы ввели не тот оператор.")