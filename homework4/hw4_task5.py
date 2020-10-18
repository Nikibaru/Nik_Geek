from functools import reduce
new_list = [x for x in range(100, 1001,1) if x % 2 == 0]
multiply = reduce(lambda x, y: x*y, new_list)
print(f'List:{new_list}')
print(f'Multiplication: {multiply}')