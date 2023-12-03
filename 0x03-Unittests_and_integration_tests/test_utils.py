#!/usr/bin/env python3
"""unit test"""

from parameterized import parameterized
from unittest.mock import patch
import requests
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
            (
                "http://example.com",
                {"payload": True}
            )
        ),
        (
            (
                "http://holberton.io",
                {"payload": False}
            )
        )
    ])
    def test_get_json(self, test_url, test_payload):
        return_value = {"return_value.json.return_value": test_payload}
        patcher = patch("requests.get", **return_value)
        mock = patcher.start()
        result = get_json(test_url)
        self.assertEqual(result, test_payload)

        mock.assert_called_once()

        patcher.stop()


if __name__ == "__main__":
    unittest.main()
