class MyError(Exception):
    def __init__(self, text):
        self.txt = text
        print(self.txt)
 
 
#test(я очень плохо понял смысл этой задачи)

a = 0 
try:
    if a == 0:
        raise MyError("Ooops! Dividing by zero")
    z = 1/a
except MyError as mr:
    z = 1          #при делении на нуль - присваиваем z например 1
    print(z)


""" Создайте собственный класс-исключение, обрабатывающий 
ситуацию деления на нуль. Проверьте его работу на данных, 
вводимых пользователем. При вводе пользователем нуля в 
качестве делителя программа должна корректно обработать 
эту ситуацию и не завершиться с ошибкой. """