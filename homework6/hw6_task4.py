class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print('the car drives')
    def stop(self):
        print('the car was stopped')
    def turn(self, direction):
        print(f'the car turn on the {direction}')
    def show_speed(self):
        print(f"car's speed {self.speed}")

class TownCar(Car):
    def show_speed(self):
        if (self.speed > 60):
            print('Over speed!')
        else:
            print(f"car's speed {self.speed}")

class WorkCar(Car):
    def show_speed(self):
        if (self.speed > 40):
            print('Over speed!')
        else:
            print(f"car's speed {self.speed}")

class SportCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self, *args, is_police=True):
        super().__init__(*args, is_police)
        

usual_car = Car(70, 'white', 'cherry', False)
town_car = TownCar(80, 'blue', 'volvo', False)
work_car = WorkCar(60, 'black', 'jeep', False)
sport_car = SportCar(120, 'pink', 'mercedes', False)
police_car = PoliceCar(100, 'black', 'ford')

print('Test speed atribute\n')
print(usual_car.speed)
print(town_car.speed)
print(work_car.speed)
print(sport_car.speed)
print(police_car.speed)

print('\nTest color atribute\n')
print(usual_car.color)
print(town_car.color)
print(work_car.color)
print(sport_car.color)
print(police_car.color)

print('\nTest name atribute\n')
print(usual_car.name)
print(town_car.name)
print(work_car.name)
print(sport_car.name)
print(police_car.name)

print('\nTest is_police atribute\n')
print(usual_car.is_police)
print(town_car.is_police)
print(work_car.is_police)
print(sport_car.is_police)
print(police_car.is_police)

#Test method show_speed
print('\nTest show_speed\n')
usual_car.show_speed()
town_car.show_speed()
work_car.show_speed()
sport_car.show_speed()
police_car.show_speed()

print('\nTest go\n')
usual_car.go()
town_car.go()
work_car.go()
sport_car.go()
police_car.go()

print('\nTest stop\n')
usual_car.stop()
town_car.stop()
work_car.stop()
sport_car.stop()
police_car.stop()

print('\nTest turn\n')
usual_car.turn('right')
town_car.turn('right')
work_car.turn('right')
sport_car.turn('right')
police_car.turn('right')



""" Реализуйте базовый класс Car. 
У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), 
которые должны сообщать, что машина поехала, 
остановилась, повернула (куда).  
Опишите несколько дочерних классов: 
TownCar, SportCar, WorkCar, PoliceCar. 
Добавьте в базовый класс метод show_speed, 
который должен показывать текущую скорость автомобиля. 
Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) 
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. 
Выполните доступ к атрибутам, выведите результат. 
Выполните вызов методов и также покажите результат. """