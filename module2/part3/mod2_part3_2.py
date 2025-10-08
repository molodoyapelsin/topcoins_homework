# Написать программу, которая по выбору пользователя возводит введенное им число в степень
# от нулевой до седьмой включительно
print("Введите число:")
that_number = int(input())
print(f"Введите степень (от 0 до 7), в которую вы хотите возвести {that_number}.")
the_stepen = int(input())
if the_stepen > 7 or the_stepen < 1:
    print("Ошибка.")
else:
    print(that_number ** the_stepen)