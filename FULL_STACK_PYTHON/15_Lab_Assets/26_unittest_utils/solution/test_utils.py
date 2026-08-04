import unittest
from utils import average, format_inr

class TestUtils(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([10, 20, 30]), 20)

    def test_average_empty(self):
        with self.assertRaises(ValueError):
            average([])

    def test_format_inr(self):
        self.assertEqual(format_inr(1234.5), "₹1,234.50")

if __name__ == "__main__":
    unittest.main()
