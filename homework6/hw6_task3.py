class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'
    def get_full_income(self):
        return self._income["wage"]+self._income["bonus"]




income = {'wage':400, 'bonus':250}
position1 = Position('Nik', 'Hosh', 'Developer', income)
income = {'wage':500, 'bonus':320}
position2 = Position('Oleg', 'Smirnov', 'manager', income)
print(position1.get_full_name())
print(position1.get_full_income())
print(position2.get_full_name())
print(position2.get_full_income())


""" Реализовать базовый класс Worker (работник),
в котором определить атрибуты:
name, surname, position (должность), income (доход). 
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. 
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного
имени сотрудника (get_full_name) и 
дохода с учетом премии (get_total_income). 
Проверить работу примера на реальных данных 
(создать экземпляры класса Position, передать данные, 
проверить значения атрибутов, вызвать методы экземпляров). """