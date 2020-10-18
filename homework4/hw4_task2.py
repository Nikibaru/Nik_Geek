l = [1, 5, 3, 45, 94, 9, 7, 16, 23, 34, 0, 12]

new_list = [l[i[0]+1] for i in enumerate(l[:-1:]) if l[i[0]+1] > l[i[0]]]
print(new_list)
