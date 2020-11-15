import unittest
from TestAssignment import Matrix

class TestMatrixMethod(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix(3, 4)
    
    def test_init_rows(self):
        self.assertEqual(self.matrix.row_value(), 3,
                        'incorrect number of rows')
    
    def test_init_cols(self):
        self.assertEqual(self.matrix.col_value(), 4,
                        'incorrect number of columns')
    
    def test_get_value(self):
        self.assertIs(self.matrix.get_value(2, 2), 0,
                    'incorrect getting value by row and column')
    
    def test_set_value(self):
        self.matrix.set_value(2, 2, 1)
        self.assertIs(self.matrix.get_value(2, 2), 1,
                    'incorrect setting value by row and column')
    
    def test_size_row_matrix(self):
        m = Matrix(3, 4)
        self.assertEqual(self.matrix.row_value(), m.row_value(),
                        'matrices have different number of rows')
    
    def test_size_col_matrix(self):
        m = Matrix(3, 4)
        self.assertEqual(self.matrix.col_value(), m.col_value(),
                        'matrices have different number of columns')
    
    def test_exc_size_matrix_foradd(self):
        m = Matrix(4, 3)
        self.assertRaises(Matrix.SizeMissMatchException, Matrix.__add__, self.matrix, m)
    
    def test_add_matrix(self):
        m1 = Matrix(1, 1, [1, 1, 1, 1])
        m2 = Matrix(1, 1, [1, 1, 1, 1])
        r = m1 + m2
        self.assertEqual(r.row_value(), m1.row_value(),
                        'number of rows in the result differs from the original')
        self.assertEqual(r.col_value(), m1.col_value(),
                        'number of columns in the result differs from the original')
        for i in range(r.row_value()):
            for j in range(r.col_value()):
                self.assertEqual(r.get_value(i, j), m1.get_value(i, j) + m2.get_value(i, j),
                                'addition error')
    
    def test_exc_size_matrix_forsub(self):
        m = Matrix(4, 3)
        self.assertRaises(Matrix.SizeMissMatchException, Matrix.__sub__, self.matrix, m)
    
    def test_sub_matrix(self):
        m1 = Matrix(1, 1, [1, 1, 1, 1])
        m2 = Matrix(1, 1, [1, 1, 1, 1])
        r = m1 - m2
        self.assertEqual(r.row_value(), m1.row_value(),
                        'number of rows in the result differs from the original')
        self.assertEqual(r.col_value(), m1.col_value(),
                        'number of columns in the result differs from the original')
        for i in range(r.row_value()):
            for j in range(r.col_value()):
                self.assertEqual(r.get_value(i, j), m1.get_value(i, j) - m2.get_value(i, j),
                                'subtraction error')
    
    def test_exc_size_matrix_formul(self):
        m = Matrix(2, 2)
        self.assertRaises(Matrix.SizeMissMatchException, Matrix.__mul__, self.matrix, m)
    
    def test_size_matrix_formul(self):
        m = Matrix(4, 1)
        self.assertEqual(self.matrix.col_value(), m.row_value(),
                        'matrices cannot be multiplied')
    
    def test_mul_matrix(self):
        m1 = Matrix(3, 2, [9, 8, -10, -4, -3, -9])
        m2 = Matrix(2, 2, [-6, 4, 4, 10])
        r = Matrix(3, 2, [-22, 116, 44, -80, -18, -102])
        #m = Matrix.__mul__(m1, m2)
        for i in range(r.row_value()):
            for j in range(r.col_value()):
                self.assertEqual(r.get_value(i, j), Matrix.__mul__(m1, m2).get_value(i, j),
                                'multiplied error')



if __name__ == '__main__':
    unittest.main()