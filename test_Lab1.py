import unittest
from Lab1 import peremiter

class TestLab1(unittest.TestCase):

    def test_ints(self):
        self.assertEqual(peremiter(1,2),6)
        self.assertEqual(peremiter(2,4),12)
        

if __name__ == '__main__':
    unittest.main()