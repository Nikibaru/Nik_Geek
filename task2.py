#вводим наш список. Как перевести строки полученные в input в нормальные форматы типа list, set и т.п. я не понял, но нашел eval и эта функция, насколько я понял, делает это автоматически
my_list = list(eval(input('введите элементы списка через запятую:')))
print(my_list)
if (len(my_list) % 2 == 0):
	my_list[::2],my_list[1::2]=my_list[1::2],my_list[::2]
else:
	my_list[:-1:2],my_list[1:-1:2]=my_list[1:-1:2],my_list[:-1:2]
print(my_list)

