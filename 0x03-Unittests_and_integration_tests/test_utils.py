#!/usr/bin/env python3
"""unit test"""

from parameterized import parameterized
from unittest.mock import patch, Mock
import unittest
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a"), KeyError),
        ({"a", 1}, ("a", "b"), KeyError)
        ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):

    @parameterized.expand([
        (
            {
                "test_url": "http://example.com",
                "test_payload": {"payload": True}
            }
        ),
        (
            {
                    "test_url": "http://holberton.io",
                    "test_payload": {"payload": False}
            }
        )
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_case, mock_get):
        with self.subTest(test_case=test_case):
            mock_get.return_value = Mock()
            mock_get.return_value.json.return_value =\
                test_case['test_payload']

            result = get_json(test_case['test_url'])
            mock_get.assert_called_once_with(test_case['test_url'])
            self.assertEqual(result, test_case['test_payload'])


if __name__ == "__main__":
    unittest.main()
