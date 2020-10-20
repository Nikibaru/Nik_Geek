numb = {0:'Нуль',1:'Один',2:'Два',3:'Три',4:'Четыре',5:'Пять',6:'Шесть',7:'Семь',8:'Восемь',9:'Девять'}
with open('text_file_for_task4.txt') as data_file:
    line = data_file.readline()
    with open('rus_file_for_task4.txt', 'w') as new_file:
        #goes line by line
        while line:
            new_file.write(f'{numb[int(line.split("-")[1])]}-{line.split("-")[1]}')
            line = data_file.readline()
        