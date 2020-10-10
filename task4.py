main_string = input('введите строку: ').split(' ')
n=1
for i in main_string: 
	print(f'{n}) {i[:10]}')
	n+=1

