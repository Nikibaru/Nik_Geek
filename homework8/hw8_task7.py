class ImaginaryNumber:
    def __init__(self, real, imagine):
        self.i = real
        self.j = imagine
    
    def __str__(self):
        if self.i != 0:
            if self.j < 0: 
                return f'{self.i} {self.j}j'
            elif self.j >0:
                return f'{self.i} + {self.j}j'
            else:
                return f'{self.i}'
        else:
            if self.j < 0: 
                return f'{self.j}j'
            elif self.j >0:
                return f'{self.j}j'
            else:
                return f'0'

    def __add__(self, other):
        return ImaginaryNumber(self.i + other.i, self.j+other.j)

    def __mul__(self, other):
        a = self.i
        b=self.j
        c=other.i
        d=other.j
        return ImaginaryNumber(a*c- b*d, a*d+b*c)

#Test
a = ImaginaryNumber(-31, 12)
b = ImaginaryNumber(7, -5)
print(a+b)
print(a*b)

