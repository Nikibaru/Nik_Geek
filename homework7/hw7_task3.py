class Cell:
    def __init__(self, num):
        self.num = num
    def __add__(self, other):
        return Cell(self.num + other.num)
    def __sub__(self, other):
        if self.num - other.num >= 0:
            return Cell(self.num - other.num)
        else:
            print('This operation is imposible!')
    
    def __mul__(self, other):
        return Cell(self.num*other.num)
    
    def __truediv__(self, other):
        return Cell(self.num // other.num)
    
    def make_order(self, num_in_row):
        my_str = ''
        for i in range(self.num // num_in_row):
            my_str += '*'*num_in_row + '\n'
        my_str += '*'*(self.num % num_in_row)
        return my_str

    
cell_type1 = Cell(53)
cell_type2 = Cell(12)
cell_new = cell_type1+cell_type2
print(f'Add_result: {cell_new.num}')
cell_new = cell_type1-cell_type2
print(f'Subtraction_result: {cell_new.num}')
cell_new = cell_type1*cell_type2
print(f'Multipication_result: {cell_new.num}')
cell_new = cell_type1/cell_type2
print(f'Division_result: {cell_new.num}')
cell_new = cell_type1*cell_type2
print(f'Make_order_result:\n{cell_new.make_order(27)}')

