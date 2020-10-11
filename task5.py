my_list = [6,4,4,2,1]
new_element = 0
while(True):
	n=0
	new_element = input('введите новый элемент списка(для выхода введите q):')
	if (new_element == 'q'): break
	
	for i in my_list:
		if (i<int(new_element)):
			my_list.insert(n , int(new_element))
			print(my_list)
			break
		
		elif (n == len(my_list) - 1):
			my_list.insert(n+1 , int(new_element))
			print(my_list)
			break
		
		else:n+=1
		
