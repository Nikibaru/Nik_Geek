class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Start drawing by {self.title}')
    
class Pen(Stationery):
    def __init__(self, *args, title = 'pen'):
        super().__init__(*args, title)
    def draw(self):
        print('Start drawing by pen')

class Pencil(Stationery):
    def __init__(self, *args, title = 'pencil'):
        super().__init__(*args, title)
    def draw(self):
        print('Start drawing by pencil')

class Handle(Stationery):
    def __init__(self, *args, title = 'pencil'):
        super().__init__(*args, title)
    def draw(self):
        print('Start drawing by handle')

#Testing 

stationery = Stationery('felt pen')
pen = Pen()
pencil = Pencil()
handle = Handle()
#Output
stationery.draw()
pen.draw()
pencil.draw()
handle.draw()







""" Реализовать класс Stationery (канцелярская принадлежность). 
Определить в нем атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение “Запуск отрисовки.” 
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
В каждом из классов реализовать переопределение метода draw. 
Для каждого из классов методы должен выводить уникальное сообщение. 
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра. """