ans_dict = {}
#this function collects all numbers from string and returns a list of it
def get_all_num(my_str):
    container = []
    one_num = ''
    for i, x in enumerate(my_str):
        if x.isdigit():
            one_num = one_num + x
        elif i > 0:
            if my_str[i-1].isdigit():
                container. append(one_num)
                one_num = ''
    return container


with open('data_for_task6.txt', mode='r') as my_file:
    next_str = my_file.readline()
    while next_str:
        my_key = next_str.split(':')[0]
        my_value = [int(x) for x in get_all_num(next_str)]
        ans_dict[my_key] = sum(my_value)
        next_str = my_file.readline()
print(ans_dict)