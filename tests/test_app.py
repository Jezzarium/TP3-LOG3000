import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_index_page(self):
        """Test that the index page loads correctly."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_calculation_add(self):
        """Test addition calculation via POST request."""
        response = self.client.post('/', data={'display': '2 + 3'})
        self.assertIn(b'5.0', response.data)

    def test_calculation_subtract(self):
        """Test subtraction calculation via POST request."""
        response = self.client.post('/', data={'display': '5 - 3'})
        self.assertIn(b'2.0', response.data)

    def test_calculation_multiply(self):
        """Test multiplication calculation via POST request."""
        response = self.client.post('/', data={'display': '4 * 2'})
        self.assertIn(b'8.0', response.data)

    def test_calculation_divide(self):
        """Test division calculation via POST request."""
        response = self.client.post('/', data={'display': '10 / 2'})
        self.assertIn(b'5.0', response.data)

    def test_invalid_expression(self):
        """Test handling of invalid expressions."""
        response = self.client.post('/', data={'display': '2 +'})
        self.assertIn(b'Error', response.data)

    def test_divide_by_zero_error(self):
        """Test handling of division by zero."""
        # Note: If operators.py doesn't handle div by zero properly, this might expose a server error or a different exception
        response = self.client.post('/', data={'display': '5 / 0'})
        self.assertIn(b'Error', response.data)

if __name__ == '__main__':
    unittest.main()
