# Дано число. Выведите в консоль первую цифру этого числа.
print("Введите число. Будет выведена первая цифра этого числа.")
the_num = int(input())
the_str = str(the_num)
print(int(the_str[0]))
print(type(int(the_str)))
