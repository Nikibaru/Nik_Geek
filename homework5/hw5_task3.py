with open('text_file_for_task3.txt') as my_file:
    data_list = my_file.readlines()
    #mid will contain salary
    mid = []
    for i in data_list:
        if float(i.split(' ')[1]) < 20000:
            print(i.split(' ')[0])
            mid.append(float(i.split(' ')[1]))

    print(f'Median salary: {round(sum(mid)/len(mid), 2)}')