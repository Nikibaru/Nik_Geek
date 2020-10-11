all_products = [] #список который нужно заполнить 
n = 1
#заполняем список характеристик товара(features):название, цена, количество и т.п.
features = []
ans = 'yes'
while(ans == 'yes' or ans == 'y'):
	features.append(input('введите характеристику товара: '))
	ans = input('продолжаем заполнение?(yes/no):')
#заполняем список товаров(all_products)
ans = 'yes'
while(ans == 'yes' or ans == 'y'):
	inform = dict()
	for i in features:
		value = input(f'{i} товара:')
		inform.setdefault(i, value)
	all_products.append(tuple([n, inform]))
	n+=1
	ans = input('продолжаем заполнение?(yes/no)')
for i in all_products:
	print(i)
#вторая часть задания где анализируется список товаров и создается словарь Analisis
Analisis = {}

for i in features:
	pot = []
	for n in all_products:
		pot.append(n[1][i])
	Analisis.setdefault(i , pot)
for i in features:
	print(i, ':', Analisis[i])
	
