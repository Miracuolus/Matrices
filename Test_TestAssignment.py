import unittest
from TestAssignment import Matrix

class TestMatrixMethod(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix()
    
    def test_isupper(self):
        self.assertTrue