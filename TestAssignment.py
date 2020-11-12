
class Matrix:
    class ValueRowError(Exception):
        pass

    class ValueColError(Exception):
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
        value = r*self._col + c
        return value

    def set_value(self, r, c, value):
        self._value[r*self._col + c] = value
    
    def __add__(self, matrix):
        if self._row != matrix._row:
            raise Matrix.ValueRowError()
        if self._col != matrix._col:
            raise Matrix.ValueColError()
        result = Matrix(self._row, self._col)
        for i in range(len(self._value)):
            result._value[i] = self._value[i] + matrix._value[i]
        return result
    
    def __str__(self):
        return f'{ self._value}'



A = Matrix(2, 2)
A.set_value(0,0,10)
B = Matrix(2, 2)
for i in range(B.row_value()):
    for j in range(B.col_value()):
        B.set_value(i, j, i+j)
C = A + B
print(A)
print(B)
print(C)