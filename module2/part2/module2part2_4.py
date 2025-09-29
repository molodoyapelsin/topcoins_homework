print("Введите поочерёдно два числа, для их сравнения.")
number1 = int(input())
number2 = int(input())
if number1 == number2:
    print("Эти два числа - равны.")
elif number1 > number2:
    print(f"Числа - не равны. Числа в порядке возрастания - {number2}, {number1}.")
elif number1 < number2:
    print(f"Числа - не равны. Числа в порядке возрастания - {number1}, {number2}.")
else:

    print("Введено что-то не то.")
