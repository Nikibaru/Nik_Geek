data_list = [19, 2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
ans_list = [data_list[i[0]] for i in enumerate(data_list) 
if (data_list[i[0]] not in data_list[:i[0]:] and data_list[i[0]] not in data_list[i[0]+1::])] 

print(ans_list)
