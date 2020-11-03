class IsNotANumber(Exception):
    pass
my_list = []
while True:
    arg = input('input number(type stop for exit): ')
    if arg == 'stop':
        break
    else:
        try:
            if arg.isdigit():
                my_list.append(int(arg))
            else:
                raise IsNotANumber()
        except IsNotANumber:
            print('Ooops! It is not a number!')

print(my_list)



""" Создайте собственный класс-исключение, который должен 
проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. 
Необходимо запрашивать у пользователя данные и 
заполнять список. Класс-исключение должен контролировать 
типы данных элементов списка. """