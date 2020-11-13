class Matrix:
    class SizeMisMatch(Exception):
        pass

    def __init__(self, row, col):
        self._row = row
        self._col = col
        self._value = [0 for _ in range(row*col)]
    
    def row_value(self):
        return self._row
    
    def col_value(self):
        return self._col
    
    def get_value(self, r, c):
        return self._value[r*self._col + c]

    def set_value(self, r, c, value):
        self._value[r*self._col + c] = value
    
    def __add__(self, matrix):
        if self._row != matrix._row or self._col != matrix._col:
            raise Matrix.SizeMisMatch()
        result = Matrix(self._row, self._col)
        for i in range(len(self._value)):
            result._value[i] = self._value[i] + matrix._value[i]
        return result
    
    def __sub__(self, matrix):
        if self._row != matrix._row or self._col != matrix._col:
            raise Matrix.SizeMisMatch()
        result = Matrix(self._row, self._col)
        for i in range(len(self._value)):
            result._value[i] = self._value[i] - matrix._value[i]
        return result
    
    def __mul__(self, matrix):
        if self._col != matrix._row:
            raise Matrix.SizeMisMatch()
        result = Matrix(self._row, matrix._col)
        for i in range(result._row):
            for j in range(result._col):
                value = 0
                for v in range(self._col):
                    value += self.get_value(i, v) * matrix.get_value(v, j)
                result.set_value(i, j, value)
        return result
    
    @staticmethod
    def fromstring(line):
        rows = line[1:-1].split(';')
        for i in range(len(rows)):
            rows[i] = rows[i].lstrip(' ').split(' ')
        for j in rows:
            l = len(j)
            if len(rows[0]) != l:
                raise Matrix.SizeMisMatch()
        m = Matrix(len(rows), len(rows[0]))
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                m.set_value(i, j, int(rows[i][j]))
        return m
    
    def __str__(self):
        return f'{ self._value}'


"""
A = Matrix(2, 2)
A.set_value(0,0,10)
B = Matrix(2, 2)
for i in range(B.row_value()):
    for j in range(B.col_value()):
        B.set_value(i, j, i+j)
C = A + B
D = C + A - C
G = A * B
print(f'A = {A}')
print(f'B = {B}')
print(f'C = {C}')
print(f'D = {D}')
print(f'G = {G}')
"""
try:
    while True:
        line = input()
        if not line or not line.strip():
            #m = Matrix.fromsting(line)#[1 2; 3 4; 5 6]
            break
        print(Matrix.fromstring(line.split('=')[1]))
    cond = input()
except ValueError:
    print('*Ошибка! Необходимо вводить данные в числовых значениях')
