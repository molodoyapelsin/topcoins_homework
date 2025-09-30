# Дано число. Выведите в консоль последнюю цифру этого числа.
print("Введите число. Будет выведена последняя цифра этого числа.")
the_num = int(input())
the_str = str(the_num)
print(int(the_str[-1]))
print(type(int(the_str)))
