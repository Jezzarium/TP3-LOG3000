import unittest
from operators import add, subtract, multiply, divide

class TestOperators(unittest.TestCase):
    def test_add(self):
        """Test addition function."""
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        """Test subtraction function."""
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self):
        """Test multiplication function."""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        """Test division function."""
        self.assertEqual(divide(6, 3), 2.0)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(10, -2), -5.0)

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            divide(1, 0)

if __name__ == '__main__':
    unittest.main()
