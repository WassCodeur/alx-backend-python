# example_module.py

import requests

def get_data():
    response = requests.get("http://example.com/data")
    return response.json()


# test_example_module.py

import unittest
from unittest.mock import patch, Mock
# from example_module import get_data

class TestExampleModule(unittest.TestCase):

    @patch('requests.get')
    def test_get_data(self, mock_requests_get):
        # Create a mock response object
        mock_response = Mock()
        mock_response.json.return_value = {'key': 'value'}

        # Configure the mock requests.get to return the mock response
        mock_requests_get.return_value = mock_response

        # Call the function under test
        result = get_data()

        # Assertions
        self.assertEqual(result, {'key': 'value'})
        mock_requests_get.assert_called_once_with("http://example.com/data")
        mock_response.json.assert_called_once()

if __name__ == '__main__':
    unittest.main()

