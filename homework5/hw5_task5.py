with open('text_file_for_task5.txt', mode ='w') as my_file:
    while True:
        numb = input('Enter the number(enter q for exit): ')
        if numb == 'q':
            break
        else:
            my_file.write(f'{numb} ')

with open('text_file_for_task5.txt') as my_file:
    num_str = my_file.readline()
    #get the list of numbers and except EOF
    num_list = [float(x) for x in num_str.split(' ')[:-1:]]
    print(f'The summ: {sum(num_list)}')
