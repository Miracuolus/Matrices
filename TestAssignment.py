"""
This module implements basic matrix operations: addition, subtraction and
multiplication.

"""
class IllegalInputException(Exception):
    """
    Execution for the data input format is incorrect
    
    Attributes
    ----------
    message : str
        Error description
    """

    def __init__(self, message):
        """
        Parameters
        ----------
        message : str
            Error description
        """
        self.message = message


class Matrix:
    """
    A class created matrix

    Attributes
    ----------
    row : int
        Number of rows in a matrix
    col : int
        Number of columns in a matrix
    values : list, optional
        Matrix values (default is None)

    Methods
    -------
    row_value()
        Returns the number of rows
    col_value()
        Returns the number of columns
    get_value(r, c)
        Returns the value by row and column
    set_value(r, c, value)
        Sets the value by row and column
    __add__(matrix)
        Overriding the addition operation
    __sub__(matrix)
        Overriding the subtraction operation
    __mul__(matrix)
        Overriding the multiplication operation
    __str__()
        Print matrix in accordance with the requirements
    
    Exception
    ----------
    SizeMissMatchException
        Raise when matrix size mismatch
    IllegalArgumentException
        Raise when matrix argument is invalid

    Staticmethod
    ----------
    fromstring(line)
        Converting data from string to matrix
    """
    class SizeMissMatchException(Exception):
        """
        Raise when matrix size mismatch
        
        Attributes
        ----------
        message : str
            Error description
        """
        def __init__(self, message):
            """
            Parameters
            ----------
            message : str
                Error description
            """
            self.message = message

    class IllegalArgumentException(Exception):
        """
        Raise when matrix argument is invalid
        
        Attributes
        ----------
        message : str
            Error description
        """
        def __init__(self, message):
            """
            Parameters
            ----------
            message : str
                Error description
            """
            self.message = message

    def __init__(self, row, col, values = None):
        """
        Parameters
        ----------
        row : int
            Number of rows in a matrix
        col : int
            Number of columns in a matrix
        values : list, optional
            Matrix values (default is None)
        """
        self._row = row
        self._col = col
        self._value = [0 for _ in range(row*col)]
        if values:
            for i in range(min(len(self._value),len(values))):
                self._value[i] = values[i]

    def row_value(self):
        """Returns the number of rows"""
        return self._row

    def col_value(self):
        """Returns the number of columns"""
        return self._col

    def get_value(self, r, c):
        """
        Returns the value by row and column.

        Parameters
        ----------
        r : int
            Number of rows in a matrix
        c : int
            Number of columns in a matrix
        """
        return self._value[r*self._col + c]

    def set_value(self, r, c, value):
        """
        Sets the value by row and column.

        Parameters
        ----------
        r : int
            Number of rows in a matrix
        c : int
            Number of columns in a matrix
        value : int
            Matrix value
        """
        self._value[r*self._col + c] = value

    def __add__(self, matrix):
        """
        Overriding the addition operation.

        Returns the result of the operation

        Parameters
        ----------
        matrix : Matrix
            Matrix with which to add the current matrix

        Raises
        ------
        SizeMissMatchException
            If the number of rows and columns of the matrices is different
        """
        if self._row != matrix._row or self._col != matrix._col:
            raise Matrix.SizeMissMatchException("Can't perform addition")
        result = Matrix(self._row, self._col)
        for i in range(len(self._value)):
            result._value[i] = self._value[i] + matrix._value[i]
        return result

    def __sub__(self, matrix):
        """
        Overriding the subtraction operation.

        Returns the result of the operation

        Parameters
        ----------
        matrix : Matrix
            Matrix with which to subtraction the current matrix

        Raises
        ------
        SizeMissMatchException
            If the number of rows and columns of the matrices is different
        """
        if self._row != matrix._row or self._col != matrix._col:
            raise Matrix.SizeMissMatchException("Can't perform subtraction")
        result = Matrix(self._row, self._col)
        for i in range(len(self._value)):
            result._value[i] = self._value[i] - matrix._value[i]
        return result

    def __mul__(self, matrix):
        """
        Overriding the multiplication operation.

        Returns the result of the operation

        Parameters
        ----------
        matrix : Matrix
            Matrix with which to multiplication the current matrix

        Raises
        ------
        SizeMissMatchException
            If the number of rows and columns of the matrices is different
        """
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
        """
        Converting data from string to matrix

        Returns the result in Matrix format

        Parameters
        ----------
        line : str
            String received on input

        Raises
        ------
        SizeMissMatchException
            If the number of rows and columns of the matrices is different
        IllegalArgumentException
            If the arrgument of the matrices is invalid
        """
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
        """Print matrix in accordance with the requirements"""
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

if __name__ == "__main__":
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
        print('Exception caughtg: ' + type(exception).__name__ + '. ' + exception.message)
    except Exception as exception:
        print('Exception caughtg: ' + type(exception).__name__ + '. Wrong input condition')