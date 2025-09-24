print("Впиши поочерёдно три числа.")
numbahone = int(input())
numbahtoo = int(input())
numbahfree = int(input())
question = input("Впиши 1 если хочешь суммировать числа, или 2 для их умножения.")

if question == "1":
   result = (numbahone + numbahtoo + numbahfree)
   print(result)

elif question == "2":
    result = (numbahone * numbahtoo * numbahfree)
    print(result)
else:
    print("это не то бро")

