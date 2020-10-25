class Road:
    def __init__(self, length, width, mass_per_square, thikness):
        self.__length = length
        self.__width = width
        self.mass_per_square = mass_per_square
        self.thikness = thikness
    
    def asphalt_mass(self):
        return self.__length*self.__width*\
        self.mass_per_square*self.thikness

road = Road(20,500,25,5)
mass = road.asphalt_mass()
if mass // 1000 != 0:
    print(f'{mass/1000} t')
else:
    print(f'{mass} kg')




""" Реализовать класс Road (дорога), в котором определить атрибуты: 
length (длина), width (ширина). 
Значения данных атрибутов должны передаваться при 
создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для 
покрытия всего дорожного полотна. Использовать формулу:
длина * ширина * масса асфальта для покрытия одного кв 
метра дороги асфальтом, толщиной в 1 см * чи сло см толщины
 полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т """