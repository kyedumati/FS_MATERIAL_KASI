import unittest
from utils import average

class TestUtils(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([10, 20, 30]), 20)

if __name__ == "__main__":
    unittest.main()
