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
    
    def test_exc_size_matrix(self):
        m = Matrix(4, 3)
        self.assertRaises(Matrix.SizeMissMatchException, Matrix.__add__, self.matrix, m)

if __name__ == '__main__':
    unittest.main()