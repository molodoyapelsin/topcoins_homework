print("Введите поочерёдно три числа.")
number1 = int(input())
number2 = int(input())
number3 = int(input())
choice = input("Вы хотите вывести; минимум, максимум, или среднеарифметическое из этих чисел?")
if choice == "минимум":
  result = min(number1, number2, number3)
  print(f"Минимум из {number1},{number2},{number3} это: {result}")
elif choice == "максимум":
  result = max(number1, number2, number3)
  print(f"Максимум из {number1},{number2},{number3} это: {result}")
elif choice == "среднеарифметическое":
  result = int((number1 + number2 + number3) / 3)
  print(f"Среднеарифметическое из {number1},{number2},{number3} это: {result}")
else:

  print("ну это не то бро")
