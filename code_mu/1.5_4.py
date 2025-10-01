# Даны два целых числа. Найдите остаток от деления первого числа на второе.
print("Введите поочерёдно два целых числа.")
the_num1 = int(input())
the_num2 = int(input())
the_sum = the_num1 % the_num2
print(f"Остаток от деления {the_num1} на {the_num2}, это - {the_sum}")