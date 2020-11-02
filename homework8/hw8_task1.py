class Data:

    def __init__(self, my_str):
        Data.my_str = my_str
    @classmethod
    def extract(self):
        l_str = self.my_str.split('-')
        l_str = [int(i) for i in l_str]
        return(l_str)
    @staticmethod
    def valid(my_str):
        month = dict([(1,31), (2,28),(3,31),(4,30),(5,31),(6,30),
        (7,31),(8,31),(9,30),(10,31),(11,30),(12,31)])
        l_str = Data(my_str).extract()
        if (l_str[1]>12 or l_str[1]<1):
            print('Ooops! Month is incorrect')
        else:
            if(l_str[0]>month[l_str[1]] or l_str[0]<1):
                print('Ooops! Day is incorrect')
            else:
                print('All right!')
#tests            
test = Data('12-2-23')
print(test.extract())

Data.valid('12-2-23')
Data.valid('42-5-43')
Data.valid('12-50-43')




""" Реализовать класс «Дата», функция-конструктор которого
должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором
@classmethod, должен извлекать число, месяц, год и 
преобразовывать их тип к типу «Число». 
Второй, с декоратором @staticmethod, должен проводить 
валидацию числа, месяца и года (например, месяц — от 1 до 12). 
Проверить работу полученной структуры на реальных данных. """