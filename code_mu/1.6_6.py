# Дана некоторая строка. Переберите и выведите в консоль по очереди все символы с конца строки.
the_stroka = 'abcde'
for i in range(len(the_stroka) - 1, -1, -1):
    print(the_stroka[i])