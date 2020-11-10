""" Объект класса Storage хранит в себе два словаря.
Первый - storage - это наш склад, он имеет вид
{производитель:{тип товара:{модель:{свойства и количество штук на складе}}}}
Второй - give_away - показывает что, кому и в каком количестве мы отдали
он имеет похожую структуру
{другой владелец(или склад):{производитель:{тип товара:{модель:{свойства и количество штук на складе}}}}} """  
class Storage:
    def __init__(self):
        self.storage = {}
        self.give_away = {}
        print('Storage is initialized')
#Добавляем новый  
    def add_new_el(self, element):
        producer = element[0]
        name = element[1]
        model=element[2]
        features = element[3]

        if producer in self.storage:
            if name in self.storage[producer]:
                if model in self.storage[producer][name]:
                    self.storage[producer][name][model]['amount']+=features['amount']
                else:
                    self.storage[producer][name][model] = features
            else:
                self.storage[producer][name] = {model : features}
        else:
            self.storage[producer] = {name:{model:features}}
#Функция для тестирования. Отдает все что есть на складе
    def get_all(self):
        for i in self.storage:
            print(i)
            print('*************************')
            for j in self.storage[i]:
                print(j)
                for k in self.storage[i][j]:
                    print(k)
                    print(f'Data:{self.storage[i][j][k]}\n')
#Удаляет указанный элемент, проверяет, чтобы не получились пустые словари
    def delete_of(self, producer, name, model, amount):
        if producer in self.storage:
            if name in self.storage[producer]:
                if model in self.storage[producer][name]:
                    if amount >= self.storage[producer][name][model]['amount']:
                        print(f'You delete all elements of {producer}--{name}--{model}')
                        
                        self.storage[producer][name].pop(model)
                        if len(self.storage[producer][name]) == 0:
                            self.storage[producer].pop(name)
                            if len(self.storage[producer]) == 0:
                                self.storage.pop(producer)
                    else:
                        self.storage[producer][name][model]['amount'] -= amount 
                else:
                    print('That element is absent')
            else:
                    print('That element is absent')
        else:
                    print('That element is absent')                    
#Эта функция передает технику указанному владельцу, чистит поле give_away от пустых словарей
    def give_it_to(self, producer, name, model, amount, owner):
        my_element = self.storage[producer][name][model].copy()
        if amount < my_element['amount']:
            my_element['amount'] = amount  
        if owner in self.give_away:
            if producer in self.give_away[owner]:
                if name in self.give_away[owner][producer]:
                    if model in self.give_away[owner][producer][name]:
                        self.give_away[owner][producer][name][model]['amount']+=\
                                my_element['amount']
                    else:
                        self.give_away[owner][producer][name][model] = my_element
                else:
                    self.give_away[owner][producer][name] = {model : my_element}
            else:
                self.give_away[owner][producer] = {name:{model:my_element}}
        else:
            self.give_away[owner] = {producer:{name:{model:my_element}}}

        self.delete_of(producer, name, model, amount)



class Equipment:
    def __init__(self, producer, name, model, mass, cost, amount=1, **special_features):
#Обязательные для всех параметры
        self.producer = producer #производитель
        self.name = name         #вид товара(принтер, сканер, телефон...)
        self.model = model       #модель   
        self.mass = mass         #масса
        self.cost = cost         #цена
        self.amount = amount     #количество
#Проверяем, что введенное количество товара является integer        
        while type(self.amount)!=type(1):
            try:
                self.amount = int(self.amount)
            except ValueError:
                self.amount = input('Problem with the type\
                of the amount(must be integer), try to enter it again:')
            
#Параметры которые вводит пользователь по своему желанию для разного оборудования
        self.special_features = special_features
#При значении trigger = 1 функция просто отдает введенные данные(для контроля)
#при других значениях trigger она отдает список в формате который использует
#класс Storage при создании полей
    def inform(self, trigger=1):
        if trigger == 1:
            print(f'Production: {self.producer}')
            print(f'Name: {self.name}')
            print(f'Model: {self.model}')
            print(f'Mass: {self.mass}')
            print(f'Cost: {self.cost}')
            print(f'Amount: {self.amount}')
            for i, j in self.special_features.items():
                print(f'{i}: {j}')
        else: 
            self.special_features['mass'] = self.mass
            self.special_features['cost'] = self.cost
            self.special_features['amount'] = self.amount
            return [self.producer, self.name, 
            self.model, self.special_features]     




class Computer(Equipment):
    def __init__(self,producer, model, mass, cost, name='computer', amount=1, **special_features):
        super().__init__(producer,name, model, mass, cost, amount,**special_features)
        

class Printer(Equipment):
    def __init__(self,producer, model, mass, cost, name='printer', amount=1, **special_features):
        super().__init__(producer,name, model, mass, cost, amount,**special_features)
        

class Phone(Equipment):
    def __init__(self,producer, model, mass, cost, name='phone', amount=1, **special_features):
        super().__init__(producer,name, model, mass, cost, amount, **special_features)
        


#Test
comp_1 = Computer(producer='hp', model = 'FX_239', mass = '2 kg', cost = '230$', 
processor = 'intel_i7', ram_val = '4 Gb', disk_val = '500 Gb', amount = 10)
comp_2 = Computer(producer='htc', model = 'FX_4379', mass = '2 kg', cost = '200$', 
processor = 'intel_i5', ram_val = '8 Gb', disk_val = '500 Gb', amount = 20)

printer_1 = Printer(producer='xerox',amount = '100', model = 'M-604', mass = '4 kg', cost = '750$', 
color='none', wireless = 'yes', speed = '100 pps')
printer_2 = Printer(producer='xerox',amount = 10, model = 'M-704', mass = '4 kg', cost = '750$', 
color='none', wireless = 'no', speed = '150 pps')

phone_1 = Phone(producer='htc',amount = 7, model = 'One-385', mass = '4 kg', cost = '750$', 
color='black', resolution = 'FullHD', ram = '4 Gb')

store = Storage()
store.add_new_el(comp_1.inform(0))
store.add_new_el(comp_1.inform(0))
store.add_new_el(comp_2.inform(0))
store.add_new_el(printer_1.inform(0))
store.add_new_el(printer_2.inform(0))
store.add_new_el(phone_1.inform(0))
#проверяем функцию add_new_el
print('****проверяем функцию add_new_el****')
store.get_all()
print('*************************************************\n')
#проверяем функцию delete_of
print('****проверяем функцию delete_of****')
store.delete_of('xerox', 'printer', 'M-604', 3)
store.get_all()
print('*************************************************\n')
#проверяем функцию give_it_away
print('****проверяем функцию give_it_away****')
store.give_it_to(producer='hp',name = 'computer', model = 'FX_239', amount = 5, owner = 'MyFriend')
store.give_it_to(producer='htc',name = 'computer', model = 'FX_4379', amount = 20, owner = 'MyFriend')
store.get_all()
print('*************************************************\n')
#проверяем заполняется ли поле give_away
print('****проверяем заполняется ли поле give_away****')
print(store.give_away)
print('*************************************************\n')
store.give_it_to(producer='hp',name = 'computer', model = 'FX_239', amount = 5, owner = 'MyFriend')
print(store.give_away)