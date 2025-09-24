print("Введите количество метров, для их перевода:")
meters = int(input())
choice = input("Отлично. Теперь выберите эквивалент перевода; мили, дюймы, или ярды.")
if choice == "мили":
    result = (meters * 0.00062137)
    print(f"Получилось {result} милей.")
elif choice == "дюймы":
    result = (meters * 39.37)
    print(f"Получилось {result} дюймов.")
elif choice == "ярды":
    result = (meters // 1.094)
    print(f"Получилось {result} ярдов.")
else:
    print("Неправильный ввод.")
