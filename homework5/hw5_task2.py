with open('text_file_for_task2.txt') as my_file:
    list_of_str = my_file.readlines()
    counter = 1
    for i in list_of_str:
        print(f'Length of string {counter} equal: {len(i.split(" "))} words')
        counter += 1
    print(f'In all we have {counter - 1} strings')

