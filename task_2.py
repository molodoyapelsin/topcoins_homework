numbers = int(input("Напишите целое число: "))
numbers = list(str(numbers))
sum = 1;

for number in numbers:
    sum = sum * int(number)

print(sum)
