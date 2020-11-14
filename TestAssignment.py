class IllegalInputException(Exception):
        def __init__(self, message):
            self.message = message
class Matrix:
    class SizeMissMatchException(Exception):
        def __init__(self, message):
            self.message = message
    
    class IllegalArgumentException(Exception):
        def __init__(self, message):
            self.message = message


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
            raise Matrix.SizeMissMatchException("Can't perform addition")
        result = Matrix(self._row, self._col)
        for i in range(len(self._value)):
            result._value[i] = self._value[i] + matrix._value[i]
        return result
    
    def __sub__(self, matrix):
        if self._row != matrix._row or self._col != matrix._col:
            raise Matrix.SizeMissMatchException("Can't perform subtraction")
        result = Matrix(self._row, self._col)
        for i in range(len(self._value)):
            result._value[i] = self._value[i] - matrix._value[i]
        return result
    
    def __mul__(self, matrix):
        if self._col != matrix._row:
            raise Matrix.SizeMissMatchException("Can't perform multiplication")
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
                raise Matrix.SizeMissMatchException("Different number of items in rows")
        m = Matrix(len(rows), len(rows[0]))
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                try:
                    m.set_value(i, j, int(rows[i][j]))
                except ValueError:
                    raise Matrix.IllegalArgumentException("Can't read matrix")
        return m
    
    def __str__(self):
        s = '['
        for i in range(self._row):
            for j in range(self._col):
                s += f'{ self._value[i*self._col+j] }'
                if j+1 != self._col:
                    s += ' '
            if i+1 != self._row:
                s += '; '
        s += ']'
        return f'{ s}'


matrix_dict = dict()
try:
    while True:
        line = input()
        if not line or not line.strip():
            if len(matrix_dict) == 0:
                raise IllegalInputException('Incorrect input pattern')
            else:
                break
        name, *value = line.split('=')
        if len(value) != 1:
            raise IllegalInputException('Incorrect input matrix')
        if not name.isupper() or len(name) != 1:
            raise Matrix.IllegalArgumentException('Wrong name of matrix')
        matrix_dict[name] = Matrix.fromstring(*value)
    cond = input()
    if not cond or not cond.strip():
        raise IllegalInputException('Incorrect input pattern')
    result = exec('print('+cond+')', matrix_dict)
except (Matrix.SizeMissMatchException, Matrix.IllegalArgumentException, IllegalInputException) as exception:
    print('Exception caughtg: ' + type(exception).__name__ +'. ' + exception.message)
