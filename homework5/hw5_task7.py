from json import dump
with open('data_for_task7.txt', mode = 'r') as my_file:
    ans_dict = {}
    next_str = my_file.readline()
    while next_str:
        my_key = next_str.split(' ')[0]
        my_value = int(next_str.split(' ')[2]) - int(next_str.split(' ')[3])
        ans_dict[my_key] = my_value
        next_str = my_file.readline()
average_profit = round(sum(ans_dict.values())/len(ans_dict), 2)
ans_list = [ans_dict, {'average_profit': average_profit}]
with open('json_for_task7.json', mode = 'w') as json_file:
    dump(ans_list, json_file)