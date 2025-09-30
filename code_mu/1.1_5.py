# Даны два слова. Проверьте, что первые буквы этих слов совпадают.
print("Введите поочерёдно два слова.")
firstword = input()
secondword = input()
if (firstword[0]) == (secondword[0]):
    print(f"Первые буквы {firstword} и {secondword} - совпадают!")
else:
    print(f"Первые буквы {firstword} и {secondword} - не совпадают.")