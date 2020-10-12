def func_man_data(name, surname, year_of_birth, city, email, phone_number):
        return f'information about this man: {name}-{surname}-{year_of_birth}-{city}-{email}-{phone_number}'

#example
param = ('name', 'surname', 'year_of_birth', 'city', 'email', 'phone_number')
data = {}
for i in param:
    data[i] = input(f'input {i}:')
print(func_man_data(**data))