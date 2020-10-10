month = int(input('введите номер месяца(1-12):'))%12
#List_method
season = ['winter', 'spring', 'summer', 'autumn']
print(f'list_method: {season[month//3]} ')
#Dict_method
month=str(month)
season={'012' : 'winter' , '345' : 'spring', '678' : 'summer', '91011' : 'autumn'}
for i in season.keys():
	if (i.find(month)>=0):
		print(f'dict_method: {season[i]}')
		break

