# Дан список с числами. Найдите сумму положительных элементов этого списка.
the_mothafucka_list = [1, 2, -3, 4, -5]
the_positive_sum = (x for x in the_mothafucka_list if x > 0)

# sum = 0
# for number in the_mothafucka_list:
#     if number > 0:
#         sum += number

print(sum(the_positive_sum))