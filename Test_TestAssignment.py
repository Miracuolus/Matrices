import unittest
from TestAssignment import Matrix

class TestMatrixMethod(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix(3, 4)
    
    def test_init(self):
        self.assertEqual(self.matrix.row_value(), 3,
                        'incorrect number of rows')
        self.assertEqual(self.matrix.col_value(), 4,
                        'incorrect number of columns')
    
    def test_getvalue(self):
        self.assertIs(self.matrix.get_value(2, 2), 0,
                    'incorrect getting value by row and column')
    
    def test_setvalue(self):
        self.matrix.set_value(2, 2, 1)
        self.assertIs(self.matrix.get_value(2, 2), 1,
                    'incorrect setting value by row and column')

if __name__ == '__main__':
    unittest.main()