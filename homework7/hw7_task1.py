class Matrix:
    def __init__(self, my_list):
        self.matrix = my_list

    def __str__(self):
        ans = ''
        for i_string in self.matrix:
            ans += (str(i_string)+'\n')
        return(ans)
    
    def __add__(self, other):
        new_matrix=[]
        for i in range(len(self.matrix)):
            new_matrix.append([])
            for j in range(len(self.matrix[i])):
                new_matrix[i].append(other.matrix[i][j] + self.matrix[i][j])
        return (Matrix(new_matrix))

        
#Test
my_list1 = [[1,2,3],[4,5,6],[7,8,9]]
my_list2 = [[0,-1,-2],[-3,-4,-5],[-6,-7,-8]]
matrix1 = Matrix(my_list1)
matrix2 = Matrix(my_list2)
matrix3 = matrix1 + matrix2
print(matrix1)
print(matrix2)
print(matrix3)



""" 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса 
(метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух 
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки 
первой матрицы складываем с первым элементом первой строки второй матрицы и т.д. """