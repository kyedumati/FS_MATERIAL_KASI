import unittest
from utils import average, format_inr

class TestUtils(unittest.TestCase):
    def test_average(self):
        # TODO
        pass

    def test_format_inr(self):
        self.assertEqual(format_inr(10), "₹10.00")

if __name__ == "__main__":
    unittest.main()
